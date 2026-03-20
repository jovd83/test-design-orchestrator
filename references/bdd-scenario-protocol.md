# BDD Scenario Protocol

Use this guide to keep scenarios executable and audit-friendly.

## Scenario Shape

Each scenario should describe one observable path with:

- `Given` for starting context
- `When` for the triggering action or event
- `Then` for the expected outcome

Use `And` only when it keeps the scenario readable.

## Scenario Rules

- One scenario should cover one business behavior.
- Titles should describe outcome and context.
- Expected results must be observable, not aspirational.
- Keep steps implementation-agnostic unless the user asks for lower-level detail.

## Alternate and Negative Paths

- Add alternate scenarios when the system legitimately branches.
- Add negative scenarios when the expected rejection behavior is known.
- If a rejection path is plausible but undefined, call it a gap instead of writing a fake `Then`.

## Traceability

- Keep the acceptance criterion, rule ID, or path reference visible.
- Reuse stable labels across tables, feature files, and detailed test cases when both are present.
