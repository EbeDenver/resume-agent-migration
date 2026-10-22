"""Tests for document naming and formatting utilities."""
import pytest
from datetime import datetime

from resume_agent.schemas import SkillMatch
from resume_agent.formatting import (
    sanitize_filename,
    analysis_doc_name,
    resume_doc_name,
    cover_letter_doc_name,
    interview_prep_doc_name,
    extract_doc_id,
    extract_spreadsheet_id,
    format_tracker_date,
    skills_to_csv
)

def test_sanitize_filename_removes_unsafe_chars():
    """Test sanitize_filename removes unsafe chars"""
    assert sanitize_filename("Job/Title @Company: Role") == "JobTitle Company Role"
    assert sanitize_filename("Hello*World?") == "HelloWorld"

def test_sanitize_filename_preserves_safe_chars():
    """Test sanitize_filename preserves safe chars"""
    assert sanitize_filename("Software_Engineer-123") == "Software_Engineer-123"
    assert sanitize_filename("Sr. Dev") == "Sr. Dev"

def test_analysis_doc_name():
    """Test analysis_doc_name format"""
    name = analysis_doc_name("Google", "Software Engineer")
    assert "Google" in name
    assert "Software Engineer" in name
    assert "Analysis" in name

def test_resume_doc_name():
    """Test resume_doc_name format"""
    name = resume_doc_name("Google", "Software Engineer")
    assert "Google" in name
    assert "Software Engineer" in name
    assert "Resume" in name

def test_cover_letter_doc_name():
    """Test cover_letter_doc_name format"""
    name = cover_letter_doc_name("Google", "Software Engineer")
    assert "Google" in name
    assert "Cover Letter" in name

def test_interview_prep_doc_name():
    """Test interview_prep_doc_name format"""
    name = interview_prep_doc_name("Google", "Software Engineer")
    assert "Google" in name
    assert "Interview Prep" in name

def test_extract_doc_id():
    """Test extract_doc_id from various Google URLs"""
    url1 = "https://docs.google.com/document/d/1csBfzkxUor6K-oHX24_rKcI159BaTahHn3wULBZSIS8/edit"
    url2 = "https://docs.google.com/document/d/1csBfzkxUor6K-oHX24_rKcI159BaTahHn3wULBZSIS8/"
    assert extract_doc_id(url1) == "1csBfzkxUor6K-oHX24_rKcI159BaTahHn3wULBZSIS8"
    assert extract_doc_id(url2) == "1csBfzkxUor6K-oHX24_rKcI159BaTahHn3wULBZSIS8"

def test_extract_spreadsheet_id():
    """Test extract_spreadsheet_id"""
    url = "https://docs.google.com/spreadsheets/d/1fXSxbi49_JY2HzKXTdPXpAOpJkNqwEcDuK8qp-uh12Y/edit"
    assert extract_spreadsheet_id(url) == "1fXSxbi49_JY2HzKXTdPXpAOpJkNqwEcDuK8qp-uh12Y"

def test_format_tracker_date():
    """Test format_tracker_date format"""
    dt = datetime(2023, 10, 5)
    formatted = format_tracker_date(dt)
    # Testing for common formats like MM/DD/YYYY
    assert formatted in ["10/05/2023", "2023-10-05", "10/5/2023"]

def test_skills_to_csv():
    """Test skills_to_csv with SkillMatch objects"""
    skills = [
        SkillMatch(skill="Python", required=True, match_level="strong", notes=""),
        SkillMatch(skill="AWS", required=False, match_level="solid", notes="")
    ]
    csv_str = skills_to_csv(skills)
    assert "Python" in csv_str
    assert "AWS" in csv_str
