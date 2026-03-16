import re
from typing import List
from .ast import DecisionContract, Rule, Condition, Outcome


RULE_PATTERN = re.compile(
    r"IF (.+)\s+THEN (.+?)(?:\s+ELSE (.+))?$",
    re.IGNORECASE
)


def parse_rule(rule_id: str, line: str) -> Rule:
    match = RULE_PATTERN.match(line.strip())

    if not match:
        raise ValueError(f"Invalid rule syntax: {line}")

    condition_expr = match.group(1)
    then_action = match.group(2)
    else_action = match.group(3)

    condition = Condition(expression=condition_expr)

    then = Outcome(action=then_action)

    otherwise = None
    if else_action:
        otherwise = Outcome(action=else_action)

    return Rule(
        rule_id=rule_id,
        condition=condition,
        then=then,
        otherwise=otherwise
    )


def parse_contract(text: str) -> DecisionContract:
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    rules: List[Rule] = []

    for i, line in enumerate(lines):
        rule = parse_rule(f"rule_{i+1}", line)
        rules.append(rule)

    return DecisionContract(
        contract_id="contract_example",
        name="Example Contract",
        version="1.0",
        inputs=[],
        rules=rules
    )
