# DebugReport

Structured root cause analysis report from the debug agent.

---

## Fields

### failure_description

- Type: string
- Required: yes
- Description: Description of the failure or error being investigated.

---

### investigation_steps

- Type: array
- Required: yes
- Description: Steps taken during the investigation.
- Items: Each item is a string describing an investigation step.

---

### root_cause

- Type: string
- Required: yes
- Description: Identified root cause of the failure.

---

### evidence

- Type: array
- Required: no
- Description: Log entries, stack traces, or code references supporting the root cause.
- Items: Each item is a string representing a piece of evidence.

---

### affected_components

- Type: array
- Required: no
- Description: Components or files affected by the issue.
- Items: Each item is a string representing a component or file path.

---

### severity

- Type: string
- Required: no
- Description: Severity assessment of the issue.
- Allowed values: critical, high, medium, low

---

### recommended_fix

- Type: string
- Required: no
- Description: Suggested approach to fix the issue.

---

### related_issues

- Type: array
- Required: no
- Description: Other issues or patterns discovered during investigation.
- Items: Each item is a string describing a related issue.