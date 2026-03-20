# State Transition Reference

Use state-transition testing when behavior depends on the current state and the legality of the next event.

## Best-Fit Inputs

- lifecycle workflows
- approval pipelines
- session or account status changes
- devices or services with operating modes

## Core Steps

1. Identify states.
2. Identify events and guard conditions.
3. Map the resulting next state and action.
4. Choose the coverage target:
   - all states
   - all transitions
   - switch coverage
5. Add invalid-transition scenarios when the rejection behavior is defined.

## Typical Output

- state list
- transition table
- path inventory
- negative-transition tests

## Common Failure Modes

- confusing process steps with persistent states
- omitting the start state
- assuming invalid transitions without knowing expected behavior
