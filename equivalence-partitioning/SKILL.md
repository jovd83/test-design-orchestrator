---
name: equivalence-partitioning
description: Use this skill when Codex needs to derive representative tests from input classes that should behave the same within each valid or invalid partition.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-output-artifacts: equivalence_partitions, test_cases, coverage_summary
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-input-artifacts: requirements, input_domains, validation_rules, traceability_context
  dispatcher-capabilities: test-design, equivalence-partitioning, partition-analysis
  dispatcher-stack-tags: testing, design, partitioning
  dispatcher-accepted-intents: design_equivalence_partition_tests, define_input_partitions
  dispatcher-category: testing
---
# Equivalence Partitioning

## Read First

- `./references/equivalence-partitioning.md`
- `./references/test-design-shared-conventions.md`
- `./assets/templates/partition-table.j2`
- `./assets/templates/test-case-table.j2`
- `./assets/templates/optimized-test-case-table.j2`
- `./assets/templates/coverage-summary.j2`

## Workflow

1. Identify each input dimension that can be divided into behaviorally equivalent classes.
2. Define valid and invalid partitions in language the user can audit.
3. Choose one representative value per partition unless the user requests deeper sampling.
4. Combine valid representatives only when it does not hide which partition is responsible for a failure.
5. Keep invalid representatives isolated by default.

## Required Output

- partition table with rationale
- representative values
- test case set
- optimized set when valid combinations can be reduced safely
- coverage summary

## Guardrails

- Do not collapse partitions that produce meaningfully different system behavior.
- Do not claim equivalence without stating the rule that makes values interchangeable.
- Hand off to BVA instead when the main risk is boundary failure rather than class behavior.
