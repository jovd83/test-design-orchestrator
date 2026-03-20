# Example Prompt: State Transition

Use $test-design-orchestrator to derive tests for this account lifecycle:

- A new account starts in `Pending Verification`.
- Verifying email moves the account to `Active`.
- Suspected fraud moves the account to `Suspended` from any active state.
- Admin review can move `Suspended` to `Active` or `Closed`.
- A `Closed` account cannot transition back to any other state.

Expected primary technique: `State Transition`

Why:

- legal behavior depends on current state
- invalid transitions matter
