---
name: patch_application
description: Applies approved AUTO block updates to architecture asset files using deterministic marker-based patching. Updates metadata and commit tracking without modifying human-editable sections.
---

# Patch Application Skill

## Purpose

This skill applies previously approved AUTO block updates to asset files.

This is the ONLY skill permitted to modify documentation files.

This skill does NOT:
- Generate new content
- Detect new changes
- Perform semantic analysis
- Suggest architectural improvements
- Perform drift detection (handled separately)

This skill ONLY:
- Reads approved content from session state
- Replaces content inside AUTO markers
- Updates metadata fields
- Updates commit tracking
- Advances session state

---

# Mirror-Only Constraint

You must strictly apply the exact approved content.

You must NEVER:
- Modify content beyond approved AUTO blocks
- Rewrite entire files
- Remove AUTO markers
- Modify human-editable sections
- Introduce additional commentary
- Reformat unrelated sections

You must apply content exactly as approved.

---

# Activation Conditions

1. Load `.asset_update_session.json`.

2. If session.phase is NOT "APPROVED_CONTENT":
   - Do NOT execute.
   - Exit immediately.

3. Load:
   - session.generated_content
   - session.approved_content
   - session.current_commit

If approved_content is null:
   - Exit immediately.

---

# Patch Application Procedure

## Step 1 — Validate Approved Content

Ensure approved_content structure matches:

```json
{
  "updates": {
    "file_path": {
      "BEGIN_AUTO_BLOCK": "content"
    }
  }
}
```

Rules:
- No unknown files
- No unknown block names
- Content must not be null
- File paths must be within project_profile/

If validation fails:
- Abort
- Report error
- Do NOT modify files

## Step 2 — For Each File
For each file in approved_content.updates:
- Verify file exists.
- Load full file content.
- For each block:
Locate markers:
```
<!-- BEGIN_AUTO_BLOCK -->
...
<!-- END_AUTO_BLOCK -->
```
- Validate both markers exist.
- Replace ONLY inner content between markers.
- Preserve:
    - Marker lines
    - File formatting
    - Indentation
    - Human sections
- If marker missing:
    - Abort entire patch
    - Do NOT partially apply changes


## Step 3 — Update Metadata Fields
After block replacement, update:
- Last Updated: {{timestamp}}
- Confidence: {{confidence_score}} or Overall Confidence
Rules:
- Only update timestamp field value
- Only update confidence numeric value
- Do NOT alter surrounding text
- Preserve field labels exactly
Timestamp format:
- ISO 8601 UTC.
Confidence value:
- Use previously computed confidence if available in session.
If not available:
- Default to 1.0

## Step 4 — Write Changes Deterministically
File writing must be handled via deterministic patch engine.
Requirements:
- Backup original file before overwrite
- Overwrite file atomically
- Ensure encoding preserved (UTF-8)
- Do NOT allow partial writes
If any file fails:
- Abort entire operation
- Restore backups

## Step 5 — Update Commit Tracking
After successful patch of all files:
1. Update .last_asset_processed_commit
    - Set to session.current_commit
2. Update .asset_update_session.json:
    ```
    {
    "phase": "APPLIED",
    "last_processed_commit": "<current_commit>"
    }
    ```
    Do NOT remove historical fields.


# Automatic Invocation Rule
After setting phase to "APPLIED":
The agent must automatically invoke:
drift-detection skill
Do NOT wait for user instruction.


# Required Output Behavior
During processing:
- Output nothing except status messages
- Do NOT print file contents
- Do NOT print markdown
- Do NOT regenerate review specs
After success:
Print:
```
Documentation assets successfully updated.
Proceeding to drift detection.
```
If failure:
```
Patch application aborted due to validation error.
No files were modified.
```

# Failure Conditions
Abort entire operation if:
- Session missing
- Phase incorrect
- Approved content missing
- File missing
- Marker missing
- Metadata field missing
- Write failure
- Backup failure

Never partially patch.
Never leave file in inconsistent state.

