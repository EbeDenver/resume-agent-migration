"""Pydantic v2 models for the job pipeline data."""
from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, HttpUrl, model_validator

class SkillMatch(BaseModel):
    """A single skill/requirement match against the master resume."""
    model_config = {'frozen': False}

    skill: str                                    # The skill/requirement from the JD
    category: Literal['matched', 'partial', 'missing']
    evidence_label: Literal[
        'direct_evidence',          # Professional/client/production
        'transferable_evidence',    # Adjacent experience
        'graduate_portfolio',       # Academic/graduate project
        'personal_project',         # Personal work
        'honest_learning_bridge',   # No direct support + learning plan
        'none'                      # Missing, no bridge
    ]
    evidence_notes: str = ''                      # Resume bullet/section reference
    is_must_have: bool = False                    # Whether JD marks it as required

class JobAnalysis(BaseModel):
    """Complete analysis results for one job."""
    model_config = {'frozen': False}

    match_score: int = Field(ge=0, le=100)        # Weighted rubric score
    interview_probability: int = Field(ge=0, le=100)
    interview_rationale: str                      # 2-4 sentence rationale
    fit_summary: str                              # 4-8 sentence summary
    matched_skills: list[SkillMatch]
    partial_skills: list[SkillMatch]
    missing_skills: list[SkillMatch]
    fit_band: Literal['strong', 'solid', 'partial', 'weak', 'poor'] = 'weak'  # Computed from match_score

    @model_validator(mode='after')
    def compute_fit_band(self) -> 'JobAnalysis':
        # 85-100 strong, 70-84 solid, 55-69 partial, 40-54 weak, <40 poor
        if self.match_score >= 85:
            self.fit_band = 'strong'
        elif self.match_score >= 70:
            self.fit_band = 'solid'
        elif self.match_score >= 55:
            self.fit_band = 'partial'
        elif self.match_score >= 40:
            self.fit_band = 'weak'
        else:
            self.fit_band = 'poor'
        return self

class JobPosting(BaseModel):
    """Parsed job posting data."""
    model_config = {'frozen': False}

    company: str
    job_title: str
    job_url: HttpUrl | str
    jd_text: str                                  # Full cleaned job description
    location: str | None = None
    employment_type: str | None = None
    raw_html: str | None = None                   # Original fetched HTML (for debugging)
    fetch_error: str | None = None                # Error if fetch failed

class GeneratedDocuments(BaseModel):
    """URLs of all generated Google Docs for a job."""
    model_config = {'frozen': False}

    analysis_doc_url: str | None = None
    resume_doc_url: str | None = None
    cover_letter_doc_url: str | None = None
    interview_prep_doc_url: str | None = None

class JobRun(BaseModel):
    """Complete state for one job through the entire pipeline."""
    model_config = {'frozen': False}

    posting: JobPosting
    analysis: JobAnalysis | None = None
    documents: GeneratedDocuments = Field(default_factory=GeneratedDocuments)
    status: Literal['pending', 'analyzing', 'generating', 'tracking', 'completed', 'partial', 'error'] = 'pending'
    run_notes: str = ''
    error: str | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
