---
name: prd-to-issues
description: Break a PRD into independently-grabbable Jira issues/tickets and output as a structured markdown document.
---

# PRD to Issues

Convert a PRD markdown file into structured, implementation-ready Jira issues in markdown format.

---

## Principles

* Every issue must be independently executable
* Avoid vague or umbrella tasks
* Prefer smaller, testable units
* Do NOT invent requirements not present in the PRD
* Extract implicit edge cases only if strongly implied

---

## Process

### 1. Locate the PRD

* Ask the user for the PRD markdown file path if not provided
* Read the full PRD before proceeding
* If large, summarize sections internally

---

### 2. Understand the PRD

Extract:

* Features
* Actors
* User flows
* Functional requirements
* Non-functional requirements
* Constraints
* Edge cases

If ambiguity exists:

* Ask clarification questions before proceeding

---

### 3. Build Structured Representation (MANDATORY)

Internally convert PRD into structured features:

* Feature name
* Flows (atomic)
* Edge cases
* Requirements

Do NOT skip this step even though final output is markdown.

---

### 4. Decompose into Work Items

Mapping:

* Feature → Epic
* Flow → Story
* Edge cases → Acceptance criteria or tasks

---

### 5. Generate Issues in Markdown

Output MUST follow this format:

```md
# PRD Breakdown: <PRD Name>

## Epic: <Epic Title>

**Description**
<epic description>

---

### Story: <Story Title>

**Description**
<story description>

**Acceptance Criteria**
- [ ] <criterion 1>
- [ ] <criterion 2>

**Tasks**
- [ ] <task 1>
- [ ] <task 2>

---
```

Rules:

* Titles must be action-oriented
* Acceptance criteria must be testable
* Tasks must be implementation-level (API, DB, UI, validation, etc.)
* Avoid vague phrases like "implement feature"

---

### 6. Quality Checks

Before returning:

* No duplicate stories
* No vague tasks
* Each story is independently testable
* Acceptance criteria cover edge cases

If quality is low:

* Refine automatically

---

### 7. (Optional) Codebase Awareness

If repository is available:

* Align stories with existing modules/services
* Avoid duplicate work
* Reference relevant components when useful

---

### 8. Iteration Mode

After generating output:

Ask user:

* Do you want finer task breakdown?
* Do you want technical details (API contracts, DB schema)?
* Should stories be grouped by team (backend/frontend/ml)?

Refine accordingly.

Do NOT close or modify the parent PRD issue.