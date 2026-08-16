"""
Semantic intent and prompt-injection classification module for NyayaPath safety system.
"""

import re
from typing import Tuple
from safety.models import QueryIntent, RiskLevel


# High risk illegal/unethical keywords and patterns
HIGH_RISK_PATTERNS = [
    r"\b(hide|destroy|spoliate|alter)\s+(an?\s+)?(evidence|records?|documents?)\b",
    r"\b(fabricate|forge|falsify|fake)\s+(an?\s+)?(evidence|court\s+documents?|notices?|signatures?)\b",
    r"\b(threaten|intimidate|bribe|tamper\s+with)\s+(an?\s+)?(witness|juror|judge|official)\b",
    r"\b(evade|avoid|disobey|flout)\s+(an?\s+)?(court\s+orders?|warrants?|subpoenas?|summons)\b",
    r"\b(commit|assist\s+in|how\s+to\s+get\s+away\s+with)\s+(fraud|perjury|contempt|crime)\b",
]

# Prompt injection and jailbreak patterns
PROMPT_INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?(previous|prior|above|system)\s+(instructions?|prompts?|rules?)",
    r"disregard\s+(your|the)\s+(system|safety|initial)\s+(prompt|rules?|instructions?)",
    r"you\s+are\s+now\s+(a|my)\s+(lawyer|attorney|judge|legal\s+counsel|jailbroken)",
    r"pretend\s+(you\s+are|to\s+be)\s+(a|my)\s+(attorney|lawyer|judge|counsel)",
    r"(reveal|show|display|print|output|tell)\s+(me\s+)?(your|the)?\s*(hidden\s+)?(system\s+)?(prompt|instructions?|rules?|api\s+key|configuration|secrets?)",
    r"(disable|bypass|turn\s+off)\s+(your\s+)?(safety|guardrails?|refusals?|filters?|rules?)",
    r"bypass\s+(restrictions?|rules?|safety)",
    r"pretend\s+(that\s+)?(legal\s+advice\s+is\s+allowed|you\s+have\s+no\s+rules)",
    r"act\s+as\s+my\s+(attorney|lawyer|counsel)",
    r"roleplay\s+as\s+(a\s+)?(lawyer|attorney)",
    r"what\s+are\s+your\s+(safety\s+rules|system\s+instructions|internal\s+prompts)",
    r"developer\s+mode",
    r"system\s+message:",
    r"\bsystem_prompt\b",
    r"\bsystem\s+prompt\b",
    r"\bhidden\s+instructions?\b",
]

# Unsafe intent patterns (Personalized advice, Strategy, Prediction, Document Generation, Interpretation)
PERSONAL_ADVICE_PATTERNS = [
    r"\bshould\s+i\b",
    r"\bwhat\s+should\s+i\b",
    r"\bwhat\s+is\s+(the\s+best|my\s+best)\s+(option|choice|action)\b",
    r"\bam\s+i\s+allowed\s+to\b",
    r"\bcan\s+i\s+sue\b",
    r"\bis\s+it\s+legal\s+for\s+me\b",
    r"\badvise\s+me\b",
    r"\bwhat\s+would\s+you\s+do\s+if\s+you\s+were\s+me\b",
    r"\bin\s+my\s+(case|situation|lawsuit)\b",
    r"\bfor\s+my\s+case\b",
]

STRATEGY_PATTERNS = [
    r"\bhow\s+can\s+i\s+(win|defeat|beat)\b",
    r"\bhow\s+to\s+(win|defeat|beat)\b",
    r"\bwhat\s+strategy\b",
    r"\bbest\s+(tactic|approach|strategy)\b",
    r"\bwrite\s+arguments\s+to\s+help\s+me\b",
    r"\bhow\s+can\s+i\s+defeat\b",
]

PREDICTION_PATTERNS = [
    r"\bwill\s+i\s+win\b",
    r"\bwhat\s+are\s+my\s+(chances|odds|probabilities)\b",
    r"\bpredict\s+(the|my)?\s*(outcome|verdict|result)\b",
    r"\bam\s+i\s+likely\s+to\s+(win|lose)\b",
    r"\bwill\s+the\s+judge\s+(rule|grant|deny)\b",
]

DOCUMENT_GEN_PATTERNS = [
    r"\b(draft|write|create|generate|make)\s+(an?|my)?\s*(petition|motion|affidavit|legal\s+notice|complaint|lawsuit|contract|legal\s+document)\b",
    r"\bcreate\s+an?\s+affidavit\b",
    r"\bcreate\s+a\s+legal\s+document\b",
]

INTERPRETATION_PATTERNS = [
    r"\binterpret\s+this\s+(statute|law|section|clause)\b",
    r"\bdoes\s+this\s+(law|statute|rule)\s+apply\s+to\s+my\s+case\b",
    r"\bhow\s+does\s+this\s+(law|section)\s+affect\s+me\b",
]


# Contextual Educational Exceptions / False Positive Prevention
EDUCATIONAL_CONTEXT_PATTERNS = [
    r"\bwhat\s+does\s+[\"']?should[\"']?\s+mean\b",
    r"\bwhat\s+should\s+(generally|typically|normally|usually)\s+happen\b",
    r"\bwhat\s+should\s+a\s+(party|plaintiff|defendant|court|judge)\s+(typically|normally|generally)\b",
    r"\bgeneral\s+purpose\b",
    r"\bcan\s+you\s+explain\b",
    r"\bwhat\s+is\s+a\b",
    r"\bwhat\s+does\s+.*\s+mean\b",
    r"\bhow\s+does\s+.*\s+work\b",
]


def classify_query(text: str) -> Tuple[QueryIntent, RiskLevel, str]:
    """
    Classify normalized user query into QueryIntent and RiskLevel with rationale.
    
    Returns:
        Tuple of (intent: QueryIntent, risk_level: RiskLevel, rationale: str)
    """
    text_lower = text.lower()

    # 1. High Risk Check
    for pattern in HIGH_RISK_PATTERNS:
        if re.search(pattern, text_lower):
            return (
                QueryIntent.HIGH_RISK,
                RiskLevel.CRITICAL,
                "Query involves potential illegal activity, evidence tampering, or court order evasion."
            )

    # 2. Prompt Injection Check
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return (
                QueryIntent.PROMPT_INJECTION,
                RiskLevel.HIGH,
                "Query contains prompt-injection or instruction-hijacking attempt."
            )

    # 3. Check Educational Exceptions First (False Positive Guard)
    is_educational_framed = any(re.search(pat, text_lower) for pat in EDUCATIONAL_CONTEXT_PATTERNS)

    # 4. Unsafe Intent Checks (only if NOT explicitly framed as general educational definition)
    if not is_educational_framed:
        for pattern in PERSONAL_ADVICE_PATTERNS:
            if re.search(pattern, text_lower):
                return (
                    QueryIntent.PERSONALIZED_LEGAL_ADVICE,
                    RiskLevel.MEDIUM,
                    "Query requests personalized legal guidance or specific action advice."
                )

        for pattern in STRATEGY_PATTERNS:
            if re.search(pattern, text_lower):
                return (
                    QueryIntent.LEGAL_STRATEGY,
                    RiskLevel.MEDIUM,
                    "Query requests tactical legal strategy or instructions to win a case."
                )

        for pattern in PREDICTION_PATTERNS:
            if re.search(pattern, text_lower):
                return (
                    QueryIntent.OUTCOME_PREDICTION,
                    RiskLevel.MEDIUM,
                    "Query requests case outcome predictions or win probabilities."
                )

        for pattern in DOCUMENT_GEN_PATTERNS:
            if re.search(pattern, text_lower):
                return (
                    QueryIntent.LEGAL_DOCUMENT_GENERATION,
                    RiskLevel.MEDIUM,
                    "Query requests custom legal document generation for a case."
                )

        for pattern in INTERPRETATION_PATTERNS:
            if re.search(pattern, text_lower):
                return (
                    QueryIntent.LEGAL_INTERPRETATION,
                    RiskLevel.MEDIUM,
                    "Query requests personalized legal interpretation of statutes."
                )

    # 5. Classify Safe Educational Sub-intents
    if any(k in text_lower for k in ["stage", "phase", "process", "lifecycle", "hearing", "trial", "appeal"]):
        return QueryIntent.CASE_STAGE_EXPLANATION, RiskLevel.LOW, "Educational query regarding case stages."
    elif any(k in text_lower for k in ["mean", "definition", "term", "define", "what is a"]):
        return QueryIntent.TERMINOLOGY, RiskLevel.LOW, "Educational query regarding legal terminology."
    elif any(k in text_lower for k in ["document", "petition", "motion", "notice", "summons", "affidavit"]):
        return QueryIntent.DOCUMENT_EXPLANATION, RiskLevel.LOW, "Educational query regarding general court document types."
    elif any(k in text_lower for k in ["procedure", "rule", "how court", "court system", "jurisdiction"]):
        return QueryIntent.PROCEDURE, RiskLevel.LOW, "Educational query regarding general court procedures."

    # Default to general Educational
    return QueryIntent.EDUCATIONAL, RiskLevel.LOW, "General educational query on judicial processes."
