import os
import json

DOCS_DIR = "project_assets/docs"
PENDING_FILE = ".bootstrap_pending_content.json"

REQUIRED_FILES = [
    "architecture.md",
    "db_schema.md",
    "api_contracts.md",
    "docker_deployment.md",
    "etl_flows.md",
    "graph_schema.md"
]


def run(generated_content: dict):
    """
    Deterministic analyze-phase executor.
    Receives structured JSON from LLM.
    """

    validate_templates_exist()
    validate_one_time_guard()
    validate_generated_structure(generated_content)

    persist_pending_content(generated_content)
    render_preview(generated_content)


# ---------------------------
# Validation
# ---------------------------

def validate_templates_exist():
    if not os.path.exists(DOCS_DIR):
        raise Exception("project_assets/docs directory not found.")

    for filename in REQUIRED_FILES:
        path = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(path):
            raise Exception(f"Missing template: {filename}")


def validate_one_time_guard():
    arch_path = os.path.join(DOCS_DIR, "architecture.md")

    with open(arch_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "{{timestamp}}" not in content or "{{confidence_score}}" not in content:
        raise Exception(
            "Documentation already initialized. Use asset_updater_agent instead."
        )


def validate_generated_structure(data: dict):
    if not isinstance(data, dict):
        raise Exception("Generated content must be a dictionary.")

    for filename in REQUIRED_FILES:
        if filename not in data:
            raise Exception(f"Missing document in generated content: {filename}")

        doc = data[filename]

        if "metadata" not in doc or "blocks" not in doc:
            raise Exception(f"Malformed structure for {filename}")

        if not isinstance(doc["blocks"], dict):
            raise Exception(f"Blocks must be dictionary in {filename}")


# ---------------------------
# Persistence
# ---------------------------

def persist_pending_content(data: dict):
    with open(PENDING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ---------------------------
# Preview
# ---------------------------

def render_preview(data: dict):
    print("\n================ PREVIEW ================\n")

    for filename, doc in data.items():
        print(f"----- {filename} -----\n")

        for block_name, content in doc["blocks"].items():
            print(f"[{block_name}]\n")
            print(content)
            print("\n")

    print("=========================================\n")
    print("Do you approve creation of these documentation assets?")
    print("Options:")
    print("- Approve All")
    print("- Reject\n")