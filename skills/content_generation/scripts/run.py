from core.session_manager import SessionManager

def run_content_generation(llm_callable):
    sm = SessionManager()

    if sm.session["phase"] != "APPROVED_CHANGES":
        return

    sm.verify_commit_unchanged()

    approved_changes = sm.session["approved_changes"]

    # Call LLM to generate AUTO blocks
    generated_content = llm_callable(approved_changes)

    sm.update_fields({
        "generated_content": generated_content
    })

    sm.transition("AWAITING_CONTENT_CONFIRMATION")