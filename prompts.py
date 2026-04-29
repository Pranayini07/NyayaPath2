"""
System prompts and safety guardrails for the Judicial Court Process Explainer Bot.

This module contains:
- The strict system prompt that enforces judicial neutrality
- Keyword-based safety checks to prevent unsafe queries
- Refusal messages for blocked requests
"""

# ============================================================================
# SYSTEM PROMPT - CRITICAL SAFETY COMPONENT
# ============================================================================
# This prompt is injected into every AI request to enforce strict boundaries.
# It must be clear, unambiguous, and audit-friendly.

SYSTEM_PROMPT = """You are a Judicial Court Process Explainer Bot designed to improve public legal awareness.

YOUR ROLE:
- Explain judicial court procedures in simple, neutral language
- Describe case lifecycle stages and terminology
- Provide educational information about how courts operate
- Use clear, accessible language suitable for the general public

YOUR STRICT LIMITATIONS:
- You MUST ONLY explain procedures, processes, and terminology
- You MUST use neutral, educational, and unbiased language
- You MUST NOT provide legal advice, opinions, or interpretations
- You MUST NOT predict case outcomes or suggest strategies
- You MUST NOT generate legal documents or arguments
- You MUST NOT encourage or discourage any legal action
- You MUST NOT interpret laws, statutes, or regulations
- You MUST NOT provide jurisdiction-specific legal guidance

HOW TO RESPOND:
- If asked about procedures: Explain the general process clearly
- If asked about terminology: Define terms in simple language
- If asked about case stages: Describe the typical lifecycle
- If asked for advice: Politely refuse and redirect to explanation-only scope
- If asked for predictions: Politely refuse and explain you only describe processes
- If asked for legal interpretation: Politely refuse and clarify your educational role

REFUSAL TEMPLATE:
"I can only explain judicial procedures and terminology. I cannot provide legal advice, interpret laws, predict outcomes, or suggest actions. For legal guidance, please consult a qualified attorney. How can I help explain court procedures instead?"

Remember: Your purpose is education and awareness, not legal guidance."""

# ============================================================================
# SAFETY GUARDRAILS - KEYWORD-BASED PRE-CHECKS
# ============================================================================
# These keywords help identify queries that violate the system's scope.
# If detected, the query is blocked BEFORE reaching the AI.

UNSAFE_KEYWORDS = [
    # Legal advice indicators
    "should i", "what should", "do you think", "would you recommend",
    "is it legal", "can i sue", "should i file", "am i allowed",
    
    # Strategy/prediction indicators
    "will i win", "chances of", "likely outcome", "what will happen",
    "predict", "forecast", "probability", "odds",
    
    # Document generation indicators
    "write a", "draft a", "create a", "generate a", "make a",
    "legal document", "petition", "motion", "brief", "affidavit",
    
    # Action recommendation indicators
    "what to do", "how to proceed", "next steps", "action plan",
    "strategy", "approach", "tactic",
    
    # Interpretation indicators
    "what does this law mean", "interpret", "explain this statute",
    "what does this mean for me", "how does this apply",
    
    # Personalization indicators
    "my case", "my situation", "in my case", "for me",
]

# Refusal messages for different violation types
REFUSAL_MESSAGES = {
    "advice": "I cannot provide legal advice. I can only explain general court procedures and terminology. For legal guidance specific to your situation, please consult a qualified attorney.",
    
    "prediction": "I cannot predict case outcomes or probabilities. I can only explain how court processes work in general terms.",
    
    "document": "I cannot generate, draft, or create legal documents. I can only explain what types of documents exist and their general purpose in court procedures.",
    
    "strategy": "I cannot suggest strategies, actions, or approaches. I can only explain how court procedures typically work.",
    
    "interpretation": "I cannot interpret laws, statutes, or regulations. I can only explain general court procedures and terminology.",
    
    "personal": "I cannot provide personalized guidance or analyze specific cases. I can only explain general court procedures and terminology.",
    
    "general": "I can only explain judicial procedures and terminology. I cannot provide legal advice, interpret laws, predict outcomes, or suggest actions. For legal guidance, please consult a qualified attorney."
}

def check_query_safety(user_query: str) -> tuple[bool, str]:
    """
    Pre-check user query for unsafe patterns before sending to AI.
    
    Args:
        user_query: The user's input query
        
    Returns:
        Tuple of (is_safe: bool, refusal_message: str)
        If is_safe is True, refusal_message will be empty.
    """
    if not user_query or not user_query.strip():
        return False, "Please enter a question about court procedures or terminology."
    
    query_lower = user_query.lower()
    
    # Check for unsafe keywords
    for keyword in UNSAFE_KEYWORDS:
        if keyword in query_lower:
            # Determine violation type for appropriate refusal message
            if any(k in query_lower for k in ["should", "recommend", "think", "advice"]):
                return False, REFUSAL_MESSAGES["advice"]
            elif any(k in query_lower for k in ["win", "chances", "outcome", "predict", "probability"]):
                return False, REFUSAL_MESSAGES["prediction"]
            elif any(k in query_lower for k in ["write", "draft", "create", "generate", "make", "document"]):
                return False, REFUSAL_MESSAGES["document"]
            elif any(k in query_lower for k in ["strategy", "approach", "tactic", "what to do", "next steps"]):
                return False, REFUSAL_MESSAGES["strategy"]
            elif any(k in query_lower for k in ["interpret", "what does this mean", "how does this apply"]):
                return False, REFUSAL_MESSAGES["interpretation"]
            elif any(k in query_lower for k in ["my case", "my situation", "for me", "in my case"]):
                return False, REFUSAL_MESSAGES["personal"]
            else:
                return False, REFUSAL_MESSAGES["general"]
    
    # Query passed safety check
    return True, ""

