---
name: dod-checker
description: Verify Definition of Done for completed tasks. Use when checking if a task meets the DoD checklist, evaluating task completion status, or auditing whether acceptance criteria and quality gates are satisfied.
---

# DoD Checker — Definition of Done Verification

Evaluate a completed task against the Definition of Done checklist. Determine which checklist items are relevant and verify whether each has been satisfied.

## Inputs Required

1. **Task context** — JIRA ticket details (title, description, requirements, acceptance criteria)
2. **Workflow results** — aggregated outputs from agents (code changes, test results, review feedback, documentation artifacts)
3. **Repository state** — access to the codebase to verify claims (files modified, tests present, docs updated)

## Evaluation Process

### Step 1: Determine Relevance

For each DoD section, assess whether it applies to this specific task. Not all items apply to every ticket.

Use these heuristics:

- **Code Quality & Standards** — Relevant if the task involved writing or modifying code.
- **Testing & Validation** — Relevant if the task involved code changes. Mark N/A for pure configuration, documentation-only, or infrastructure provisioning tasks with no testable logic.
- **Documentation & Knowledge Transfer** — README relevant if new setup steps introduced. API docs relevant if APIs created or changed. Architecture diagrams relevant if system design changed. Deployment guide relevant if deployment process changed. Troubleshooting guide relevant only for complex operational components. Knowledge transfer relevant only if explicitly required by the ticket.
- **Security & Compliance** — Relevant if the task handles data, credentials, access controls, or introduces new dependencies. Mark N/A for internal tooling changes with no security surface.
- **Deployment & Operations** — Relevant if the task produces a deployable artifact. Mark N/A for library-only or shared-module changes that deploy as part of a larger system. Monitoring/alerting relevant only for production-facing services.
- **Peer Review & Collaboration** — Code review is always relevant for code changes. Knowledge sharing session relevant only if the ticket scope warrants it.
- **Project Management** — Acceptance criteria and JIRA status are always relevant. Time tracking and stakeholder communication are relevant based on team process.

### Step 2: Verify Each Relevant Item

For each relevant item, check against available evidence:

- **Code quality**: Inspect changed files for docstrings, naming, hardcoded values
- **Testing**: Check for test files, coverage data if available, CI status
- **Documentation**: Check if README, API docs, architecture docs were updated
- **Security**: Check for credentials in code, review dependency additions
- **Deployment**: Check deployment logs/status, monitoring configuration
- **Peer review**: Check MR/PR review status, reviewer comments
- **Project management**: Check JIRA ticket status, acceptance criteria completion

### Step 3: Mark the Checklist

For each checklist item in the template at `references/checklist_template.md`, apply one of these markers:

- `[x]` — Done. Evidence confirms the item is satisfied.
- `[ ]` — Not Done. Item is relevant but not yet satisfied.
- `[N/A]` — Not Applicable. Item does not apply to this task.
- `[?]` — Unverifiable. Item is relevant but cannot be confirmed from available evidence.

## Output Format

The output must be a completed markdown file following the template in `references/checklist_template.md`.

Rules for filling the template:

1. **Header fields** — Fill in Task Name, JIRA Link, Developer, Date from the task context. Leave Reviewer blank if not known.
2. **Checklist items** — Replace each `[ ]` with the appropriate marker.
3. **Notes fields** — Replace placeholder text with:
   - For N/A items: brief justification why the item doesn't apply
   - For Not Done items: what is missing
   - For Unverifiable items: what evidence would be needed
   - For Done items: brief evidence reference (e.g. "docstrings present in all new functions")
4. **Section-specific fields** — Fill in Test Coverage %, Documentation Links, Security Scan Results, Environment URLs, Reviewer names, Time Spent etc. where evidence is available. Use "N/A" for fields in irrelevant sections.
5. **Task Status** — Mark one of: In Progress, Ready for Review, or Complete based on the overall result.
6. **Final Sign-off** — Leave sign-off fields for manual completion by the developer and reviewer.

### Overall Status Logic

- **Complete** — All relevant items are `[x]` or `[N/A]`
- **Ready for Review** — No blocking `[ ]` items remain, but some `[?]` items need human verification
- **In Progress** — One or more relevant items are `[ ]` (not done)

## Judgment Guidelines

- Be pragmatic, not bureaucratic. A 2-line config change doesn't need architecture diagrams.
- When in doubt about relevance, lean toward N/A with justification rather than flagging Not Done.
- If an item is partially done, mark it `[ ]` and explain what's missing in Notes.
- Always provide reasoning for N/A decisions so the reviewer understands the judgment.
