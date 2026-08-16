"""
AI Integration module for Google Gemini with Multi-Layer Safety Controls.

This module handles:
- Gemini API configuration & model invocation
- Output safety validation & retry loops
- Output sanitization
- Secure error handling with reference IDs
"""

import os
import time
import google.generativeai as genai
from typing import Tuple, Optional

from prompts import SYSTEM_PROMPT
from safety.models import SafetyDecision, AIResponse
from safety.output_validator import validate_output, sanitize_output
from safety.observability import log_safety_audit

MAX_SAFE_RETRIES = 1
CANDIDATE_MODELS = [
    "gemini-flash-latest",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.1-flash-lite",
    "gemma-4-26b-a4b-it"
]


def initialize_ai() -> None:
    """
    Initialize Google AI Studio API with API key from environment variable.
    
    Raises:
        ValueError: If API key is missing or not set.
    """
    try:
        from dotenv import load_dotenv
        load_dotenv(override=True)
    except ImportError:
        pass

    api_key = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
    
    if not api_key or api_key.strip() == "" or api_key.strip() == "your_api_key_here":
        raise ValueError("MISSING_API_KEY")
    
    genai.configure(api_key=api_key.strip())


def get_ai_response(user_query: str, decision: SafetyDecision) -> AIResponse:
    """
    Process allowed user query through Gemini with system prompt injection,
    output validation, retries, and sanitization.
    """
    request_id = decision.request_id
    start_time = time.time()
    
    try:
        initialize_ai()
    except ValueError as e:
        log_safety_audit(
            request_id=request_id,
            intent=decision.intent.value,
            risk_level=decision.risk_level.value,
            allowed=False,
            error_code="MISSING_API_KEY"
        )
        return AIResponse(
            success=False,
            text=f"API key not configured in .env. Reference ID: {request_id}",
            error_code="MISSING_API_KEY",
            request_id=request_id
        )

    last_error_code = None
    
    for model_name in CANDIDATE_MODELS:
        try:
            model = genai.GenerativeModel(
                model_name=model_name,
                system_instruction=SYSTEM_PROMPT
            )
            
            # Initial generation attempt
            response = model.generate_content(user_query)
            raw_text = response.text.strip() if (response and response.text) else ""
            
            # Output Safety Check
            is_safe, violation_reason = validate_output(raw_text)
            
            # Output Repair Retry if output safety check failed
            retry_count = 0
            if not is_safe and retry_count < MAX_SAFE_RETRIES:
                retry_count += 1
                stricter_prompt = (
                    f"{user_query}\n\n"
                    "IMPORTANT REMINDER: Provide strictly neutral, general educational information. "
                    "Do NOT offer personal advice, recommend actions ('you should...'), or predict outcomes."
                )
                response = model.generate_content(stricter_prompt)
                raw_text = response.text.strip() if (response and response.text) else ""
                is_safe, violation_reason = validate_output(raw_text)
            
            if is_safe and raw_text:
                sanitized_text = sanitize_output(raw_text)
                elapsed_ms = (time.time() - start_time) * 1000
                log_safety_audit(
                    request_id=request_id,
                    intent=decision.intent.value,
                    risk_level=decision.risk_level.value,
                    allowed=True,
                    latency_ms=elapsed_ms,
                    retry_count=retry_count,
                    model_name=model_name
                )
                return AIResponse(
                    success=True,
                    text=sanitized_text,
                    error_code=None,
                    request_id=request_id
                )
            elif not is_safe:
                last_error_code = "OUTPUT_SAFETY_VIOLATION"

        except Exception as e:
            error_str = str(e).lower()
            if "quota" in error_str or "limit" in error_str:
                last_error_code = "QUOTA_EXCEEDED"
            elif "invalid" in error_str and "key" in error_str:
                last_error_code = "INVALID_API_KEY"
            else:
                last_error_code = "MODEL_ERROR"
            continue

    # Graceful failure response with Reference ID
    elapsed_ms = (time.time() - start_time) * 1000
    log_safety_audit(
        request_id=request_id,
        intent=decision.intent.value,
        risk_level=decision.risk_level.value,
        allowed=False,
        latency_ms=elapsed_ms,
        error_code=last_error_code or "SERVICE_UNAVAILABLE"
    )

    if last_error_code == "QUOTA_EXCEEDED":
        user_msg = f"API quota limit exceeded. Please try again shortly. Reference ID: {request_id}"
    elif last_error_code == "INVALID_API_KEY":
        user_msg = f"Invalid API key configured. Reference ID: {request_id}"
    else:
        user_msg = f"We are temporarily unable to process this request. Reference ID: {request_id}"

    return AIResponse(
        success=False,
        text=user_msg,
        error_code=last_error_code or "SERVICE_UNAVAILABLE",
        request_id=request_id
    )
