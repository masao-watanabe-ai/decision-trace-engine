from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class BoundaryRule:
    rule_id: str
    name: str
    condition: str
    result: str
    description: Optional[str] = None


@dataclass
class BoundaryDefinition:
    boundary_id: str
    name: str
    version: str
    description: Optional[str] = None
    boundary_type: Optional[str] = None
    rules: List[BoundaryRule] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
