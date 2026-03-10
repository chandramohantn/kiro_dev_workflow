# Database and Repository Standards

Scope: Database access, repository pattern, transactions, performance, migrations, reliability

1. Purpose
This document defines strict standards for database interaction and repository design to ensure:
- Clear separation of concerns
- Performance and scalability
- Transaction safety
- Testability
- Security
- Maintainability
Database misuse is a critical architectural violation.

2. Core Principles
- Database access must be isolated in repositories.
- Business logic must not exist in repositories.
- Transactions must be managed at the service layer.
- Queries must be predictable and optimized.
- Schema evolution must be controlled via migrations.

3. Repository Pattern (Mandatory)
All database access must occur through repository classes.

- 3.1 Repository Responsibilities
    Repositories are responsible for:
    - CRUD operations
    - Query construction
    - Data persistence
    - Returning domain models
    Repositories must NOT:
    - Contain business logic
    - Handle HTTP concerns
    - Perform cross-domain orchestration

- 3.2 Example Repository Structure
```
repositories/
 ├── user_repository.py
 ├── order_repository.py
 └── graph_repository.py
```

- 3.3 Dependency Injection Required
    Repositories must receive DB session/connection via injection.
    Forbidden:
    ```
    class UserRepository:
        def __init__(self):
            self.session = create_session()
    ```

    Required:
    ```
    class UserRepository:
        def __init__(self, session: Session):
            self.session = session
    ```

4. Database Session Management
- 4.1 Session Scope
    - Session lifecycle must be request-scoped for APIs.
    - Long-lived global sessions are forbidden.

- 4.2 Transaction Handling
    Transactions must be controlled in the service layer.
    Example:
    ```
    with session.begin():
        service.create_user(...)
    ```
    Repositories must NOT manage transactions independently unless explicitly required.

5. Query Standards
- 5.1 No Raw SQL in API Layer
    All queries must be inside repository.

- 5.2 Raw SQL Usage
    Allowed only when:
    - ORM is insufficient
    - Performance-critical optimization required
    Must include:
    - Justification comment
    - Parameterized queries
    - No string concatenation
    Forbidden:
    ```
    query = f"SELECT * FROM users WHERE id = {user_id}"
    ```

6. Performance Guidelines
- 6.1 Avoid N+1 Queries
    Use:
    - Joins
    - Eager loading
    - Batch queries
    N+1 issues must be detected in review.

- 6.2 Indexing Rules
    Indexes must be added for:
    - Foreign keys
    - Frequently filtered columns
    - Frequently sorted columns
    All indexes must be defined via migrations.

- 6.3 Bulk Operations
    For large inserts/updates:
    - Use batch operations
    - Avoid row-by-row commits
    - Use optimized bulk methods

7. Migrations (Mandatory)
All schema changes must use migration tools (e.g., Alembic).
Forbidden:
- Manual DB changes
- Auto-create schema in production

Rules:
- One migration per schema change
- Migrations must be reviewed
- Down migrations must exist (if feasible)

8. Schema Design Standards
- 8.1 Naming Conventions
    - Item -> Convention
    - Tables: snake_case plural
    - Columns: snake_case
    - Foreign Keys: <entity>_id
    - Indexes: idx_<table>_<column>

- 8.2 Primary Keys
    - Use surrogate keys (e.g., UUID or integer)
    - Avoid composite primary keys unless justified

- 8.3 Timestamps
    All persistent entities must include:
    - created_at
    - updated_at
    Managed automatically where possible.

9. Graph Database Standards
- 9.1 Query Encapsulation
    All graph queries must be encapsulated in repository methods.
    Forbidden:
    ```
    graph.query("MATCH (n) RETURN n")
    ```

    Required:
    ```
    def fetch_all_nodes(self) -> list[Node]:
    ```

- 9.2 Query Centralization
    Graph query strings must:
    - Be centralized
    - Not scattered across services

- 9.3 Relationship Naming
    Relationships must:
    - Be uppercase
    - Verb-based
    - Directionally meaningful
    Example:
    ```
    (:User)-[:PURCHASED]->(:Order)
    ```

10. Concurrency & Isolation
- 10.1 Isolation Level
    Default isolation level must be documented.
    If custom isolation level used:
    - Must include justification
    - Must be documented in repository

- 10.2 Optimistic Locking (Recommended)
    Use version columns for high-concurrency systems.

11. Error Handling
- 11.1 Translate DB Exceptions
    Database exceptions must be translated into domain-specific exceptions.
    Do not leak raw DB errors upward.

- 11.2 Retry Logic
    Retry logic for transient errors must:
    - Be limited
    - Use exponential backoff
    - Be implemented at service/infrastructure layer

12. Connection Management
- 12.1 Connection Pooling
    Connection pooling must be enabled.
    Parameters must be:
    - Configurable
    - Documented

- 12.2 Timeouts
    All connections must have:
    - Connect timeout
    - Read timeout
    - Statement timeout (if supported)

13. Multi-Repository Coordination
If multiple repositories are involved:
- Service layer must coordinate
- Single transaction must wrap operation
Repositories must not call each other directly.

14. Testing Requirements
Repositories must have:
- Integration tests against test DB
- Edge case validation tests
- Constraint violation tests
Test DB must not be production DB.

15. Security Requirements
- Always use parameterized queries
- Never log raw SQL with sensitive parameters
- Validate inputs before persistence
- Use least-privilege DB credentials

16. Large Data Handling
For large datasets:
- Use streaming queries
- Avoid loading entire tables in memory
- Use pagination or chunking

17. Data Integrity Rules
- Use foreign key constraints
- Use NOT NULL where appropriate
- Use unique constraints where required
- Validate at application and DB level

18. Anti-Patterns (Strictly Forbidden)
- DB queries inside route handlers
- Global DB sessions
- Auto-committing inside repositories
- N+1 query patterns
- Hardcoded SQL strings with interpolation
- Schema modification outside migrations
- Business logic inside repository methods

19. Scaling Guidelines
When system grows:
- Introduce read replicas if needed
- Separate write-heavy and read-heavy workloads
- Consider partitioning for large tables
- Monitor slow query logs

20. Definition of Correct Repository Design
Repository layer is correct when:
- It contains only data access logic
- It is injectable
- It does not contain business rules
- It does not manage cross-domain workflows
- It supports efficient querying
- It is testable independently

