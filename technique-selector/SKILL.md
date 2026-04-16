---
name: technique-selector
description: Use this skill when Codex needs to choose the best black-box test design technique for a requirement, user story, rule set, workflow, or state model before generating tests.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-output-artifacts: technique_selection, routing_decision, rationale
  dispatcher-risk: low
  dispatcher-writes-files: false
  dispatcher-input-artifacts: requirements, analysis_context, risk_notes, design_constraints
  dispatcher-capabilities: test-technique-selection, black-box-analysis, design-routing
  dispatcher-stack-tags: testing, design, orchestration
  dispatcher-accepted-intents: select_test_design_technique, route_test_design_request
  dispatcher-category: testing
---
# Technique Selector

Select the best-fit technique. Do not generate the final test cases here.


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## Read First

- `./references/technique-selection-matrix.md`
- `./references/test-design-shared-conventions.md`

## Decision Process

1. Identify the dominant problem shape:
   - ordered ranges or limits
   - equivalence classes
   - discrete rules and outcomes
   - interacting parameters
   - states and transitions
   - actor-system flows
   - acceptance criteria at behavior level
2. Check whether the user already mandated a technique.
3. If the scenario is too vague to distinguish between two plausible techniques, ask a focused clarification question instead of guessing.
4. Prefer the technique that best matches the main defect risk, not the technique that produces the largest number of tests.

## Required Output

Return a compact recommendation with exactly these sections:

- `Primary technique`
- `Why it fits`
- `Secondary option`
- `Why not the others`
- `Missing information`, only if the analysis is blocked or materially uncertain

## Guardrails

- Recommend one primary technique.
- Name a secondary option only when it is genuinely plausible.
- If the artifact mixes several shapes, choose the one that should drive the first pass and mention any residual gap briefly.
- Do not produce tables, test steps, or detailed scenarios in this skill.
