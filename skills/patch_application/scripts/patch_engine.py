import os
import shutil
from datetime import datetime

def apply_patch(approved_content: dict):
    """
    approved_content format:
    {
        "updates": {
            "project_assets/api_contracts.md": {
                "BEGIN_AUTO_ENDPOINTS": "...markdown..."
            }
        }
    }
    """

    updates = approved_content.get("updates", {})

    for file_path, blocks in updates.items():
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")

        backup_file(file_path)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        for block_name, new_content in blocks.items():
            if new_content is None:
                continue

            begin_marker = f"<!-- {block_name} -->"
            end_marker = f"<!-- END_AUTO_{block_name.split('BEGIN_AUTO_')[-1]} -->"

            if begin_marker not in content or end_marker not in content:
                raise Exception(f"Markers not found in {file_path} for {block_name}")

            pre, rest = content.split(begin_marker, 1)
            _, post = rest.split(end_marker, 1)

            content = (
                pre
                + begin_marker
                + "\n"
                + new_content.strip()
                + "\n"
                + end_marker
                + post
            )

        content = update_metadata(content)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)


def backup_file(file_path):
    backup_path = file_path + ".bak"
    shutil.copyfile(file_path, backup_path)


def update_metadata(content: str) -> str:
    now = datetime.utcnow().isoformat() + "Z"

    if "Last Updated:" in content:
        content = replace_line(content, "Last Updated:", f"Last Updated: {now}")

    if "Confidence:" in content:
        content = replace_line(content, "Confidence:", "Confidence: 1.0")

    return content


def replace_line(content: str, prefix: str, new_line: str) -> str:
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith(prefix):
            lines[i] = new_line
            break
    return "\n".join(lines)