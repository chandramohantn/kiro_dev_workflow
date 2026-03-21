# Task

Represents a single task in an execution plan.

---

## Fields

### task_id

- Type: string
- Required: yes
- Description: Unique identifier for the task.

---

### agent

- Type: string
- Required: yes
- Description: Name of the specialized agent responsible for executing the task.

---

### description

- Type: string
- Required: yes
- Description: Clear description of the task objective.

---

### dependencies

- Type: array
- Required: no
- Description: List of task IDs that must be completed before this task begins.
- Items: Each item is a string representing a task ID.

---

### priority

- Type: string
- Required: no
- Description: Optional task priority.
- Allowed values: low, medium, high
