---
name: knowledge-graph-standards
description: Enforce knowledge graph design and query standards. Use when building, reviewing, or evaluating graph database code.
---

# Knowledge Graph Standards

Enforce mandatory standards for knowledge graph systems.

## Architecture
Graph interactions must follow: `API/MCP → Service → Graph Repository → Graph DB`. Queries never from route handlers or services directly.

## Schema (Mandatory)
- Each node type documented with: label, required/optional properties, constraints, indexes
- Relationships: UPPERCASE, verb form, directionally meaningful
  - Correct: `(:User)-[:PURCHASED]->(:Order)`
  - Forbidden: `(:User)-[:order]->(:Order)`
- Direction must reflect logical semantics and be consistent

## Constraints & Indexes
- Unique constraints on identifiers
- Indexes on frequently filtered properties
- Created via migration/startup script — never manually

## Query Rules
- All queries encapsulated in repository methods (no inline `graph.query(...)`)
- Complex query strings centralized in `queries/` — no duplication
- All queries parameterized (no string interpolation)
  - Forbidden: `f"MATCH (u:User {{user_id: '{user_id}'}})"`
  - Required: `MATCH (u:User {user_id: $user_id})`

## Idempotency
- Use MERGE instead of CREATE when appropriate
- Unique constraints prevent silent duplication

## Performance
- No full graph scans (`MATCH (n) RETURN n` forbidden unless justified)
- Profile complex queries with EXPLAIN/PROFILE before merging
- Always use LIMIT — no unbounded result sets

## Data Integrity
- Validate required properties before insertion
- Create relationships atomically with nodes
- Ensure node existence before relationship creation (no dangling relationships)

## Transactions
Managed in service layer, not scattered across repositories. Wrap multi-step operations.

## Bulk Operations
Batching for large writes. No per-node transactions.

## Observability
Log: query execution time, nodes/relationships affected, batch sizes. Do NOT log full results for large datasets.

## Anti-Patterns (Forbidden)
- Graph queries in route handlers
- String-interpolated Cypher
- No constraints on unique identifiers
- Full graph scans in production
- Silent duplicate node creation
- Business logic in repository
