---
name: database-standards
description: Enforce database and repository design standards. Use when writing, reviewing, or evaluating database access code.
---

# Database & Repository Standards

Enforce mandatory standards for database interaction and repository design.

## Core Rules
- All DB access through repository classes
- Business logic must NOT exist in repositories
- Transactions managed at service layer
- Repositories receive DB session via injection

## Repository Pattern

### Responsibilities
CRUD operations, query construction, data persistence, returning domain models.

### Must NOT
Contain business logic, handle HTTP concerns, perform cross-domain orchestration, manage transactions independently.

## Session Management
- Request-scoped sessions for APIs
- No long-lived global sessions
- Transactions controlled in service layer

## Query Standards
- No raw SQL in API layer — all queries in repositories
- Raw SQL allowed only when ORM insufficient (requires justification comment + parameterized queries)
- String concatenation in queries is forbidden: `f"SELECT * FROM users WHERE id = {user_id}"`

## Performance
- No N+1 queries — use joins, eager loading, batch queries
- Indexes on: foreign keys, frequently filtered/sorted columns (defined via migrations)
- Bulk operations for large inserts/updates (no row-by-row commits)

## Migrations (Mandatory)
- All schema changes via migration tools (e.g., Alembic)
- No manual DB changes, no auto-create in production
- One migration per schema change, down migrations where feasible

## Schema Conventions
- Tables: `snake_case` plural
- Columns: `snake_case`
- Foreign keys: `<entity>_id`
- Indexes: `idx_<table>_<column>`
- All entities must have `created_at`, `updated_at`

## Graph DB Rules
- Queries encapsulated in repository methods
- Query strings centralized (not scattered)
- Relationships: UPPERCASE, verb-based, directionally meaningful
- All queries parameterized (no string interpolation)

## Error Handling
- Translate DB exceptions into domain-specific exceptions
- Retry logic: limited, exponential backoff, at service/infrastructure layer

## Connections
- Connection pooling enabled with configurable parameters
- All connections must have: connect timeout, read timeout, statement timeout

## Multi-Repository
- Service layer coordinates
- Single transaction wraps operation
- Repositories must not call each other

## Anti-Patterns (Forbidden)
- DB queries in route handlers
- Global DB sessions
- Auto-committing inside repositories
- N+1 query patterns
- String-interpolated SQL
- Schema changes outside migrations
- Business logic in repositories
