import json
import os
import subprocess
from datetime import datetime
from typing import Dict, Any


SESSION_FILE = ".asset_update_session.json"
COMMIT_FILE = ".last_asset_processed_commit"


VALID_STATES = {
    "IDLE",
    "AWAITING_CHANGE_CONFIRMATION",
    "APPROVED_CHANGES",
    "AWAITING_CONTENT_CONFIRMATION",
    "APPROVED_CONTENT",
    "APPLIED",
    "DRIFT_REPORTED",
    "ERROR"
}


VALID_TRANSITIONS = {
    "IDLE": ["AWAITING_CHANGE_CONFIRMATION"],
    "AWAITING_CHANGE_CONFIRMATION": ["APPROVED_CHANGES", "IDLE", "ERROR"],
    "APPROVED_CHANGES": ["AWAITING_CONTENT_CONFIRMATION", "ERROR"],
    "AWAITING_CONTENT_CONFIRMATION": ["APPROVED_CONTENT", "IDLE", "ERROR"],
    "APPROVED_CONTENT": ["APPLIED", "ERROR"],
    "APPLIED": ["DRIFT_REPORTED", "ERROR"],
    "DRIFT_REPORTED": ["IDLE", "ERROR"],
    "ERROR": ["IDLE"]
}


REQUIRED_FIELDS = {
    "IDLE": [],
    "AWAITING_CHANGE_CONFIRMATION": ["detected_changes", "current_commit"],
    "APPROVED_CHANGES": ["detected_changes", "approved_changes"],
    "AWAITING_CONTENT_CONFIRMATION": ["approved_changes", "generated_content"],
    "APPROVED_CONTENT": ["approved_changes", "generated_content", "approved_content"],
    "APPLIED": ["approved_content", "current_commit"],
    "DRIFT_REPORTED": [],
    "ERROR": ["error_message"]
}


class SessionManager:

    def __init__(self):
        self.session = self._load_or_initialize()

    # -------------------------
    # Core Load / Save
    # -------------------------

    def _load_or_initialize(self) -> Dict[str, Any]:
        if not os.path.exists(SESSION_FILE):
            session = self._default_session()
            self._write(session)
            return session

        with open(SESSION_FILE, "r") as f:
            return json.load(f)

    def _default_session(self) -> Dict[str, Any]:
        return {
            "phase": "IDLE",
            "detected_changes": None,
            "approved_changes": None,
            "generated_content": None,
            "approved_content": None,
            "last_processed_commit": self._read_commit_file(),
            "current_commit": None,
            "error_message": None,
            "created_at": self._now(),
            "updated_at": self._now()
        }

    def _write(self, session: Dict[str, Any]):
        session["updated_at"] = self._now()
        tmp_file = SESSION_FILE + ".tmp"
        with open(tmp_file, "w") as f:
            json.dump(session, f, indent=2)
        os.replace(tmp_file, SESSION_FILE)

    # -------------------------
    # State Transition Logic
    # -------------------------

    def transition(self, next_state: str):
        current = self.session["phase"]

        if next_state not in VALID_STATES:
            raise Exception(f"Invalid state: {next_state}")

        if next_state not in VALID_TRANSITIONS[current]:
            raise Exception(f"Illegal transition: {current} → {next_state}")

        self.session["phase"] = next_state
        self._validate_required_fields(next_state)
        self._write(self.session)

    def _validate_required_fields(self, phase: str):
        required = REQUIRED_FIELDS.get(phase, [])
        for field in required:
            if not self.session.get(field):
                raise Exception(f"Missing required field '{field}' for phase '{phase}'")

    # -------------------------
    # Data Update Helpers
    # -------------------------

    def update_fields(self, updates: Dict[str, Any]):
        for k, v in updates.items():
            self.session[k] = v
        self._write(self.session)

    # -------------------------
    # Commit Integrity
    # -------------------------

    def set_current_commit(self):
        self.session["current_commit"] = self._get_head_commit()
        self._write(self.session)

    def verify_commit_unchanged(self):
        current_head = self._get_head_commit()
        if current_head != self.session.get("current_commit"):
            self._set_error("Repository changed during update session.")
            raise Exception("Repository changed during update session.")

    def finalize_commit(self):
        commit = self.session.get("current_commit")
        with open(COMMIT_FILE, "w") as f:
            f.write(commit)

        self.session["last_processed_commit"] = commit
        self._write(self.session)

    # -------------------------
    # Error Handling
    # -------------------------

    def _set_error(self, message: str):
        self.session["phase"] = "ERROR"
        self.session["error_message"] = message
        self._write(self.session)

    def reset(self):
        self.session = self._default_session()
        self._write(self.session)

    # -------------------------
    # Utilities
    # -------------------------

    def _get_head_commit(self) -> str:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).decode().strip()

    def _read_commit_file(self) -> str:
        if not os.path.exists(COMMIT_FILE):
            return self._get_head_commit()
        with open(COMMIT_FILE, "r") as f:
            return f.read().strip()

    def _now(self) -> str:
        return datetime.utcnow().isoformat() + "Z"