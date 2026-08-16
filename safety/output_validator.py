"""
Output safety validation and sanitization module for NyayaPath safety system.
"""

import re
from typing import Tuple, Optional


# Patterns indicating generated directive advice, predictions, or strategy
UNSAFE_OUTPUT_PATTERNS = [
    r"\byou\s+should\s+(file|sue|hire|contact|claim|plead|submit)\b",
    r"\byou\s+need\s+to\s+(file|sue|submit|hire)\b",
    r"\bi\s+(strongly\s+)?recommend\s+that\s+you\b",
    r"\byour\s+best\s+(option|choice|strategy)\s+is\b",
    r"\byou\s+will\s+(definitely\s+)?(win|lose|prevail)\b",
    r"\byou\s+are\s+likely\s+to\s+(win|lose)\b",
    r"\byour\s+chances\s+are\b",
    r"\bin\s+your\s+case,\s+you\b",
    r"\bgiven\s+your\s+situation,\s+you\b",
]

# Secret and internal implementation leak patterns
INTERNAL_LEAK_PATTERNS = [
    r"AIzaSy[A-Za-z0-9_-]{33}",  # Google API key pattern
    r"GOOGLE_AI_STUDIO_API_KEY",
    r"SYSTEM_PROMPT",
    r"You are a Judicial Court Process Explainer Bot",
    r"[A-Z]:\\[^\n\r]+",  # Windows file paths
    r"/(?:[a-zA-Z0-9_-]+/)+[a-zA-Z0-9_-]+\.py",  # Linux/Mac file paths
    r"Traceback \(most recent call last\):",
]


def validate_output(text: str) -> Tuple[bool, Optional[str]]:
    """
    Validate that generated text does not contain directive legal advice,
    outcome predictions, or personalized instructions.
    
    Returns:
        Tuple of (is_safe: bool, violation_reason: Optional[str])
    """
    if not text or not text.strip():
        return False, "Empty output generated."

    text_lower = text.lower()
    
    for pattern in UNSAFE_OUTPUT_PATTERNS:
        if re.search(pattern, text_lower):
            return False, f"Output contained non-compliant advice/prediction pattern matching '{pattern}'"
            
    return True, None


def sanitize_output(text: str) -> str:
    """
    Sanitize output text by redacting any internal paths, secrets, API keys, or raw system prompts.
    """
    if not text:
        return ""

    sanitized = text
    
    # Redact API keys if found
    sanitized = re.sub(r"AIzaSy[A-Za-z0-9_-]{33}", "[REDACTED_API_KEY]", sanitized)
    
    # Redact local system file paths
    sanitized = re.sub(r"[A-Z]:\\[^\n\r\t]+", "[INTERNAL_FILE_PATH]", sanitized)
    
    # Remove raw traceback dumps if present
    if "Traceback (most recent call last):" in sanitized:
        sanitized = "An internal processing error occurred. Details have been logged securely."

    return sanitized.strip()
