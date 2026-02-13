# Performance Guidelines

## Purpose
These rules ensure the system remains:
- Predictable
- Scalable
- Cost-effective
- Reliable under load

They apply to APIs, pipelines, ML jobs, and background workers.

---

## 1. Core Principles

- Measure before optimizing
- Optimize the hot path, not the hypothetical one
- Prefer simple, predictable performance over clever tricks
- Avoid unbounded work

---

## 2. API Performance (FastAPI / Services)

- Be mindful of:
  - Blocking I/O
  - N+1 queries
  - Unbounded loops over user input
- Prefer:
  - Async I/O where appropriate
  - Batching over per-item calls
  - Pagination for large result sets
- Always consider:
  - Timeouts
  - Retries
  - Circuit breakers (if applicable)

---

## 3. Data Pipeline Performance

- Be mindful of:
  - Data volume growth
  - Memory usage
  - Shuffle / join costs
- Prefer:
  - Streaming or chunked processing
  - Incremental updates over full recomputes
  - Idempotent and restartable steps
- Avoid:
  - Loading entire datasets into memory
  - Unbounded intermediate state

---

## 4. Database & I/O

- Always:
  - Use indexes where appropriate
  - Avoid N+1 patterns
  - Limit result sizes
- Prefer:
  - Bulk operations
  - Prepared / parameterized queries
- Be explicit about:
  - Transactions
  - Isolation levels if relevant

---

## 5. Caching

- Cache:
  - Expensive computations
  - Frequently accessed, slow-changing data
- Always consider:
  - Cache invalidation strategy
  - TTLs
  - Consistency requirements
- Do NOT:
  - Cache without understanding correctness implications

---

## 6. Resource Usage

- Watch:
  - CPU
  - Memory
  - Disk
  - Network
- Avoid:
  - Unbounded queues
  - Unbounded concurrency
  - Unbounded retries
- Always set:
  - Limits
  - Timeouts
  - Backpressure where applicable

---

## 7. Observability & Measurement

- Add metrics for:
  - Latency
  - Throughput
  - Error rates
  - Queue sizes / backlog
- Log:
  - Slow operations
  - Timeouts
- You can’t optimize what you can’t see.

---

## 8. Performance Review Checklist

Before shipping:

- [ ] No obvious N+1 or unbounded loops
- [ ] Large operations are paginated / chunked / streamed
- [ ] Timeouts and limits are set
- [ ] Critical paths are measured or at least reasoned about
- [ ] No accidental full-table scans or full-dataset loads

---

## 9. When to Trade Performance for Simplicity

- It’s OK if:
  - The scale is known to be small
  - The path is not hot
  - You document the assumption
- If performance might matter later:
  - Leave a note
  - Or add a TODO with context
