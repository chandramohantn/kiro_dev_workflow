# Testing and Quality Standards

Scope: Unit testing, integration testing, ML validation, coverage, CI enforcement, code quality

1. Purpose
This document defines mandatory standards for testing and code quality to ensure:
- Reliability
- Maintainability
- Regression prevention
- Deterministic behavior
- Production safety
Untested code is considered incomplete.

2. Core Testing Principles
- Every feature must be testable.
- Tests must be deterministic.
- Tests must not depend on external systems unless explicitly integration tests.
- Tests must be fast and isolated.
- Critical business logic must have high coverage.

3. Required Tooling
All repositories must use:
- pytest
- pytest-cov
- mypy
- flake8
- black
- isort
CI must enforce all checks.

4. Test Types (Mandatory Classification)
Every project must include appropriate test types.

- 4.1 Unit Tests
    Scope:
    - Pure business logic
    - Transformation functions
    - Validation logic
    - Utility functions

    Rules:
    - No real DB
    - No real external APIs
    - Use mocks where required
    - Must run fast (<100ms per test ideally)

- 4.2 Integration Tests
    Scope:
    - Repository layer
    - DB interaction
    - Graph DB operations
    - ETL load phase

    Rules:
    - Use dedicated test database
    - No production DB usage
    - Clean state between tests

- 4.3 API Tests
    Scope:
    - Endpoint correctness
    - Validation behavior
    - Auth behavior
    - Error responses
    Must test:
    - Success cases
    - Validation failures
    - Unauthorized access
    - Edge cases

- 4.4 ETL Tests
    Must include:
    - Transform logic unit tests
    - Schema validation tests
    - Failure case simulation
    - Idempotency verification

- 4.5 ML Tests
    Must include:
    - Data validation tests
    - Feature transformation tests
    - Model inference tests
    - Metric computation tests
    - Serialization/deserialization tests

5. Coverage Requirements
Minimum thresholds:
Component -> Coverage
- Service Layer	≥ 85%
- Core Utilities ≥ 90%
- Repositories ≥ 80%
- ML Transform Logic ≥ 85%
Coverage must be enforced in CI.
Coverage is not a substitute for good test quality.

6. Test Structure
- 6.1 Directory Structure
    ```
    tests/
    ├── unit/
    ├── integration/
    ├── api/
    ├── etl/
    ├── ml/
    └── conftest.py
    ```

- 6.2 Naming Convention
    Test files must follow:
    ```
    test_<module_name>.py
    ```
    Test functions must follow:
    ```
    test_<behavior_description>()
    ```
    Example:
    ```
    def test_create_user_returns_201():
    ```

7. Deterministic Testing Rules
Tests must not:
- Depend on system time (unless mocked)
- Depend on randomness (unless seeded)
- Depend on network
- Depend on order of execution
If randomness is used:
- Seed must be fixed
- Seed must be documented

8. Fixtures & Test Isolation
- 8.1 Use Fixtures
    Use pytest fixtures for:
    - DB setup
    - Mock services
    - Test data factories

- 8.2 No Shared Mutable State
    Tests must not:
    - Share mutable global variables
    - Depend on previous test execution
    - Each test must run independently.

9. Mocking Standards
Use mocks only when necessary.
Mock:
- External services
- Third-party APIs
- Expensive operations
Do NOT mock:
- Core business logic
- Repository layer in integration tests
- Over-mocking reduces confidence.

10. Database Testing Standards
- 10.1 Test Database Required
    - Use separate DB instance
    - Use transactional rollback per test where possible

- 10.2 Clean State Guarantee
    Tests must:
    - Clean up after execution
    - Not pollute DB state

11. ML Testing Standards
- 11.1 Inference Determinism
    Inference results must be:
    - Reproducible
    - Within tolerance for floating-point comparisons
    Use tolerance-based comparisons:
    ```
    assert abs(predicted - expected) < 1e-6
    ```

- 11.2 Data Drift Validation
    If drift detection exists:
    - Tests must validate drift logic
    - Edge-case drift scenarios must be tested

- 11.3 Model Artifact Validation
    Tests must verify:
    - Model loads correctly
    - Model version matches expected
    - Corrupted model files raise errors

12. ETL Testing Standards
Must test:
- Idempotency
- Checkpoint restart
- Duplicate handling
- Invalid data behavior
Large datasets should use synthetic test data.

13. Performance Testing (When Required)
Critical systems must include:
- API latency benchmarks
- ETL throughput benchmarks
- ML inference latency checks
Performance regressions must be detectable.

14. Static Analysis Requirements
CI must enforce:
- Type checking (mypy)
- Linting (flake8)
- Formatting (black)
- Import ordering (isort)
Type errors are merge blockers.

15. Mutation & Edge Case Testing
Critical services must test:
- Boundary values
- Invalid inputs
- Empty inputs
- Large inputs
- Failure scenarios
Tests must not only test happy path.

16. Test Data Management
Test data must:
- Be minimal
- Be representative
- Not include production secrets
- Be synthetic when possible
Avoid storing large static datasets in repository.

17. CI Requirements
CI pipeline must:
- Install dependencies
- Run linters
- Run type checks
- Run tests
- Enforce coverage threshold
No merge allowed if CI fails.

18. Flaky Test Policy
Flaky tests are unacceptable.
If test is flaky:
- Fix immediately
- Do not disable silently
- Investigate root cause

19. Code Quality Gates
A PR cannot be merged unless:
- All tests pass
- Coverage threshold met
- No lint errors
- No type errors
- No skipped tests without justification

20. Anti-Patterns (Strictly Forbidden)
- Tests without assertions
- Tests that depend on execution order
- Tests that use production DB
- Random sleep-based synchronization
- Disabling failing tests without issue tracking
- Testing private implementation details instead of behavior

21. Definition of High-Quality Test Suite
A high-quality test suite:
- Detects regressions
- Covers critical logic
- Is deterministic
- Is fast
- Is isolated
- Is maintainable
- Validates failure modes



