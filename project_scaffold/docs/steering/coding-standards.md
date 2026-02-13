# Coding Standards (Python)

## Purpose
These rules define how we write, structure, and review Python code in this project.
They are **mandatory** for all changes unless an ADR explicitly states otherwise.

Agents and humans must follow these rules.

---

## 1. General Principles

- Prefer **clarity over cleverness**
- Write **boring, readable, testable** code
- Keep functions:
  - Small
  - Single-purpose
  - Side-effect aware
- Favor **explicitness** over magic
- Avoid premature optimization

---

## 2. Project Structure & Layering

- Respect existing layering (e.g., API → Service → Repo / Domain → Infra)
- Do not bypass layers unless explicitly allowed in `docs/steering/architecture.md`
- Keep:
  - I/O at the edges
  - Business logic in the middle
  - Data access isolated

---

## 3. Naming Conventions

- Files: `snake_case.py`
- Classes: `PascalCase`
- Functions & variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Be descriptive:
  - ❌ `process()`
  - ✅ `process_user_events_batch()`

---

## 4. Typing & Type Safety

- Use type hints for:
  - Public functions
  - Service boundaries
  - Complex data structures
- Prefer:
  - `typing` / `typing_extensions`
  - `pydantic` models for schemas and contracts
- Avoid:
  - `Any` unless absolutely necessary (and document why)
- If a function is hard to type:
  - That’s a design smell—consider refactoring

---

## 5. Error Handling

- Never silently swallow exceptions
- Prefer:
  - Explicit exception types
  - Domain-specific exceptions where useful
- At boundaries (API, jobs, workers):
  - Catch and translate exceptions into:
    - Proper HTTP errors
    - Proper job failure states
- Log errors with **context**, not just stack traces

---

## 6. Logging

- Use structured logging if available
- Log:
  - Important state transitions
  - Errors with context
  - Warnings for suspicious but recoverable situations
- Do NOT:
  - Log secrets
  - Log full payloads if they contain sensitive data
- Prefer:
  - `logger.info("event happened", extra={...})`
  - Over `print()`

---

## 7. Formatting & Style

- Follow PEP8
- Use:
  - Black (or project formatter)
  - isort (if used in project)
- Keep line length reasonable (typically ≤ 100–120)
- Avoid deeply nested code:
  - Refactor into smaller functions

---

## 8. Imports

- Group imports:
  1. Standard library
  2. Third-party
  3. Local/project
- Avoid wildcard imports
- Avoid circular imports

---

## 9. Documentation & Docstrings

- Public modules, classes, and functions must have docstrings
- Docstrings should explain:
  - What the function does
  - Important parameters
  - Important side effects or invariants
- Do NOT restate obvious code—document **intent**

---

## 10. Tests

- All non-trivial logic must be covered by tests
- Bugfixes MUST include a regression test
- Tests should be:
  - Deterministic
  - Isolated
  - Readable
- Prefer pytest (unless project says otherwise)

---

## 11. Code Review Checklist

Before considering a change “done”:

- [ ] Code follows naming and structure conventions
- [ ] Types are present where appropriate
- [ ] Errors are handled explicitly
- [ ] Logging is appropriate and safe
- [ ] Tests cover the behavior
- [ ] No unnecessary complexity or scope creep

---

## 12. When to Break These Rules

- Only with:
  - A clear justification
  - Preferably an ADR
- Document:
  - Why the rule was broken
  - What the risk is
  - What would fix it later
