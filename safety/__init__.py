"""
NyayaPath Multi-Layer AI Safety System package.
"""

from safety.models import QueryIntent, RiskLevel, SafetyDecision, AIResponse
from safety.input_validator import validate_input
from safety.classifier import classify_query
from safety.policy import evaluate_policy
from safety.output_validator import validate_output, sanitize_output
from safety.observability import generate_request_id, log_safety_audit


def evaluate_query(user_query: str) -> SafetyDecision:
    """
    Execute full input safety pipeline:
    Length Validation -> Normalization -> Classification -> Policy Decision -> Audit Logging.
    
    Returns:
        SafetyDecision object
    """
    request_id = generate_request_id()
    
    # Step 1: Input Validation & Normalization
    is_valid, normalized_text, validation_error = validate_input(user_query)
    
    if not is_valid:
        decision = SafetyDecision(
            allowed=False,
            intent=QueryIntent.OUT_OF_SCOPE,
            risk_level=RiskLevel.MEDIUM,
            reason="Input validation failed.",
            refusal_message=validation_error,
            request_id=request_id,
            sanitized_query=normalized_text
        )
        log_safety_audit(
            request_id=request_id,
            intent=decision.intent.value,
            risk_level=decision.risk_level.value,
            allowed=False,
            error_code="VALIDATION_ERROR"
        )
        return decision

    # Step 2: Semantic Intent & Risk Classification
    intent, risk_level, rationale = classify_query(normalized_text)
    
    # Step 3: Policy Decision Engine
    decision = evaluate_policy(
        intent=intent,
        risk_level=risk_level,
        rationale=rationale,
        request_id=request_id,
        sanitized_query=normalized_text
    )
    
    # Step 4: Audit Logging
    log_safety_audit(
        request_id=request_id,
        intent=decision.intent.value,
        risk_level=decision.risk_level.value,
        allowed=decision.allowed
    )
    
    return decision
