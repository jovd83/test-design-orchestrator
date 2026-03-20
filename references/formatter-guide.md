# Formatter Guide

Use the formatter only after the test logic is already designed.

## Supported Formats

- review-ready markdown
- BDD feature text
- Xray-compatible Gherkin feature files
- Zephyr Scale CSV
- TestLink-oriented output based on the bundled PDF reference

## Minimum Input Fields

Different targets need different metadata, but most formatted outputs require:

- title or scenario name
- traceability reference when available
- preconditions or starting context
- ordered steps or Given-When-Then flow
- expected result

For Zephyr Scale or TestLink, additional fields may be required by the target import workflow.

## Formatting Strategy

1. Normalize the source artifact into a stable internal structure.
2. Check which required fields are missing for the chosen target.
3. Ask for the missing required fields.
4. Render the output without adding analysis commentary.

## Unsupported Requests

If a user requests a tool that is not backed by a bundled contract in this repository, say that it is unsupported in the current implementation rather than improvising a schema.
