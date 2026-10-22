"""Tests for Pydantic data models (job, tracker, formatting)."""
import pytest
from datetime import datetime
from pydantic import ValidationError

from resume_agent.schemas import (
    SkillMatch, JobAnalysis, JobPosting, JobRun, TrackerRow, 
    GeneratedDocuments, ColorPalette, Typography, PageLayout
)

def test_skill_match_creation():
    """Test SkillMatch creation and validation"""
    match = SkillMatch(skill="Python", required=True, match_level="strong", notes="Used daily")
    assert match.skill == "Python"
    assert match.match_level == "strong"

def test_job_analysis_fit_band():
    """Test JobAnalysis fit_band computation for each band (strong/solid/partial/weak/poor)"""
    bands = ["strong", "solid", "partial", "weak", "poor"]
    for band in bands:
        analysis = JobAnalysis(
            score=95,
            fit_band=band,
            strengths=["Python"],
            weaknesses=[],
            missing_requirements=[],
            key_skills=[]
        )
        assert analysis.fit_band == band

def test_job_analysis_score_validation():
    """Test JobAnalysis score validation (ge=0, le=100 boundaries)"""
    with pytest.raises(ValidationError):
        JobAnalysis(
            score=105,
            fit_band="strong",
            strengths=[],
            weaknesses=[],
            missing_requirements=[],
            key_skills=[]
        )
    with pytest.raises(ValidationError):
        JobAnalysis(
            score=-5,
            fit_band="strong",
            strengths=[],
            weaknesses=[],
            missing_requirements=[],
            key_skills=[]
        )

def test_job_posting_minimal_data():
    """Test JobPosting with minimal data"""
    job = JobPosting(title="Software Engineer", company="Google", url="https://google.com/jobs/1")
    assert job.title == "Software Engineer"
    assert job.company == "Google"
    assert job.url == "https://google.com/jobs/1"

def test_job_posting_full_data():
    """Test JobPosting with full data"""
    job = JobPosting(
        title="Software Engineer",
        company="Google",
        url="https://google.com/jobs/1",
        description="Write code",
        location="Remote",
        salary_range="$100k-$150k"
    )
    assert job.location == "Remote"
    assert job.salary_range == "$100k-$150k"

def test_job_run_status_transitions():
    """Test JobRun status transitions"""
    job = JobPosting(title="Dev", company="Test", url="http://test.com")
    run = JobRun(job=job, status="pending")
    assert run.status == "pending"
    run.status = "analyzing"
    assert run.status == "analyzing"

def test_tracker_row_to_sheets_row():
    """Test TrackerRow.to_sheets_row() returns correct 14-element list"""
    row = TrackerRow(
        date="2023-10-10",
        company="Google",
        title="Software Engineer",
        url="http://example.com",
        status="Applied"
    )
    sheets_row = row.to_sheets_row()
    assert isinstance(sheets_row, list)
    assert len(sheets_row) == 14

def test_tracker_row_from_job_run():
    """Test TrackerRow.from_job_run() correctly maps fields"""
    job = JobPosting(title="Dev", company="Test", url="http://test.com")
    run = JobRun(job=job, status="completed")
    row = TrackerRow.from_job_run(run)
    assert row.company == "Test"
    assert row.title == "Dev"

def test_formatting_constants_color_palette():
    """Test formatting constants are correct (ColorPalette)"""
    assert hasattr(ColorPalette, "NAVY")
    assert ColorPalette.NAVY == "#17365D"

def test_formatting_constants_typography():
    """Test formatting constants are correct (Typography)"""
    assert hasattr(Typography, "BODY_TEXT")
    assert Typography.BODY_TEXT == "#1F1F1F"

def test_formatting_constants_page_layout():
    """Test formatting constants are correct (PageLayout)"""
    assert hasattr(PageLayout, "MARGINS")

def test_generated_documents_defaults():
    """Test GeneratedDocuments defaults to all None"""
    docs = GeneratedDocuments()
    assert docs.resume_url is None
    assert docs.cover_letter_url is None
    assert docs.analysis_doc_url is None
