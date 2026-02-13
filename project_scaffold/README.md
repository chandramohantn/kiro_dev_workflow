# docs/steering/ — Project Rules (Non-Negotiables)
This folder contains the rules of the world for this project. Agents must follow these.
You should add documents like:
 - architecture.md — layering, boundaries, patterns, high-level design
 - coding-standards.md — style, typing, error handling, logging, structure
 - security.md — auth, secrets, data access, trust boundaries
 - performance.md — SLAs, latency budgets, scaling rules

How it’s used:
 - Planner uses this to shape the plan
 - Implementer must follow these rules
 - Reviewer checks compliance
 - Verifier flags violations

If it’s a rule, it belongs here.

# docs/adr/ — Architecture Decision Records
This folder stores important technical decisions and why they were made.
## Examples:
 - Why we chose MSSQL over Postgres
 - Why this pipeline is batch instead of streaming
 - Why this service is synchronous instead of async
 - Why we adopted a certain library or pattern

## Each ADR should answer:
 - What decision was made?
 - What alternatives were considered?
 - Why was this chosen?
 - What are the consequences?

## How it’s used:
 - Agents read this to avoid re-litigating old decisions
 - Humans use this to understand historical context
 - Notes Writer and Planner may link to ADRs

If a decision would confuse a new team member in 6 months, write an ADR.


# knowledge/ — Domain & Tribal Knowledge
This folder is your long-term memory for the project.
## Typical files you’ll add:
 - domain.md — business/domain concepts, data meaning, mental models
 - constraints.md — hard constraints (infra, org, legal, cost, tooling)
 - gotchas.md — “we learned this the hard way”
 - glossary.md — shared vocabulary for humans + agents

## How it’s used:
 - Jira Ingest uses this to write better specs
 - Planner uses this to avoid bad plans
 - Implementer and Tester use this to avoid repeating mistakes
 - Reviewer and Verifier use this to spot risky assumptions

If someone says “everyone knows that,” it probably belongs here.


# notes/ — Project History (One File Per Ticket)
This folder is a human-readable history of what changed in this project.
## Convention:
 - One file per Jira ticket
 - File name format:
     - YYYY-MM-DD-JIRA-XXXX-short-title.md

## Each note should summarize:
 - Why the change was made
 - What changed (at a high level)
 - Key design decisions
 - What is done vs still pending
 - Links to Jira, code, spec, ADRs

## How it’s used:
 - New team members can read this to understand project evolution
 - You can reconstruct why things look the way they do
 - This acts like a narrative changelog + design diary

If Git is “what changed”, notes are “why it changed”.

# How to Use This Scaffold in a Real Project
 - Add Kiro folders (from the main workflow repo):
     - agents/
     - workflows/
     - templates/
 - Fill in:
     - docs/steering/ with your project rules
     - knowledge/ with domain context and constraints
     - Start adding ADRs in docs/adr/ as decisions happen
 - As you work on tickets:
     - Specs go to: docs/specs/
     - Plans go to: docs/specs/*.plan.md
     - Notes go to: notes/YYYY-MM-DD-JIRA-XXXX-...md
 - Let the Kiro workflows:
     - Ingest Jira tickets
     - Create specs and plans
     - Implement and test
     - Verify against acceptance criteria
     - Update Jira
     - Write notes here


# Design Principles
 - Specs are the source of truth
 - Steering docs are non-negotiable
 - Knowledge prevents repeated mistakes
 - ADRs preserve decisions
 - Notes preserve history
 - Jira reflects reality, not optimism

 