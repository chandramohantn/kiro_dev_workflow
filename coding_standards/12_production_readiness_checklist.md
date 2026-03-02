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

## API Review Checklist (If Applicable)
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

## Database Review Checklist (If Applicable)
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

## ETL Review Checklist (If Applicable)
- Extract, transform, load clearly separated
- Idempotency ensured
- Checkpointing implemented
- Validation implemented
- No hardcoded paths
- Bulk operations used
- Transactions used
- Logging added
- Metrics exposed
- Tests written

## Knowledge Graph Review Checklist (If Applicable)
- Node schema documented
- Relationships follow naming conventions
- Constraints defined
- Queries parameterized
- No full graph scans
- MERGE used appropriately
- Tests added
- Query performance validated
- No business logic in repository
- Idempotency ensured

## Testing Review Checklist
- Unit tests added
- Integration tests added (if DB involved)
- Edge cases covered
- Negative scenarios tested
- No flaky behavior
- Coverage threshold met
- No over-mocking
- Deterministic behavior verified

## Observability Review Checklist (If Applicable)
- Structured logging implemented
- Correlation ID propagated
- Sensitive data masked
- Metrics exposed
- Health endpoints implemented
- Critical operations logged
- Error logging implemented
- Slow operations measurable
- No print statements

## ML System Readiness (If Applicable)
- Random seeds fixed and configurable
- Model version logged
- Feature version logged
- Model artifact versioned
- Model loads correctly in clean environment
- Inference latency measured
- Drift monitoring hooks present (if applicable)
- No training logic inside inference service
- Hardware utilization understood (CPU/GPU/memory)

## Security Validation
- No hardcoded secrets
- Environment variables used for credentials
- Inputs validated
- Parameterized queries used
- HTTPS enforced (if applicable)
- CORS configured properly
- Dependencies scanned for vulnerabilities
- Principle of least privilege applied to DB

## Performance Validation
- Load expectations defined
- API latency measured
- ETL throughput measured
- ML inference latency measured
- Resource usage measured (CPU, memory)
- No obvious bottlenecks
- Caching used where appropriate

## Deployment Validation
- Environment-specific config verified
- Build reproducible
- Container image verified (if containerized)
- Required environment variables documented
- Startup logs verified
- Graceful shutdown implemented
- Rollback strategy documented

## Failure & Recovery Readiness
- Service restart safe
- ETL restart safe
- Retry logic bounded
- Timeouts configured
- Circuit breaker strategy considered (if external calls heavy)
- No infinite retry loops
- Error alerts configured

## Scalability Validation
- System can handle expected peak load
- Horizontal scaling possible (stateless services preferred)
- DB connection limits respected
- No single-thread bottlenecks in async services
- Background tasks separated from request threads

## Monitoring & Alerting Validation
- Error rate alert configured
- Latency alert configured
- Resource usage alert configured
- ETL job failure alert configured
- ML inference error alert configured
- Pager/on-call procedure documented
