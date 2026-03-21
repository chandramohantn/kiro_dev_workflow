---
name: jira-comment-builder
description: Build a structured Jira comment from development results. Use when updating a Jira ticket with the outcome of a development workflow.
---

# Jira Comment Builder

Build a structured comment for posting to a Jira ticket after development is complete.

## Inputs Required

1. **ticket_id** — the Jira ticket being updated
2. **Development results** — aggregated outputs from the workflow (code changes, test results, review feedback, documentation artifacts)

## Comment Structure

Build a comment containing:

| Field | Description |
|-------|-------------|
| ticket_id | The ticket being updated |
| development_summary | One-paragraph summary of what was done |
| implementation_details | List of specific changes made (files modified, features added, bugs fixed) |
| tests_added | List of tests written with brief descriptions |
| review_status | Current review state (reviewed/pending/changes requested) |
| next_steps | Any remaining work, follow-ups, or blockers |

## Guidelines

- Keep the summary concise — one paragraph max.
- Implementation details should reference specific files or components.
- If no tests were added, state why (e.g., "config-only change, no testable logic").
- Next steps should be empty if the work is fully complete — state "None — work complete."

## Output

Return a structured comment conforming to the `jira_comment` schema, ready to be posted via Jira MCP tools.
