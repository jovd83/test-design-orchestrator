# Test Design Orchestrator

`test-design-orchestrator` is an AgentSkill for turning requirements into structured, traceable software test artifacts. It is built as a composite skill: the root skill chooses the best-fit black-box test design technique, routes execution to a technique-specific subskill, and optionally formats the result for downstream tooling.

This repository is intentionally split into two layers:

- the installable skill itself: `SKILL.md`, subskill folders, `references/`, `assets/templates/`, `agents/openai.yaml`
- repository-facing support material: `README.md`, `examples/`, `evals/`, and validation scripts

## What This Skill Does

- Selects an appropriate test design technique for a given requirement shape.
- Generates test artifacts using boundary value analysis, equivalence partitioning, decision tables, classification trees with n-wise reduction, state transitions, acceptance criteria, or use case analysis.
- Preserves traceability, assumptions, and coverage notes.
- Formats output for review-ready markdown, BDD feature files, Xray-compatible Gherkin feature bundles, Zephyr Scale CSV, or TestLink-oriented import workflows.

## What This Skill Does Not Do

- It does not replace domain requirements analysis. Missing business rules are surfaced, not invented.
- It does not provide shared-memory infrastructure. Cross-agent memory belongs in a separate shared-memory skill.
- It does not claim support for every ALM tool beyond the bundled targets and references.

## Repository Layout

```text
.
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- acceptance-criteria-to-test-cases/
|-- boundary-value-analysis/
|-- classification-tree-nwise/
|-- decision-table/
|-- equivalence-partitioning/
|-- state-transition/
|-- technique-selector/
|-- test-case-formatter/
|-- use-case-testing/
|-- references/
|-- assets/templates/
|-- examples/
|-- evals/
`-- scripts/
```

## Supported Workflow

1. Normalize the request into inputs, rules, actors, states, and desired outputs.
2. Choose one primary test design technique with a defensible rationale.
3. Generate the test artifacts using the matching subskill.
4. Format only when the user asks for a specific target representation.
5. Return assumptions, traceability, and residual risk with the artifact unless the user requested artifact-only output.

## Installation

Install from GitHub with `npx skills`:

```bash
npx skills add <owner>/<repo> --skill test-design-orchestrator
```

If your installer supports direct GitHub URLs, this form is also commonly used:

```bash
npx skills add https://github.com/<owner>/<repo> --skill test-design-orchestrator
```

After installation, restart Codex so it reloads the newly installed skill.

For a manual install, place this folder in your skill directory and publish it under a lowercase hyphen-case folder name such as `test-design-orchestrator`.

The required installable files are:

- `SKILL.md`
- subskill `SKILL.md` files
- `agents/openai.yaml`

Everything else is supportive but strongly recommended for maintainability.

## Inputs and Outputs

Useful inputs include:

- raw requirements
- business rules
- user stories and acceptance criteria
- use cases
- lifecycle or state descriptions
- a requested export target such as markdown, BDD, Xray Gherkin, Zephyr Scale, or TestLink

Typical outputs include:

- technique recommendation with rationale
- partition tables and representative values
- decision tables and optimized rules
- transition paths and invalid-transition tests
- scenario lists and detailed test cases
- import-oriented formatted artifacts

## Memory Model

Runtime memory:

- ephemeral only
- used for requirement normalization, assumptions, traceability IDs, and current output format

Project-local persistent memory:

- optional
- only appropriate when the user explicitly wants a reusable test-design brief saved in their project

Shared memory:

- intentionally excluded from this repository
- integrate an external shared-memory skill if cross-agent reuse is required

## Validation and Evaluation

Run the repository checks:

```powershell
python scripts/validate-skill-repo.py
python scripts/format-validator.py bdd examples/checkout-feature.feature
python scripts/package-xray-features.py examples/xray-checkout.feature --output dist/xray-features.zip
```

Use the evaluation fixtures:

- `evals/trigger-queries.json` for description triggering checks
- `evals/technique-selection-cases.json` for manual or agent-assisted forward testing

Use the prompt examples in `examples/` to sanity-check the end-to-end workflow.

## Optional Integrations

- `assets/templates/zephyr-scale.csv.j2` for Zephyr Scale CSV generation
- `assets/templates/xray-gherkin.feature.j2` plus `scripts/package-xray-features.py` for Xray Gherkin feature import bundles
- `references/testlink-import-file-formats.pdf` for TestLink import guidance
- `assets/templates/bdd-feature.j2` plus the BDD protocol references for feature-file output

These integrations are supported only to the extent that the bundled templates and references cover them. If a target tool requires fields that are not available in the input, the skill should stop and ask for them.

## Contributing

Keep changes tightly scoped and auditable:

- improve trigger quality by updating `SKILL.md` and `evals/trigger-queries.json` together
- keep technique guidance in `references/` concise and technique-specific
- keep renderable output contracts in `assets/templates/`
- add or update example prompts whenever the workflow changes materially

## License

This repository is released under the MIT License. See [LICENSE](./LICENSE).

## Publishing Notes

Before publishing to GitHub or a skill registry:

- rename the repository folder to lowercase hyphen-case
- run `python scripts/validate-skill-repo.py`
- optionally run the upstream skill quick validator against the root folder
