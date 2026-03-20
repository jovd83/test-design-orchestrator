---
name: use-case-testing
description: Use this skill when requirements are expressed as actor-system interactions with preconditions, main flows, alternate flows, and postconditions.
metadata:
  author: jovd83
  version: v2.0.0
---

# Use Case Testing

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
