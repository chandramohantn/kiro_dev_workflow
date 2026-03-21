---
name: coding-standards-reviewer
description: Infer code domains from diffs and review changes against project coding standards. Use when reviewing code for standards compliance, during MR reviews, code implementation, or spec design.
---

# Coding Standards Reviewer

Infer applicable domains from code changes and review against the corresponding coding standard documents.

## Inputs Required

1. **Code changes** — diffs, changed files, or code snippets to review
2. **Coding standards** — the `coding_standards/*.md` files loaded as resources

## Process

### Step 1: Infer Domains

Analyze the code to determine applicable domains using these signals:

| Signal | Domain |
|--------|--------|
| Python files, general logic, naming, typing | `general_python` |
| Module structure, layering, imports, dependency direction | `architecture` |
| FastAPI/Flask routes, request/response models, middleware | `api` |
| SQLAlchemy, Alembic, repository patterns, queries | `database` |
| Pipeline orchestration, data transforms, scheduling | `etl` |
| Neo4j, graph traversal, Cypher queries | `knowledge_graph` |
| Training loops, experiment tracking, hyperparameters | `ml_training` |
| Model serving, inference endpoints, model registry | `ml_deployment` |
| Test files, fixtures, assertions, coverage | `testing` |
| Logging, metrics, tracing, alerting config | `observability` |
| Caching, async, connection pooling, batch processing | `performance` |
| Deployment configs, health checks, env management | `production_readiness` |

Always include: `general_python`, `architecture`, `performance`, `production_readiness`.

### Step 2: Map Domains to Standards

- general_python → `python-standards` skill
- architecture → `02_project_structure_and_architecture.md` (reference file)
- api → `api-standards` skill
- database → `database-standards` skill
- etl → `etl-standards` skill
- knowledge_graph → `knowledge-graph-standards` skill
- ml_training → `07_machine_learning_training_standards.md` (reference file, if populated)
- ml_deployment → `08_ml_model_deployment_standards.md` (reference file, if populated)
- testing → `testing-standards` skill
- observability → `observability-standards` skill
- performance → `11_performance_and_scalability_standards.md` (reference file, if populated)
- production_readiness → `12_production_readiness_checklist.md` (reference file)

For domains mapped to skills, follow the skill instructions. For domains mapped to reference files, read the file content. Do not assume contents of either.

### Step 3: Review Against Standards

For each identified domain, compare the code against the corresponding standard. Classify findings:

- **CRITICAL** — Security, data loss, production failure risk
- **MAJOR** — Architectural or scalability risk
- **MINOR** — Maintainability concern
- **SUGGESTION** — Improvement opportunity

For each finding, state: what is wrong, why it matters, what risk it introduces, and a recommendation. Provide minimal refactoring snippets only when they clarify the fix.

## Output

Return:
1. **Domains detected** — list of inferred domains
2. **Standards applied** — list of standard files consulted
3. **Findings** — classified list of issues with explanations
4. **Domain-wise observations** — per-domain summary grounded in the standard

## Guidelines

- Do not invent standards that do not exist in the documents.
- Do not flag trivial stylistic issues unless they violate a documented standard.
- Prioritize: correctness > production safety > architecture > maintainability.
