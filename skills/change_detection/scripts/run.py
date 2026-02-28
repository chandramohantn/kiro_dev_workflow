from core.session_manager import SessionManager
import subprocess
import json

def run_change_detection(llm_callable):
    sm = SessionManager()

    if sm.session["phase"] != "IDLE":
        return  # Do nothing

    sm.set_current_commit()

    last_commit = sm.session["last_processed_commit"]
    current_commit = sm.session["current_commit"]

    diff = subprocess.check_output(
        ["git", "diff", "--name-status", last_commit, current_commit]
    ).decode()

    if not diff.strip():
        print("Documentation is up to date.")
        return

    # Load changed files content
    changed_files = [line.split("\t")[1] for line in diff.splitlines()]
    file_contents = {}

    for f in changed_files:
        try:
            with open(f, "r") as fh:
                file_contents[f] = fh.read()
        except:
            file_contents[f] = None

    # Call LLM for structural extraction
    detected_changes = llm_callable(file_contents)

    sm.update_fields({
        "detected_changes": detected_changes
    })

    sm.transition("AWAITING_CHANGE_CONFIRMATION")