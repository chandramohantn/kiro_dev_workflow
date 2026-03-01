# MR/PR Review Checklist

# Code Review Checklist
- All functions typed
- Docstrings present
- Lint passes
- Type checks pass
- Tests added
- No prints
- No hardcoded secrets
- No layering violations

# Architecture Review Checklist
- No DB logic in routes
- No business logic in repositories
- Dependencies injected
- No circular imports
- Layering respected
- Config centralized
- Services testable without external systems

## API Review Checklist
- Response models defined
- Validation models defined
- No business logic in routes
- Proper HTTP status codes used
- Pagination implemented (if list endpoint)
- Auth checks present
- Logging added
- Tests written
- No unbounded queries
- No blocking code in async route

## Database Review Checklist
- No DB logic in routes
- No business logic in repository
- Transactions managed at service layer
- Queries optimized
- Indexes defined where needed
- Migration added (if schema changed)
- No string-interpolated SQL
- Tests added
- Connection pooling configured
- Exceptions translated properly
