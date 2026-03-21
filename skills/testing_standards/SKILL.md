---
name: testing-standards
description: Enforce testing and code quality standards. Use when writing tests, reviewing test coverage, or evaluating test quality.
---

# Testing & Quality Standards

Enforce mandatory standards for testing and code quality.

## Core Principles
- Every feature must be testable
- Tests must be deterministic
- Tests must be fast and isolated
- Untested code is incomplete

## Tooling (CI Mandatory)
pytest, pytest-cov, mypy, flake8, black, isort. All must pass before merge.

## Test Types

### Unit Tests
Pure business logic, transforms, validation, utilities. No real DB/APIs. Use mocks. Fast (<100ms each).

### Integration Tests
Repository layer, DB interaction, graph operations, ETL load. Dedicated test DB. Clean state between tests.

### API Tests
Endpoint correctness, validation, auth, error responses. Test success, failures, unauthorized, edge cases.

### ETL Tests
Transform logic, schema validation, failure simulation, idempotency verification.

### ML Tests
Data validation, feature transforms, inference, metric computation, serialization/deserialization.

## Coverage Thresholds
- Service layer: ≥ 85%
- Core utilities: ≥ 90%
- Repositories: ≥ 80%
- ML transform logic: ≥ 85%

## Structure
```
tests/
├── unit/
├── integration/
├── api/
├── etl/
├── ml/
└── conftest.py
```
Files: `test_<module>.py`. Functions: `test_<behavior>()`.

## Rules
- Tests must not depend on: system time (unless mocked), randomness (unless seeded), network, execution order
- Use pytest fixtures for DB setup, mock services, test data
- No shared mutable state between tests
- Mock only external services/APIs/expensive ops — not core business logic
- Test DB separate from production, transactional rollback per test
- ML: tolerance-based float comparisons (`abs(predicted - expected) < 1e-6`)
- Test edge cases: boundary values, invalid/empty/large inputs, failure scenarios

## Quality Gates (Merge Blockers)
All tests pass, coverage threshold met, no lint/type errors, no skipped tests without justification.

## Anti-Patterns (Forbidden)
- Tests without assertions
- Tests depending on execution order
- Tests using production DB
- Sleep-based synchronization
- Disabling failing tests silently
- Testing private implementation instead of behavior
- Flaky tests (fix immediately)
