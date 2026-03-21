# AgentResult

Structured result returned by a specialized agent after completing a task.

---

## Fields

### task_id

- Type: string
- Required: yes
- Description: Identifier of the task that was executed.

---

### agent

- Type: string
- Required: yes
- Description: Name of the agent that executed the task.

---

### status

- Type: string
- Required: yes
- Description: Completion status of the task.
- Allowed values: SUCCESS, PARTIAL_SUCCESS, FAILED

---

### summary

- Type: string
- Required: no
- Description: Brief summary of the work performed.

---

### artifacts

- Type: array
- Required: no
- Description: Files created or modified during the task.
- Items: Each item is a string representing a file path.

---

### issues

- Type: array
- Required: no
- Description: Issues encountered during execution.
- Items: Each item is a string describing an issue.

---

### recommendations

- Type: array
- Required: no
- Description: Optional suggestions for follow-up work.
- Items: Each item is a string describing a recommendation.
