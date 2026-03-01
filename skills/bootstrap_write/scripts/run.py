import os
import shutil
import subprocess
import json
from datetime import datetime

DOCS_DIR = "project_assets/docs"
REQUIRED_FILES = [
    "architecture.md",
    "db_schema.md",
    "api_contracts.md",
    "deployment.md",
    "etl_flows.md",
    "graph_schema.md"
]

SESSION_FILE = ".asset_update_session.json"
COMMIT_FILE = ".last_asset_processed_commit"


# ---------------------------------------------------
# Public Entry Point
# ---------------------------------------------------

def run(approved_content: dict):
    """
    Deterministic bootstrap write executor.
    """

    validate_one_time_guard()
    validate_json_contract(approved_content)

    backups = []

    try:
        # Backup all files first
        for filename in REQUIRED_FILES:
            path = os.path.join(DOCS_DIR, filename)
            backup_path = path + ".bak"
            shutil.copyfile(path, backup_path)
            backups.append((path, backup_path))

        # Apply updates
        for filename in REQUIRED_FILES:
            apply_document_update(filename, approved_content[filename])

        # Initialize mirror agent artifacts
        initialize_session_files()

        # Remove backups on success
        for _, backup_path in backups:
            os.remove(backup_path)

        print("\nBootstrap documentation created successfully.")
        print("Mirror maintenance is now enabled.")
        print("Use asset_updater_agent for incremental updates.\n")

    except Exception as e:
        # Restore backups
        for original, backup in backups:
            if os.path.exists(backup):
                shutil.copyfile(backup, original)
                os.remove(backup)

        print("\nBootstrap write aborted due to validation error.")
        print("No files were modified.\n")
        raise e


# ---------------------------------------------------
# Validation
# ---------------------------------------------------

def validate_one_time_guard():
    arch_path = os.path.join(DOCS_DIR, "architecture.md")

    if not os.path.exists(arch_path):
        raise Exception("architecture.md template missing.")

    with open(arch_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "{{timestamp}}" not in content or "{{confidence_score}}" not in content:
        raise Exception("Documentation already initialized. Bootstrap cannot run again.")


def validate_json_contract(data: dict):
    if not isinstance(data, dict):
        raise Exception("Approved content must be a dictionary.")

    for filename in REQUIRED_FILES:
        if filename not in data:
            raise Exception(f"Missing document in approved content: {filename}")

        doc = data[filename]

        if "metadata" not in doc or "blocks" not in doc:
            raise Exception(f"Malformed structure for {filename}")

        if "last_updated" not in doc["metadata"] or "confidence" not in doc["metadata"]:
            raise Exception(f"Missing metadata fields in {filename}")

        if not isinstance(doc["blocks"], dict):
            raise Exception(f"Blocks must be a dictionary in {filename}")


# ---------------------------------------------------
# Document Update Logic
# ---------------------------------------------------

def apply_document_update(filename: str, doc_data: dict):
    path = os.path.join(DOCS_DIR, filename)

    if not os.path.exists(path):
        raise Exception(f"Template missing: {filename}")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = doc_data["blocks"]

    for block_name, new_content in blocks.items():
        content = replace_auto_block(content, block_name, new_content)

    content = replace_metadata(content, doc_data["metadata"])

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def replace_auto_block(content: str, block_name: str, new_content: str) -> str:
    begin_marker = f"<!-- {block_name} -->"
    end_marker = f"<!-- END_AUTO_{block_name.split('BEGIN_AUTO_')[-1]} -->"

    if begin_marker not in content or end_marker not in content:
        raise Exception(f"Marker mismatch for {block_name}")

    before, remainder = content.split(begin_marker, 1)
    _, after = remainder.split(end_marker, 1)

    updated_block = (
        begin_marker
        + "\n"
        + new_content.strip()
        + "\n"
        + end_marker
    )

    return before + updated_block + after


def replace_metadata(content: str, metadata: dict) -> str:
    last_updated = metadata["last_updated"]
    confidence = metadata["confidence"]

    if "{{timestamp}}" not in content:
        raise Exception("Timestamp placeholder missing.")

    if "{{confidence_score}}" not in content:
        raise Exception("Confidence placeholder missing.")

    content = content.replace("{{timestamp}}", last_updated)
    content = content.replace("{{confidence_score}}", str(confidence))

    return content


# ---------------------------------------------------
# Session Initialization
# ---------------------------------------------------

def initialize_session_files():
    head_commit = get_current_commit()
    now = datetime.utcnow().isoformat() + "Z"

    session_data = {
        "phase": "IDLE",
        "detected_changes": None,
        "approved_changes": None,
        "generated_content": None,
        "approved_content": None,
        "last_processed_commit": head_commit,
        "current_commit": None,
        "error_message": None,
        "created_at": now,
        "updated_at": now
    }

    write_atomic_json(SESSION_FILE, session_data)

    with open(COMMIT_FILE, "w", encoding="utf-8") as f:
        f.write(head_commit)


def write_atomic_json(path: str, data: dict):
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp_path, path)


def get_current_commit() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"]
    ).decode().strip()