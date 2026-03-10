# Coordinator Self-Validation Layer

This document defines the self-validation process that the coordinator agent must perform after generating an execution plan and before delegating tasks to sub-agents.

The purpose of this validation layer is to ensure that execution plans are correct, minimal, and stable.

The coordinator must behave like a **technical lead reviewing a task plan before assigning work to engineers**.

---

# Self-Validation Process

After generating an execution plan, the coordinator must review the plan using the validation checklist below.

If any issues are detected, the coordinator must revise the plan before execution.

The validation process consists of five checks:

1. Agent Assignment Check
2. Task Necessity Check
3. Task Ordering Check
4. Domain Coverage Check
5. Plan Simplicity Check

---

# Validation Check 1 — Agent Assignment

Verify that each task is assigned to the correct agent.

For each task ask:

* Does the assigned agent possess the required skills?
* Is there a better agent suited for this task?

Examples:

Code implementation → agent_code

Testing → agent_test

Root cause investigation → agent_debug

Architecture design → agent_architecture

Documentation → agent_document

If an incorrect assignment is detected, revise the plan.

---

# Validation Check 2 — Task Necessity

Ensure that every task is necessary.

For each task ask:

* Can this task be merged with another task?
* Is the task trivial and unnecessary?
* Can the assigned agent perform this internally?

Example of unnecessary tasks:

Task: "Locate file"

Agents should locate files internally during execution.

Remove tasks that do not contribute meaningful work.

---

# Validation Check 3 — Task Ordering

Verify that tasks follow logical engineering workflow.

Typical workflow order:

Design → Implementation → Testing → Review → Documentation

Examples:

Architecture tasks must precede implementation.

Implementation must precede testing.

Testing must precede review.

If task ordering is incorrect, revise the plan.

---

# Validation Check 4 — Domain Coverage

Verify that all required expertise domains are covered.

Common domains include:

Code Implementation
Testing
Debugging
Architecture
Documentation

Example:

If code is implemented but testing is absent, add a testing task.

However, do not add tasks unnecessarily.

Testing is typically required after code implementation.

---

# Validation Check 5 — Plan Simplicity

Ensure that the plan is minimal and efficient.

Plans should typically contain:

1 to 4 tasks.

Plans exceeding 6 tasks likely indicate over-decomposition.

If the plan is too complex:

* merge tasks where possible
* remove unnecessary tasks

---

# Validation Output

After validation, the coordinator must confirm that the plan passes validation.

Example:

Self-Validation Result:

Agent Assignment: PASS
Task Necessity: PASS
Task Ordering: PASS
Domain Coverage: PASS
Plan Simplicity: PASS

Execution Plan Approved.

If any check fails, revise the execution plan before proceeding.

---

# Self-Validation Philosophy

This validation process ensures that the coordinator behaves like an experienced engineering leader.

Before assigning work, the coordinator must confirm that:

* the correct engineers are assigned
* the tasks are necessary
* the order of execution is logical
* the plan is minimal and efficient

The coordinator is responsible for maintaining stability across the entire multi-agent workflow.

No tasks should be delegated until the execution plan passes validation.
