---
name: classification-tree-nwise
description: Use this skill when Codex needs to model interacting parameters and generate reduced pairwise or n-wise combinations instead of an impractical full Cartesian set.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-output-artifacts: classification_tree, nwise_matrix, test_cases
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-input-artifacts: requirements, parameters, interaction_constraints, traceability_context
  dispatcher-capabilities: test-design, classification-tree, n-wise-generation
  dispatcher-stack-tags: testing, design, combinatorial
  dispatcher-accepted-intents: design_nwise_tests, model_parameter_interactions
  dispatcher-category: testing
---

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

# Classification Tree and N-Wise Testing

## Read First

- `./references/classification-tree-nwise.md`
- `./references/test-design-shared-conventions.md`
- `./assets/templates/minimum-criterion-table.j2`
- `./assets/templates/pairwise-table.j2`
- `./assets/templates/threewise-table.j2`
- `./assets/templates/nwise-table.j2`

## Workflow

1. List classifications and allowed values.
2. Capture constraints and impossible combinations before generating data.
3. Default to pairwise coverage unless the user asks for a different interaction depth.
4. Escalate to 3-wise or n-wise only when the risk justifies the extra volume.
5. Preserve traceability from each generated combination back to the parameter values it covers.

## Required Output

- classification inventory
- explicit constraint list
- selected interaction depth and rationale
- generated combination set
- note on remaining uncovered higher-order interactions

## Guardrails

- Do not emit a full Cartesian product unless the user explicitly wants exhaustive coverage or the space is already small.
- Remove impossible combinations before counting coverage.
- If one parameter dominates the risk, say so instead of pretending all dimensions matter equally.