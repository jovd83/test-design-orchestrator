# BDD Feature Protocol

Use this guide when producing feature files from acceptance criteria or behavior-focused test design.

## Feature Scope

- Keep one feature file centered on one capability, story, or coherent business rule set.
- Split features when a file becomes hard to review or combines unrelated behavior.

## Recommended Structure

```gherkin
Feature: Capability name
  As a role
  I want a capability
  So that a business outcome is achieved
```

Use these optional sections only when they improve clarity:

- `Background:` for shared setup
- `Rule:` for clustered business rules
- `Scenario Outline:` for controlled data variation

## Tagging

Use tags only when they carry real meaning, such as:

- requirement ID
- persona or actor
- execution type
- risk or path type

## Quality Bar

- Feature titles should read like business intent, not ticket labels.
- Scenarios should stay readable by product, QA, and engineering stakeholders.
- Keep feature files deterministic enough that the expected outcome is reviewable without the implementation.
