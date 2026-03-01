---
name: bootstrap-write
description: Applies approved bootstrap documentation content to asset templates and initializes repository documentation state. Executes only after user confirmation.
---

# Bootstrap Write Skill

## Purpose

This skill applies approved bootstrap-generated documentation content to templates located in:

project_assets/docs/

It performs deterministic file mutation and initializes repository documentation state.

This skill:

- Writes AUTO blocks
- Updates metadata fields
- Initializes session artifacts
- Executes only once
- Does NOT perform analysis
- Does NOT regenerate content

---

# Activation Condition

This skill must execute ONLY after:

1. bootstrap-analyze has generated structured JSON content
2. User explicitly selects: "Approve All"

If approval has not been granted:
→ Do NOT execute.

---

# One-Time Execution Guard

Before writing any files:

1. Open:
   project_assets/docs/architecture.md

2. Inspect header fields:

If `Last Updated:` does NOT contain `{{timestamp}}`
OR `Overall Confidence:` does NOT contain `{{confidence_score}}`

→ Abort immediately.

Output:

Documentation already initialized.
Bootstrap cannot be executed again.

Do NOT modify any file.

---

# Input Contract

This skill receives structured JSON in the following format:

{
  "architecture.md": {
    "metadata": {
      "last_updated": "ISO8601 UTC",
      "confidence": number
    },
    "blocks": {
      "BEGIN_AUTO_SERVICES": "...",
      ...
    }
  },
  ...
}

The structure must match exactly what bootstrap-analyze produced.

If structure is malformed:
→ Abort.

---

# Deterministic Write Rules

For each document:

1. Load template file from:
   project_assets/docs/<filename>

2. For each block:

   Locate:

   <!-- BEGIN_AUTO_* -->
   ...
   <!-- END_AUTO_* -->

3. Replace ONLY the inner content.

4. Preserve:
   - Marker comments
   - Human sections
   - File structure
   - Markdown formatting

5. Replace metadata fields:

   - Replace `{{timestamp}}` with metadata.last_updated
   - Replace `{{confidence_score}}` with metadata.confidence

Do NOT modify:
- Header titles
- Section ordering
- Any content outside AUTO blocks
- Marker syntax

---

# Required Documents

You must write ALL of the following:

- architecture.md
- db_schema.md
- api_contracts.md
- docker_deployment.md
- etl_flows.md
- graph_schema.md

If any template missing:
→ Abort entire operation.
→ Do NOT partially write.

---

# Atomic Write Requirement

All documents must be written successfully.

If any failure occurs:
- Restore all modified files from backup
- Abort
- Print failure message

Never leave repository in partial state.

---

# Session Initialization

After successful write:

1. Create `.asset_update_session.json` at repository root with:

{
  "phase": "IDLE",
  "detected_changes": null,
  "approved_changes": null,
  "generated_content": null,
  "approved_content": null,
  "last_processed_commit": "<current HEAD commit>",
  "current_commit": null,
  "error_message": null,
  "created_at": "ISO8601 UTC",
  "updated_at": "ISO8601 UTC"
}

2. Create `.last_asset_processed_commit` at repository root.

Set value to:

git rev-parse HEAD

These artifacts enable asset_updater_agent to function.

---

# Post-Execution Output

After successful write:

Output:

Bootstrap documentation created successfully.

Mirror maintenance is now enabled.
Use asset_updater_agent for incremental updates.

---

# Failure Conditions

Abort if:

- Templates missing
- Metadata missing
- Any required block missing
- JSON malformed
- Write failure
- Git commit detection fails

In case of failure:

Output:

Bootstrap write aborted due to validation error.
No files were modified.

---

# Safety Constraints

This skill must:

- Never analyze repository
- Never regenerate content
- Never re-bootstrap
- Never overwrite existing populated documentation
- Never bypass one-time guard

---

# End of Skill