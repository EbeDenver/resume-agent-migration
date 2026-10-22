from typing import Any
import re
from datetime import datetime, timezone
from resume_agent.graph.state import AgentState
from resume_agent.models.job import JobRun, JobPosting

def resolve_jobs_node(state: AgentState, scraper_service: Any = None) -> AgentState:
    """Parses raw input, fetches JDs, and populates initialized JobRun objects."""
    raw_inputs = state.get("raw_jobs_input", [])
    jobs = state.get("jobs", [])
    
    seen_urls = set()
    
    for input_item in raw_inputs:
        input_item = input_item.strip()
        if not input_item:
            continue
            
        # Basic URL detection
        is_url = input_item.startswith("http://") or input_item.startswith("https://")
        
        if is_url:
            if input_item in seen_urls:
                continue
            seen_urls.add(input_item)
            
            jd_text = ""
            company = "Unknown Company"
            job_title = "Unknown Title"
            fetch_error = None
            status: str = "pending"
            
            if scraper_service:
                try:
                    scraped_data = scraper_service.scrape_job(input_item)
                    jd_text = scraped_data.get("description", "")
                    company = scraped_data.get("company", company)
                    job_title = scraped_data.get("title", job_title)
                except Exception as e:
                    fetch_error = f"Failed to fetch JD from URL: {str(e)}"
                    status = "error"
            else:
                fetch_error = "No scraper service provided."
                status = "error"
                
            posting = JobPosting(
                company=company,
                job_title=job_title,
                job_url=input_item,
                jd_text=jd_text,
                fetch_error=fetch_error
            )
            
            job_run = JobRun(
                posting=posting,
                status=status,
                error=fetch_error,
                started_at=datetime.now(timezone.utc)
            )
            jobs.append(job_run)
        else:
            # Assume raw text or search query
            # For simplicity, treating as raw pasted JD here
            posting = JobPosting(
                company="Unknown Company",
                job_title="Provided JD",
                job_url="raw-text",
                jd_text=input_item
            )
            job_run = JobRun(
                posting=posting,
                status="pending",
                started_at=datetime.now(timezone.utc)
            )
            jobs.append(job_run)

    state["jobs"] = jobs
    if "current_job_index" not in state or state["current_job_index"] is None:
        state["current_job_index"] = 0
        
    return state
