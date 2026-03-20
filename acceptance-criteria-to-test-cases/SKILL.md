---
name: acceptance-criteria-to-test-cases
description: Use this skill when Codex needs to convert user stories or acceptance criteria into traceable behavior-focused scenarios or structured test cases.
metadata:
  author: jovd83
  version: v2.0.0
---

# Acceptance Criteria to Test Cases

## Read First

- `./references/acceptance-criteria-to-test-cases.md`
- `./references/bdd-feature-protocol.md`
- `./references/bdd-scenario-protocol.md`
- `./references/test-design-shared-conventions.md`
- `./assets/templates/bdd-feature.j2`
- `./assets/templates/test-case.j2`

## Workflow

1. Separate the user story, acceptance criteria, and any notes or examples.
2. Map each criterion to at least one observable scenario.
3. Add negative or alternate scenarios only when the expected behavior is explicit or safely inferable from the criterion set.
4. If the acceptance criteria are too thin to define the expected failure behavior, flag the gap instead of inventing it.
5. Keep a traceability map from each acceptance criterion to its scenarios or test cases.

## Required Output

- criterion-to-scenario mapping
- behavior scenarios in BDD or structured test-case form
- explicit assumptions and coverage gaps

## Guardrails

- Do not turn vague product wishes into deterministic assertions without saying they are assumptions.
- Do not merge unrelated acceptance criteria into a single scenario if traceability becomes muddy.
