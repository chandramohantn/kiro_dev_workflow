# ArchitectureAnalysis

Structured output from the architecture agent containing system design analysis, recommendations, and trade-offs.

---

## Fields

### analysis_scope

- Type: string
- Required: yes
- Description: Description of the system or component being analyzed.

---

### current_state

- Type: string
- Required: yes
- Description: Summary of the current architecture or design.

---

### identified_issues

- Type: array
- Required: no
- Description: Architectural issues, anti-patterns, or risks identified.
- Items: Each item is a string describing an issue.

---

### recommendations

- Type: array
- Required: no
- Description: Architectural recommendations with reasoning and trade-offs.
- Items: Each item is an object with: recommendation (string), reasoning (string), trade_offs (string).

---

### dependency_analysis

- Type: string
- Required: no
- Description: Analysis of component dependencies and coupling.

---

### scalability_assessment

- Type: string
- Required: no
- Description: Evaluation of scalability characteristics and concerns.

---

### proposed_design

- Type: string
- Required: no
- Description: Description of the recommended design or architecture changes.

---

### diagrams

- Type: array
- Required: no
- Description: Text-based diagrams or references to architectural diagrams.
- Items: Each item is a string representing a diagram or reference.

---

### risks

- Type: array
- Required: no
- Description: Potential risks associated with the proposed changes.
- Items: Each item is a string describing a risk.