# Boundary Value Analysis Reference

Use BVA when the requirement defines ordered limits and the main defect risk is around those limits.

## Best-Fit Inputs

- numeric ranges
- text length limits
- date windows
- item counts
- ranked or sequential positions

## Core Steps

1. Identify each bounded condition.
2. Confirm whether the limits are inclusive or exclusive.
3. Define the valid region and invalid region around each boundary.
4. Generate values just below, on, and just above the boundary unless the user wants a smaller or larger set.

## Typical Output

- boundary inventory
- valid and invalid samples
- tests linked to each sampled boundary

## Common Failure Modes

- using BVA for unordered categories
- ignoring unit boundaries such as bytes versus characters
- missing the zero case when zero is meaningful
- mixing several invalid boundaries into one test and losing diagnostic value
