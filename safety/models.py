"""
Core models and data structures for the NyayaPath safety system.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional


class QueryIntent(Enum):
    # Safe Educational Intents
    EDUCATIONAL = "educational"
    TERMINOLOGY = "terminology"
    PROCEDURE = "procedure"
    CASE_STAGE_EXPLANATION = "case_stage_explanation"
    DOCUMENT_EXPLANATION = "document_explanation"

    # Unsafe / Disallowed Legal Intents
    PERSONALIZED_LEGAL_ADVICE = "personalized_legal_advice"
    LEGAL_STRATEGY = "legal_strategy"
    OUTCOME_PREDICTION = "outcome_prediction"
    LEGAL_INTERPRETATION = "legal_interpretation"
    LEGAL_DOCUMENT_GENERATION = "legal_document_generation"

    # Security & Abuse Intents
    HIGH_RISK = "high_risk"
    PROMPT_INJECTION = "prompt_injection"
    OUT_OF_SCOPE = "out_of_scope"


class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass
class SafetyDecision:
    allowed: bool
    intent: QueryIntent
    risk_level: RiskLevel
    reason: str
    refusal_message: Optional[str]
    request_id: str
    sanitized_query: str


@dataclass
class AIResponse:
    success: bool
    text: str
    error_code: Optional[str]
    request_id: str
