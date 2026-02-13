# <TICKET-ID>: <Title>

## Problem Statement
Describe the API problem or feature:
- What endpoint or behavior is missing or broken?
- Who consumes this API?
- What is the impact?

## Background / Context
- Current API behavior
- Related endpoints or services
- Relevant business or system context

## Goals / Acceptance Criteria
Each item must be testable via API calls:
- AC1: Endpoint <METHOD> <PATH> returns <EXPECTED_BEHAVIOR>
- AC2: Validation: <RULE> is enforced with <ERROR_RESPONSE>
- AC3: Authorization / auth behavior: <EXPECTED>
- AC4: Performance / latency constraint: <IF ANY>

## API Contract
- Endpoint(s):
  - METHOD PATH
- Request schema:
  - Fields, types, required/optional
- Response schema:
  - Success response
  - Error responses
- Status codes:
  - 2xx:
  - 4xx:
  - 5xx:

## Non-Goals / Out of Scope
- ...
- ...

## Constraints
- Backward compatibility requirements
- AuthN/AuthZ requirements
- Performance / latency budgets
- Logging / observability requirements
- Dependency constraints

## Assumptions
- ...

## Open Questions
- ...

## Success Criteria
- Which clients should work after this?
- What observable behavior proves success?
