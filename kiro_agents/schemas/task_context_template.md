# Task Context Template for Sub-Agents

Every specialized agent receives task instructions using this standardized format.

This ensures that agents have consistent context and can execute tasks reliably.

The coordinator agent must always provide tasks using this structure.

---

# Task Identifier

Unique identifier assigned by the coordinator.

Example:

Task ID: T1

---

# Assigned Agent

Name of the specialized agent responsible for the task.

Example:

Assigned Agent: agent_code

---

# Task Objective

Clear description of what must be accomplished.

The objective must be concise and actionable.

Example:

Implement retry logic for PostgreSQL database connections.

---

# Detailed Task Description

Provide additional details required to understand the task.

This may include:

* technical background
* system context
* behavior expectations

Example:

The current PostgreSQL connection initialization does not handle transient failures.
Add retry logic using exponential backoff when establishing connections.

---

# Input Context

Provide any relevant information the agent may need.

Examples:

Relevant Files
Relevant Logs
Architecture Notes
Existing Implementations

Example:

Relevant Files:

* db/connection.py
* config/database.yaml

Architecture Notes:
Connection pool uses SQLAlchemy.

---

# Dependencies

List tasks that must be completed before this task begins.

If none, specify:

Dependencies: None

Example:

Dependencies:

* T1

---

# Constraints

Specify rules the agent must follow.

Examples:

* Maintain existing coding style
* Avoid introducing new dependencies
* Ensure backward compatibility

Example:

Constraints:

* Use existing SQLAlchemy engine
* Maintain current configuration structure

---

# Tools Available

List MCP tools the agent is allowed to use.

Example:

Tools Available:

* filesystem
* repo_search
* context7

Agents must **only use the tools listed here**.

---

# Expected Output Format

All agents must return results following the Task Execution Contract.

Reference:

schemas/agent_task_execution_contract.md

---

# Success Criteria

Define what constitutes successful completion of the task.

Example:

Success Criteria:

* Retry logic implemented
* Transient failures handled
* No regression in existing functionality

---

# Failure Handling

If the task cannot be completed:

The agent must:

1. Explain the failure
2. Identify the root cause
3. Provide recommendations
4. Mark completion status as FAILED
