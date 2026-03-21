---
name: mr-size-evaluator
description: Classify merge request size and assess reviewability. Use when evaluating whether an MR should be split or is appropriately scoped.
---

# MR Size Evaluator

Classify the size of a merge request and assess its reviewability.

## Inputs Required

1. **Total files changed**
2. **Total lines added**
3. **Total lines deleted**
4. **File list** (optional — for context on change spread)

## Classification

| Category | Files | Lines Changed (add+delete) | Reviewability |
|----------|-------|---------------------------|---------------|
| Small | 1–5 | < 200 | Easy |
| Moderate | 6–15 | 200–500 | Manageable |
| Large | 16–30 | 500–1000 | Difficult |
| Excessive | 30+ | 1000+ | Risky |

Use judgment — a 10-file MR with only config changes may still be "Small" in complexity. A 3-file MR with 800 lines of dense logic may be "Large" in review effort.

## Output

Return:
1. **Classification** — Small / Moderate / Large / Excessive
2. **Reasoning** — brief justification based on files, lines, and change spread
3. **Recommendations** — if Large or Excessive, suggest how to split and explain reviewability concerns and production risk. If Small or Moderate, state "No size concerns."
