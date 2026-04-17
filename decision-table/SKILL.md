---
name: decision-table
description: Use this skill when requirements describe discrete business rules, multiple conditions, or outcome logic that should be modeled as a rule table.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-output-artifacts: decision_table, test_cases, rule_coverage_summary
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-input-artifacts: requirements, rule_conditions, outcomes, traceability_context
  dispatcher-capabilities: test-design, decision-table-analysis, rule-modeling
  dispatcher-stack-tags: testing, design, rule-based
  dispatcher-accepted-intents: design_decision_table_tests, model_business_rules
  dispatcher-category: testing
---

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

# Decision Table

## Read First

- `./references/decision-table.md`
- `./references/test-design-shared-conventions.md`
- `./assets/templates/decision-table.j2`
- `./assets/templates/optimized-decision-table.j2`
- `./assets/templates/test-case-table.j2`

## Workflow

1. Extract conditions and resulting actions.
2. Distinguish stated rules from unstated combinations.
3. Build the full rule space only as far as the requirement supports it.
4. Mark impossible or unspecified combinations explicitly.
5. Optimize only when multiple columns truly produce the same outcome and the same oracle.
6. Derive one scenario per retained rule column.

## Required Output

- condition list
- action list
- full or partially constrained decision table
- optimized decision table when valid
- scenario list tied back to retained rules

## Guardrails

- Do not invent policy for unspecified combinations.
- Do not use "don't care" to hide a meaningful rule difference.
- Prefer a coverage gap note over a fake complete matrix.