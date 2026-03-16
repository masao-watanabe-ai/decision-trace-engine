import json
from pathlib import Path

import yaml

from .models import BoundaryDefinition, BoundaryRule


def parse_boundary_dict(data: dict) -> BoundaryDefinition:
    rules = [
        BoundaryRule(
            rule_id=rule["rule_id"],
            name=rule["name"],
            condition=rule["condition"],
            result=rule["result"],
            description=rule.get("description")
        )
        for rule in data.get("rules", [])
    ]

    return BoundaryDefinition(
        boundary_id=data["boundary_id"],
        name=data["name"],
        version=data["version"],
        description=data.get("description"),
        boundary_type=data.get("boundary_type"),
        rules=rules,
        metadata=data.get("metadata", {})
    )


def load_boundary(path: str) -> BoundaryDefinition:
    text = Path(path).read_text()

    if path.endswith(".json"):
        data = json.loads(text)
    elif path.endswith(".yaml") or path.endswith(".yml"):
        data = yaml.safe_load(text)
    else:
        raise ValueError("Boundary file must be .json, .yaml, or .yml")

    return parse_boundary_dict(data)
