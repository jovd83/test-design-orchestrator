---
name: test-case-formatter
description: Compatibility bridge for the old test-design-orchestrator formatter entrypoint. Prefer the standalone `test-artifact-export-skill` skill for formatting existing test cases, BDD/TDD/plain-text rendering, and tool-export artifacts.
metadata:
  author: jovd83
  version: v2.0.0
---

# Test Case Formatter

This formatter is no longer the canonical entrypoint.

Use `C:\projects\skills\test-artifact-export-skill\SKILL.md` for all new formatting and export work. Keep this file only as a compatibility pointer for older references inside the orchestrator family.

## Migration Rule

- Route formatting and export requests to `C:\projects\skills\test-artifact-export-skill\SKILL.md`.
- Do not expand this compatibility bridge with new output contracts.
