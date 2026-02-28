from core.session_manager import SessionManager

def run_drift_detection(llm_callable):
    sm = SessionManager()

    if sm.session["phase"] != "APPLIED":
        return

    drift_json = llm_callable()

    # Patch drift_report.md deterministically here

    sm.transition("DRIFT_REPORTED")
    sm.transition("IDLE")