# General Python Standards

Python Version: 3.10+ (Mandatory)

1. Purpose
This document defines mandatory Python coding standards for all projects.
The goal is to ensure:
- Readability
- Maintainability
- Determinism
- Production readiness
- Consistency across teams

These standards are not optional and must be enforced via CI.

2. Core Engineering Principles
- Code is read more often than it is written.
- Explicit is better than implicit.
- Simple is better than clever.
- Deterministic behavior is required in production systems.
- Production-grade quality is the default expectation.

3. Tooling & Enforcement (Mandatory)
All repositories MUST use:
- black
- isort
- flake8
- mypy
- pytest

    - 3.1 CI Requirements
        Every pull request must pass:
        - Formatting check
        - Lint check
        - Type check
        - Test execution
        - Minimum coverage threshold

        No PR may bypass CI.

4. Formatting Rules
- 4.1 Line Length
    - Maximum: 88 characters
    - Do not manually override formatting that conflicts with black

- 4.2 Indentation
    - 4 spaces only
    - Tabs are forbidden

- 4.3 Trailing Commas
    - Required in multi-line collections:
    ```
    items = [
        "user",
        "admin",
    ]
    ```

5. Import Standards
- 5.1 Import Order
    - Standard library
    - Third-party libraries
    - Local modules
    Example:
    ```
    import os
    import logging

    import numpy as np
    from fastapi import FastAPI

    from app.services.user_service import UserService
    ```

- 5.2 Rules
    - Wildcard imports are forbidden.
    - Circular imports are forbidden.
    - Imports inside functions are discouraged except:
        - To resolve circular dependencies
        - For optional heavy dependencies

6. Naming Conventions
Item -> Convention
- Variables: snake_case
- Functions: snake_case
- Classes: PascalCase
- Constants: UPPER_CASE
- Private attributes/methods: _leading_underscore
- Modules: snake_case

- 6.1 Clarity Rule
    Avoid abbreviations unless industry standard.

7. Type Hints (Strictly Mandatory)
All public functions and methods must include full type hints.
- 7.1 Function Example
    ```
    def fetch_user(user_id: int) -> User:
    ...
    ```
- 7.2 Collections (Python 3.10+)
    Use built-in generics:
    ```
    def process(items: list[str]) -> dict[str, int]:
    ```
    Avoid typing.List and typing.Dict.

- 7.3 Optional Types
    ```
    def get_user(user_id: int) -> User | None:
    ```

- 7.4 Any Usage
    Usage of Any must include justification in a comment.

8. Function Design Rules
- 8.1 Function Length
    - Recommended maximum: 40 lines
    - Hard limit: 60 lines
    Refactor if exceeded.

- 8.2 Parameter Count
    - Soft limit: 4 parameters
    - Use dataclass or configuration object beyond that

- 8.3 No Hidden Side Effects
    Functions must not:
    - Mutate global state
    - Modify input arguments unexpectedly

9. Class Design Rules
- 9.1 Single Responsibility Principle
    A class must have one clear responsibility.

- 9.2 Size Limits
    Refactor if a class exceeds:
    - 300 lines
    - 15 public methods

- 9.3 Dependency Injection
    Dependencies must be injected.
    Bad:
    ```
    class Service:
        def __init__(self):
            self.db = Database()
    ```

    Good:
    ```
    class Service:
        def __init__(self, db: Database):
            self.db = db
    ```

10. Docstring Standards (Google Style)
All public:
- Modules
- Classes
- Functions
Must include docstrings.

Example:
```
def calculate_score(values: list[float]) -> float:
    """Calculate the mean score.

    Args:
        values: List of numeric values.

    Returns:
        The average value.

    Raises:
        ValueError: If values is empty.
    """
```

11. Exception Handling Standards
- 11.1 Bare Except is Forbidden
    ```
    except:
        pass
    ```
    Is not allowed.

- 11.2 Specific Exceptions Only
    Always catch specific exception types.

- 11.3 Logging Before Raising
    When catching and re-raising in service layers:
    ```
    except ValueError as exc:
        logger.error("Invalid input: %s", exc)
        raise
    ```

- 11.4 Custom Exceptions
    Domain-specific errors must use custom exception classes.

12. Logging Standards
- print() is forbidden in production code.
- Use the logging module.
```
import logging

logger = logging.getLogger(__name__)
```

- 12.1 Logging Rules
Logs must include:
- Context identifiers
- Relevant metadata
- Correlation IDs (if available)

Log levels must be used correctly:
- DEBUG – development diagnostics
- INFO – normal operations
- WARNING – recoverable issues
- ERROR – failure of operation
- CRITICAL – system-level failure

13. Configuration Management
- Hardcoded secrets are forbidden.
- Hardcoded environment values are forbidden.
- Use environment variables or configuration classes.

Forbidden:
```
DB_PASSWORD = "admin123"
```

14. Global State
Global mutable state is forbidden except:
- Immutable constants
- Explicitly documented singletons

15. Concurrency Rules
- Async functions must not call blocking I/O.
- Shared mutable state must be protected or avoided.
- Thread safety must be documented where relevant.

16. Determinism Requirements (Critical for ML & ETL)
If randomness is used:
- Random seed must be configurable.
- Random seed must be logged.
- Seed must be set explicitly.

17. Dependency Management
- All dependencies must be pinned.
- Lock files are mandatory.
- Broad version ranges (>=) are discouraged.
- Unused dependencies must be removed.

18. Code Complexity
- Maximum cyclomatic complexity per function: 10
- If exceeded, refactor into smaller functions.

19. Anti-Patterns (Strictly Forbidden)
- Business logic inside route handlers
- Database queries in controllers
- Silent exception swallowing
- Circular imports
- Hidden global mutation
- Overuse of inheritance
- Magic numbers (use constants instead)

21. Definition of Acceptable Code
Code is acceptable only if it is:
- Readable
- Typed
- Testable
- Deterministic
- Configurable
- Observable
- Secure
- Maintainable
