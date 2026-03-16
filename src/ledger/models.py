from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import Any, Dict, Optional
import uuid


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class DecisionLedgerEntry:
    """
    Immutable-style record for preserving a decision outcome
    and its trace metadata.
    """

    ledger_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = field(default_factory=utc_now_iso)

    event_id: Optional[str] = None
    signal_id: Optional[str] = None
    contract_id: Optional[str] = None
    behavior_tree_id: Optional[str] = None
    boundary_id: Optional[str] = None

    decision: Optional[str] = None
    actor: str = "system"   # system / human / agent
    status: str = "recorded"

    trace_ref: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
