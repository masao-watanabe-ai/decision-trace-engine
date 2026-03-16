from .ast import DecisionContract


def validate_contract(contract: DecisionContract):

    if not contract.rules:
        raise ValueError("DecisionContract must contain at least one rule")

    for rule in contract.rules:

        if not rule.condition.expression:
            raise ValueError(f"{rule.rule_id} missing condition")

        if not rule.then.action:
            raise ValueError(f"{rule.rule_id} missing action")
