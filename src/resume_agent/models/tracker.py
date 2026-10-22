"""Pydantic model for a Job Tracker row."""
import datetime
import zoneinfo
from typing import Literal, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from resume_agent.models.job import JobRun

class TrackerRow(BaseModel):
    """One row in the Job Tracker Google Sheet (columns A-N)."""
    model_config = {'frozen': False}

    date: str                     # YYYY-MM-DD HH:MM (America/Denver)
    company: str
    job_title: str
    job_url: str
    match_score: int
    interview_probability: int
    matched_skills: str           # Comma-separated
    missing_skills: str           # Comma-separated
    resume_link: str = ''
    cover_letter_link: str = ''
    analysis_link: str = ''
    status: Literal['Generated', 'Partial', 'Error'] = 'Generated'
    run_notes: str = ''
    interaction_url: str = ''

    def to_sheets_row(self) -> list[str]:
        """Convert to a list of strings for Google Sheets append."""
        return [
            self.date,
            self.company,
            self.job_title,
            self.job_url,
            str(self.match_score),
            str(self.interview_probability),
            self.matched_skills,
            self.missing_skills,
            self.resume_link,
            self.cover_letter_link,
            self.analysis_link,
            self.status,
            self.run_notes,
            self.interaction_url
        ]

    @classmethod
    def from_job_run(cls, job_run: 'JobRun', interaction_url: str = '') -> 'TrackerRow':
        """Create a TrackerRow from a completed JobRun."""
        # Generate date in America/Denver
        now = datetime.datetime.now(zoneinfo.ZoneInfo('America/Denver'))
        date_str = now.strftime('%Y-%m-%d %H:%M')

        match_score = 0
        interview_probability = 0
        matched_skills = ""
        missing_skills = ""
        analysis_link = ""
        resume_link = ""
        cover_letter_link = ""

        if job_run.analysis:
            match_score = job_run.analysis.match_score
            interview_probability = job_run.analysis.interview_probability
            matched_skills = ", ".join(sm.skill for sm in job_run.analysis.matched_skills)
            missing_skills = ", ".join(sm.skill for sm in job_run.analysis.missing_skills)

        if job_run.documents:
            analysis_link = job_run.documents.analysis_doc_url or ""
            resume_link = job_run.documents.resume_doc_url or ""
            cover_letter_link = job_run.documents.cover_letter_doc_url or ""

        status_mapping: dict[str, Literal['Generated', 'Partial', 'Error']] = {
            'completed': 'Generated',
            'error': 'Error'
        }
        status_val = status_mapping.get(job_run.status, 'Partial')

        return cls(
            date=date_str,
            company=job_run.posting.company,
            job_title=job_run.posting.job_title,
            job_url=str(job_run.posting.job_url),
            match_score=match_score,
            interview_probability=interview_probability,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            resume_link=resume_link,
            cover_letter_link=cover_letter_link,
            analysis_link=analysis_link,
            status=status_val,
            run_notes=job_run.run_notes,
            interaction_url=interaction_url
        )
