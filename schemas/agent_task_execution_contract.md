# Task Execution Contract for Sub-Agents

All specialized agents must return results using a consistent structure.

This ensures that the coordinator agent can reliably interpret outputs and continue the workflow.

Every agent response must contain the following sections.

---

# Response Structure

## Task Summary

Briefly restate the task that was assigned.

Example:

Task: Implement retry logic for PostgreSQL connections.

---

## Execution Steps

Describe the steps taken to complete the task.

Keep steps concise and technical.

Example:

1. Located the database connection implementation.
2. Designed exponential backoff retry logic.
3. Updated connection initialization.
4. Added retry wrapper.

---

## Result

Describe the outcome of the task.

Example:

Retry logic implemented successfully with exponential backoff.

---

## Artifacts Produced

List files created or modified.

Example:

Modified:

* db/connection.py

Created:

* tests/test_retry_logic.py

---

## Observations

Optional section.

Include relevant technical observations discovered during the task.

Example:

The current connection initialization does not handle transient failures.

---

## Issues or Risks

Describe any problems encountered.

Example:

Potential performance impact if retry limit is too high.

---

## Recommendations

Optional improvements or follow-up work.

Example:

Add monitoring for retry counts.

---

# Completion Status

Must be one of:

SUCCESS
PARTIAL_SUCCESS
FAILED

---

# Final Output Example

Task Summary:
Implement retry logic for PostgreSQL connections.

Execution Steps:

1. Located connection module.
2. Designed exponential retry strategy.
3. Implemented retry wrapper.

Result:
Retry logic successfully added.

Artifacts Produced:
Modified:

* db/connection.py

Completion Status:
SUCCESS
