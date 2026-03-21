# WorkflowState

Tracks the execution state of a multi-agent workflow.

---

## Fields

### workflow_id

- Type: string
- Required: no
- Description: Unique identifier for the workflow session.

---

### completed_tasks

- Type: array
- Required: no
- Description: Tasks that have successfully completed.
- Items: Each item is a string representing a task ID.

---

### pending_tasks

- Type: array
- Required: no
- Description: Tasks waiting to be executed.
- Items: Each item is a string representing a task ID.

---

### failed_tasks

- Type: array
- Required: no
- Description: Tasks that failed during execution.
- Items: Each item is a string representing a task ID.

---

### retry_counts

- Type: object
- Required: no
- Description: Tracks retry attempts for each task. Keys are task IDs, values are integers representing retry counts.

---

### current_task

- Type: string
- Required: no
- Description: Task currently being executed.
