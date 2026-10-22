from typing import Any
from resume_agent.graph.state import AgentState
from resume_agent.models.job import JobAnalysis

def analyze_job_node(state: AgentState, llm_service: Any = None) -> AgentState:
    """Analyzes JD against master resume using weighted rubric."""
    jobs = state.get("jobs", [])
    idx = state.get("current_job_index", 0)
    
    if idx >= len(jobs):
        return state
        
    job_run = jobs[idx]
    
    # Skip if already failed in resolution
    if job_run.status == "error":
        return state
        
    job_run.status = "analyzing"
    master_resume = state.get("master_resume_text", "")
    jd_text = job_run.posting.jd_text
    
    system_prompt = (
        "You are an expert technical recruiter analyzing a candidate's fit for a role. "
        "STRICT NO FABRICATION CONSTRAINT: Do not invent or assume any experience, skills, "
        "or qualifications that are not explicitly stated in the master resume. "
        "Analyze the provided Job Description against the Master Resume using this EXACT weighted rubric:\n"
        "- Must-have skills/requirements: 40%\n"
        "- Relevant experience/domain: 25%\n"
        "- Tools/stack/methods: 15%\n"
        "- Education/certs: 10%\n"
        "- Nice-to-have/extras: 10%\n\n"
        "Output MUST be structured according to the JobAnalysis schema."
    )
    
    user_prompt = f"Master Resume:\n{master_resume}\n\nJob Description:\n{jd_text}"
    
    if llm_service:
        try:
            analysis_result = llm_service.generate_structured(
                model_class=JobAnalysis,
                system_prompt=system_prompt,
                user_prompt=user_prompt
            )
            job_run.analysis = analysis_result
        except Exception as e:
            job_run.status = "error"
            job_run.error = f"Analysis failed: {str(e)}"
    else:
        # Dummy fallback
        job_run.error = "No LLM service provided."
        job_run.status = "error"
        
    jobs[idx] = job_run
    state["jobs"] = jobs
    
    return state
