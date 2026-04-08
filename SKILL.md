---
name: test-design-orchestrator
description: Use this skill when Codex needs to turn requirements, user stories, acceptance criteria, business rules, use cases, or state models into structured software test artifacts. It selects the most appropriate black-box test design technique and routes work to the matching generation subskill. When the work is already designed and only needs formatting or export, prefer the standalone `test-artifact-export-skill` skill.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-category: testing
  dispatcher-capabilities: test-design, black-box-technique-selection, confirmation-test-design
  dispatcher-accepted-intents: design_confirmation_tests, select_test_design_technique, generate_structured_test_cases
  dispatcher-input-artifacts: requirement_text, acceptance_criteria, user_story, business_rules, use_case, state_model
  dispatcher-output-artifacts: test_case_set, technique_selection, assumptions_log, routing_request
  dispatcher-stack-tags: testing, framework-agnostic, black-box
  dispatcher-risk: medium
  dispatcher-writes-files: false
---

# Test Design Orchestrator

Coordinate a disciplined test-design workflow instead of free-form brainstorming.

## Goal

Produce traceable, reviewable test artifacts from incomplete product or requirements inputs while keeping assumptions explicit and technique choice defensible.

## Input Contract

Accept any of the following as the starting artifact:

- requirement text
- acceptance criteria or user stories
- business rules or decision logic
- use cases or workflow descriptions
- state models or lifecycle descriptions
- partially structured test ideas that still need technique selection or formatting

Capture these optional signals when present:

- target format or test-management tool
- risk focus or priority areas
- traceability identifiers such as story IDs or requirement IDs
- coverage target such as happy path only, full negative coverage, pairwise, or all transitions
- explicit user preference for a specific technique

## Output Contract

When the user does not request an import-ready format, return a concise package with:

1. normalized requirement summary
2. selected primary technique and brief rationale
3. explicit assumptions and open gaps
4. generated test artifacts
5. coverage notes or residual risk

When the user requests an import-ready format, finish with only the formatted artifact unless a blocking clarification is required.

## Memory Model

Use a small runtime scratchpad while working:

- normalized requirement
- selected technique
- assumptions and unresolved questions
- requested output format
- traceability IDs

Do not persist this scratchpad automatically.

Project-local persistent memory is optional and only appropriate when the user explicitly asks to save a reusable test-design brief or when the task spans multiple passes in the user's project.

Shared memory is out of scope for this skill. If the user wants cross-project or cross-agent reuse, integrate an external shared-memory skill instead of storing shared knowledge here.

## Dispatcher Integration

Use `skill-dispatcher` as the primary integration layer whenever this skill needs help beyond its own technique-selection and generation scope.

- Prefer dispatching by intent instead of naming an external sibling skill directly.
- Keep direct skill paths as a compatibility fallback only when the dispatcher has no valid registry match.
- Keep shared memory limited to stable cross-project policy, not task-local routing decisions.
- Preserve this skill's role: choose and apply black-box design techniques, then hand off formatting or downstream execution only when needed.

## Execution Workflow

### 1. Normalize the Request

- Identify the source artifact type.
- Extract constraints, actors, inputs, rules, states, and required outputs.
- If critical information is missing, ask one focused clarification round before continuing.
- Default to review-ready markdown if no format is specified.

### 2. Choose the Technique

- If the user explicitly requests a valid technique, honor it and note any mismatch risk.
- Otherwise, read and apply `./technique-selector/SKILL.md`.
- Use `./references/technique-selection-matrix.md` and `./references/test-design-shared-conventions.md` as the shared decision baseline.
- Prefer one primary technique. Add a secondary technique only when it closes a real coverage gap that the primary technique cannot address.

### 3. Route to the Execution Subskill

Map the chosen technique to exactly one primary generation subskill:

- `Boundary Value Analysis` -> `./boundary-value-analysis/SKILL.md`
- `Equivalence Partitioning` -> `./equivalence-partitioning/SKILL.md`
- `Decision Table` -> `./decision-table/SKILL.md`
- `Classification Tree / N-Wise` -> `./classification-tree-nwise/SKILL.md`
- `State Transition` -> `./state-transition/SKILL.md`
- `Acceptance Criteria to Test Cases` -> `./acceptance-criteria-to-test-cases/SKILL.md`
- `Use Case Testing` -> `./use-case-testing/SKILL.md`

Read the selected subskill and its referenced guidance before generating output.

### 4. Hand Off Formatting And Export

- If the user wants import-ready, narrative-format, or tool-specific output after the tests are designed, dispatch `render_test_artifact` through `skill-dispatcher`.
- Use `C:\projects\skills\test-artifact-export-skill\SKILL.md` only as a compatibility fallback when dispatcher routing is unavailable.
- Keep this skill focused on technique selection and test generation.
- Keep unsupported formats out of scope. Do not invent schemas or field mappings.

### 5. Finalize Cleanly

- Distinguish source facts from inferred assumptions.
- Call out unresolved ambiguities instead of silently filling them in.
- Keep negative tests independent when combined invalid data would hide the real defect signal.
- Avoid combinatorial explosion. If the input would create an impractical Cartesian product, explain the reduction strategy and use the minimum coverage level that still matches the user's request.

## Guardrails

- Do not fabricate requirements, states, rules, or expected outcomes.
- Do not claim "full coverage" unless the artifact actually supports it.
- Do not mix multiple techniques into one table unless the user explicitly asks for a hybrid deliverable.
- Do not browse for missing external schemas from inside this skill. If a format is unsupported, say so plainly.
- Treat templates as output contracts, not as sources of missing business logic.

## Gotchas

- **Combinatorial Explosion**: Applying techniques like Decision Tables or Classification Trees to many variables can quickly lead to an unmanageable number of test cases. Always use reduction strategies (like N-Wise) and explain the coverage trade-off.
- **Weak Oracles**: If the input requirements do not define expected outcomes for specific inputs or state transitions, the generated tests will have weak or generic oracles. Call these out as assumptions or open gaps.
- **Masking Defects**: Combining multiple invalid inputs into a single test case can mask the true cause of a failure. Keep negative test cases independent unless specifically testing system resilience to multiple errors.
- **Assumption Silencing**: It is tempting to "fill in the blanks" when requirements are vague (e.g., assuming a range is inclusive). Always make these inferences explicit to avoid a false sense of test accuracy.
- **Transition Dead Ends**: In state-transition testing, missing requirements for "uncovered" events in certain states can lead to incomplete test suites. Explicitly identify states with no defined exit paths for common events.
- **Tool-Specific Field Misalignment**: When exporting to external tools (e.g., Zephyr, Xray), missing source metadata like priority or story IDs can result in incomplete import files. This skill does not fabricate these IDs; it uses placeholders or asks for them.

## Reference Map

- Shared conventions: `./references/test-design-shared-conventions.md`
- Technique selection: `./references/technique-selection-matrix.md`
- Output rules for generated artifacts before export: `./references/formatting-guidelines.md`
- Templates: `./assets/templates/`

## Quality Checks

Before finishing, confirm that:

- the selected technique matches the shape of the problem
- every generated test has a clear oracle
- assumptions are visible
- traceability is preserved when IDs were supplied
- the response format matches the user's requested destination
