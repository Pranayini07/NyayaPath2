"""
Service layer for Jurisdiction-Aware Legal Navigator.
"""

from dataclasses import dataclass
from typing import Optional, Tuple
import os
import time
import google.generativeai as genai

from safety import evaluate_query
from safety.models import SafetyDecision, AIResponse
from safety.output_validator import validate_output, sanitize_output
from safety.observability import log_safety_audit
from prompts import JURISDICTION_SYSTEM_PROMPT, build_jurisdiction_prompt
from ai_handler import CANDIDATE_MODELS, MAX_SAFE_RETRIES, initialize_ai


@dataclass
class JurisdictionContext:
    country: str
    state: Optional[str] = None
    court_level: Optional[str] = None
    legal_domain: Optional[str] = None


def get_jurisdiction_response(
    question: str,
    jurisdiction: JurisdictionContext
) -> Tuple[SafetyDecision, AIResponse]:
    """
    Process question with jurisdiction context through the safety pipeline and Gemini AI engine.
    
    Returns:
        Tuple of (SafetyDecision, AIResponse)
    """
    # 1. Safety Evaluation (reuses existing multi-layer safety engine)
    decision = evaluate_query(question)
    request_id = decision.request_id
    
    if not decision.allowed:
        ai_resp = AIResponse(
            success=False,
            text=decision.refusal_message or "Request blocked by safety policy.",
            error_code="SAFETY_BLOCK",
            request_id=request_id
        )
        return decision, ai_resp

    # 2. AI Execution with Jurisdiction Context
    start_time = time.time()
    try:
        initialize_ai()
    except ValueError:
        log_safety_audit(
            request_id=request_id,
            intent=decision.intent.value,
            risk_level=decision.risk_level.value,
            allowed=False,
            error_code="MISSING_API_KEY"
        )
        ai_resp = AIResponse(
            success=False,
            text=f"API key not configured in .env. Reference ID: {request_id}",
            error_code="MISSING_API_KEY",
            request_id=request_id
        )
        return decision, ai_resp

    prompt_text = build_jurisdiction_prompt(question, jurisdiction)
    last_error_code = None

    for model_name in CANDIDATE_MODELS:
        try:
            model = genai.GenerativeModel(
                model_name=model_name,
                system_instruction=JURISDICTION_SYSTEM_PROMPT
            )
            
            response = model.generate_content(prompt_text)
            raw_text = response.text.strip() if (response and response.text) else ""
            
            is_safe, violation_reason = validate_output(raw_text)
            retry_count = 0
            
            if not is_safe and retry_count < MAX_SAFE_RETRIES:
                retry_count += 1
                stricter_prompt = (
                    f"{prompt_text}\n\n"
                    "IMPORTANT REMINDER: Provide strictly neutral educational information. "
                    "Do NOT offer personal advice ('you should...'), legal strategy, or outcome predictions."
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
                ai_resp = AIResponse(
                    success=True,
                    text=sanitized_text,
                    error_code=None,
                    request_id=request_id
                )
                return decision, ai_resp
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

    # Fallback failure handling
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
    else:
        user_msg = f"We are temporarily unable to process this request. Reference ID: {request_id}"

    ai_resp = AIResponse(
        success=False,
        text=user_msg,
        error_code=last_error_code or "SERVICE_UNAVAILABLE",
        request_id=request_id
    )
    return decision, ai_resp
