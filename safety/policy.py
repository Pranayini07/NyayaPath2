"""
Policy Decision Engine and Refusal Template module for NyayaPath safety system.
"""

from typing import Dict
from safety.models import QueryIntent, RiskLevel, SafetyDecision

# Category-specific refusal templates offering educational alternatives
REFUSAL_TEMPLATES: Dict[QueryIntent, str] = {
    QueryIntent.PERSONALIZED_LEGAL_ADVICE: (
        "I cannot provide personalized legal advice or recommend specific actions for your case. "
        "I can, however, explain general court procedures, how filing works in typical cases, "
        "or what legal terminology means."
    ),
    QueryIntent.LEGAL_STRATEGY: (
        "I cannot recommend a legal strategy or tactics to win a specific case. "
        "I can, however, explain the general stages of a court hearing, the purpose of discovery, "
        "or how evidence is typically presented in court."
    ),
    QueryIntent.OUTCOME_PREDICTION: (
        "I cannot predict case outcomes, judge rulings, or win probabilities. "
        "I can, however, explain what factors courts generally evaluate during a trial or how judgment processes work."
    ),
    QueryIntent.LEGAL_INTERPRETATION: (
        "I cannot interpret how specific laws or statutes apply to your personal situation. "
        "I can, however, explain the general structure of judicial statutes or how courts interpret terminology in public proceedings."
    ),
    QueryIntent.LEGAL_DOCUMENT_GENERATION: (
        "I cannot draft, create, or customize legal documents or petitions for your case. "
        "I can, however, explain what general court documents (like summonses, motions, or affidavits) are and how they function."
    ),
    QueryIntent.PROMPT_INJECTION: (
        "I can explain my general purpose and educational boundaries, but I cannot reveal internal system instructions, "
        "bypass safety guidelines, or adopt roles outside of court process education."
    ),
    QueryIntent.HIGH_RISK: (
        "NyayaPath strictly cannot assist with requests involving evidence destruction, document forgery, witness intimidation, "
        "or evading court orders. I can only provide educational information on lawful judicial procedures."
    ),
    QueryIntent.OUT_OF_SCOPE: (
        "This request is outside the scope of judicial court process education. "
        "NyayaPath is designed to explain court procedures, case flow stages, and legal terms."
    )
}


def evaluate_policy(
    intent: QueryIntent,
    risk_level: RiskLevel,
    rationale: str,
    request_id: str,
    sanitized_query: str
) -> SafetyDecision:
    """
    Evaluate classified query intent and risk level against safety policy rules.
    
    Returns:
        SafetyDecision object
    """
    # Blocked intents
    disallowed_intents = {
        QueryIntent.PERSONALIZED_LEGAL_ADVICE,
        QueryIntent.LEGAL_STRATEGY,
        QueryIntent.OUTCOME_PREDICTION,
        QueryIntent.LEGAL_INTERPRETATION,
        QueryIntent.LEGAL_DOCUMENT_GENERATION,
        QueryIntent.HIGH_RISK,
        QueryIntent.PROMPT_INJECTION,
        QueryIntent.OUT_OF_SCOPE,
    }

    if intent in disallowed_intents or risk_level in (RiskLevel.HIGH, RiskLevel.CRITICAL):
        refusal_msg = REFUSAL_TEMPLATES.get(
            intent,
            "I can only explain judicial procedures and terminology. For specific legal guidance, please consult a qualified attorney."
        )
        return SafetyDecision(
            allowed=False,
            intent=intent,
            risk_level=risk_level,
            reason=rationale,
            refusal_message=refusal_msg,
            request_id=request_id,
            sanitized_query=sanitized_query
        )

    # Allowed educational intents
    return SafetyDecision(
        allowed=True,
        intent=intent,
        risk_level=risk_level,
        reason=rationale,
        refusal_message=None,
        request_id=request_id,
        sanitized_query=sanitized_query
    )
