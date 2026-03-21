# TestReport

Structured test execution report from the test agent.

---

## Fields

### test_scope

- Type: string
- Required: yes
- Description: Description of what was tested.

---

### tests_written

- Type: array
- Required: no
- Description: Tests that were written as part of this task.
- Items: Each item is an object with: test_name (string), test_file (string), description (string).

---

### tests_executed

- Type: integer
- Required: no
- Description: Total number of tests executed.

---

### tests_passed

- Type: integer
- Required: no
- Description: Number of tests that passed.

---

### tests_failed

- Type: integer
- Required: no
- Description: Number of tests that failed.

---

### failures

- Type: array
- Required: no
- Description: Details of failed tests.
- Items: Each item is an object with: test_name (string), error (string), file (string).

---

### coverage_summary

- Type: string
- Required: no
- Description: Summary of code coverage if available.

---

### test_artifacts

- Type: array
- Required: no
- Description: Test files created or modified.
- Items: Each item is a string representing a file path.

---

### recommendations

- Type: array
- Required: no
- Description: Suggestions for additional test coverage or improvements.
- Items: Each item is a string describing a recommendation.