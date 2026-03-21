---
name: failure-recovery
description: Classify task failures and determine recovery actions. Use when a delegated task fails and the coordinator needs to decide whether to retry, debug, replan, or escalate.
---

# Failure Recovery

Classify a task failure and determine the appropriate recovery action.

## Inputs Required

1. **Failed task result** — the agent's response including failure details
2. **Retry count** — how many times this task has already been retried
3. **Workflow state** — completed tasks, pending tasks, current progress

## Process

### Step 1: Classify Failure Type

| Type | Signals |
|------|---------|
| Implementation error | Code doesn't compile, runtime error, wrong logic |
| Test failure | Tests fail, assertions don't match expected behavior |
| Design issue | Approach is fundamentally wrong, needs rethinking |
| External failure | Tool unavailable, MCP timeout, permission denied |
| Unknown | Cannot determine cause from available information |

### Step 2: Determine Recovery Action

| Failure Type | Retry < 2 | Retry >= 2 |
|-------------|-----------|------------|
| Implementation error | Retry with debug context | Escalate — request revised plan from planner |
| Test failure | Retry: debug → fix → retest | Escalate |
| Design issue | Escalate immediately — request revised plan | Escalate |
| External failure | Retry after brief wait | Escalate with environment issue report |
| Unknown | Assign to agent_debug for investigation | Escalate |

### Step 3: Preserve Completed Work
Recovery must never discard completed tasks. When replanning, carry forward all successful results.

## Output

Return:
1. **Failure classification** — type and reasoning
2. **Recovery action** — retry / debug / replan / escalate
3. **Recovery context** — what information to pass to the next attempt
4. **Preserved state** — confirmation that completed work is retained

## Constraints

- Maximum 2 retries per task before escalating.
- Do not retry design issues — escalate immediately.
- Always include failure details when retrying so the agent has context on what went wrong.
