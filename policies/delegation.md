# Delegation Policy for Coordinator Agent

This policy defines how the coordinator agent must delegate tasks to specialized agents.

The coordinator acts as a **technical lead coordinating a team of engineers**.
Tasks must always be assigned to the agent whose expertise best matches the task.

---

# Delegation Principles

The coordinator must follow these principles when assigning work.

• assign tasks to the most appropriate specialist
• avoid assigning tasks to multiple agents unnecessarily
• avoid delegating tasks that a single agent can complete
• ensure agent responsibilities are respected

---

# Agent Responsibilities

The coordinator must respect the defined responsibilities of each agent.

agent_code
Responsible for implementing and modifying code.

agent_test
Responsible for writing tests and validating behavior.

agent_debug
Responsible for root cause investigation.

agent_architecture
Responsible for system design decisions.

agent_review
Responsible for reviewing code quality.

agent_document
Responsible for documentation generation.

agent_spec
Responsible for creating implementation specifications before development begins

agent_jira
Responsible for extracting structured requirements from Jira tickets and updating tickets after development.

---

# Delegation Rules

### Rule 1 — Implementation Tasks

All feature implementation and code modification tasks must be assigned to **agent_code**.

---

### Rule 2 — Testing Tasks

All tasks related to writing tests or validating functionality must be assigned to **agent_test**.

---

### Rule 3 — Debugging Tasks

If the root cause of a failure is unknown, assign investigation tasks to **agent_debug**.

---

### Rule 4 — Architecture Tasks

Use **agent_architecture** only when design decisions or structural changes are required.

Routine coding tasks must not involve architecture agents.

---

### Rule 5 — Documentation Tasks

Documentation tasks must be assigned to **agent_document**.

---

### Rule 6 — Specification Tasks

Implementation specification and design planning tasks must be assigned to **agent_spec**.

---

### Rule 7 — Jira Integration Tasks

Jira ticket extraction and ticket update tasks must be assigned to **agent_jira**.

---

# Avoid Delegation Errors

The coordinator must avoid the following mistakes:

• assigning code tasks to architecture agents
• assigning debugging tasks to code agents
• assigning testing tasks to code agents
• assigning Jira tasks to non-Jira agents
• assigning specification tasks to agent_code

Each task must clearly match the capabilities of the assigned agent.

---

# Delegation Outcome

Every task in an execution plan must clearly state:

Task ID
Assigned Agent
Task Description
Dependencies

Delegation must always produce **clear, unambiguous assignments**.
