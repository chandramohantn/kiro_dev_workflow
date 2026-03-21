---
name: etl-standards
description: Enforce ETL and data pipeline standards. Use when building, reviewing, or evaluating data pipelines.
---

# ETL & Data Pipeline Standards

Enforce mandatory standards for production-ready data pipelines.

## Core Principles
- Pipelines must be idempotent and restart-safe
- Every stage independently testable
- No silent data corruption
- Observability mandatory
- Configurations externalized

## Architecture
Clear stage separation: `Extract → Validate → Transform → Validate → Load`
- No monolithic scripts
- Transform must not perform DB writes
- Extract must only fetch (no transform/load)

## Idempotency (Mandatory)
Strategies: upserts, checkpoint tracking, deduplication keys, watermarking. Pipelines must not produce duplicates on rerun.

## Standards by Stage

### Extract
- Source isolation (fetch only)
- Timeouts on all external calls
- Retry with exponential backoff

### Transform
- Pure functions preferred (deterministic, no side effects, no global state)
- Schema validation before and after transformation
- No invalid data passes silently

### Load
- Batch writes (no row-by-row)
- Transactions with rollback on failure
- Handle unique constraints and duplicates safely

## Checkpointing & Recovery
- Restart from last successful checkpoint
- Strategies: offset tracking, timestamp watermark, batch ID
- Checkpoint storage must be durable

## Observability
Every pipeline logs: job start/end, records processed/failed, execution duration, job ID, batch ID.
Metrics: records processed, records failed, processing rate, retry count, lag (streaming).

## Error Handling
- No silent failures (`except: pass` forbidden)
- Classify: transient (retryable), permanent (data issue), system failure
- Retries must have limits
- Invalid records: logged, isolated, not silently discarded

## Validation
Before transform and before load: required fields, type consistency, value ranges, referential integrity.

## Configuration
- No hardcoded values/paths
- Environment-aware (dev/staging/production)
- Typed configuration classes

## Other Rules
- Large datasets: chunk processing, generators, no full-dataset memory loads
- Data lineage: document source, transformations, versioning
- Reproducibility: versioned code, config, and transform logic
- Scheduling: prevent overlapping runs, support retry and alerting

## Anti-Patterns (Forbidden)
- Monolithic ETL scripts
- Silent data drops
- Non-idempotent pipelines
- Hardcoded file paths
- Row-by-row DB writes for large datasets
- No checkpointing
- Logging entire datasets
