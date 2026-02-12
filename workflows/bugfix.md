# Workflow: Bugfix

## Purpose
This workflow defines the end-to-end process for fixing a bug from a Jira ticket:
Jira → Spec → Reproduction → Regression Test → Fix → Review → Verify → Update Jira → Write Notes

It enforces:
- Clear understanding of the bug
- A failing test that reproduces the issue
- A fix that makes the test pass
- Protection against regressions
- Honest status updates to Jira
- Long-term project memory via notes

---

## Entry Criteria

- A Jira ticket ID is provided (e.g., JIRA-5678)
- Jira MCP server is available
- Repo contains:
  - agents/
  - templates/
  - docs/steering/
  - knowledge/
  - project.md (optional but recommended)

---

## Step-by-Step Flow

### Step 1: Ingest Jira Ticket → Create Spec
**Agent:** Jira Ingest  
**Input:** Jira ticket ID  
**Output:** docs/specs/<TICKET-ID>.md  

**Gate:**  
- Spec clearly describes:
  - Observed behavior (the bug)
  - Expected behavior
  - Any known conditions or steps to reproduce
- Acceptance criteria reflect:
  - Bug is fixed
  - No regression for related behavior

If reproduction steps are missing or unclear:
- Add them to "Open Questions" in the spec
- Do not proceed until clarified as much as possible

---

### Step 2: Create Fix Plan
**Agent:** Planner  
**Input:** docs/specs/<TICKET-ID>.md  
**Output:** docs/specs/<TICKET-ID>.plan.md  

**Gate:**  
- Plan includes:
  - Hypothesis about root cause
  - Where to add regression test
  - Where the fix is likely to go
  - Risks of the change

---

### Step 3: Write Regression Test (Reproduce the Bug)
**Agent:** Tester  
**Input:**  
- Spec
- Plan
- Current code  
**Output:**  
- A new or updated test that:
  - Fails due to the bug
  - Clearly demonstrates the incorrect behavior

**Gate:**  
- The test must fail before the fix
- The failure must correspond to the bug described in the spec

If the bug cannot be reproduced in a test:
- Call it out explicitly
- Decide whether to proceed with:
  - Manual reproduction steps, or
  - Better instrumentation / logging first

---

### Step 4: Implement the Fix
**Agent:** Implementer  
**Input:**  
- Spec
- Plan
- Failing test  
**Output:** Code changes that fix the bug  

**Gate:**  
- The previously failing test now passes
- No unrelated behavior is changed
- The fix is minimal and targeted

---

### Step 5: Review the Fix
**Agent:** Reviewer  
**Input:**  
- Spec
- Plan
- Code changes
- Tests  
**Output:** Review report (PASS / NEEDS_CHANGES)  

**Gate:**  
- If PASS → continue  
- If NEEDS_CHANGES → return to Step 4 (Implementer) and fix issues, then re-review

---

### Step 6: Verify Against Acceptance Criteria
**Agent:** Verifier  
**Input:**  
- Spec
- Plan
- Code
- Tests  
**Output:** Verification report with AC checklist  

**Gate:**  
- Bug is marked as fixed (AC met)
- Regression test is listed as evidence
- Any side-effects or partial fixes are clearly called out

If AC is not fully met:
- Return to Step 4 (Implementer) and/or Step 3 (Tester)

---

### Step 7: Update Jira Ticket
**Agent:** Jira Updater  
**Input:**  
- Verification report
- Spec
- (Optional) GitLab MCP info  
**Output:** Comment posted to Jira ticket  

**Gate:**  
- Comment includes:
  - Summary of root cause (if known)
  - Summary of the fix
  - Regression test mention
  - AC checklist

---

### Step 8: Write Project Notes
**Agent:** Notes Writer  
**Input:**  
- Spec
- Plan
- Verification report
- (Optional) Jira comment / GitLab info  
**Output:**  
- notes/<YYYY-MM-DD>-<TICKET-ID>-<short-title>.md  

**Gate:**  
- Note explains:
  - What the bug was
  - Why it happened (if known)
  - How it was fixed
  - What test prevents it from coming back

---

## Exit Criteria

The workflow is complete when:

- A regression test exists and passes
- The fix is implemented and reviewed
- Verification confirms the bug is fixed
- Jira ticket is updated with evidence
- A notes entry exists for this bugfix

---

## Failure Handling

- If the bug cannot be reproduced:
  - Document this explicitly
  - Prefer adding observability or diagnostics before guessing a fix
- If the fix causes regressions:
  - Roll back and reassess the plan

---

## Quality Principles Enforced by This Workflow

- No fix without reproduction
- No fix without a regression test (unless impossible, and documented)
- Evidence over assumptions
- Jira reflects real status
- Notes preserve debugging history

---

## Example Invocation (Conceptual)

"Run bugfix workflow for JIRA-5678"

This should execute:
1. Jira Ingest
2. Planner
3. Tester (reproduce bug)
4. Implementer (fix)
5. Reviewer
6. Verifier
7. Jira Updater
8. Notes Writer
