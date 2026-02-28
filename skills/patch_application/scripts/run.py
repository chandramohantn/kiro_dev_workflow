from core.session_manager import SessionManager
from patch_engine import apply_patch

def run_patch_application():
    sm = SessionManager()

    if sm.session["phase"] != "APPROVED_CONTENT":
        return

    sm.verify_commit_unchanged()

    approved_content = sm.session["approved_content"]

    apply_patch(approved_content)

    sm.finalize_commit()

    sm.transition("APPLIED")