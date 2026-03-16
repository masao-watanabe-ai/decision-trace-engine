from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class Condition:
    expression: str
    inputs: List[str] = field(default_factory=list)


@dataclass
class Outcome:
    action: str
    outcome: Optional[str] = None
    parameters: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Rule:
    rule_id: str
    condition: Condition
    then: Outcome
    otherwise: Optional[Outcome] = None


@dataclass
class DecisionContract:
    contract_id: str
    name: str
    version: str
    inputs: List[str]
    rules: List[Rule]
    default_outcome: Optional[str] = None
