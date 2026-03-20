# Example Prompt: Decision Table

Use $test-design-orchestrator to design review-ready tests for these rules:

- Approve the loan when the applicant is over 21, income is at least 40000, and fraud flag is false.
- Send for manual review when the applicant is over 21, income is at least 40000, and fraud flag is true.
- Reject the loan when the applicant is 21 or younger.
- Reject the loan when income is below 40000.

Expected primary technique: `Decision Table`

Why:

- the behavior is defined by discrete condition combinations
- the outcome depends on more than one independent rule input
