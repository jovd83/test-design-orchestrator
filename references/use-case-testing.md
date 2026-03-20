# Use Case Testing Reference

Use use-case testing when the requirement is organized around actor goals, triggers, flows, and outcomes.

## Best-Fit Inputs

- formal use cases
- workflow narratives
- actor-centered interaction documents
- main flow plus alternate flow descriptions

## Core Steps

1. Identify actor, trigger, preconditions, and postconditions.
2. Walk the main success scenario.
3. Branch each alternate or exception path into its own testable scenario.
4. Keep path references visible in the output.

## Typical Output

- use-case summary
- path list
- main-flow and alternate-flow scenarios
- postcondition checks

## Common Failure Modes

- losing the alternate path reference
- testing only the happy path
- skipping the final state or business outcome
