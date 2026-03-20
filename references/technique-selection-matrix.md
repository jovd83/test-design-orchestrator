# Technique Selection Matrix

Use this reference to choose the primary test design technique.

| Scenario shape | Primary technique | Why it fits | Common fallback |
|---|---|---|---|
| Numeric ranges, lengths, dates, counts, or ordered limits | Boundary Value Analysis | Finds off-by-one and edge-condition defects around stated boundaries | Equivalence Partitioning |
| Distinct valid or invalid value classes | Equivalence Partitioning | Samples one representative per behaviorally equivalent class | Boundary Value Analysis |
| Multiple discrete conditions leading to actions or outcomes | Decision Table | Makes rule coverage explicit and auditable | Classification Tree / N-Wise |
| Several interacting parameters with combinatorial risk | Classification Tree / N-Wise | Reduces combinations while preserving interaction coverage | Decision Table |
| Explicit states, events, guards, or lifecycle phases | State Transition | Focuses on valid and invalid transitions over time | Use Case Testing |
| Actor-system flows with main and alternate paths | Use Case Testing | Preserves end-to-end interaction intent | Acceptance Criteria to Test Cases |
| User stories or acceptance criteria written at behavior level | Acceptance Criteria to Test Cases | Converts behavior statements into traceable scenarios quickly | Use Case Testing |

## Fast Heuristics

- Pick BVA when the main risk is at the edges.
- Pick equivalence partitioning when the main risk is inside value classes.
- Pick decision tables when the requirement reads like "if these conditions, then this outcome."
- Pick classification trees or n-wise when several dimensions matter together and exhaustive coverage is impractical.
- Pick state transition when legality depends on current state.
- Pick use cases when the artifact is organized around actors and flows.
- Pick acceptance-criteria conversion when the source is already phrased as expected behavior.

## When to Pause

Ask for clarification when the choice depends on missing information such as:

- whether a range is inclusive or exclusive
- whether a flow has durable system states
- whether combinations are allowed or constrained
- whether acceptance criteria define only happy paths or also rejection behavior

## Hybrid Cases

Choose one primary technique for the first pass. Mention a secondary technique only when it closes a real gap, for example:

- Equivalence Partitioning plus BVA when partitions have explicit boundaries
- Use Case Testing plus Decision Table when one step contains dense rule logic
- State Transition plus BVA when events include threshold checks
