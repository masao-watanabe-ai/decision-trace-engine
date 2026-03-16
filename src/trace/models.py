from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Event:
    event_id: str
    type: str
    timestamp: str
    source: Optional[str] = None
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Signal:
    signal_id: str
    name: str
    value: Any
    value_type: Optional[str] = None
    source: Optional[str] = None
    confidence: Optional[float] = None
    timestamp: Optional[str] = None


@dataclass
class EvaluatedRule:
    rule_id: str
    expression: str
    result: bool
    inputs: List[str] = field(default_factory=list)
    action: Optional[str] = None


@dataclass
class ContractEvaluation:
    contract_id: str
    result: str
    contract_name: Optional[str] = None
    contract_version: Optional[str] = None
    rules_evaluated: List[EvaluatedRule] = field(default_factory=list)
    selected_outcome: Optional[str] = None


@dataclass
class ExecutedNode:
    node_id: str
    node_type: str
    status: str
    node_name: Optional[str] = None
    condition_result: Optional[bool] = None
    action_result: Optional[str] = None
    timestamp: Optional[str] = None


@dataclass
class BehaviorTreeExecution:
    tree_id: str
    result: str
    path: List[ExecutedNode] = field(default_factory=list)
    tree_name: Optional[str] = None
    tree_version: Optional[str] = None


@dataclass
class BoundaryCheck:
    boundary_id: str
    name: str
    result: str
    boundary_type: Optional[str] = None
    reason: Optional[str] = None
    triggered_by: List[str] = field(default_factory=list)


@dataclass
class HumanReview:
    required: bool
    review_status: str
    reason: Optional[str] = None
    reviewer_id: Optional[str] = None
    review_timestamp: Optional[str] = None
    notes: Optional[str] = None


@dataclass
class Decision:
    outcome: str
    decision_type: Optional[str] = None
    reason: Optional[str] = None
    issued_by: Optional[str] = None
    confidence: Optional[float] = None


@dataclass
class LedgerContext:
    ledger_id: Optional[str] = None
    recorded_at: Optional[str] = None
    ledger_backend: Optional[str] = None
    immutable: Optional[bool] = None
    engine_version: Optional[str] = None


@dataclass
class Artifact:
    type: str
    path: str
    description: Optional[str] = None


@dataclass
class DecisionTrace:
    trace_id: str
    timestamp: str
    event: Event
    signals: List[Signal]
    decision: Decision
    trace_version: Optional[str] = None
    domain: Optional[str] = None
    status: Optional[str] = None
    contract_evaluation: Optional[ContractEvaluation] = None
    behavior_tree_execution: Optional[BehaviorTreeExecution] = None
    boundary_checks: List[BoundaryCheck] = field(default_factory=list)
    human_review: Optional[HumanReview] = None
    ledger_context: Optional[LedgerContext] = None
    artifacts: List[Artifact] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
