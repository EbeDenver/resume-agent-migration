from typing import TypedDict, Any
from resume_agent.models.job import JobRun

class AgentState(TypedDict):
    config: dict[str, Any]
    master_resume_text: str
    resume_instructions: str
    cover_letter_instructions: str
    raw_jobs_input: list[str]
    jobs: list[JobRun]
    current_job_index: int
    completed_jobs: list[dict[str, Any]]
    failed_jobs: list[dict[str, Any]]
    final_summary: str
    mode: str
    fact_finding_questions: list[str]
    user_fact_finding_answers: dict[str, str]
    fact_finding_completed: bool
