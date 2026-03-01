---
name: bootstrap-analyze
description: Performs full repository analysis and generates initial documentation content for all architecture assets using predefined templates. Produces preview only and does not write files.
---

# Bootstrap Analyze Skill

## Purpose

This skill performs a full repository analysis and generates complete AUTO block content for all documentation assets located in:

project_assets/docs/

This skill:

- Executes only if documentation has not yet been created.
- Reads repository codebase fully.
- Reads asset templates.
- Generates structured documentation content.
- Produces preview output.
- Does NOT write any files.
- Does NOT initialize session artifacts.

---

# One-Time Execution Guard

Before performing any analysis:

1. Open:
   - project_assets/docs/architecture.md

2. Inspect header fields:
```
Last Updated: {{timestamp}}
Overall Confidence: {{confidence_score}}
```
If BOTH placeholders are still present:
- Continue bootstrap.

If either field contains actual values:
- STOP execution immediately.
    - Output:
        - Documentation already initialized.
        - Use asset_updater_agent for incremental updates.

Do NOT analyze repository.
Do NOT generate content.

---

# Mirror-Only Constraint
You must strictly mirror repository reality.
You must NOT:
- Suggest improvements
- Recommend architectural changes
- Introduce speculative services
- Infer undocumented systems
- Fabricate dependencies
- Add advisory commentary

Only document what is observable in code.

If insufficient information exists:
- Explicitly state: "Insufficient data to determine."

Do not hallucinate structure.

---

# Repository Analysis Scope
You may analyze:
- Entire repository tree
- All Python files
- Dockerfiles
- docker-compose files
- YAML files
- Requirements / pyproject
- Graph-related files
- ETL-related directories
- Config files
- ansible files
- ci/cd files

You must build a structural understanding of:
- Services
- APIs
- Database models
- Relationships
- Graph usage
- Deployment topology
- ETL pipelines
- Messaging systems
- Data stores

---

# Template Usage Rules
Templates exist in:
project_assets/docs/

Files include:
- architecture.md
- db_schema.md
- api_contracts.md
- deployment.md
- etl_flows.md
- graph_schema.md

You must:
- Preserve entire file structure
- Populate ONLY AUTO blocks
- Preserve marker comments
- Preserve human-editable sections
- Populate metadata fields:
  - Last Updated
  - Overall Confidence (or Confidence)

---

# Required Output Format (STRICT JSON)
You MUST return ONLY the following JSON structure:
```json
{
  "architecture.md": {
    "metadata": {
      "last_updated": "ISO8601 UTC",
      "confidence": 0.0-1.0
    },
    "blocks": {
      "BEGIN_AUTO_SERVICES": "markdown",
      "BEGIN_AUTO_RESPONSIBILITIES": "markdown",
      "BEGIN_AUTO_INTERNAL_DEPENDENCIES": "markdown",
      "BEGIN_AUTO_EXTERNAL_DEPENDENCIES": "markdown",
      "BEGIN_AUTO_DATA_STORES": "markdown",
      "BEGIN_AUTO_MESSAGING": "markdown",
      "BEGIN_AUTO_DIAGRAM": "markdown",
      "BEGIN_AUTO_CHANGE_SUMMARY": "markdown"
    }
  },

  "db_schema.md": {
    "metadata": {
      "last_updated": "ISO8601 UTC",
      "confidence": 0.0-1.0
    },
    "blocks": {
      "BEGIN_AUTO_TABLES": "markdown",
      "BEGIN_AUTO_RELATIONSHIPS": "markdown",
      "BEGIN_AUTO_INDEXES": "markdown",
      "BEGIN_AUTO_MIGRATIONS": "markdown",
      "BEGIN_AUTO_DRIFT": "markdown"
    }
  },

  "api_contracts.md": {
    "metadata": {
      "last_updated": "ISO8601 UTC",
      "confidence": 0.0-1.0
    },
    "blocks": {
      "BEGIN_AUTO_ENDPOINTS": "markdown",
      "BEGIN_AUTO_REQUEST_SCHEMAS": "markdown",
      "BEGIN_AUTO_RESPONSE_SCHEMAS": "markdown",
      "BEGIN_AUTO_COMPATIBILITY": "markdown"
    }
  },

  "deployment.md": {
    "metadata": {
      "last_updated": "ISO8601 UTC",
      "confidence": 0.0-1.0
    },
    "blocks": {
      "BEGIN_AUTO_ENVIRONMENT_OVERVIEW": "markdown",
      "BEGIN_AUTO_DEPLOYMENT_UNITS": "markdown",
      "BEGIN_AUTO_INFRA_COMPONENTS": "markdown",
      "BEGIN_AUTO_SERVICE_EXPOSURE": "markdown",
      "BEGIN_AUTO_CICD_PIPELINE": "markdown",
      "BEGIN_AUTO_CONFIG_MANAGEMENT": "markdown",
      "BEGIN_AUTO_RUNTIME_DEPENDENCIES": "markdown",
      "BEGIN_AUTO_DEP_GRAPH": "markdown",
      "BEGIN_AUTO_SCALING_MODEL": "markdown",
      "BEGIN_AUTO_OBSERVABILITY": "markdown",
      "BEGIN_AUTO_RISK": "markdown",
      "BEGIN_AUTO_ROLLBACK": "markdown",
      "BEGIN_AUTO_DEPLOYMENT_DRIFT": "markdown"
    }
  },

  "etl_flows.md": {
    "metadata": {
      "last_updated": "ISO8601 UTC",
      "confidence": 0.0-1.0
    },
    "blocks": {
      "BEGIN_AUTO_PIPELINES": "markdown",
      "BEGIN_AUTO_LINEAGE": "markdown",
      "BEGIN_AUTO_FAILURE": "markdown",
      "BEGIN_AUTO_PERFORMANCE": "markdown"
    }
  },

  "graph_schema.md": {
    "metadata": {
      "last_updated": "ISO8601 UTC",
      "confidence": 0.0-1.0
    },
    "blocks": {
      "BEGIN_AUTO_GRAPH_METADATA": "markdown",
      "BEGIN_AUTO_NODE_LABELS": "markdown",
      "BEGIN_AUTO_NODE_PROPERTIES": "markdown",
      "BEGIN_AUTO_REL_TYPES": "markdown",
      "BEGIN_AUTO_REL_PROPERTIES": "markdown",
      "BEGIN_AUTO_CONSTRAINTS": "markdown",
      "BEGIN_AUTO_GRAPH_STATS": "markdown",
      "BEGIN_AUTO_QUERY_PATTERNS": "markdown",
      "BEGIN_AUTO_GRAPH_DRIFT": "markdown"
    }
  }
}
```

# Rules:
- No prose outside JSON.
- No markdown outside JSON.
- Do not omit any required block.
- If block not applicable:
    - return meaningful placeholder like:
    - "No graph system detected."

# Confidence Scoring Rule
Confidence must be assigned deterministically:
- 1.0 → All domains detected clearly
- 0.8 → Minor inference required
- 0.5 → Limited structural signals
- 0.3 → Sparse evidence

Do not assign arbitrary confidence.

# After JSON Generation
You must:
- Present a human-readable preview of each document.
- Display only AUTO content.
- Clearly separate each asset.
- Ask for confirmation:
```
Do you approve creation of these documentation assets?

Options:
- Approve All
- Reject
```

Then STOP.

Do NOT write files.
Do NOT initialize session.
Do NOT modify repository.

# Failure Conditions
Abort if:
- Templates missing
- architecture.md missing
- Header fields malformed
- Repository unreadable

Output clear error and stop.
