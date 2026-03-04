# Testing Patterns

## Purpose
This document defines standardized testing patterns used across the repository.
The Testing Agent must follow these patterns when generating tests.
These patterns ensure:
- consistency
- readability
- maintainability
- deterministic behavior

All tests must follow the conventions described in this document.

---

## Test Structure
All tests must follow the **Arrange → Act → Assert** pattern.
Example:

```python
def test_calculate_discount_valid_user():

    # Arrange
    service = DiscountService()
    user = User(type="premium")

    # Act
    result = service.calculate_discount(user)

    # Assert
    assert result == 0.20
```

Rules:
- Arrange block prepares inputs and dependencies
- Act block executes the behavior under test
- Assert block validates outcomes
- Avoid mixing these sections.

## Test Naming Conventions
Test names must clearly describe the behavior being tested.
Format:
test_<functionality><condition><expected_result>

Example:
- test_create_user_valid_input_success
- test_create_user_duplicate_email_error
- test_login_invalid_password_denied

Avoid vague names like:
- test_user
- test_case_1
- test_example

## File Naming Conventions
Test files must mirror the source file structure.
Example:

Source file:
- services/user_service.py

Test file:
- tests/services/test_user_service.py

Structure:
- tests/
- services/
- test_user_service.py
- repositories/
- test_user_repository.py
- api/
- test_user_api.py

## Unit Test Pattern
Unit tests validate isolated logic.
Dependencies must be mocked.
Example:
```
import pytest
from services.user_service import UserService

def test_create_user_success(mocker):

    # Arrange
    mock_repo = mocker.Mock()
    service = UserService(repository=mock_repo)

    user_data = {
        "name": "Alice",
        "email": "alice@example.com"
    }

    mock_repo.save.return_value = {"id": 1}

    # Act
    result = service.create_user(user_data)

    # Assert
    assert result["id"] == 1
    mock_repo.save.assert_called_once()
```

Rules:
- isolate business logic
- mock external dependencies
- test both success and failure cases

## Edge Case Testing Pattern
Tests must include edge conditions.
Examples:
- empty input
- null values
- boundary values
- invalid formats

Example:
```
def test_divide_by_zero_error():

    # Arrange
    calculator = Calculator()

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
```

## Exception Testing Pattern
When testing error scenarios, use explicit exception assertions.
Example:
```
def test_invalid_email_raises_error():

    # Arrange
    service = UserService()

    # Act & Assert
    with pytest.raises(InvalidEmailError):
        service.create_user({"email": "invalid"})
```

## Fixture Pattern
Reusable test data must be implemented using pytest fixtures.
Example:
```
import pytest

@pytest.fixture
def sample_user():
    return {
        "name": "Alice",
        "email": "alice@example.com"
    }
```

Usage: 
```
def test_user_creation(sample_user):
    service = UserService()
    result = service.create_user(sample_user)

    assert result is not None
```

## Factory Pattern for Complex Objects
Factories should be used for complex test objects.
Example:
```
class UserFactory:

    @staticmethod
    def create_user(**kwargs):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "role": "user"
        }
        data.update(kwargs)
        return data
```

Usage: 
```
user = UserFactory.create_user(role="admin")
```

## Mocking Pattern
External dependencies must be mocked using pytest-mock.
Examples of dependencies that should be mocked:
- database repositories
- external APIs
- cloud storage
- message queues

Example:
```
def test_external_api_call(mocker):

    mock_api = mocker.patch("services.payment_service.external_api")

    mock_api.process_payment.return_value = {"status": "success"}

    result = process_payment()

    assert result["status"] == "success"
```

## API Testing Pattern
API tests validate request/response behavior.
Example:
```
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_api():

    response = client.post("/users", json={
        "name": "Alice",
        "email": "alice@example.com"
    })

    assert response.status_code == 201
    assert response.json()["email"] == "alice@example.com"
```

Validation rules:
API tests must check:
- status code
- response schema
- error responses

## Integration Test Pattern
Integration tests validate component interactions.
These tests may use real infrastructure such as:
- test databases
- docker containers

Example:
```
def test_user_repository_insert(test_db):

    repo = UserRepository(db=test_db)

    user = repo.insert({
        "name": "Alice",
        "email": "alice@example.com"
    })

    assert user.id is not None
```

Integration tests must:
- avoid mocking core components
- validate real interactions

## End-to-End Testing Pattern
E2E tests validate complete system workflows.
Example scenario:
- User uploads an image → system returns prediction.

Example:
```
def test_image_prediction_flow(client):

    response = client.post("/predict", files={
        "file": ("image.jpg", open("tests/data/image.jpg", "rb"))
    })

    assert response.status_code == 200
    assert "prediction" in response.json()
```

## Regression Test Pattern
Regression tests protect against previously fixed bugs.
Example:

Bug:
- PNG upload previously failed.

Regression test:
```
def test_png_upload_regression(client):

    response = client.post("/upload", files={
        "file": ("test.png", open("tests/data/test.png", "rb"))
    })

    assert response.status_code == 200
```

## ML Model Testing Pattern
ML tests should validate:
- input schema
- output format
- prediction stability

Example:
```
def test_model_prediction_format(model):

    result = model.predict("tests/data/cat.jpg")

    assert "label" in result
    assert "confidence" in result
```

Optional validation:
- confidence between 0 and 1

## Data Pipeline Testing Pattern
Data pipeline tests must validate:
- schema
- transformations
- output integrity

Example:
```
def test_data_transformation():

    input_data = {"age": 30}

    result = transform_data(input_data)

    assert "age_bucket" in result
```

## Flaky Test Prevention
Tests must avoid:
- sleep-based timing
- real network calls
- random behavior without seeding

If randomness is required:
- set deterministic seed

## Test Isolation Rules
Each test must be independent.
Tests must not:
- depend on execution order
- depend on shared mutable state
- modify global state

## Coverage Guidelines
Coverage should guide improvements but not dictate test design.
Focus areas for additional testing:
- new logic branches
- error handling
- critical business rules

## Testing Agent Compliance
When generating tests, the Testing Agent must:
- Follow these patterns.
- Generate readable and maintainable tests.
- Prefer fixtures and factories over inline data.
- Avoid brittle test logic.
