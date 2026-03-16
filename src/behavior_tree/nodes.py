from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class BaseNode:
    node_id: Optional[str]
    node_type: str
    name: Optional[str] = None
    description: Optional[str] = None


@dataclass
class SequenceNode(BaseNode):
    children: List["Node"] = field(default_factory=list)

    def __init__(
        self,
        node_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        children: Optional[List["Node"]] = None
    ):
        super().__init__(node_id=node_id, node_type="Sequence", name=name, description=description)
        self.children = children or []


@dataclass
class SelectorNode(BaseNode):
    children: List["Node"] = field(default_factory=list)

    def __init__(
        self,
        node_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        children: Optional[List["Node"]] = None
    ):
        super().__init__(node_id=node_id, node_type="Selector", name=name, description=description)
        self.children = children or []


@dataclass
class ConditionNode(BaseNode):
    condition: Dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        node_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        condition: Optional[Dict[str, Any]] = None
    ):
        super().__init__(node_id=node_id, node_type="Condition", name=name, description=description)
        self.condition = condition or {}


@dataclass
class ActionNode(BaseNode):
    action: Dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        node_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        action: Optional[Dict[str, Any]] = None
    ):
        super().__init__(node_id=node_id, node_type="Action", name=name, description=description)
        self.action = action or {}


Node = BaseNode | SequenceNode | SelectorNode | ConditionNode | ActionNode
