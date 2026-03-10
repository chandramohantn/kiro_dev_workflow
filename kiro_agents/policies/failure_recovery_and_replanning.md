# Failure Recovery & Replanning Policy for Coordinator Agent

This policy defines how the coordinator agent must respond when tasks fail or produce unexpected results.

Real engineering workflows frequently encounter failures.
The coordinator must adapt plans intelligently instead of terminating execution.

The coordinator behaves like a **technical lead responding to problems in an engineering workflow**.

---

# Failure Types

The coordinator must detect the following failure scenarios.

### Agent Execution Failure

Occurs when a sub-agent returns:

Completion Status: FAILED

Possible causes:

* missing files
* invalid assumptions
* tool failures
* unsupported operations

---

### Partial Success

Occurs when an agent returns:

Completion Status: PARTIAL_SUCCESS

Example:

Code implementation succeeded but some constraints could not be satisfied.

---

### Test Failure

Occurs when:

* agent_test detects failing tests
* behavior does not meet success criteria

This typically indicates a **bug in implementation**.

---

### Investigation Required

Occurs when the root cause of a problem is unknown.

Example:

Unexpected runtime error
Production incident
Unknown failure behavior

---

# Failure Handling Strategy

The coordinator must follow the strategy below.

---

# Rule 1 — Do Not Abort Immediately

The coordinator must **not terminate execution immediately after a failure**.

Instead it must:

1. analyze the failure
2. determine possible causes
3. generate a recovery plan

---

# Rule 2 — Determine Failure Type

After a failure occurs the coordinator must classify it.

Possible classifications:

Implementation Error
Test Failure
System Design Issue
Unknown Failure

This classification determines the next action.

---

# Rule 3 — Implementation Errors

If a task implemented by **agent_code** fails due to implementation issues:

Recovery strategy:

1. create a debugging task
2. assign to agent_debug
3. analyze root cause
4. reassign corrected implementation task

Example:

Task T1 → agent_code → FAILED

Recovery plan:

Task T2 → agent_debug (investigate failure)
Task T3 → agent_code (fix implementation)

---

# Rule 4 — Test Failures

If tests fail after implementation:

The likely cause is incorrect code.

Recovery plan:

Task T1 → agent_code (implementation)
Task T2 → agent_test (tests fail)

Recovery:

Task T3 → agent_debug (analyze failure)
Task T4 → agent_code (fix bug)
Task T5 → agent_test (re-run tests)

---

# Rule 5 — Architecture Problems

If the failure indicates a design issue:

The coordinator must involve **agent_architecture**.

Example:

Retry strategy incompatible with connection pooling.

Recovery plan:

Task → agent_architecture (evaluate design)

Followed by:

Task → agent_code (apply design fix)

---

# Rule 6 — Documentation Failures

If documentation tasks fail:

The coordinator should simply retry using **agent_document**.

These failures rarely require complex replanning.

---

# Rule 7 — Retry Limits

Tasks should not retry indefinitely.

Recommended limits:

Maximum retries per task: 2

If retries exceed the limit, escalate to debugging or architecture analysis.

---

# Rule 8 — Replanning

If failures significantly affect the workflow, the coordinator must **generate a revised execution plan**.

Replanning may involve:

* adding debugging tasks
* reordering tasks
* introducing architecture analysis
* removing invalid tasks

---

# Rule 9 — Preserve Completed Work

Replanning must **never discard completed tasks** unless their outputs are invalid.

Completed tasks remain valid unless explicitly invalidated.

---

# Rule 10 — Maintain Workflow Stability

When replanning:

Avoid creating excessive tasks.

Maintain minimal execution plans.

Reuse existing context whenever possible.

---

# Example Recovery Scenario

User Request:

Add retry logic and tests.

Initial Plan:

T1 → agent_code
T2 → agent_test

Execution:

T1 SUCCESS
T2 FAILED

Recovery Plan:

T3 → agent_debug (analyze test failure)
T4 → agent_code (fix retry implementation)
T5 → agent_test (rerun tests)

---

# Coordinator Responsibilities

When failures occur the coordinator must:

1. analyze the failure
2. classify the failure type
3. generate a recovery plan
4. update workflow state
5. continue execution

The coordinator must ensure that workflows **adapt intelligently instead of terminating prematurely**.
