import yaml

from .nodes import (
    SequenceNode,
    SelectorNode,
    ConditionNode,
    ActionNode,
)


def parse_node(data: dict):
    node_type = data.get("type")
    node_id = data.get("id")
    name = data.get("name")
    description = data.get("description")

    if node_type == "Sequence":
        children = [parse_node(child) for child in data.get("children", [])]
        return SequenceNode(
            node_id=node_id,
            name=name,
            description=description,
            children=children
        )

    if node_type == "Selector":
        children = [parse_node(child) for child in data.get("children", [])]
        return SelectorNode(
            node_id=node_id,
            name=name,
            description=description,
            children=children
        )

    if node_type == "Condition":
        return ConditionNode(
            node_id=node_id,
            name=name,
            description=description,
            condition=data.get("condition", {})
        )

    if node_type == "Action":
        return ActionNode(
            node_id=node_id,
            name=name,
            description=description,
            action=data.get("action", {})
        )

    raise ValueError(f"Unsupported node type: {node_type}")


def parse_behavior_tree(text: str):
    data = yaml.safe_load(text)

    if not isinstance(data, dict):
        raise ValueError("Behavior tree file must be a YAML object")

    root_data = data.get("root")
    if not root_data:
        raise ValueError("Behavior tree must contain 'root'")

    return {
        "tree_id": data.get("tree_id"),
        "name": data.get("name"),
        "version": data.get("version"),
        "description": data.get("description"),
        "domain": data.get("domain"),
        "root": parse_node(root_data),
    }
