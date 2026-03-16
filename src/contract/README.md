# Decision Contract DSL

This directory contains a minimal reference implementation
for parsing Decision Contract DSL used in the Decision Trace Model.

The goal is not to provide a full production runtime,
but to illustrate how decision contracts can be interpreted
as structured decision rules.

---

## DSL Example
IF fraud_probability > 0.8
THEN escalate_to_human
ELSE approve_transaction

This rule means:

- If the fraud probability is higher than 0.8  
- escalate the decision to human review  
- otherwise approve the transaction.

---

## Example Usage

```python
from src.contract import load_contract

contract = load_contract("decision-contract.dsl")

print(contract)
This loads the DSL contract and converts it into a structured
DecisionContract object.
Purpose
This implementation serves as a reference example showing:
how decision contracts can be parsed
how decision logic can be externalized from application code
how contracts can later be executed by the Decision Trace Engine
For a full runtime implementation see:
decision-trace-engine
