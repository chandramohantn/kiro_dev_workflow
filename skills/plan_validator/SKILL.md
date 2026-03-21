---
name: plan-validator
description: Validate an execution plan before handoff to the coordinator. Use when verifying that a generated plan has correct agent assignments, necessary tasks, logical ordering, domain coverage, and minimal complexity.
---

# Plan Validator

Validate an execution plan to ensure it is correct, minimal, and ready for execution.

## Inputs Required

1. **Execution plan** — the plan to validate (list of tasks with agent assignments, dependencies, descriptions)

## Validation Checks

### Check 1 — Agent Assignment
For each task: is the assigned agent the correct specialist?

- Code implementation → agent_code
- Testing → agent_test
- Root cause investigation → agent_debug
- Architecture/design → agent_architecture
- Documentation → agent_document
- Specification → agent_spec
- Jira integration → agent_jira
- Code review → agent_review

### Check 2 — Task Necessity
For each task: is it required?

- Can it be merged with another task?
- Is it trivial (e.g., "locate file") and should be internal to the agent?
- Does it contribute meaningful work?

### Check 3 — Task Ordering
Do tasks follow logical engineering workflow?

Design → Implementation → Testing → Review → Documentation

- Architecture before implementation
- Implementation before testing
- Testing before review

### Check 4 — Domain Coverage
Are all required expertise domains addressed?

- If code is implemented, is testing included?
- If new APIs are added, is documentation covered?
- Don't add unnecessary tasks — only flag genuine gaps.

### Check 5 — Plan Simplicity
Is the plan minimal?

- Target: 1–4 tasks
- Plans exceeding 6 tasks likely indicate over-decomposition
- Merge tasks where possible

## Output

Return validation result per check:

| Check | Status | Notes |
|-------|--------|-------|
| Agent Assignment | PASS/FAIL | Details if FAIL |
| Task Necessity | PASS/FAIL | Details if FAIL |
| Task Ordering | PASS/FAIL | Details if FAIL |
| Domain Coverage | PASS/FAIL | Details if FAIL |
| Plan Simplicity | PASS/FAIL | Details if FAIL |

If any check is FAIL, provide specific revision recommendations.
