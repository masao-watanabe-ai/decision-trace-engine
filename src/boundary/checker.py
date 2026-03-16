from .models import BoundaryDefinition


def evaluate_expression(expression: str, context: dict) -> bool:
    """
    Minimal reference evaluator.
    Evaluates a simple Python-like expression against the provided context.
    This is only for conceptual/reference use.
    """
    try:
        return bool(eval(expression, {}, context))
    except Exception:
        return False


def check_boundary(boundary: BoundaryDefinition, context: dict) -> dict:
    """
    Evaluate boundary rules in order and return the first matched result.
    If no rule matches, returns PASS by default.
    """
    for rule in boundary.rules:
        matched = evaluate_expression(rule.condition, context)
        if matched:
            return {
                "boundary_id": boundary.boundary_id,
                "rule_id": rule.rule_id,
                "name": rule.name,
                "result": rule.result,
                "condition": rule.condition,
                "matched": True
            }

    return {
        "boundary_id": boundary.boundary_id,
        "rule_id": None,
        "name": boundary.name,
        "result": "PASS",
        "condition": None,
        "matched": False
    }
