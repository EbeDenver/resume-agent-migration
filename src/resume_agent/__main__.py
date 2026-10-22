"""CLI module execution entrypoint for python -m resume_agent."""
import sys
from pathlib import Path

def main():
    try:
        from resume_agent.cli import app
        app()
    except (ImportError, ModuleNotFoundError) as err:
        # Fallback to zero-dependency unified runner
        root_dir = Path(__file__).resolve().parent.parent.parent
        run_agent_script = root_dir / "run_agent.py"
        if run_agent_script.exists():
            import runpy
            runpy.run_path(str(run_agent_script), run_name="__main__")
        else:
            raise err

if __name__ == "__main__":
    main()

