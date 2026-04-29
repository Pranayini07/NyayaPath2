"""
AI integration module for Google AI Studio API (Gemini Flash).

This module handles:
- Secure API key loading from environment variables
- Connection to Google AI Studio
- Safe query processing with system prompt injection
- Error handling and graceful failures
"""

import os
import google.generativeai as genai
from prompts import SYSTEM_PROMPT

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, skip .env loading
    pass

# ============================================================================
# CONFIGURATION
# ============================================================================

def initialize_ai() -> None:
    """
    Initialize Google AI Studio API with API key from environment variable.
    
    Raises:
        ValueError: If API key is not found in environment variables
    """
    api_key = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_AI_STUDIO_API_KEY not found in environment variables. "
            "Please set it in your .env file or environment."
        )
    
    genai.configure(api_key=api_key)

def get_ai_response(user_query: str) -> tuple[bool, str]:
    """
    Process user query through Gemini Flash with system prompt injection.
    
    Args:
        user_query: The user's question about court procedures
        
    Returns:
        Tuple of (success: bool, response: str)
        If success is False, response contains error message
    """
    try:
        # Initialize API if not already done
        try:
            initialize_ai()
        except ValueError as e:
            return False, str(e)
        
        # Configure the model with system instruction
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
        
        # Generate response
        response = model.generate_content(user_query)
        
        # Extract text from response
        if response and response.text:
            return True, response.text.strip()
        else:
            return False, "I apologize, but I couldn't generate a response. Please try rephrasing your question."
            
    except Exception as e:
        # Handle any API errors gracefully
        error_msg = str(e).lower()
        
        if "api_key" in error_msg or "authentication" in error_msg:
            return False, "API authentication error. Please check your GOOGLE_AI_STUDIO_API_KEY."
        elif "quota" in error_msg or "limit" in error_msg:
            return False, "API quota exceeded. Please try again later."
        elif "safety" in error_msg:
            return False, "The query was blocked by safety filters. Please rephrase your question to focus on general court procedures."
        else:
            return False, f"An error occurred: {str(e)}. Please try again."

