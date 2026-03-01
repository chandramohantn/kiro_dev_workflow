# API Development Standards

Scope: API design, validation, error handling, versioning, performance, reliability

1. Purpose
This document defines mandatory standards for building and maintaining APIs to ensure:
- Consistency
- Reliability
- Security
- Observability
- Scalability
- Maintainability
All APIs must follow these standards.

2. API Design Principles
- APIs must be predictable and consistent.
- APIs must be explicit and self-documenting.
- Business logic must not exist in route handlers.
- APIs must fail loudly and clearly.
- Backward compatibility must be preserved once released.

3. Layering Requirements
API Layer must:
- Handle request parsing
- Validate input
- Authenticate/authorize
- Call service layer
- Return response

API Layer must NOT:
- Access database directly
- Contain business rules
- Manage transactions
- Call external services directly

4. Route Structure
- 4.1 Directory Structure
    ```
    api/
    ├── routes/
    │    ├── users.py
    │    ├── orders.py
    │    └── health.py
    ├── dependencies.py
    └── middleware.py
    ```
    Routes must be grouped by domain.

- 4.2 Route Handler Rules
    Route handlers must:
    - Be thin
    - Contain minimal logic
    - Call a single service function
    Example:
    ```
    @router.post("/users", response_model=UserResponse)
    async def create_user(
        request: CreateUserRequest,
        service: UserService = Depends(get_user_service),
    ) -> UserResponse:
        return await service.create_user(request)
    ```

5. Request & Response Validation
- 5.1 Input Validation (Mandatory)
    All input must be validated using Pydantic models.
    Forbidden:
    ```
    async def create_user(name: str, age: int):
    ```

    Required:
    ```
    class CreateUserRequest(BaseModel):
        name: str
        age: int
    ```

- 5.2 Response Models Required
    Every endpoint must define response_model.
    This ensures:
    - Schema consistency
    - Auto-generated documentation
    - Safe serialization

- 5.3 No Raw Dict Responses
    Forbidden:
    ```
    return {"status": "ok"}
    ```
    Use typed response model instead.

6. HTTP Status Codes
Use correct status codes:
Scenario -> Code
- Successful GET: 200
- Resource Created: 201
- Accepted: 202
- Bad Request: 400
- Unauthorized: 401
- Forbidden: 403
- Not Found: 404
- Conflict: 409
- Validation Error: 422
- Internal Error: 500
Do not always return 200.

7. Error Handling Standards
- 7.1 No Generic Exception Leakage
    Internal exceptions must not leak stack traces.
    Use structured error responses.

- 7.2 Standard Error Format
    All errors must follow consistent structure:
    ```
    {
    "error": {
        "code": "USER_NOT_FOUND",
        "message": "User does not exist",
        "details": {}
        }
    }
    ```

- 7.3 Domain Exceptions
    Service layer must raise domain-specific exceptions.
    API layer must translate them into HTTP responses.

8. Dependency Injection
Dependencies must be injected using framework mechanisms.
Inject:
- Services
- DB sessions
- Config
- External clients
Never instantiate services inside route handlers.

9. Authentication & Authorization
- 9.1 Authentication
    - Must be handled via middleware or dependency.
    - No manual token parsing inside routes.

- 9.2 Authorization
    Authorization checks must:
    - Be explicit
    - Happen before service call
    - Use role/permission abstraction

10. Pagination Standards
All list endpoints must support pagination.
Required query parameters:
- limit
- offset
Or cursor-based pagination.
Never return unbounded result sets.

11. Versioning Strategy
All public APIs must be versioned.
Example:
```
/api/v1/users
```
Rules:
- Breaking changes require new version
- Old versions must be supported for defined deprecation window

12. Async vs Sync Rules
- 12.1 Async Required When:
    - Calling async DB
    - Calling async HTTP clients
    - Performing I/O operations

- 12.2 Async Must Not:
    - Call blocking code
    - Perform heavy CPU-bound tasks
    CPU-heavy tasks must use:
    - Background workers
    - Task queues

13. Performance Standards
- 13.1 Avoid N+1 Queries
    Service layer must ensure efficient DB access.

- 13.2 Response Size Control
    - Avoid returning large payloads
    - Use pagination
    - Support filtering

- 13.3 Timeout Policies
    External calls must have explicit timeouts.

14. Logging & Observability
Each request must log:
- Request ID / correlation ID
- Route
- Status code
- Execution time
Sensitive data must not be logged.

15. Rate Limiting
Public APIs must support rate limiting.
Required for:
- Authentication endpoints
- Write-heavy endpoints
- Public endpoints

16. Health & Readiness Endpoints
Every service must expose:
- /health → basic liveness
- /ready → readiness (DB, cache connectivity)
Health endpoints must not require authentication.

17. Idempotency Rules
POST endpoints creating resources must:
- Support idempotency keys where applicable
- Prevent duplicate resource creation
Especially important for payments and critical writes.

18. File Upload & Download Standards
- Enforce size limits
- Validate content type
- Scan for malicious content (if applicable)

19. Background Task Handling
Heavy operations must not block request thread.
Use:
- Background tasks
- Task queues (e.g., Celery)

20. API Documentation
OpenAPI documentation must be:
- Enabled
- Accurate
- Updated with every change
All models must have descriptions.

21. Testing Requirements
Every API must have:
- Route-level tests
- Authentication tests
- Error handling tests
- Integration tests with DB (where applicable)
Mock external services in unit tests.

22. Security Requirements
- Input validation mandatory
- Prevent SQL injection via ORM usage
- Validate file uploads
- Enforce HTTPS
- Set proper CORS policies

23. Anti-Patterns (Strictly Forbidden)
- Business logic in route handlers
- DB queries in controllers
- Unbounded list endpoints
- Always returning 200
- Swallowing exceptions
- Logging secrets
- Returning internal stack traces

24. Definition of Production-Ready API
An API is production-ready when:
- Fully validated
- Fully typed
- Properly layered
- Versioned
- Authenticated
- Rate limited
- Logged
- Tested
- Observable
- Secure

