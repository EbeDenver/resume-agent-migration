from typing import Any
from datetime import datetime, timezone
from resume_agent.graph.state import AgentState
from resume_agent.models.job import GeneratedDocuments

def generate_docs_node(state: AgentState, llm_service: Any = None, docs_service: Any = None) -> AgentState:
    """Generates analysis, resume, and cover letter docs for the current job."""
    jobs = state.get("jobs", [])
    idx = state.get("current_job_index", 0)
    
    if idx >= len(jobs):
        return state
        
    job_run = jobs[idx]
    
    if job_run.status == "error":
        return state
        
    job_run.status = "generating"
    
    config = state.get("config", {})
    candidate_name = config.get("candidate_name", "Candidate Name")
    analyses_folder_id = config.get("job_analyses_folder_id")
    resumes_folder_id = config.get("generated_resumes_folder_id")
    cover_letters_folder_id = config.get("cover_letters_folder_id")
    
    company = job_run.posting.company
    job_title = job_run.posting.job_title
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    analysis_doc_title = f"Analysis — {company} — {job_title} — {date_str}"
    resume_doc_title = f"{candidate_name} — {company} — {job_title} — Resume"
    cl_doc_title = f"Cover Letter — {candidate_name} — {company} — {job_title} — {date_str}"
    
    docs = GeneratedDocuments()
    
    if docs_service and llm_service:
        try:
            # 1. Analysis Doc
            analysis_content = f"Fit Band: {job_run.analysis.fit_band}\nScore: {job_run.analysis.match_score}\n\n{job_run.analysis.fit_summary}"
            analysis_url = docs_service.create_document(
                title=analysis_doc_title,
                content=analysis_content,
                folder_id=analyses_folder_id
            )
            docs.analysis_doc_url = analysis_url
            
            # 2. Curated Resume
            # In a full implementation, LLM would generate the tailored content here.
            # Applying styling spec: Strict #17365D navy headers/accent styling.
            resume_content = "Tailored Resume Content"
            resume_url = docs_service.create_document(
                title=resume_doc_title,
                content=resume_content,
                folder_id=resumes_folder_id,
                styling={"header_color": "#17365D"}
            )
            docs.resume_doc_url = resume_url
            
            # 3. Cover Letter
            # 4 paragraphs, 250-350 words, #17365D header.
            cl_content = "Cover Letter Content - 4 paragraphs"
            cl_url = docs_service.create_document(
                title=cl_doc_title,
                content=cl_content,
                folder_id=cover_letters_folder_id,
                styling={"header_color": "#17365D"}
            )
            docs.cover_letter_doc_url = cl_url
            
        except Exception as e:
            job_run.status = "error"
            job_run.error = f"Doc generation failed: {str(e)}"
    else:
        # Mocking for absence of services
        docs.analysis_doc_url = f"mock://{analysis_doc_title.replace(' ', '_')}"
        docs.resume_doc_url = f"mock://{resume_doc_title.replace(' ', '_')}"
        docs.cover_letter_doc_url = f"mock://{cl_doc_title.replace(' ', '_')}"

    if not job_run.error:
        job_run.documents = docs

    jobs[idx] = job_run
    state["jobs"] = jobs
    
    return state
