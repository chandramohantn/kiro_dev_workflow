from skills.patch_application.scripts.run import run_patch_application
from core.session_manager import SessionManager

def run():
    # LLM invocation wrapper
    run_patch_application(llm_callable=None)