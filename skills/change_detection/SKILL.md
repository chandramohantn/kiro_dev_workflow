---
name: change_detection
description: Detects repository changes using git diff and performs semantic structural analysis of modified files. Produces a structured change review specification and initializes the asset update session state.
---

# Change Detection Skill

## Purpose

This skill detects repository changes since the last processed commit and extracts structural modifications across architecture domains.

This skill does NOT:
- Modify any asset files
- Generate documentation updates
- Perform drift detection
- Produce advisory recommendations

This skill ONLY:
- Detects changed files
- Analyzes their structural impact
- Produces structured JSON describing changes
- Creates Review Spec #1
- Initializes session state

---

# Mirror-Only Constraint

You must strictly mirror repository reality.

You must NEVER:
- Suggest improvements
- Evaluate design quality
- Recommend architectural changes
- Infer intent beyond observable code
- Invent metadata not present in changed files

If insufficient context exists:
- Explicitly request additional files
- Do NOT assume missing structure

---

# Activation Conditions

1. If `.asset_update_session.json` does NOT exist:
   - Initialize it with phase = "IDLE"

2. Load `.asset_update_session.json`.

3. If session.phase is NOT "IDLE":
   - Do NOT execute.
   - Exit immediately.

4. Load `.last_asset_processed_commit`.

5. Determine current HEAD commit.

---

# Change Detection Procedure

## Step 1 — Git Diff

Run:
```
git diff --name-status LAST_PROCESSED_COMMIT HEAD
```

If no changes detected:
- Output: "Documentation is up to date."
- Do NOT modify session.
- Exit.

If changes detected:
- Collect:
  - File path
  - Change type (A/M/D)
  - Full file content (for A/M)
  - Diff content (optional)

---

## Step 2 — Domain Classification (LLM-Based)

Analyze ONLY changed files.

Classify impacted domains based on content and path:

- API
- DB
- Architecture
- Deployment
- ETL
- Graph

Do NOT scan entire repository.

Do NOT infer impact beyond provided files.

---

## Step 3 — Structural Change Extraction

From changed files, extract:

### API Domain
- Endpoints added
- Endpoints modified
- Endpoints removed
- Request schema changes
- Response schema changes

### DB Domain
- Tables added
- Tables modified
- Tables removed
- Columns added
- Columns modified
- Columns removed
- Index changes
- Constraint changes

### Architecture Domain
- New services detected
- Service removals
- New external dependencies
- Dependency changes

### Deployment Domain
- Docker services added/removed
- Port changes
- Image changes
- Environment variable changes
- CI/CD changes
- Ansible services

### ETL Domain
- Pipelines added/modified/removed
- Source changes
- Sink changes

### Graph Domain
- Node labels added/removed
- Relationship types added/removed
- Constraint changes

If no structural change detected within a domain:
- Return empty arrays for that domain.

---

# Required Output Format (STRICT JSON)

You MUST produce ONLY the following JSON structure:

```json
{
  "domains_impacted": [],
  "changes": {
    "api": {
      "endpoints_added": [],
      "endpoints_modified": [],
      "endpoints_removed": [],
      "schemas_changed": []
    },
    "db": {
      "tables_added": [],
      "tables_modified": [],
      "tables_removed": [],
      "columns_added": [],
      "columns_modified": [],
      "columns_removed": [],
      "indexes_changed": [],
      "constraints_changed": []
    },
    "architecture": {
      "services_added": [],
      "services_removed": [],
      "dependencies_added": [],
      "dependencies_removed": []
    },
    "deployment": {
      "services_added": [],
      "services_removed": [],
      "ports_changed": [],
      "env_changed": [],
      "ci/cd_changes": []
    },
    "etl": {
      "pipelines_added": [],
      "pipelines_modified": [],
      "pipelines_removed": []
    },
    "graph": {
      "node_labels_added": [],
      "node_labels_removed": [],
      "relationships_added": [],
      "relationships_removed": [],
      "constraints_changed": []
    }
  }
}
```

# Session State Update
After producing the JSON:
- Update .asset_update_session.json:
```
{
  "phase": "AWAITING_CHANGE_CONFIRMATION",
  "detected_changes": { ...structured JSON above... },
  "approved_changes": null,
  "generated_content": null,
  "approved_content": null,
  "last_processed_commit": "<previous_commit>",
  "current_commit": "<head_commit>"
}
```
- Save file.


# Review Spec #1 Generation
After session update, produce a human-readable Change Review Spec.
This must include:
- Domains impacted
- Structural changes grouped by domain
- Clear bullet format
- No suggestions
- No advisory language
- No speculation

End the spec with:
```
Do you approve these detected structural changes?

Options:
- Approve All
- Approve Selected Domains
- Reject
- Request Clarification
```

Then STOP.
Do NOT proceed to content generation.
Save the spec as: 
- project_assets/specs/asset_updater/<short-title>-<change>.md


# Failure Conditions
If:
- Git command fails
- Commit reference missing
- Session file corrupted
Then:
- Report error clearly
- Do NOT modify session
- Do NOT proceed
