---
name: re-review-checker
description: Verify whether prior review feedback has been addressed in the current code state. Use during follow-up MR reviews or when checking if previous review comments were resolved.
---

# Re-review Checker

Compare prior review feedback against the current code state to determine what has been addressed.

## Inputs Required

1. **Prior review comments** — from one or both of:
   - GitLab MR discussion notes/threads
   - A prior review artifact file (`reviews/<MR-ID>_review.md`)
2. **Current diff** — the latest unified diff of the MR

## Process

### Step 1: Extract Prior Issues
Parse all prior review comments and the prior review artifact (if it exists). Extract each distinct issue or feedback item.

### Step 2: Match Against Current Code
For each prior issue, check the current diff to determine if the relevant code has been changed in a way that addresses the feedback.

### Step 3: Classify Each Item

- **RESOLVED** — the issue has been addressed in the current code
- **PARTIALLY_ADDRESSED** — some aspect was fixed but the concern is not fully resolved
- **UNRESOLVED** — no change was made to address this issue

## Output

Return a structured follow-up table:

| # | Prior Issue Summary | Source | Status | Notes |
|---|---------------------|--------|--------|-------|
| 1 | Description | GitLab comment / Prior artifact | RESOLVED / PARTIALLY_ADDRESSED / UNRESOLVED | Brief explanation |

Followed by: **Summary** — X of Y prior issues resolved, Z remain open.

## Guidelines

- If no prior review context exists (first review), skip and state: "No prior review context available."
- Be precise about what was and wasn't addressed — don't mark RESOLVED unless the code clearly fixes the concern.
