from .models import DecisionTrace


VALID_TRACE_STATUS = {
    "SUCCESS",
    "FAILURE",
    "ESCALATED",
    "PENDING_REVIEW",
    "BLOCKED",
}

VALID_DECISION_TYPES = {
    "automated",
    "human_confirmed",
    "overridden",
    "blocked",
}


def validate_trace(trace: DecisionTrace):
    if not trace.trace_id:
        raise ValueError("trace_id is required")

    if not trace.timestamp:
        raise ValueError("timestamp is required")

    if not trace.event:
        raise ValueError("event is required")

    if not trace.event.event_id:
        raise ValueError("event.event_id is required")

    if not trace.event.type:
        raise ValueError("event.type is required")

    if trace.signals is None:
        raise ValueError("signals must not be None")

    if not trace.decision:
        raise ValueError("decision is required")

    if not trace.decision.outcome:
        raise ValueError("decision.outcome is required")

    if trace.status and trace.status not in VALID_TRACE_STATUS:
        raise ValueError(f"invalid trace status: {trace.status}")

    if trace.decision.decision_type and trace.decision.decision_type not in VALID_DECISION_TYPES:
        raise ValueError(f"invalid decision type: {trace.decision.decision_type}")
