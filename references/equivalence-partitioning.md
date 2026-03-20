# Equivalence Partitioning Reference

Use equivalence partitioning when many input values should behave the same and one representative value can stand in for the class.

## Best-Fit Inputs

- allowed and disallowed categories
- validated input classes
- ranges where the interior matters less than the class boundary
- protocol or format classes such as valid and invalid identifiers

## Core Steps

1. Identify each input condition.
2. Split it into valid and invalid classes.
3. Explain why values inside a class are expected to behave the same.
4. Choose one representative per class.
5. Combine valid representatives only when it keeps failures diagnosable.

## Typical Output

- partition table with rationale
- representative values
- full and optionally optimized test sets
- coverage statement

## Common Failure Modes

- treating every value as its own partition
- collapsing classes without behavioral evidence
- forgetting invalid partitions
- combining invalid representatives and obscuring the defect source
