# WorkflowTemplate

Defines a reusable workflow template with ordered stages.

---

## Fields

### workflow_name

- Type: string
- Required: no
- Description: Name of the workflow.

---

### description

- Type: string
- Required: no
- Description: Description of the workflow.

---

### stages

- Type: array
- Required: no
- Description: List of stages in the workflow.
- Items: Each item is an object with the following fields:
  - stage_id (string): Unique identifier for the stage.
  - name (string): Name of the stage.
  - agent (string): Agent responsible for the stage.
  - checkpoint (string): Checkpoint or gate for the stage.
  - depends_on (array of strings): Stage IDs this stage depends on.
  - outputs (array of strings): Expected outputs from the stage.
