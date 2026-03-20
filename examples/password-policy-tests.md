### TC-BVA-001

**Title:** Reject password shorter than minimum length

**Description:** Validate the lower invalid boundary for password length.

**Technique:** Boundary Value Analysis

**Traceability**
- REQ-PASSWORD-LENGTH

**Preconditions**
1. The registration form is open.

**Steps**

| Step | Action | Expected Result |
|---|---|---|
| 1 | Enter a password with 7 characters. | The password is rejected. |
| 2 | Submit the form. | The user sees "Password length is invalid." |

**Metadata**

- Execution Type: Manual
- Design Status: Draft
- Test Suite: Registration Validation
