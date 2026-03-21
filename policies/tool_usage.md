# Tool Usage Policy

This policy defines how agents should use tools when executing tasks.

Tools provide access to external systems such as the filesystem, repositories, documentation sources, or runtime environments.

Improper tool usage can significantly increase context size and slow down reasoning.

Agents must use tools carefully and only when necessary.

---

# General Tool Principles

Agents must follow these principles.

• use tools only when necessary
• avoid redundant tool calls
• avoid retrieving excessive data
• retrieve only relevant information

---

# Tool Scope

- Each agent has a predefined list of allowed tools.
- Agents must only use tools listed in their **tools.yaml** configuration.
- Agents must never attempt to use tools that are not explicitly allowed.

---

# Coordinator Tool Restrictions

- The coordinator agent must not perform repository exploration or execution tasks.
- The coordinator's role is orchestration.
- Allowed coordinator tools should typically be limited to reasoning tools such as:
    - sequential_thinking

---

# Efficient Retrieval

When retrieving information from tools:
- Agents must prefer **focused queries** over broad scanning.
    Example:
    Bad:
        Scan entire repository.
    Better:
        Search for the database connection implementation.

---

# Avoid Redundant Tool Calls

Agents must avoid repeatedly calling tools for the same information.
If relevant information has already been retrieved, reuse it.

---

# Tool Usage Outcome

Tool calls must support task execution.
Tools should not be used for unnecessary exploration or speculative analysis.
