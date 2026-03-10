# Knowledge Graph Standards

Scope: Graph schema design, query standards, repository design, performance, integrity, scalability

1. Purpose
This document defines mandatory standards for designing and interacting with knowledge graphs to ensure:
- Schema clarity
- Query consistency
- Performance
- Data integrity
- Maintainability
- Scalability
Knowledge graphs are not schemaless data dumps. They require strict structure and discipline.

2. Core Principles
- Graph schema must be defined explicitly.
- Queries must be encapsulated in repositories.
- Relationships must be semantically meaningful.
- Graph operations must be deterministic and idempotent.
- Performance considerations must be built-in from day one.

3. Graph Architecture
Graph interactions must follow layered architecture:
```
API / MCP Layer
        ↓
Service Layer
        ↓
Graph Repository Layer
        ↓
Graph Database
```

Graph queries must never be executed from:
- Route handlers
- Service layer directly
- Utility modules

4. Graph Project Structure
```
graph/
 ├── schema/
 │    ├── nodes.py
 │    └── relationships.py
 ├── repositories/
 ├── services/
 ├── queries/
 ├── validators/
 └── tests/
```

- 4.1 Directory Responsibilities
    - schema/ → Node and relationship definitions
    - repositories/ → Encapsulated graph CRUD
    - queries/ → Centralized query templates
    - services/ → Business logic
    - validators/ → Graph data validation
    - tests/ → Unit + integration tests

5. Schema Standards (Mandatory)
- 5.1 Explicit Node Definitions
    Each node type must be documented with:
    - Label
    - Required properties
    - Optional properties
    - Constraints
    - Indexes

    Example:
    ```
    Node: User
    Properties:
    - user_id (unique, required)
    - name (required)
    - created_at (required)
    ```

- 5.2 Relationship Naming Conventions
    Relationships must:
    - Be uppercase
    - Use verb form
    - Be directionally meaningful
    Correct:
    ```
    (:User)-[:PURCHASED]->(:Order)
    ```
    Forbidden:
    ```
    (:User)-[:order]->(:Order)
    ```

- 5.3 Relationship Direction
    Relationship direction must reflect logical semantics.
    - Direction must be consistent across system.
    - Bidirectional semantics must be explicitly documented.

6. Constraints & Indexes (Mandatory)
For each node:
- Unique constraints must be defined where applicable.
- Frequently filtered properties must be indexed.
- Constraints must be created via migration or startup initialization script — never manually.

7. Query Encapsulation (Strictly Required)
Graph queries must be encapsulated in repository methods.
Forbidden:
```
graph.query("MATCH (u:User) RETURN u")
```
Required:
```
class UserGraphRepository:
    def get_user_by_id(self, user_id: str) -> User:
        ...
```

8. Query Centralization
Complex query strings must:
- Be defined in queries/
- Not be scattered across files
- Not be duplicated
No copy-paste query strings across services.

9. Parameterization (Mandatory)
All queries must use parameter binding.
Forbidden:
```
query = f"MATCH (u:User {{user_id: '{user_id}'}}) RETURN u"
```
Required:
```
query = """
MATCH (u:User {user_id: $user_id})
RETURN u
"""
```

10. Idempotency Rules
Graph write operations must be idempotent where possible.
Use:
- MERGE instead of CREATE when appropriate
- Unique constraints to prevent duplication
Duplicate nodes must not be allowed silently.

11. Bulk Operations
For large graph writes:
- Use batching
- Avoid per-node transactions
- Use optimized bulk APIs

12. Transaction Management
Transactions must:
- Be managed in service layer
- Not be scattered across repositories
- Wrap multi-step graph operations

13. Performance Standards
- 13.1 Avoid Full Graph Scans
    Forbidden:
    ```
    MATCH (n) RETURN n
    ```
    Unless explicitly justified.

- 13.2 Query Profiling Required
    Before merging complex queries:
    - Profile with EXPLAIN/PROFILE
    - Validate index usage
    - Document performance characteristics

- 13.3 Limit Result Sets
    Always:
    - Use LIMIT when appropriate
    - Avoid returning unbounded nodes

14. Data Integrity
- 14.1 Required Properties
    Required properties must be validated before insertion.

- 14.2 No Orphan Nodes
    Relationships must be created atomically with nodes where applicable.

- 14.3 Referential Consistency
    Ensure:
    - Node existence before relationship creation
    - No dangling relationships

15. Graph Evolution & Versioning
Graph schema changes must:
- Be versioned
- Be documented
- Include migration scripts if required
Never modify schema ad hoc in production.

16. Concurrency Considerations
For high-write systems:
- Use optimistic locking strategies
- Use unique constraints to prevent race duplicates
- Handle constraint violation errors gracefully

17. Testing Requirements
Each graph repository must have:
- Node creation tests
- Relationship creation tests
- Query correctness tests
- Constraint violation tests
Integration tests must run against test graph DB.

18. Observability & Logging
Log:
- Query execution time
- Number of nodes affected
- Batch sizes
Do NOT log:
- Full query results for large datasets
- Sensitive properties

19. Security Standards
- Parameterize queries
- Validate input before query execution
- Restrict DB credentials to least privilege
- Avoid exposing graph internals in API responses

20. Large Graph Scaling
When graph size grows:
- Use proper indexing strategy
- Monitor query plans
- Archive or partition historical data if necessary
- Consider read replicas if supported

21. Anti-Patterns (Strictly Forbidden)
- Graph queries in route handlers
- String-interpolated Cypher queries
- No constraints on unique identifiers
- Full graph scans in production endpoints
- Silent duplicate node creation
- Business logic inside repository

22. Definition of Production-Ready Graph System
A knowledge graph system is production-ready when:
- Schema is documented
- Constraints are enforced
- Queries are encapsulated
- Performance is validated
- Writes are idempotent
- Data integrity is preserved
- Observability is implemented
- Tests exist


