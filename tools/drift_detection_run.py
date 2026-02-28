from skills.drift_detection.scripts.run import run_drift_detection
from core.session_manager import SessionManager

def run():
    # LLM invocation wrapper
    run_drift_detection(llm_callable=None)