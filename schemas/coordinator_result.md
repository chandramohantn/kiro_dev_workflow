# CoordinatorResult

Final consolidated output from the coordinator agent after executing a multi-agent workflow.

---

## Fields

### workflow_id

- Type: string
- Required: no
- Description: Unique identifier for the workflow session.

---

### workflow_summary

- Type: string
- Required: yes
- Description: High-level summary of the workflow execution.

---

### tasks_executed

- Type: array
- Required: yes
- Description: Tasks executed during the workflow.
- Items: Each item is an object with: task_id (string), agent (string), status (string: SUCCESS/PARTIAL_SUCCESS/FAILED), summary (string).

---

### aggregated_artifacts

- Type: array
- Required: no
- Description: All files created or modified across all tasks.
- Items: Each item is a string representing a file path.

---

### issues_encountered

- Type: array
- Required: no
- Description: Issues encountered during workflow execution.
- Items: Each item is a string describing an issue.

---

### failed_tasks

- Type: array
- Required: no
- Description: Task IDs that failed after all retry attempts.
- Items: Each item is a string representing a task ID.

---

### recommendations

- Type: array
- Required: no
- Description: Follow-up work or improvements suggested.
- Items: Each item is a string describing a recommendation.

---

### overall_status

- Type: string
- Required: yes
- Description: Overall workflow completion status.
- Allowed values: COMPLETED, PARTIALLY_COMPLETED, FAILED