---
name: observability-standards
description: Enforce logging, monitoring, and observability standards. Use when implementing or reviewing logging, metrics, health checks, or alerting.
---

# Observability Standards

Enforce mandatory standards for logging, monitoring, and observability.

## Core Principles
- Logs must be structured (JSON preferred)
- Metrics must be measurable and actionable
- Systems must expose health signals
- No sensitive data in logs
- Failures must be diagnosable without redeploying

## Logging

### Rules
- `print()` forbidden in production — use `logging` module
- Structured JSON format with: timestamp, level, service, correlation_id, message, metadata
- Correct log levels: DEBUG (dev), INFO (normal ops), WARNING (recoverable), ERROR (op failed), CRITICAL (system failure)

### Required Events
Startup, shutdown, config summary (no secrets), errors with context, external service calls, retries, background task failures.

### Correlation IDs (Mandatory for APIs)
Generate/propagate per request. Include in all logs. Propagate through service → repository → external calls.

### Sensitive Data
Never log: passwords, tokens, API keys, PII, raw request bodies. Mask before logging.

## Metrics (Mandatory)

### Minimum
Request count, error count, latency, resource usage, retry count.

### By Domain
- API: requests per endpoint, status distribution, latency P50/P95/P99, rate limit hits
- ETL: records processed/failed, processing rate, batch duration, lag
- ML: inference latency, throughput, model version, prediction error rate

## Health Checks
- `/health` — liveness (process running, no external deps)
- `/ready` — readiness (DB, cache, broker connectivity)
- No auth required

## Alerting
Required for: high error rate, high latency, service crash, retry failures, DB connectivity failure, ETL job failure, ML inference errors. Alerts must be actionable, not noisy.

## Other Rules
- Distributed tracing for multi-service systems (trace IDs correlate with log correlation IDs)
- Resource monitoring: CPU, memory, disk, DB pool, threads
- Exception logging: include context + correlation ID, no duplicate logging, no silent swallowing
- ETL: log job ID, batch ID, record count, failure count, checkpoint, execution time
- Graph: log query time, nodes affected, slow queries (configurable threshold)

## Anti-Patterns (Forbidden)
- `print()` in production
- Logging secrets
- Logging entire large datasets
- Logging without correlation IDs
- Swallowing exceptions without logging
- Silent retries
