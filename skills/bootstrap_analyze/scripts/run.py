import os
import json
from datetime import datetime

DOCS_DIR = "project_assets/docs"
PENDING_FILE = ".bootstrap_pending_content.json"
REVIEW_DIR = "project_assets/docs/asset_bootstrap/"
REVIEW_FILE = os.path.join(REVIEW_DIR, "bootstrap_review_spec.md")

REQUIRED_FILES = [
    "architecture.md",
    "db_schema.md",
    "api_contracts.md",
    "deployment.md",
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
    persist_pending_content(generated_content)

    print("\nReview spec created at:")
    print("project_assets/review/bootstrap_review_spec.md")
    print("\nPlease review and confirm before writing.\n")


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

def generate_review_spec(data: dict):
    os.makedirs(REVIEW_DIR, exist_ok=True)

    now = datetime.utcnow().isoformat() + "Z"

    with open(REVIEW_FILE, "w", encoding="utf-8") as f:
        f.write("# Bootstrap Documentation Review Spec\n\n")
        f.write(f"Generated At: {now}\n\n")
        f.write("No files have been modified yet.\n\n")
        f.write("---\n\n")

        f.write("## Document Summary\n\n")
        f.write("| Document | Confidence |\n")
        f.write("|----------|------------|\n")

        for filename, doc in data.items():
            confidence = doc["metadata"]["confidence"]
            f.write(f"| {filename} | {confidence} |\n")

        f.write("\n---\n\n")
        f.write("## Proposed AUTO Block Content\n\n")

        for filename, doc in data.items():
            f.write(f"---\n\n")
            f.write(f"### {filename}\n\n")

            for block_name, content in doc["blocks"].items():
                f.write(f"#### {block_name}\n\n")
                f.write(content.strip() + "\n\n")

    print("=========================================\n")
    print("Do you approve creation of these documentation assets?")
    print("Options:")
    print("- Approve All")
    print("- Reject\n")