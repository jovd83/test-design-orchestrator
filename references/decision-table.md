# Decision Table Reference

Use decision tables when the requirement defines discrete conditions that combine into outcomes or actions.

## Best-Fit Inputs

- eligibility rules
- pricing or discount rules
- approval and rejection logic
- multi-flag policy decisions

## Core Steps

1. List the conditions.
2. List the actions or outcomes.
3. Enumerate stated combinations.
4. Mark impossible or unspecified combinations explicitly.
5. Optimize only when the outcome remains unchanged and auditable.

## Typical Output

- condition and action inventory
- decision table
- optimized decision table
- one scenario per retained rule

## Common Failure Modes

- inventing behavior for unstated combinations
- merging rule columns too aggressively
- hiding business ambiguity behind "don't care" cells
