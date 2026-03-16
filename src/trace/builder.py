from datetime import datetime, UTC
from .models import (
    DecisionTrace,
    Event,
    Signal,
    Decision,
)


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def build_trace(
    trace_id: str,
    event: Event,
    signals: list[Signal],
    decision: Decision,
    *,
    trace_version: str = "1.0",
    domain: str | None = None,
    status: str = "SUCCESS",
    contract_evaluation=None,
    behavior_tree_execution=None,
    boundary_checks=None,
    human_review=None,
    ledger_context=None,
    artifacts=None,
    metadata=None,
) -> DecisionTrace:
    return DecisionTrace(
        trace_id=trace_id,
        trace_version=trace_version,
        timestamp=utc_now_iso(),
        domain=domain,
        status=status,
        event=event,
        signals=signals,
        contract_evaluation=contract_evaluation,
        behavior_tree_execution=behavior_tree_execution,
        boundary_checks=boundary_checks or [],
        human_review=human_review,
        decision=decision,
        ledger_context=ledger_context,
        artifacts=artifacts or [],
        metadata=metadata or {},
    )
