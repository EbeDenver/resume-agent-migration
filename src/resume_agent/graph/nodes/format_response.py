from resume_agent.graph.state import AgentState

def format_response_node(state: AgentState) -> AgentState:
    """Builds a markdown summary table of all processed jobs."""
    jobs = state.get("jobs", [])
    config = state.get("config", {})
    tracker_url = config.get("job_tracker_url", "#")
    
    completed = []
    failed = []
    
    md_lines = [
        "## Job Processing Summary",
        f"**Total Jobs Processed:** {len(jobs)}",
        f"**[View Job Tracker]({tracker_url})**\n",
        "### Completed Jobs",
        "| Company | Title | Match Score | Interview Prob. | Missing Skills | Documents |",
        "|---|---|---|---|---|---|"
    ]
    
    for job in jobs:
        if job.status in ("completed", "partial"):
            score = job.analysis.match_score if job.analysis else "N/A"
            prob = job.analysis.interview_probability if job.analysis else "N/A"
            
            missing = ""
            if job.analysis and job.analysis.missing_skills:
                missing = ", ".join([sm.skill for sm in job.analysis.missing_skills])
            
            docs = []
            if job.documents:
                if job.documents.analysis_doc_url:
                    docs.append(f"[Analysis]({job.documents.analysis_doc_url})")
                if job.documents.resume_doc_url:
                    docs.append(f"[Resume]({job.documents.resume_doc_url})")
                if job.documents.cover_letter_doc_url:
                    docs.append(f"[Cover Letter]({job.documents.cover_letter_doc_url})")
            docs_str = " <br> ".join(docs) if docs else "None"
            
            md_lines.append(f"| {job.posting.company} | {job.posting.job_title} | {score} | {prob} | {missing} | {docs_str} |")
            
            completed.append({"company": job.posting.company, "title": job.posting.job_title, "status": job.status})
        else:
            failed.append({"company": job.posting.company, "title": job.posting.job_title, "error": job.error})
            
    if failed:
        md_lines.append("\n### Failed Jobs")
        md_lines.append("| Company | Title | Error |")
        md_lines.append("|---|---|---|")
        for f in failed:
            md_lines.append(f"| {f['company']} | {f['title']} | {f['error']} |")
            
    state["final_summary"] = "\n".join(md_lines)
    state["completed_jobs"] = completed
    state["failed_jobs"] = failed
    
    return state
