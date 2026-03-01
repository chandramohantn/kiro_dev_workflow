---
name: content_generation
description: Generates updated AUTO block content for architecture assets based on confirmed structural repository changes. Produces structured content review specification without modifying any files.
---

# Content Generation Skill

## Purpose

This skill generates updated AUTO block content for architecture assets using approved structural change data.

This skill does NOT:
- Modify any files
- Apply patches
- Detect new repository changes
- Perform drift detection
- Suggest architectural improvements

This skill ONLY:
- Reads approved structural changes
- Reads relevant asset files
- Generates updated AUTO block content
- Produces Review Spec #2
- Updates session state

---

# Mirror-Only Constraint

You must strictly mirror repository reality.

You must NEVER:
- Suggest improvements
- Evaluate architecture quality
- Recommend refactors
- Add speculative commentary
- Invent undocumented behavior
- Modify human-editable sections

If approved change data is insufficient:
- Explicitly state missing information
- Do NOT fabricate content

All generated content must reflect:
- Observable code structure
- Confirmed structural changes
- Current repository state

---

# Activation Conditions

1. Load `.asset_update_session.json`.

2. If session.phase is NOT "APPROVED_CHANGES":
   - Do NOT execute.
   - Exit immediately.

3. Load:
   - session.detected_changes
   - session.approved_changes
   - session.current_commit

If approved_changes is null:
   - Exit immediately.

---

# Asset Scope

You may update ONLY the following files:

- project_assets/docs/api_contracts.md
- project_assets/docs/db_schema.md
- project_assets/docs/architecture.md
- project_assets/docs/deployment.md
- project_assets/docs/etl_flows.md
- project_assets/docs/graph_schema.md

You must NOT:
- Create new files
- Modify file structure
- Remove AUTO markers
- Modify human-editable sections
- Modify non-impacted domains

---

# Content Generation Procedure

## Step 1 — Determine Impacted Assets

Based on approved_changes.domains_impacted:

Map domain → asset file:

- api → api_contracts.md
- db → db_schema.md
- architecture → architecture.md
- deployment → deployment.md
- etl → etl_flows.md
- graph → graph_schema.md

Only load relevant asset files.

---

## Step 2 — Extract Existing AUTO Blocks

From each impacted asset:
Identify all AUTO blocks:
```
<!-- BEGIN_AUTO_* -->

...

<!-- END_AUTO_* -->
```


Do NOT modify human sections.

Preserve block structure exactly.

---

## Step 3 — Generate Updated Block Content

For each impacted domain:

Generate ONLY inner block content.

You must:

- Reflect approved structural changes exactly
- Maintain markdown formatting
- Maintain table structures
- Maintain mermaid formatting (if applicable)
- Avoid narrative explanations inside AUTO blocks
- Avoid advisory language

If no changes required for a block:
- Return null for that block.

---

# Required Output Format (STRICT JSON)

You MUST produce ONLY the following JSON structure:

```json
{
  "updates": {
    "project_assets/api_contracts.md": {
      "BEGIN_AUTO_ENDPOINTS": "markdown content or null",
      "BEGIN_AUTO_REQUEST_SCHEMAS": "markdown content or null",
      "BEGIN_AUTO_RESPONSE_SCHEMAS": "markdown content or null",
      "BEGIN_AUTO_COMPATIBILITY": "markdown content or null"
    },
    "project_assets/db_schema.md": {
      "BEGIN_AUTO_TABLES": "markdown content or null",
      "BEGIN_AUTO_RELATIONSHIPS": "markdown content or null",
      "BEGIN_AUTO_INDEXES": "markdown content or null",
      "BEGIN_AUTO_MIGRATIONS": "markdown content or null",
      "BEGIN_AUTO_DRIFT": "markdown content or null"
    },
    "project_assets/architecture.md": {
      "BEGIN_AUTO_SERVICES": "markdown content or null",
      "BEGIN_AUTO_RESPONSIBILITIES": "markdown content or null",
      "BEGIN_AUTO_INTERNAL_DEPENDENCIES": "markdown content or null",
      "BEGIN_AUTO_EXTERNAL_DEPENDENCIES": "markdown content or null",
      "BEGIN_AUTO_DATA_STORES": "markdown content or null",
      "BEGIN_AUTO_MESSAGING": "markdown content or null",
      "BEGIN_AUTO_DIAGRAM": "markdown content or null",
      "BEGIN_AUTO_CHANGE_SUMMARY": "markdown content or null"
    },
    "project_assets/deployment.md": {
      "BEGIN_AUTO_ENVIRONMENT_OVERVIEW": "markdown content or null",
      "BEGIN_AUTO_DEPLOYMENT_UNITS": "markdown content or null",
      "BEGIN_AUTO_INFRA_COMPONENTS": "markdown content or null",
      "BEGIN_AUTO_SERVICE_EXPOSURE": "markdown content or null",
      "BEGIN_AUTO_CICD_PIPELINE": "markdown content or null",
      "BEGIN_AUTO_CONFIG_MANAGEMENT": "markdown content or null",
      "BEGIN_AUTO_RUNTIME_DEPENDENCIES": "markdown content or null",
      "BEGIN_AUTO_DEP_GRAPH": "markdown content or null",
      "BEGIN_AUTO_SCALING_MODEL": "markdown content or null",
      "BEGIN_AUTO_OBSERVABILITY": "markdown content or null",
      "BEGIN_AUTO_RISK": "markdown content or null",
      "BEGIN_AUTO_ROLLBACK": "markdown content or null",
      "BEGIN_AUTO_DEPLOYMENT_DRIFT": "markdown content or null"
    },
    "project_assets/etl_flows.md": {
      "BEGIN_AUTO_PIPELINES": "markdown content or null",
      "BEGIN_AUTO_LINEAGE": "markdown content or null",
      "BEGIN_AUTO_FAILURE": "markdown content or null",
      "BEGIN_AUTO_PERFORMANCE": "markdown content or null"
    },
    "project_assets/graph_schema.md": {
      "BEGIN_AUTO_GRAPH_METADATA": "markdown content or null",
      "BEGIN_AUTO_NODE_LABELS": "markdown content or null",
      "BEGIN_AUTO_NODE_PROPERTIES": "markdown content or null",
      "BEGIN_AUTO_REL_TYPES": "markdown content or null",
      "BEGIN_AUTO_REL_PROPERTIES": "markdown content or null",
      "BEGIN_AUTO_CONSTRAINTS": "markdown content or null",
      "BEGIN_AUTO_GRAPH_STATS": "markdown content or null",
      "BEGIN_AUTO_QUERY_PATTERNS": "markdown content or null",
      "BEGIN_AUTO_GRAPH_DRIFT": "markdown content or null"
    }
  }
}
```

# Rules:
- If file not impacted → omit it.
- If block not impacted → return null.
- Never omit block keys for impacted files.
- Never include extra keys.
- Never output markdown outside JSON.


# Session State Update
After generating the JSON:
Update .asset_update_session.json:
```
{
  "phase": "AWAITING_CONTENT_CONFIRMATION",
  "generated_content": { ...updates JSON... }
}
```
Do NOT modify:
- last_processed_commit
- current_commit
Save file.

# Review Spec #2 Generation
After updating session:
Generate a human-readable proposal.
For each impacted file:
- Show file name
- Show only blocks where content is not null
- Display proposed block content clearly
- Do NOT include advisory explanations
End with:
Do you approve these documentation updates?
Options:
- Approve All
- Approve Selected Files
- Reject
- Request Clarification

THEN STOP.
Do NOT proceed to patch-application.
Save the spec as: 
- project_assets/specs/asset_updater/<short-title>-<content>.md

# Failure Conditions
If:
- Session missing
- approved_changes missing
- Asset file missing
- AUTO markers missing
Then:
- Report error clearly
- Do NOT modify session
- Do NOT generate partial output
