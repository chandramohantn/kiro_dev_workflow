# JiraCommentUpdate

Structured comment format used when updating Jira tickets.

---

## Fields

### ticket_id

- Type: string
- Required: yes
- Description: Jira ticket identifier.

---

### development_summary

- Type: string
- Required: yes
- Description: Summary of the development work performed.

---

### implementation_details

- Type: array
- Required: no
- Description: Details of the implementation.
- Items: Each item is a string describing an implementation detail.

---

### tests_added

- Type: array
- Required: no
- Description: Tests added as part of the work.
- Items: Each item is a string describing a test.

---

### review_status

- Type: string
- Required: no
- Description: Current review status.

---

### next_steps

- Type: string
- Required: no
- Description: Next steps to be taken.
