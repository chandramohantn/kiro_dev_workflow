# Logging, Monitoring, and Observability Standards

Scope: Logging, metrics, tracing, health checks, alerting, and production visibility

1. Purpose
This document defines mandatory standards for logging and observability to ensure:
- Production visibility
- Faster debugging
- Performance monitoring
- Incident response capability
- System reliability
If a system is not observable, it is not production-ready.

2. Core Principles
- Logs must be structured.
- Metrics must be measurable and actionable.
- Systems must expose health signals.
- Observability must not leak sensitive data.
- Logging must not significantly degrade performance.
- Failures must be diagnosable without redeploying.

3. Logging Standards
- 3.1 Logging Library
    - Use Python logging module or structured logging wrapper.
    - print() is strictly forbidden in production code.

- 3.2 Structured Logging (Mandatory)
    Logs must be structured (JSON format preferred).
    Example structure:
    ```
    {
    "timestamp": "2025-01-01T12:00:00Z",
    "level": "INFO",
    "service": "user-api",
    "correlation_id": "abc123",
    "message": "User created",
    "metadata": {
        "user_id": "u-123"
    }
    }
    ```
    Unstructured string-only logs are discouraged.

- 3.3 Log Levels (Strict Usage)
    Level -> Usage
    - DEBUG: Development diagnostics
    - INFO: Normal operations
    - WARNING: Recoverable issue
    - ERROR: Operation failed
    - CRITICAL: System-level failure
    Misuse of log levels is a review failure.

- 3.4 Required Logging Events
    Systems must log:
    - Application startup
    - Application shutdown
    - Configuration summary (without secrets)
    - Errors with context
    - External service calls (without sensitive payloads)
    - Long-running operations
    - Retry attempts
    - Background task failures

4. Correlation IDs (Mandatory for APIs)
Each incoming request must:
- Generate or propagate correlation ID
- Include correlation ID in all logs
Correlation ID must propagate through:
- Service layer
- Repository layer
- External service calls

5. Sensitive Data Protection
Logs must NOT contain:
- Passwords
- Tokens
- API keys
- Full personal identifiable information (PII)
- Raw request bodies (unless sanitized)
Mask sensitive fields before logging.

6. Metrics Standards
- 6.1 Metrics Are Mandatory
    All production services must expose metrics.
    At minimum:
    - Request count
    - Error count
    - Latency
    - Resource usage
    - Retry count

6.2 API Metrics
    Track:
    - Requests per endpoint
    - Response status distribution
    - Latency percentiles (P50, P95, P99)
    - Rate limit hits

6.3 ETL Metrics
    Track:
    - Records processed
    - Records failed
    - Processing rate
    - Batch duration
    - Retry attempts
    - Lag (for streaming)

6.4 ML Metrics
    Track:
    - Inference latency
    - Throughput
    - Model version
    - Prediction error rate (if applicable)
    - Resource usage (CPU/GPU/memory)

7. Tracing Standards
For distributed systems:
- Distributed tracing must be enabled.
- External calls must propagate trace headers.
- Trace IDs must correlate with log correlation IDs.
Trace spans must include:
- DB calls
- External HTTP calls
- Message queue processing
- Long-running computations

8. Health Checks
All services must expose:
- /health → liveness check
- /ready → readiness check

- 8.1 Liveness
    Indicates service process is running.
    Must not check external dependencies.

8.2 Readiness
    Checks:
    - DB connectivity
    - Cache connectivity
    - Message broker connectivity
    - External dependencies (if required)
    Must return non-200 if dependency unavailable.

9. Alerting Standards
Alerts must exist for:
- High error rate
- High latency
- Service crash
- Repeated retry failures
- DB connectivity failure
- ETL job failure
- ML inference errors
Alerts must be actionable.
No noisy alerts.

10. Log Retention Policy
Log retention must:
- Comply with compliance requirements
- Avoid indefinite storage
- Avoid excessive storage costs
Retention duration must be documented.

11. Performance Logging
For critical operations:
- Log execution time
- Log batch sizes
- Log throughput
Do not log per-record events for large batches.

12. Exception Logging Rules
When logging exceptions:
- Include context
- Include correlation ID
- Avoid logging full sensitive payload
- Avoid duplicate logging of same exception
Exception must not be silently swallowed.

13. Observability in ML Systems
ML services must log:
- Model version
- Feature version
- Input schema version
- Inference latency
- Prediction metadata (if safe)
Must NOT log full raw feature vectors unless sanitized.

14. Observability in ETL Systems
ETL jobs must log:
- Job ID
- Batch ID
- Record count
- Failure count
- Checkpoint location
- Execution time
On failure:
- Log failing stage
- Log sample of failing records (sanitized)

15. Observability in Graph Systems
Must log:
- Query execution time
- Node/relationship counts affected
- Slow queries
Slow query threshold must be configurable.

16. Resource Monitoring
Systems must monitor:
- CPU usage
- Memory usage
- Disk usage
- DB connection pool usage
- Thread/async worker usage
Resource exhaustion must trigger alerts.

17. Rate Limiting Observability
APIs must log:
- Rate limit hits
- Client identifiers (sanitized)
- Endpoint affected
Excessive rate-limit events must trigger monitoring review.

18. Startup & Shutdown Logging
On startup:
- Log version
- Log environment
- Log config summary (excluding secrets)
On shutdown:
- Log graceful termination
- Log in-flight request completion

19. Anti-Patterns (Strictly Forbidden)
- Using print() in production
- Logging secrets
- Logging entire large datasets
- Logging unbounded request bodies
- Logging without correlation IDs
- Swallowing exceptions without logging
- Silent retries without logging

20. Definition of Observable System
A system is observable when:
- Failures are diagnosable from logs
- Performance bottlenecks are measurable
- Dependencies are health-checked
- Errors are traceable across services
- Metrics are exportable
- Alerts are actionable
- Sensitive data is protected

