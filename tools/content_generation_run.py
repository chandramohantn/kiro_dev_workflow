from skills.content_generation.scripts.run import run_content_generation
from core.session_manager import SessionManager

def run():
    # LLM invocation wrapper
    run_content_generation(llm_callable=None)