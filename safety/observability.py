"""
Observability and privacy-preserving audit logging module for NyayaPath safety system.
"""

import uuid
import logging
import time
from typing import Optional, Dict, Any

# Configure privacy-aware logger
logger = logging.getLogger("NyayaPathSafety")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [ReqID: %(request_id)s] %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def generate_request_id() -> str:
    """Generate short unique reference request ID e.g. NP-8F21A."""
    unique_suffix = uuid.uuid4().hex[:6].upper()
    return f"NP-{unique_suffix}"


def log_safety_audit(
    request_id: str,
    intent: str,
    risk_level: str,
    allowed: bool,
    latency_ms: Optional[float] = None,
    retry_count: int = 0,
    model_name: Optional[str] = None,
    error_code: Optional[str] = None
) -> None:
    """
    Log safety decision and execution metrics without storing sensitive PII or raw user text.
    """
    extra_data = {"request_id": request_id}
    msg_parts = [
        f"Intent={intent}",
        f"Risk={risk_level}",
        f"Allowed={allowed}",
        f"Retries={retry_count}"
    ]
    if latency_ms is not None:
        msg_parts.append(f"Latency={latency_ms:.2f}ms")
    if model_name:
        msg_parts.append(f"Model={model_name}")
    if error_code:
        msg_parts.append(f"ErrorCode={error_code}")
        
    log_msg = " | ".join(msg_parts)
    logger.info(log_msg, extra=extra_data)
