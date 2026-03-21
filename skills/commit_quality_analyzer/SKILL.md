---
name: commit-quality-analyzer
description: Evaluate commit history quality for a set of changes. Use when reviewing MR commits, assessing commit hygiene, or auditing change history.
---

# Commit Quality Analyzer

Evaluate the quality of a commit history associated with a set of changes.

## Inputs Required

1. **Commit list** — commits with SHAs, messages, authors, and timestamps
2. **Changed files** — files modified per commit (if available)

## Evaluation Criteria

### Message Quality
- Are messages descriptive and meaningful?
- Do they explain *what* and *why*, not just *how*?
- Do they follow a consistent format (e.g., imperative mood)?

### Atomicity
- Does each commit represent a single logical change?
- Are unrelated changes mixed into a single commit?

### Logical Separation
- Are commits ordered logically (e.g., refactor before feature)?
- Could the history be bisected meaningfully?

### Accuracy
- Do commit messages accurately reflect the actual changes in the diff?
- Are there misleading or vague messages?

## Output

Return a structured assessment:
1. **Summary** — overall assessment of commit structure and clarity
2. **Observations** — bullet list of specific findings
3. **Recommendations** — concrete improvements if needed; state "No commit structure concerns identified." if none
