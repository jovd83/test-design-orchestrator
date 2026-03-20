# Shared Test Design Conventions

Use these conventions across all subskills.

## Core Principles

- Keep source facts separate from inferred assumptions.
- Prefer the smallest useful test set that still matches the requested risk coverage.
- Preserve traceability whenever the input contains IDs or named requirements.
- Make each expected result observable and falsifiable.
- Stop and ask when a missing business rule changes the oracle, not just the wording.

## Default Deliverable Shape

Unless the user asks for import-ready output only, structure the response in this order:

1. requirement or scenario summary
2. assumptions and open questions
3. chosen technique and why it fits
4. generated artifacts
5. coverage notes and residual risk

## Traceability

- Carry forward requirement IDs, story IDs, use-case IDs, or rule IDs unchanged.
- If the input has no identifiers, create simple local labels such as `AC-1`, `RULE-2`, or `PATH-3`.
- Keep one artifact anchored to one dominant source item whenever possible.

## Assumptions

Mark assumptions explicitly when:

- inclusivity or exclusivity is unclear
- invalid-input behavior is not defined
- state transitions are implied but not stated
- combinatorial constraints are missing
- the tool-specific export requires metadata that the source does not provide

## Negative Coverage

- Keep invalid cases independent by default.
- Combine invalid conditions only for resilience or stress testing, and label that intent.
- If the system's expected rejection behavior is unknown, say so instead of inventing it.

## Optimization Rules

- Reduce test volume only when the oracle remains clear.
- Explain the reduction strategy for pairwise, rule-table optimization, or valid-value combination.
- Never describe a reduced set as exhaustive unless it truly is.

## Output Discipline

- Prefer markdown tables for review-ready summaries.
- Use tool-specific templates only when the user asks for them.
- If the user requests artifact-only output, remove commentary from the final artifact.
