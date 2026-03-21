# Task Splitting Policy

This policy defines when tasks should be split into subtasks and when they should remain combined.
The coordinator must avoid unnecessary task decomposition.
Over-splitting tasks creates inefficient workflows.

---

# Splitting Principles

Tasks should only be split when multiple expertise domains are required.
Typical domain boundaries include:
- Code Implementation
- Testing
- Debugging
- Architecture
- Documentation

---

# Appropriate Task Splitting

Example:

User Request:

Add retry logic and write tests.

Execution Plan:
Task T1 → agent_code
Task T2 → agent_test

This split is appropriate because different agents are responsible.

---

# Avoid Micro Tasks

Tasks should never be split into trivial steps.

Bad example:
Task T1 → locate file
Task T2 → open file
Task T3 → modify code

These steps should be performed internally by the assigned agent.

---

# Combine Related Tasks

If a single agent can complete multiple related tasks, they should be combined.

Example:

Add logging and validation.

Correct:
Task T1 → agent_code (implement logging and validation)

Incorrect:
Task T1 → add logging
Task T2 → add validation

---

# Maximum Plan Size

Typical execution plans should contain:

1–4 tasks.

Plans exceeding 6 tasks should be reconsidered and simplified.

---

# Task Splitting Outcome

Execution plans must remain **minimal and efficient** while ensuring that expertise boundaries are respected.
