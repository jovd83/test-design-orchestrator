---
name: state-transition
description: Use this skill when a system has discrete states, events, guards, or lifecycle phases and Codex needs transition-focused test design.
metadata:
  author: jovd83
  version: v2.0.0
---

# State Transition

## Read First

- `./references/state-transition.md`
- `./references/test-design-shared-conventions.md`
- `./assets/templates/state-table.j2`
- `./assets/templates/state-transition-table.j2`
- `./assets/templates/test-case-list.j2`

## Workflow

1. Identify states, events, guards, and resulting actions.
2. Confirm the start state and invalid-transition behavior when the requirement does not make them obvious.
3. Build a transition model before writing tests.
4. Select the coverage target: all states, all transitions, or switch coverage.
5. Include invalid-transition tests when the system rejects illegal events explicitly.

## Required Output

- state inventory
- transition model
- path set for the requested coverage level
- negative-transition scenarios when supported
- traceable test list

## Guardrails

- Do not use state-transition testing when the requirement is really just a rule matrix or a simple range check.
- Do not invent hidden states to make the model look complete.
- Separate valid transitions from inferred invalid ones.
