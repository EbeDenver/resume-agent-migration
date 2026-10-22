"""Node for generating comprehensive interview preparation document."""

import datetime
from resume_agent.graph.state import AgentState

def interview_prep_node(state: AgentState, llm_service=None, docs_service=None, web_search_service=None) -> AgentState:
    """
    Researches company & domain and generates a 13-section deep interview prep document.
    Creates a Google Doc and saves its URL to the job run state.
    """
    current_job_index = state.get("current_job_index", 0)
    jobs = state.get("jobs", [])
    if not jobs or current_job_index >= len(jobs):
        return state
        
    current_job = jobs[current_job_index]
    company = current_job.posting.company
    job_title = current_job.posting.job_title
    
    # 1. Perform Web Search
    search_results = ""
    if web_search_service:
        try:
            query = f"{company} {job_title} recent news culture interview process"
            search_data = web_search_service.search(query)
            search_results = str(search_data)
        except Exception:
            search_results = "No recent specific data found."
            
    # 2. Generate content via LLM
    content = ""
    if llm_service:
        prompt = f"""
        Generate a 13-section deep interview prep package for the candidate applying to {job_title} at {company}.
        Use these formatting rules precisely:
        - Section titles MUST use canonical navy HTML color #17365D, e.g., <span style="color:#17365D; font-size:16pt; font-weight:bold;">Section Name</span>
        - Subsections MUST use green #008000
        - Bold labels MUST use blood orange #C00000
        
        Sections required:
        1) Role, Company & Sector Brief
        2) Candidate Fit Narrative & Gap Map
        3) 60-90s Elevator Pitch
        4) HR/Recruiter Q&A Bank
        5) Deep Technical & Strategy Q&A
        6) Challenge Q&A Bank (gaps, pushback, trade-offs)
        7) Verified STAR Story Bank (DOI FBMS, Acxiom, Muscato, DU AI)
        8) Questions to Ask Interviewer
        9) 30/60/90-Day Outline
        10) Compensation/Work-Auth/Location Guidance
        11) Interview-Day Checklist
        12) Curated Reading List (3-6 sources with direct URLs + takeaways)
        13) Formatting Instructions Acknowledgment
        
        Incorporate this research context:
        {search_results}
        
        Return the raw HTML or rich text compatible format.
        """
        try:
            content = llm_service.generate_text(prompt)
        except Exception as e:
            content = f"Failed to generate content: {str(e)}"
    else:
        content = "Interview prep content generation requires LLM service."
        
    # 3. Create Google Doc
    if docs_service:
        try:
            config = state.get("config", {})
            folder_id = config.get("job_analyses_folder_id", "")
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            doc_title = f"Interview Preparation — {company} — {job_title} — {date_str}"
            
            doc_url = docs_service.create_document(
                title=doc_title,
                content=content,
                folder_id=folder_id
            )
            current_job.documents.interview_prep_doc_url = doc_url
        except Exception as e:
            pass
            
    return state
