from .models import BoundaryDefinition


VALID_RESULTS = {"PASS", "FAIL", "ESCALATE", "BLOCK"}


def validate_boundary(boundary: BoundaryDefinition):
    if not boundary.boundary_id:
        raise ValueError("boundary_id is required")

    if not boundary.name:
        raise ValueError("name is required")

    if not boundary.version:
        raise ValueError("version is required")

    if not boundary.rules:
        raise ValueError("BoundaryDefinition must contain at least one rule")

    for rule in boundary.rules:
        if not rule.rule_id:
            raise ValueError("Each boundary rule must have rule_id")
        if not rule.name:
            raise ValueError(f"{rule.rule_id}: name is required")
        if not rule.condition:
            raise ValueError(f"{rule.rule_id}: condition is required")
        if rule.result not in VALID_RESULTS:
            raise ValueError(
                f"{rule.rule_id}: result must be one of {sorted(VALID_RESULTS)}"
            )
