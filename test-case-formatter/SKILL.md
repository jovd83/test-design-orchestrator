---
name: test-case-formatter
description: Compatibility bridge for the old test-design-orchestrator formatter entrypoint. Prefer the standalone `test-artifact-export-skill` skill for formatting existing test cases, BDD/TDD/plain-text rendering, and tool-export artifacts.
metadata:
  author: jovd83
  version: v2.0.0
  dispatcher-output-artifacts: formatted_test_artifact, export_bundle, compatibility_guidance
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-input-artifacts: approved_test_cases, export_preferences, target_format, traceability_context
  dispatcher-capabilities: test-artifact-formatting-bridge, export-routing, compatibility-bridge
  dispatcher-stack-tags: testing, formatting, compatibility
  dispatcher-accepted-intents: render_test_artifact, export_test_cases, format_test_cases
  dispatcher-category: testing
---
# Test Case Formatter

This formatter is no longer the canonical entrypoint.

Use `skill-dispatcher` to route `render_test_artifact`, `format_test_cases`, or `export_test_cases` to the active formatting skill. Keep `C:\projects\skills\test-artifact-export-skill\SKILL.md` only as the fallback compatibility target when dispatcher routing is unavailable.


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## Migration Rule

- Route formatting and export requests through `skill-dispatcher` first, using `render_test_artifact`, `format_test_cases`, or `export_test_cases`.
- Use `C:\projects\skills\test-artifact-export-skill\SKILL.md` only as a fallback when dispatcher routing is unavailable.
- Do not expand this compatibility bridge with new output contracts.
