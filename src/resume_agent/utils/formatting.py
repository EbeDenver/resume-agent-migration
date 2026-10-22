"""Document naming, text sanitization, and formatting utilities."""
import re
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Any

TZ = ZoneInfo('America/Denver')


def sanitize_filename(name: str) -> str:
    """Remove characters unsafe for Drive/filesystem: \\ / : * ? \" < > |"""
    return re.sub(r'[\\/:*?"<>|]', '', name).strip()


def now_denver() -> datetime:
    """Current datetime in America/Denver."""
    return datetime.now(TZ)


def format_tracker_date(dt: datetime | None = None) -> str:
    """Format as YYYY-MM-DD HH:MM for tracker."""
    if dt is None:
        dt = now_denver()
    return dt.strftime('%Y-%m-%d %H:%M')


def analysis_doc_name(company: str, title: str, date: datetime | None = None) -> str:
    """Analysis — {Company} — {Job Title} — {YYYY-MM-DD}"""
    if date is None:
        date = now_denver()
    date_str = date.strftime('%Y-%m-%d')
    return f"Analysis — {company} — {title} — {date_str}"


def resume_doc_name(candidate: str, company: str, title: str) -> str:
    """{Candidate Name} — {Company} — {Job Title} — Resume"""
    return f"{candidate} — {company} — {title} — Resume"


def cover_letter_doc_name(candidate: str, company: str, title: str, date: datetime | None = None) -> str:
    """Cover Letter — {Candidate Name} — {Company} — {Job Title} — {YYYY-MM-DD}"""
    if date is None:
        date = now_denver()
    date_str = date.strftime('%Y-%m-%d')
    return f"Cover Letter — {candidate} — {company} — {title} — {date_str}"


def interview_prep_doc_name(company: str, title: str, date: datetime | None = None) -> str:
    """Interview Preparation — {Company} — {Job Title} — {YYYY-MM-DD}"""
    if date is None:
        date = now_denver()
    date_str = date.strftime('%Y-%m-%d')
    return f"Interview Preparation — {company} — {title} — {date_str}"


def extract_doc_id(url: str) -> str:
    """Extract Google Doc/Sheet ID from a URL."""
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
    if match:
        return match.group(1)
    return url


def extract_spreadsheet_id(url: str) -> str:
    """Extract spreadsheet ID from a Google Sheets URL."""
    return extract_doc_id(url)


def skills_to_csv(skills: list[Any]) -> str:
    """Convert a list of SkillMatch objects to comma-separated skill names."""
    names = []
    for skill in skills:
        if hasattr(skill, 'name'):
            names.append(skill.name)
        elif hasattr(skill, 'skill'):
            names.append(skill.skill)
        elif isinstance(skill, dict) and 'name' in skill:
            names.append(skill['name'])
        else:
            names.append(str(skill))
    return ", ".join(names)
