# Classification Tree and N-Wise Reference

Use this technique when several parameters interact and exhaustive testing is too large.

## Best-Fit Inputs

- configurable product options
- forms with many independent selectors
- combinatorial integration points
- matrices of channels, roles, products, or environments

## Core Steps

1. Define classifications.
2. List allowed values in each classification.
3. Record invalid or impossible combinations first.
4. Pick the interaction depth:
   - minimum criterion for broad smoke coverage
   - pairwise for default interaction coverage
   - 3-wise or higher only when justified
5. Generate the reduced combination set and explain what is not covered.

## Typical Output

- classification inventory
- constraints
- reduced data combination set
- coverage rationale

## Common Failure Modes

- generating the full Cartesian product by habit
- ignoring constraints until after case generation
- using high-order combinations without a risk reason
