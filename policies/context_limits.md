# Context Limits Policy

This policy defines how context should be managed across agents.
Large or irrelevant context can degrade reasoning performance and increase computational cost.

Agents must operate with **focused and minimal context**.

---

# Context Minimization Principles

Agents should receive only the information required to complete the task.
The coordinator must avoid sending excessive information to sub-agents.

---

# Required Context Elements

Every task context must include:
- Task ID
- Task Objective
- Relevant Files
- Dependencies
- Constraints
- Allowed Tools
- Success Criteria

These elements are defined in:
    schemas/task_context_template.md

---

# Avoid Context Overload

The coordinator must avoid sending:

• full repository listings
• large documentation dumps
• irrelevant conversation history

Only relevant context should be included.

---

# Context Reuse

If context has already been provided to previous tasks and remains valid, it should be reused instead of re-fetching information.

---

# Agent Context Boundaries

Each agent should operate only within the context of its assigned task.
Agents must not attempt to infer unrelated information outside their provided context.

---

# Context Efficiency Outcome

Maintaining focused context ensures:

• faster reasoning
• reduced hallucination
• more reliable task execution
