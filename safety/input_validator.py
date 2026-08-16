"""
Input normalization and validation module for NyayaPath safety system.
"""

import unicodedata
import re
from typing import Tuple, Optional

MAX_QUERY_LENGTH = 1000
MIN_QUERY_LENGTH = 2


def normalize_input(text: str) -> str:
    """
    Perform Unicode NFKC normalization and clean excessive whitespace.
    """
    if not text:
        return ""
    # Unicode normalization
    normalized = unicodedata.normalize("NFKC", text)
    # Strip null bytes and control chars except standard whitespace
    cleaned = "".join(ch for ch in normalized if unicodedata.category(ch)[0] != "C" or ch in ("\n", "\r", "\t"))
    # Collapse multiple whitespace characters into single space for spaces/tabs
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    # Collapse excessive newlines
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def validate_input(text: str) -> Tuple[bool, str, Optional[str]]:
    """
    Validate input length, format, and structure.
    
    Returns:
        Tuple of (is_valid: bool, normalized_text: str, validation_error: Optional[str])
    """
    normalized = normalize_input(text)
    
    if not normalized or len(normalized) < MIN_QUERY_LENGTH:
        return False, normalized, "Please enter a valid question about court procedures or terminology."
        
    if len(normalized) > MAX_QUERY_LENGTH:
        return (
            False,
            normalized[:MAX_QUERY_LENGTH],
            f"Your question exceeds the maximum length of {MAX_QUERY_LENGTH} characters. Please shorten your question."
        )

    # Check for excessive repeated characters (e.g., "aaaaa..." or "????...")
    if re.search(r"(.)\1{25,}", normalized):
        return False, normalized, "Your input contains excessive repeated characters. Please rephrase your question."

    return True, normalized, None
