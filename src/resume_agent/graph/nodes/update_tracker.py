from typing import Any
from datetime import datetime, timezone
from resume_agent.graph.state import AgentState
from resume_agent.models.tracker import TrackerRow

def update_tracker_node(state: AgentState, sheets_service: Any = None) -> AgentState:
    """Appends job results to the Google Sheet tracker."""
    jobs = state.get("jobs", [])
    idx = state.get("current_job_index", 0)
    
    if idx >= len(jobs):
        return state
        
    job_run = jobs[idx]
    
    if job_run.status == "error":
        # Keep status as error
        pass
    else:
        # Assuming successful generation if it didn't error out earlier
        job_run.status = "completed"
        
    job_run.completed_at = datetime.now(timezone.utc)
        
    if sheets_service:
        try:
            tracker_row = TrackerRow.from_job_run(job_run)
            sheets_service.append_row(
                tab_name="Tracker",
                row_data=tracker_row.to_sheets_row()
            )
        except Exception as e:
            # Revert to error if tracking fails
            job_run.status = "error"
            job_run.error = f"Failed to update tracker: {str(e)}"
    
    jobs[idx] = job_run
    state["jobs"] = jobs
    
    # Move to next job or finalize
    state["current_job_index"] = idx + 1
    
    return state
