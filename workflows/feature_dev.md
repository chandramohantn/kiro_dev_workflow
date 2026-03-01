# Workflow: Feature Development

## Purpose
This workflow defines the end-to-end, spec-driven process for implementing a new feature from a Jira ticket:
Jira → Spec → Plan → Code → Review → Tests → Verify → Update Jira → Write Notes

It enforces:
- Clear requirements
- Planned execution
- Test-backed changes
- Acceptance-criteria traceability
- Proper communication back to Jira
- Long-term project memory via notes

---

## Entry Criteria

- A Jira ticket ID is provided (e.g., JIRA-1234)
- Jira MCP server is available
- Repo contains:
  - agents/
  - templates/
  - project_assets/docs/
  - project.md (optional but recommended)

---

## Step-by-Step Flow

### Step 1: Ingest Jira Ticket → Create Spec
**Agent:** Jira Ingest  
**Input:** Jira ticket ID  
**Output:** project_assets/specs/<TICKET-ID>/<TICKET-ID>.md  

**Gate:**  
- Spec exists
- Acceptance criteria are clearly listed
- Open questions and assumptions are explicit

If the spec is unclear or missing critical info:
- Stop here
- Ask for clarification before proceeding

---

### Step 2: Create Implementation Plan
**Agent:** Planner  
**Input:** project_assets/specs/<TICKET-ID>/<TICKET-ID>.md  
**Output:** project_assets/specs/<TICKET-ID>/<TICKET-ID>.plan.md  

**Gate:**  
- Plan covers all acceptance criteria
- Risks and testing strategy are included
- Impacted areas are identified

If the plan exposes spec issues:
- Flag them
- Resolve before continuing

---

### Step 3: Implement the Feature
**Agent:** Implementer  
**Input:**  
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.md  
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.plan.md  
**Output:** Code changes in repo  

**Gate:**  
- Implementation follows plan
- No scope creep
- Steering rules respected

If blockers appear:
- Stop and report
- Do not improvise around spec/plan

---

### Step 4: Review the Implementation
**Agent:** Reviewer  
**Input:**  
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.md
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.plan.md
- Code changes  
**Output:** project_assets/specs/<TICKET-ID><TICKET-ID>.review.md (Review report - PASS / NEEDS_CHANGES)

**Gate:**  
- If PASS → continue  
- If NEEDS_CHANGES → return to Step 3 (Implementer) and fix issues, then re-review

This loop can repeat until review passes.

---

### Step 5: Add / Update Tests
**Agent:** Tester  
**Input:**  
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.md (acceptance criteria)
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.plan.md
- Code  
**Output:** Test changes in repo  

**Gate:**  
- All acceptance criteria have test coverage
- Key edge cases covered
- Regression tests added if applicable

If tests reveal bugs:
- Return to Step 3 (Implementer)
- Then re-run Step 4 (Reviewer) if changes are significant

---

### Step 6: Verify Against Acceptance Criteria
**Agent:** Verifier  
**Input:**  
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.md 
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.plan.md
- Code
- Tests  
**Output:** project_assets/specs/<TICKET-ID>/<TICKET-ID>.verify.md  (Verification report with AC checklist)

**Gate:**  
- Each AC is marked: Met / Partially Met / Not Met
- Evidence is provided for each “Met” item

If critical ACs are not met:
- Return to Step 3 (Implementer) and/or Step 5 (Tester)

---

### Step 7: Update Jira Ticket
**Agent:** Jira Updater  
**Input:**  
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.verify.md
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.md
- (Optional) GitLab MCP info  
**Output:** Comment posted to Jira ticket  

**Gate:**  
- Comment includes:
  - Implementation summary
  - AC checklist
  - Callouts for partial or missing items
  - Test summary

---

### Step 8: Write Project Notes
**Agent:** Notes Writer  
**Input:**  
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.md
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.plan.md
- project_assets/specs/<TICKET-ID>/<TICKET-ID>.verify.md
- (Optional) Jira comment / GitLab info  
**Output:**  
- project_assets/notes/<YYYY-MM-DD>-<TICKET-ID>-<short-title>.md  

**Gate:**  
- Note explains:
  - Why the change was made
  - What changed
  - Key design decisions
  - What’s done vs pending
- File name follows naming rules

---

## Exit Criteria

The workflow is complete when:

- Code is implemented and reviewed
- Tests cover acceptance criteria
- Verification report is generated
- Jira ticket has an up-to-date comment
- A notes entry exists for this ticket

---

## Failure Handling

- If any step fails its gate:
  - Do not proceed forward
  - Loop back to the appropriate earlier step
- Never:
  - Skip verification
  - Skip Jira update
  - Skip notes for completed work

---

## Quality Principles Enforced by This Workflow

- Specs are the source of truth
- Plans make work predictable
- Tests prove behavior
- Verification proves requirements are met
- Jira reflects reality, not optimism
- Notes preserve project memory

---

## Example Invocation (Conceptual)

"Run feature_dev workflow for JIRA-1234"

This should execute:
1. Jira Ingest
2. Planner
3. Implementer
4. Reviewer (loop until pass)
5. Tester
6. Verifier
7. Jira Updater
8. Notes Writer
