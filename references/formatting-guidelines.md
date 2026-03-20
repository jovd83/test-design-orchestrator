# Formatting Guidelines

Use this file when rendering output, not when choosing the test logic.

## Review-Ready Markdown

- Start with a short title or section heading.
- Prefer tables for summaries and step-by-step lists for execution detail.
- Keep IDs stable across summary tables and detailed cases.

## BDD Feature Output

- Use plain Gherkin with `Feature`, `Scenario`, `Given`, `When`, and `Then`.
- Add tags only when you have meaningful traceability or execution metadata.
- Keep each scenario focused on one observable behavior.

## Xray Gherkin Output

- Use valid plain Gherkin feature files.
- Prefer stable requirement tags when traceability exists.
- Keep the feature portable so it can be imported directly or packaged into a zip bundle.

## Zephyr Scale CSV

- Do not generate a CSV row until every required field is known.
- Escape embedded quotes, commas, or newlines before rendering.
- Repeat parent test case metadata only as required by the import contract.

## TestLink-Oriented Output

- Follow the bundled PDF reference.
- Stop and ask when the input is missing fields required by the chosen import shape.
- Prefer explicit placeholders only when the target workflow formally allows them.

## Formatting Guardrails

- Do not invent metadata just to satisfy a template.
- Do not mix analysis commentary into import-ready output.
- If the user wants a human-review artifact, optimize for clarity instead of for raw import syntax.
