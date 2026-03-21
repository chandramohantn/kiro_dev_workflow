# MergeRequestReview

Structured review of a merge request.

---

## Fields

### mr_url

- Type: string
- Required: no
- Description: URL of the merge request.

---

### summary

- Type: string
- Required: no
- Description: Summary of the merge request.

---

### domains_detected

- Type: array
- Required: no
- Description: Domains or areas affected by the merge request.
- Items: Each item is a string representing a domain.

---

### commit_quality

- Type: string
- Required: no
- Description: Assessment of commit quality.

---

### mr_size_evaluation

- Type: string
- Required: no
- Description: Evaluation of the merge request size.

---

### issues

- Type: array
- Required: no
- Description: Issues found during review.
- Items: Each item is a string describing an issue.

---

### recommendations

- Type: array
- Required: no
- Description: Recommendations for improvement.
- Items: Each item is a string describing a recommendation.

---

### overall_assessment

- Type: string
- Required: no
- Description: Overall assessment of the merge request.
