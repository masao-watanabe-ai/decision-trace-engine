from .nodes import (
    SequenceNode,
    SelectorNode,
    ConditionNode,
    ActionNode,
)


def validate_node(node):
    if isinstance(node, (SequenceNode, SelectorNode)):
        if not node.children:
            raise ValueError(f"{node.node_type} node must have at least one child")
        for child in node.children:
            validate_node(child)

    elif isinstance(node, ConditionNode):
        if "expression" not in node.condition:
            raise ValueError("Condition node must contain 'condition.expression'")

    elif isinstance(node, ActionNode):
        if "name" not in node.action:
            raise ValueError("Action node must contain 'action.name'")

    else:
        raise ValueError(f"Unknown node type: {type(node)}")


def validate_behavior_tree(tree: dict):
    if not tree.get("root"):
        raise ValueError("Behavior tree must contain root node")

    validate_node(tree["root"])
