# .kiro/tools/bootstrap_write_run.py

import json
import os
from skills.bootstrap_write.scripts.run import run as write_run


PENDING_FILE = ".bootstrap_pending_content.json"


def run():
    """
    Tool wrapper for bootstrap write phase.
    Applies previously approved documentation content.
    """

    if not os.path.exists(PENDING_FILE):
        print("No pending bootstrap content found.")
        print("Run bootstrap analyze first.")
        return

    try:
        with open(PENDING_FILE, "r", encoding="utf-8") as f:
            approved_content = json.load(f)

        write_run(approved_content)

        # Remove pending file after successful write
        os.remove(PENDING_FILE)

    except Exception as e:
        print("\nBootstrap write failed.")
        print(str(e))
        raise e