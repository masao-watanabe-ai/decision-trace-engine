# Behavior Tree Reference

This directory contains a minimal reference implementation
for parsing and validating Behavior Tree definitions used
in the Decision Trace Model.

The purpose of this code is not to provide a full production
runtime, but to illustrate how execution structures can be
represented explicitly and transformed into structured objects.

---

## Supported Node Types

- `Sequence`
- `Selector`
- `Condition`
- `Action`

These node types are sufficient to demonstrate the core
execution structure of traceable decision workflows.

---

## Example YAML

```yaml
tree_id: bt_retail_001
name: Store Promotion Flow
version: "1.0"
domain: retail

root:
  type: Selector
  id: root_selector
  children:
    - type: Sequence
      id: high_inventory_sequence
      children:
        - type: Condition
          id: inventory_check
          condition:
            expression: inventory_risk == "high"
        - type: Action
          id: apply_discount_action
          action:
            name: apply_discount
    - type: Action
      id: no_action_fallback
      action:
        name: no_promotion
Example Usage
from pathlib import Path
from src.behavior_tree import parse_behavior_tree, validate_behavior_tree

text = Path("behavior-tree.yaml").read_text()
tree = parse_behavior_tree(text)
validate_behavior_tree(tree)

print(tree)
Purpose
This implementation serves as a reference example showing:
how behavior trees can be represented in YAML
how execution structures can be parsed into objects
how decision flow can be separated from application code
For a full runtime implementation see:
decision-trace-engine

---

# 6. あると良いサンプルファイル

`src/behavior_tree/` にこれも置くと見やすいです。

## `src/behavior_tree/example-tree.yaml`

```yaml
tree_id: bt_example_001
name: Fraud Review Flow
version: "1.0"
domain: fraud

root:
  type: Selector
  id: root_selector
  children:
    - type: Sequence
      id: fraud_sequence
      children:
        - type: Condition
          id: fraud_check
          condition:
            expression: fraud_proba
