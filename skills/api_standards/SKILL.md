---
name: api-standards
description: Enforce API development standards. Use when building, reviewing, or evaluating REST APIs for standards compliance.
---

# API Standards

Enforce mandatory standards for building production-ready APIs.

## Layering
API layer handles: request parsing, input validation, auth, calling service layer, returning response.
API layer must NOT: access DB directly, contain business rules, manage transactions, call external services.

## Rules

### Route Handlers
- Must be thin — call a single service function
- Group routes by domain in `api/routes/`
- No business logic in handlers

### Validation (Mandatory)
- All input via Pydantic models (no raw parameters)
- Every endpoint must define `response_model`
- No raw dict responses

### HTTP Status Codes
200 (GET), 201 (created), 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found), 409 (conflict), 422 (validation), 500 (internal). Do not always return 200.

### Error Handling
- No internal exception/stack trace leakage
- Standard error format: `{"error": {"code": "...", "message": "...", "details": {}}}`
- Service raises domain exceptions → API translates to HTTP responses

### Dependency Injection
- Services, DB sessions, config, clients injected via framework mechanisms
- Never instantiate services inside route handlers

### Auth
- Authentication via middleware or dependency (no manual token parsing)
- Authorization checks explicit, before service call, using role/permission abstraction

### Pagination
All list endpoints must support pagination (`limit`/`offset` or cursor). No unbounded result sets.

### Versioning
Public APIs versioned (`/api/v1/...`). Breaking changes require new version.

### Async
- Required for async DB, HTTP clients, I/O
- Must not call blocking code
- CPU-heavy tasks → background workers / task queues

### Performance
- No N+1 queries
- Pagination for large payloads
- Explicit timeouts on external calls

### Observability
Each request logs: request ID, route, status code, execution time. No sensitive data in logs.

### Other
- Rate limiting on public/auth/write endpoints
- `/health` (liveness) and `/ready` (readiness) endpoints required, no auth
- Idempotency keys for critical POST endpoints
- File uploads: size limits, content type validation
- OpenAPI docs enabled, accurate, updated

## Anti-Patterns (Forbidden)
- Business logic in route handlers
- DB queries in controllers
- Unbounded list endpoints
- Always returning 200
- Swallowing exceptions
- Logging secrets
- Returning internal stack traces
