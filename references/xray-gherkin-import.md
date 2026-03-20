# Xray Gherkin Import Reference

This repository supports Xray through Gherkin `.feature` files and zipped feature bundles.

## Supported Contract

- one or more `.feature` files
- plain Gherkin syntax with `Feature`, `Scenario`, `Given`, `When`, and `Then`
- optional tags for traceability
- optional zip packaging when a CI or import workflow wants a bundled archive

## Practical Rules

- Keep feature files valid plain Gherkin.
- Preserve traceability tags when they exist.
- Package multiple feature files into a `.zip` only after validating them as Gherkin.
- Stay within feature-file import support; do not improvise unsupported Xray JSON schemas in this repository.
