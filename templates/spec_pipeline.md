# <TICKET-ID>: <Title>

## Problem Statement
Describe the pipeline issue or feature:
- Which pipeline or job?
- What is wrong or missing?
- What is the impact on data or downstream systems?

## Background / Context
- Current pipeline behavior
- Data sources and sinks involved
- Downstream consumers (dashboards, ML, APIs, etc.)

## Goals / Acceptance Criteria
Each item must be testable or verifiable:
- AC1: Pipeline produces <EXPECTED_OUTPUT> for <INPUT_CONDITION>
- AC2: Data quality rule: <RULE> is enforced
- AC3: Failure handling: <EXPECTED_BEHAVIOR>
- AC4: Performance / SLA: <EXPECTED_RUNTIME / FRESHNESS>

## Data Flow
- Source(s):
- Transformations:
- Sink(s):
- Storage / intermediate steps:

## Non-Goals / Out of Scope
- ...

## Constraints
- Data volume / scale
- Runtime / SLA
- Infrastructure constraints
- Schema compatibility
- Cost constraints

## Assumptions
- ...

## Open Questions
- ...

## Success Criteria
- What data properties prove success?
- What downstream systems should improve or stop breaking?
