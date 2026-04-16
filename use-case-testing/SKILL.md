---
name: use-case-testing
description: Use this skill when requirements are expressed as actor-system interactions with preconditions, main flows, alternate flows, and postconditions.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-output-artifacts: use_case_tests, flow_map, coverage_summary
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-input-artifacts: use_case, actor_flows, preconditions, postconditions
  dispatcher-capabilities: test-design, use-case-analysis, flow-based-scenario-generation
  dispatcher-stack-tags: testing, design, use-case
  dispatcher-accepted-intents: design_use_case_tests, model_actor_system_flows
  dispatcher-category: testing
---
# Use Case Testing


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## Read First

- `./references/use-case-testing.md`
- `./references/test-design-shared-conventions.md`
- `./assets/templates/test-case-table.j2`
- `./assets/templates/test-case.j2`

## Workflow

1. Extract actor, trigger, preconditions, main success scenario, alternate flows, exceptions, and postconditions.
2. Generate at least one scenario for the main flow.
3. Generate separate scenarios for each alternate or exception path that changes system behavior or outcome.
4. Keep the path reference visible in every generated scenario.

## Required Output

- use-case summary
- path inventory
- scenario list or detailed test cases
- coverage note showing which flows are covered

## Guardrails

- Do not rewrite the use case into lower-level rule tables unless the user asks for a secondary pass.
- Do not skip postcondition checks on alternate paths.
