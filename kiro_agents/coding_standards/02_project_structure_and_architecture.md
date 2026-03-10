# Project Structure & Architecture Standards

Scope: Repository layout, layering rules, architectural boundaries, dependency management

1. Purpose
This document defines mandatory architectural standards to ensure:
- Clear separation of concerns
- Scalable system design
- Maintainable codebases
- Testability
- Production-grade reliability
Architecture violations are considered critical review failures.

2. Core Architectural Principles
- Separation of concerns is mandatory.
- Business logic must be framework-independent.
- Infrastructure must be replaceable.
- Dependencies must point inward (clean architecture principle).
- No cross-layer shortcuts.
- Code must be testable without external systems where possible.

3. Layered Architecture (Mandatory)
All production systems must follow layered architecture.

- 3.1 Standard Backend Layering
    ```
    Presentation Layer (API / MCP / CLI)
            ↓
    Service Layer (Business Logic)
            ↓
    Repository Layer (Data Access)
            ↓
    Infrastructure Layer (DB, External APIs, File Systems)
    ```

- 3.2 Layer Responsibilities
    - 3.2.1 Presentation Layer
        Examples:
        - FastAPI routes
        - MCP handlers
        - CLI commands
        Responsibilities:
        - Request parsing
        - Input validation
        - Response formatting
        - HTTP status codes
        - Authentication/authorization checks
        Forbidden:
        - Database queries
        - Business logic
        - External service orchestration

    - 3.2.2 Service Layer
        Responsibilities:
        - Business rules
        - Workflow orchestration
        - Transaction coordination
        - Domain validation
        Forbidden:
        - Direct HTTP handling
        - Raw SQL
        - Framework-specific logic
        Services must be pure Python logic wherever possible.

    - 3.2.3 Repository Layer
        Responsibilities:
        - Database CRUD
        - Graph queries
        - Data persistence logic
        Rules:
        - No business rules
        - No HTTP handling
        - No cross-repository logic
        Repositories must be injectable.

    - 3.2.4 Infrastructure Layer
        Responsibilities:
        - DB connections
        - External APIs
        - File storage
        - Cache systems
        - Message queues
        - Infrastructure must be abstracted behind interfaces.

4. Directory Structure Standards
- 4.1 API Service Structure
    ```
    app/
    ├── main.py
    ├── api/
    │    ├── routes/
    │    └── dependencies/
    ├── services/
    ├── repositories/
    ├── models/
    ├── schemas/
    ├── core/
    │    ├── config.py
    │    ├── logging.py
    │    └── security.py
    ├── infrastructure/
    └── tests/
    ```

    Rules:
    - Routes only in api/routes
    - Business logic only in services
    - DB access only in repositories
    - Config centralized in core/config.py

- 4.2 ETL Project Structure
    ```
    etl/
    ├── extract/
    ├── transform/
    ├── load/
    ├── pipelines/
    ├── jobs/
    ├── validators/
    ├── config/
    └── tests/
    ```

    Rules:
    - Extract, transform, load must be modular
    - Pipelines orchestrate modules
    - Jobs define execution entrypoints
    - No hardcoded paths

- 4.3 Machine Learning Project Structure
    ```
    ml/
    ├── data/
    ├── features/
    ├── training/
    ├── evaluation/
    ├── inference/
    ├── models/
    ├── config/
    └── tests/
    ```

    Strict separation required:
    - Training code must not be imported by inference modules
    - Inference must not depend on training logic

- 4.4 MCP Server Structure
    ```
    mcp/
    ├── protocol/
    ├── handlers/
    ├── services/
    ├── repositories/
    ├── config/
    └── tests/
    ```

    Rules:
    - Protocol handling separated from business logic
    - Handlers must call services
    - No DB logic in protocol layer

5. Dependency Direction Rules
Dependencies must follow this rule:
- API → Services → Repositories → Infrastructure
- Never reverse

Forbidden:
- Repository importing Service
- Service importing Route
- Infrastructure importing Business Logic

6. Configuration Management
- Configuration must be centralized.
- No scattered environment variable reads.
- Use a typed configuration class.
Example:
```
class Settings:
    database_url: str
    redis_url: str
```

7. Dependency Injection (Mandatory)
Dependencies must be injected at construction.
Forbidden:
```
class UserService:
    def __init__(self):
        self.repo = UserRepository()
```
Required:
```
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
```

8. No Cross-Layer Shortcuts
Forbidden:
- Calling DB directly from route
- Calling external API from repository
- Running training inside API route
- All communication must respect layering.

9. Transaction Management
Transactions must be managed in:
- Service layer
- Not in routes
- Not scattered across repositories
Services coordinate multi-repository operations.

10. Circular Dependency Prevention
Rules:
- Shared logic must go to a lower-level module
- Common utilities must live in core or utils
- No mutual imports between services

11. Module Size Guidelines
Refactor if:
- Module exceeds 500 lines
- Service contains unrelated logic
- Repository handles multiple domains
One domain per module principle.

12. Domain-Driven Boundaries (Recommended)
Group by domain, not by technical type, when system grows.
Example:
```
users/
 ├── api.py
 ├── service.py
 ├── repository.py
 └── schemas.py
```
Preferred for large systems.

13. Testability Requirements
Architecture must allow:
- Service unit tests without DB
- Repository integration tests with DB
- API tests without business logic mocking where possible
If something cannot be tested in isolation, architecture is incorrect.

14. Anti-Patterns (Strictly Forbidden)
- Fat controllers
- God services
- Multi-responsibility repositories
- Shared global DB session
- Hidden singleton dependencies
- Tight coupling between modules
- Hardcoded infrastructure inside business logic

15. Scaling Guidelines
As system grows:
- Split domains into packages
- Introduce internal SDK layer
- Extract shared modules into reusable libraries
- Consider microservice split only when domain boundaries are clear
Premature microservices are discouraged.

16. Definition of Architecturally Correct Code
Code is architecturally correct when:
- Each layer has one responsibility
- Dependencies flow inward only
- Business logic is framework-agnostic
- Infrastructure is replaceable
- Modules are domain-focused
- Code is testable in isolation

