# Boundary Reference

This directory contains a minimal reference implementation
for representing and evaluating boundaries used in the
Decision Trace Model.

A boundary defines the points where automated decisions
must be constrained by policy, safety, compliance,
or human responsibility.

The purpose of this code is not to provide a full production
policy engine, but to illustrate how boundary logic can be
externalized as explicit structures.

---

## What is a Boundary?

In the Decision Trace Model, a boundary represents a control point
where the system checks whether a decision can proceed safely.

Typical boundary outcomes include:

- `PASS`
- `FAIL`
- `ESCALATE`
- `BLOCK`

Examples:

- escalate high-risk decisions to human review
- block actions that violate safety constraints
- fail closed when policy conditions are not satisfied

---

## Example Boundary Definition

```yaml
boundary_id: boundary_fraud_001
name: Fraud Review Boundary
version: "1.0"
boundary_type: human_review
description: Escalates high-risk transactions to human review

rules:
  - rule_id: rule_001
    name: High Fraud Probability
    condition: fraud_probability > 0.8
    result: ESCALATE
    description: Escalate to human review when fraud probability is high

  - rule_id: rule_002
    name: Very High Transaction Amount
    condition: transaction_amount > 10000
    result: BLOCK
    description: Block transaction if amount exceeds operational limit
```

Example Usage
from src.boundary import load_boundary, validate_boundary, check_boundary

boundary = load_boundary("example-boundary.yaml")
validate_boundary(boundary)

context = {
    "fraud_probability": 0.91,
    "transaction_amount": 8500
}

result = check_boundary(boundary, context)
print(result)
Purpose
This implementation serves as a reference example showing:
how boundary logic can be externalized
how policy and safety checks can be represented explicitly
how human escalation points can be modeled
For a full runtime implementation see:
decision-trace-engine
