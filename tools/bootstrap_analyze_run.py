# .kiro/tools/bootstrap_analyze_run.py

from skills.bootstrap_analyze.scripts.run import run as analyze_run


def run(generated_content: dict):
    """
    Tool wrapper for bootstrap analyze phase.

    The LLM executes SKILL.md and produces structured JSON.
    That JSON is passed here as generated_content.
    """

    try:
        analyze_run(generated_content)

    except Exception as e:
        print("\nBootstrap analyze failed.")
        print(str(e))
        raise e