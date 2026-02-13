# Project Profile Contents
## Gold-standard example of how a project should describe itself to the Kiro system.

### It answers:
 - What kind of project is this?
 - What are the architectural rules?
 - What are the constraints?
 - What domain knowledge matters?
 - What decisions have already been made?

### It’s not meant to be copied blindly. It’s meant to be:
 - A reference
 - A template you evolve
 - A place to design and refine your standards

### Think of it like:
 - “This is how a well-described project should look.”


## What each file is for
### project.md
 - High-level project identity:
     - Domain (API, pipeline, ML, infra, etc.)
     - Tech stack (FastAPI, MSSQL, Docker, etc.)
     - Non-negotiables
     - Team conventions

### docs/steering/
 - Rules of the world for this project:
     - architecture.md → layering, boundaries, patterns
     - coding-standards.md → style, typing, error handling, logging
     - security.md → auth, secrets, data access, trust boundaries
     - performance.md → SLAs, budgets, scaling rules

### docs/adr/
 - Architecture Decision Records
 - Why you chose:
     - MSSQL over Postgres
     - Sync vs async
     - Batch vs streaming
     - Certain libraries or patterns

### knowledge/
 - Tribal knowledge / long-term memory
     - domain.md → business/domain concepts (KG, ML, data meaning, etc.)
     - constraints.md → hard constraints (infra, org, legal, cost, etc.)
     - gotchas.md → “we learned this the hard way”
     - glossary.md → shared vocabulary for humans + agents

### How it’s used
 - You evolve this over time as your ideal project description
 - Agents can be tested mentally against this structure
 - You copy pieces of this when bootstrapping real projects
 - It’s your reference architecture + knowledge model
