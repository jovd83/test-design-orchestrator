---
name: boundary-value-analysis
description: Use this skill when a requirement contains ordered values such as ranges, lengths, dates, counts, or sequence limits and Codex needs boundary-focused test scenarios.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-output-artifacts: boundary_partitions, test_cases, coverage_summary
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-input-artifacts: requirements, value_ranges, constraints, traceability_context
  dispatcher-capabilities: test-design, boundary-value-analysis, partition-design
  dispatcher-stack-tags: testing, design, boundary-analysis
  dispatcher-accepted-intents: design_boundary_value_tests, identify_boundary_conditions
  dispatcher-category: testing
---
# Boundary Value Analysis


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## Read First

- `./references/boundary-value-analysis.md`
- `./references/test-design-shared-conventions.md`
- `./assets/templates/partition-table.j2`
- `./assets/templates/test-case-table.j2`
- `./assets/templates/test-case.j2`

## Workflow

1. Confirm the requirement has a true ordered boundary.
2. Extract each condition with its inclusive or exclusive limits.
3. If inclusivity, units, or the meaning of zero are unclear, ask before proceeding.
4. Use 3-value BVA by default: just below, on, and just above each boundary.
5. Use 2-value BVA only when the user explicitly asks for it.
6. Generate tests that keep the cause of failure obvious. Avoid combining multiple invalid boundaries in one test unless the user asks for stress coverage.

## Required Output

- boundary inventory
- boundary-to-test mapping
- detailed or summarized test cases, depending on the user's requested level of detail
- coverage note describing which boundaries were exercised

## Guardrails

- Do not treat unordered categories as BVA candidates.
- Do not invent boundaries that are not implied by the requirement.
- Separate inferred boundaries from stated ones.
