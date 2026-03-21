# Task Planning Heuristics

This document defines planning heuristics that guide **agent_planner** when decomposing tasks and assigning specialized agents.

These heuristics ensure that task planning is efficient, stable, and aligned with real-world engineering workflows.

---

# Core Planning Philosophy

Plan work the way an experienced technical lead would coordinate a team of engineers.

The planner must:

* Minimize unnecessary complexity
* Avoid over-decomposition
* Assign tasks to the most appropriate specialist
* Maintain logical task order
* Avoid redundant work

A good execution plan is **clear, minimal, and logically structured**.

---

# Heuristic 1 — Prefer Single-Agent Solutions

If a single agent can reasonably complete the task, assign the task to that agent without splitting it.

Example:

User Request:
"Add validation to the login endpoint."

Correct Plan:

Task 1
Agent: agent_code
Description: Add validation logic to login endpoint.

Incorrect Plan:

Task 1 → Analyze endpoint
Task 2 → Design validation logic
Task 3 → Implement validation logic

This is unnecessary decomposition.

---

# Heuristic 2 — Split Tasks When Skill Domains Differ

Tasks should be split when different expertise domains are required.

Common domain boundaries include:

Code Implementation
Testing
Architecture Design
Debugging
Documentation

Example:

User Request:
"Add retry logic and tests."

Correct Plan:

Task 1
Agent: agent_code
Description: Implement retry logic.

Task 2
Agent: agent_test
Description: Write unit tests for retry behavior.

---

# Heuristic 3 — Respect Natural Engineering Workflow

Engineering tasks usually follow a natural order:

Design → Implementation → Testing → Review → Documentation

Example:

Architecture change:

Task 1 → agent_architecture (design)
Task 2 → agent_code (implementation)
Task 3 → agent_test (testing)

Never reverse this order.

---

# Heuristic 4 — Avoid Architecture Tasks Unless Necessary

Architecture agents should only be used when:

* system design decisions are required
* trade-offs must be evaluated
* structural system changes are involved

Do NOT involve architecture agents for routine coding tasks.

Example:

Adding retry logic usually does NOT require architecture analysis.

---

# Heuristic 5 — Use Debug Agent Only for Investigation

The debug agent should only be used when the root cause of a problem is unknown.

Appropriate scenarios:

* failing tests
* runtime exceptions
* production incidents
* unexpected system behavior

Do NOT use debug agents when the problem is clearly defined.

Example:

User Request:
"Fix syntax error in database module."

Correct agent: agent_code

---

# Heuristic 6 — Avoid Micro-Tasks

Do not break tasks into trivial steps.

Bad example:

Task 1 → Locate file
Task 2 → Open file
Task 3 → Modify function

These should be combined into a single task.

---

# Heuristic 7 — Combine Related Work

If multiple tasks can be handled by the same agent in one operation, combine them.

Example:

User Request:
"Add logging and validation to endpoint."

Correct Plan:

Task 1
Agent: agent_code
Description: Add validation and logging to endpoint.

Incorrect Plan:

Task 1 → Add validation
Task 2 → Add logging

---

# Heuristic 8 — Always Follow Implementation with Tests

When code is implemented or modified, testing should usually follow.

Example:

Task 1 → agent_code
Task 2 → agent_test

Testing tasks should verify the newly introduced behavior.

---

# Heuristic 9 — Documentation Is Optional

Documentation should only be added when:

* user explicitly requests documentation
* architecture changes are introduced
* public APIs are modified

Do not generate documentation unnecessarily.

---

# Heuristic 10 — Avoid Redundant Debugging

If the problem and solution are clearly stated by the user, do not perform debugging tasks.

Example:

User Request:
"Add retry logic."

Do not assign:

Task → agent_debug

---

# Heuristic 11 — Maintain Minimal Execution Plans

Execution plans should contain the smallest number of tasks necessary to complete the request.

Typical plans contain between:

1 and 4 tasks.

Plans with more than 6 tasks should be avoided unless the problem is complex.

---

# Heuristic 12 — Ensure Task Dependencies Are Logical

Tasks must respect dependencies.

Example:

Task 1 → agent_code (implement feature)
Task 2 → agent_test (write tests)

Incorrect order:

Testing before implementation.

---

# Heuristic 13 — Avoid Tool Exploration Tasks

Do not create tasks solely for exploration.

Example of bad planning:

Task → Explore repository structure.

Agents should explore internally as part of execution.

---

# Heuristic 14 — Prioritize Clarity

Each task description must be clear and actionable.

Bad:

"Handle retry logic."

Better:

"Implement exponential retry logic for PostgreSQL connection initialization."

---

# Heuristic 15 — Reuse Existing System Knowledge

If context already provides sufficient information, avoid re-analyzing the system.

Do not create redundant investigation tasks.

---

# Summary

When planning tasks, the planner should:

1. Understand the user request
2. Identify required expertise domains
3. Apply planning heuristics
4. Produce a minimal execution plan
5. Assign the correct agents

A stable plan:

* uses the correct agents
* contains minimal tasks
* follows engineering workflow
* avoids unnecessary complexity
