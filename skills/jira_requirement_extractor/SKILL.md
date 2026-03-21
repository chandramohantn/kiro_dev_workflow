---
name: jira-requirement-extractor
description: Extract structured requirements from a Jira ticket. Use when ingesting a Jira ticket to produce a structured requirement for planning.
---

# Jira Requirement Extractor

Extract structured engineering requirements from a Jira ticket.

## Inputs Required

1. **Jira ticket data** — retrieved via Jira MCP tools (ticket ID, title, description, fields, comments)

## Extraction Fields

From the ticket, extract and structure:

| Field | Source | Required |
|-------|--------|----------|
| ticket_id | Ticket key (e.g., PROJ-123) | Yes |
| title | Summary field | Yes |
| description | Description field | Yes |
| requirements | Parsed from description/acceptance criteria | Yes |
| acceptance_criteria | Explicit AC if present, else inferred from description | Yes |
| technical_constraints | Constraints mentioned in description or comments | No |
| related_components | Components/labels/affected modules | No |
| priority | Priority field | Yes |

## Guidelines

- Extract requirements as a list of discrete, actionable items.
- If acceptance criteria are not explicitly listed, infer them from the description — but flag them as inferred.
- Technical constraints may appear in comments or description — check both.
- If fields are missing or empty, note them as absent rather than inventing content.

## Output

Return a structured requirement conforming to the `jira_requirement` schema with all extracted fields populated.
