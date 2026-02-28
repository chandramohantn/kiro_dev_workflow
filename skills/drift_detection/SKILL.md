---
name: drift_detection
description: Detects structural inconsistencies across repository domains and generates a structured drift report without modifying core documentation assets.
---

# Drift Detection Skill

## Purpose

This skill detects structural inconsistencies ("drift") across repository domains and writes results to:

project_profile/drift_report.md

This skill does NOT:
- Modify architecture assets
- Modify AUTO blocks in core documentation files
- Suggest architectural improvements
- Recommend fixes
- Evaluate design quality

This skill ONLY:
- Observes mismatches
- Classifies drift
- Writes structured drift report
- Updates drift metadata
- Advances session state

---

# Mirror-Only Constraint

You must strictly report observable inconsistencies.

You must NEVER:
- Suggest improvements
- Recommend corrective action
- Use advisory language (should, consider, recommend)
- Speculate about intent

Only describe detected structural mismatches.

If insufficient data exists:
- Report "Insufficient data to evaluate"
- Do NOT infer missing structure

---

# Activation Conditions

1. Load `.asset_update_session.json`.

2. If session.phase is NOT "APPLIED":
   - Do NOT execute.
   - Exit immediately.

3. Ensure drift_report.md exists.
   If missing:
   - Create file using predefined template structure
   - Include required AUTO blocks

---

# Drift Detection Scope

Analyze current repository state.

You may inspect:
- project_profile/*.md
- services/*
- Dockerfile
- docker-compose.yml
- ETL directories
- Graph-related code
- Any relevant repo files

Do NOT rely on session.detected_changes.

Drift detection must analyze CURRENT repository state.

---

# Drift Categories

You must detect and classify drift in the following domains:

---

## 1. Database Drift

Detect mismatches such as:

- Table defined in models but not referenced in API
- Column referenced in API but not present in models
- Table present in migrations but not present in models
- Index inconsistencies
- Constraint inconsistencies

If no drift:
Return empty list.

---

## 2. API Drift

Detect mismatches such as:

- Route exists but not present in api_contracts.md
- api_contracts.md lists endpoint not present in code
- Response schema fields mismatch observable models
- Duplicate route definitions

---

## 3. Deployment Drift

Detect mismatches such as:

- Service directory exists but not in docker-compose.yml
- docker-compose service references non-existent build context
- Environment variable referenced in code but not declared in deployment file
- Dockerfile missing for declared service

---

## 4. ETL Drift

Detect mismatches such as:

- Pipeline defined but not documented
- Documented pipeline not present in code
- Source or sink mismatch

---

## 5. Graph Drift

Detect mismatches such as:

- Node label present in code but not documented
- Relationship type undocumented
- Constraint mismatch between code and graph_schema.md

---

## 6. Cross-Domain Drift

Detect structural inconsistencies such as:

- DB column not referenced anywhere
- API referencing non-existent DB model
- Deployment referencing removed service
- ETL referencing removed table

Do NOT assess impact.
Only report mismatch.

---

# Severity Classification (Deterministic)

Assign severity using rules:

- MAJOR:
  - Missing service
  - API referencing non-existent model
  - Deployment referencing missing directory
  - Broken cross-domain reference

- MINOR:
  - Undocumented endpoint
  - Undocumented column
  - Missing documentation entry

- NONE:
  - No drift detected

Do NOT allow LLM to invent severity beyond these rules.

---

# Required Output Format (STRICT JSON)

Before writing report, produce:

```json
{
  "db_drift": [
    {
      "description": "string",
      "severity": "MAJOR|MINOR"
    }
  ],
  "api_drift": [],
  "deployment_drift": [],
  "etl_drift": [],
  "graph_drift": [],
  "cross_domain_drift": []
}
```

# Drift Report Update Procedure
After JSON generation:
1. Load project_profile/drift_report.md
2. Replace inner content of following AUTO blocks:
    - BEGIN_AUTO_DB_DRIFT
    - BEGIN_AUTO_API_DRIFT
    - BEGIN_AUTO_DEPLOYMENT_DRIFT
    - BEGIN_AUTO_ETL_DRIFT
    - BEGIN_AUTO_GRAPH_DRIFT
    - BEGIN_AUTO_CROSS_DRIFT
    - BEGIN_AUTO_SUMMARY
3. Format drift items as bullet list:
Example:
- [MAJOR] API route /users references missing table users_archive
- [MINOR] Column last_login undocumented in api_contracts.md
If no drift in a domain:
Write: No drift detected.


# Drift Summary Section
Compute:
Total Drift Items: X
Major: Y
Minor: Z

Determine Overall Drift Status:
NONE → if X = 0
MINOR → if Y = 0 and Z > 0
MAJOR → if Y > 0
Write into BEGIN_AUTO_SUMMARY block.


# Metadata Update
Update:
Last Evaluated: ISO 8601 UTC timestamp
Overall Drift Status
Confidence: 1.0

Confidence remains 1.0 unless evaluation incomplete.


# Session Update
After successful report update:
Update .asset_update_session.json:
```
{
  "phase": "DRIFT_REPORTED"
}
```
Preserve previous session data.


# Required Output Behavior
After completion, output:
Drift report updated successfully.

If failure:
Drift detection aborted due to validation error.
No files modified.


# Failure Conditions
Abort if:
- drift_report.md missing and cannot be created
- Required AUTO markers missing
- File write fails
- Session file missing
- Session phase incorrect

Never partially update report.

