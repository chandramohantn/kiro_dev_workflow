from skills.change_detection.scripts.run import run_change_detection
from core.session_manager import SessionManager

def run():
    # LLM invocation wrapper
    run_change_detection(llm_callable=None)