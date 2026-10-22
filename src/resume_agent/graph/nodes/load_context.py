"""Load Context Node.

Loads master resume text, structured MasterResumeModel, and instruction docs
from local disk (data/master_resume.md) or configured Google Docs.
"""
from pathlib import Path
from typing import Any
from resume_agent.graph.state import AgentState
from resume_agent.models.resume import MasterResumeModel

DEFAULT_MASTER_RESUME_PATH = Path("data/master_resume.md")

def load_context_node(state: AgentState, docs_service: Any = None) -> AgentState:
    """Load Master Resume and instructions into AgentState."""
    print("[node:load_context] Loading master resume & instructions context...")
    
    # 1. Load Master Resume text
    resume_text = ""
    if DEFAULT_MASTER_RESUME_PATH.exists():
        with open(DEFAULT_MASTER_RESUME_PATH, "r", encoding="utf-8") as f:
            resume_text = f.read()
    else:
        # Fallback to default MasterResumeModel
        model = MasterResumeModel(
            professional_summary=(
                "AI-first transformation and Program Analyst with 20+ years turning fragmented legacy "
                "environments into unified enterprise platforms across federal and financial sectors."
            ),
            core_competencies=[
                "AI-First Transformation Strategy", "AI Governance & Risk", "Unison PRISM",
                "Federal Acquisition (GS-13)", "RAG & Agentic Workflows", "ROI Modeling"
            ]
        )
        resume_text = model.to_full_markdown()

    state["master_resume_text"] = resume_text

    # 2. Load Resume Generation Instructions
    state["resume_instructions"] = (
        "Follow the approved DOL IT Analyst visual system: single-column layout, "
        "Cambria serif typography, canonical navy #17365D headers and headings, "
        "light blue #5B9BD5 employer text, dark charcoal #1F1F1F body text. "
        "Strict NO FABRICATION rule. Display University of Denver credential as: "
        "'Graduate Certificate, AI Strategy & Applications in IT : University of Denver' without dates."
    )

    # 3. Load Cover Letter Instructions
    state["cover_letter_instructions"] = (
        "Four-paragraph structure (~300 words target). 1) Gratitude & value prop, "
        "2) Strongest evidence, 3) Secondary evidence & sabbatical context, "
        "4) Contributing to team & feedback request. Strictly no fabrication."
    )

    print(f"[node:load_context] Master resume loaded ({len(resume_text)} chars).")
    return state
