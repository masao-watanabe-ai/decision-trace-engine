contract:
  name: material_selection
  version: 1.0
  domain: manufacturing
  description: Material selection contract for corrosion-sensitive components

inputs:

  event:
    component_type
    operating_environment
    temperature

  signals:
    corrosion_risk
    cost_increase
    procurement_delay
    safety_margin

options:

  - id: SUS304
    description: Standard stainless steel
    cost_level: low
    corrosion_resistance: medium

  - id: SUS316
    description: High corrosion resistance stainless steel
    cost_level: high
    corrosion_resistance: high

concerns:

  - corrosion_risk
  - cost_increase
  - procurement_delay
  - safety_margin

evaluation:

  corrosion_risk:
    type: categorical
    values: [low, medium, high]

  cost_increase:
    type: categorical
    values: [low, medium, high]

  procurement_delay:
    type: categorical
    values: [low, medium, high]

rules:

  - rule_id: R1
    description: Use SUS316 when corrosion risk is high
    condition:
      corrosion_risk: high
    decision:
      select_option: SUS316
      reason: corrosion_protection

  - rule_id: R2
    description: Use SUS304 when corrosion risk is low and cost pressure is high
    condition:
      corrosion_risk: low
      cost_increase: high
    decision:
      select_option: SUS304
      reason: cost_optimization

  - rule_id: R3
    description: Prefer SUS316 when safety margin is critical
    condition:
      safety_margin: low
    decision:
      select_option: SUS316
      reason: safety_priority

stop_conditions:

  - id: SC1
    description: Test results not available
    trigger: test_result_missing

  - id: SC2
    description: Safety standard verification incomplete
    trigger: safety_standard_unconfirmed

output:

  decision:
    selected_option
    decision_reason
    rule_applied

ledger_record:

  record_event: true
  record_signals: true
  record_rule: true
  record_decision: true
  record_timestamp: true
