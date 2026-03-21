---
name: python-standards
description: Enforce general Python coding standards. Use when writing, reviewing, or evaluating Python code for standards compliance.
---

# Python Standards

Enforce mandatory Python coding standards for production-ready code.

## Tooling (Must Pass CI)
black, isort, flake8, mypy, pytest — all mandatory. No PR bypasses CI.

## Rules

### Formatting
- Line length: 88 chars (black default)
- 4-space indentation, no tabs
- Trailing commas in multi-line collections

### Imports
- Order: stdlib → third-party → local
- No wildcard imports
- No circular imports

### Naming
- Variables/functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`
- Private: `_leading_underscore`
- No abbreviations unless industry standard

### Type Hints (Strictly Mandatory)
- All public functions must have full type hints
- Use built-in generics (`list[str]`, `dict[str, int]`) — not `typing.List`
- Use `X | None` — not `Optional[X]`
- `Any` requires justification comment

### Functions
- Max 40 lines recommended, 60 hard limit
- Max 4 parameters (use dataclass beyond that)
- No hidden side effects, no global state mutation

### Classes
- Single responsibility
- Max 300 lines, 15 public methods
- Dependencies must be injected (no self-instantiation)

### Docstrings (Google Style)
Required on all public modules, classes, functions. Must include Args, Returns, Raises.

### Exception Handling
- Bare `except:` forbidden
- Catch specific exceptions only
- Log before re-raising in service layers
- Use custom exceptions for domain errors

### Logging
- `print()` forbidden in production
- Use `logging` module with `__name__`
- Include context identifiers and correlation IDs
- Correct log levels: DEBUG/INFO/WARNING/ERROR/CRITICAL

### Configuration
- No hardcoded secrets or environment values
- Use env vars or config classes

### Other Rules
- No global mutable state (except immutable constants)
- Async must not call blocking I/O
- Random seeds must be configurable and logged
- All dependencies pinned with lock files
- Max cyclomatic complexity: 10 per function

## Anti-Patterns (Forbidden)
- Business logic in route handlers
- DB queries in controllers
- Silent exception swallowing
- Hidden global mutation
- Magic numbers (use constants)
- Overuse of inheritance
