# Example Prompt: Boundary Value Analysis

Use $test-design-orchestrator to design tests for this requirement:

`Password length must be between 8 and 12 characters inclusive. Passwords shorter than 8 or longer than 12 must be rejected with the message "Password length is invalid."`

Expected primary technique: `Boundary Value Analysis`

Why:

- the dominant risk is at the stated inclusive limits
- the rejection behavior is explicit
