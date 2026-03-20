# Acceptance Criteria to Test Cases Reference

Use this approach when the source material is a user story or a list of acceptance criteria and the goal is behavior-focused scenarios.

## Best-Fit Inputs

- user stories with explicit acceptance criteria
- refinement notes with example behaviors
- requirements already phrased as user-observable outcomes

## Core Steps

1. Separate each acceptance criterion.
2. Identify the actor, trigger, and expected outcome.
3. Create at least one scenario per criterion.
4. Add alternate or negative scenarios only when the expected behavior is known or safely implied.
5. Preserve criterion-to-scenario traceability.

## Typical Output

- acceptance-criteria mapping table
- BDD scenarios or structured test cases
- coverage gaps for undefined negative behavior

## Common Failure Modes

- merging multiple criteria into one scenario and losing traceability
- inventing rejection behavior that the criteria never define
- turning vague language into hard assertions without flagging the assumption
