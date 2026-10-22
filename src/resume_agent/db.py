"""SQLite Database Manager for Job Intelligence & Search Findings.

Provides persistent, local deduplication and tracking for all discovered jobs.
Zero external dependencies (uses standard library sqlite3).
Enforces unique constraints on job_key to prevent duplicate entries across runs,
while preserving user interaction status (applied, deleted) and timestamps.
"""

import sqlite3
import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = PROJECT_ROOT / "data" / "jobs.db"

def get_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Return a configured connection with row dictionary access."""
    target = db_path or DB_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(target))
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: Optional[Path] = None):
    """Initialize the schema and indexes."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_key TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        employer TEXT NOT NULL,
        department TEXT,
        category TEXT,
        location TEXT,
        location_type TEXT,
        salary_band TEXT,
        salary_max INTEGER,
        match_score INTEGER NOT NULL,
        interview_prob INTEGER NOT NULL,
        fit_band TEXT,
        match_tier TEXT NOT NULL,
        linkedin_url TEXT,
        direct_url TEXT,
        search_landing_url TEXT,
        why_matched TEXT,
        top_skills TEXT,
        gap_bridge TEXT,
        package_action TEXT,
        output_dir TEXT,
        source TEXT,
        source_label TEXT,
        posted_date TEXT,
        is_reposted INTEGER DEFAULT 0,
        reposted_date TEXT,
        agent_executed_at TEXT,
        status TEXT DEFAULT 'active',
        applied_at TEXT,
        first_seen_at TEXT,
        last_seen_at TEXT
    );
    """)
    # Check existing columns and alter table if needed (safe migrations)
    cursor.execute("PRAGMA table_info(jobs);")
    existing_cols = {row[1] for row in cursor.fetchall()}
    for col_name, col_type in [
        ("source", "TEXT"),
        ("source_label", "TEXT"),
        ("posted_date", "TEXT"),
        ("is_reposted", "INTEGER DEFAULT 0"),
        ("reposted_date", "TEXT"),
        ("agent_executed_at", "TEXT")
    ]:
        if col_name not in existing_cols:
            cursor.execute(f"ALTER TABLE jobs ADD COLUMN {col_name} {col_type};")

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_score ON jobs(match_score DESC);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_tier ON jobs(match_tier);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_category ON jobs(category);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_source ON jobs(source);")
    conn.commit()
    conn.close()

def compute_tier(score: int) -> str:
    """Map match score (0-100) to its increment tier."""
    if score >= 90:
        return "90-100"
    elif score >= 80:
        return "80-89"
    elif score >= 70:
        return "70-79"
    elif score >= 60:
        return "60-69"
    elif score >= 50:
        return "50-59"
    else:
        return "under-50"

def upsert_job(job_data: Dict[str, Any], db_path: Optional[Path] = None) -> Dict[str, Any]:
    """Insert or update a job.
    
    If job already exists (by job_key):
    - Preserves existing user status ('applied', 'deleted') and applied_at.
    - Updates last_seen_at and refreshed scores/details.
    - Avoids repetition/duplicate records!
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    now_iso = datetime.now().isoformat()

    job_key = job_data.get("job_key") or job_data.get("direct_url") or job_data.get("linkedin_url")
    if not job_key:
        job_key = f"{job_data.get('employer', '')}:{job_data.get('title', '')}".strip()

    top_skills_val = job_data.get("top_skills", [])
    if isinstance(top_skills_val, list):
        top_skills_str = json.dumps(top_skills_val)
    else:
        top_skills_str = str(top_skills_val)

    match_score = int(job_data.get("match_score", 0))
    match_tier = job_data.get("match_tier") or compute_tier(match_score)

    cursor.execute("SELECT id, status, applied_at, first_seen_at FROM jobs WHERE job_key = ?", (job_key,))
    existing = cursor.fetchone()

    source = job_data.get("source", "linkedin")
    source_label = job_data.get("source_label", "LinkedIn")
    posted_date = job_data.get("posted_date", "Recent")
    is_reposted = 1 if job_data.get("is_reposted") else 0
    reposted_date = job_data.get("reposted_date", None)
    agent_executed_at = job_data.get("agent_executed_at") or now_iso

    if existing:
        # Preserve user state
        status = existing["status"]
        applied_at = existing["applied_at"]
        first_seen_at = existing["first_seen_at"] or now_iso
        job_id = existing["id"]

        cursor.execute("""
            UPDATE jobs SET
                title = ?,
                employer = ?,
                department = ?,
                category = ?,
                location = ?,
                location_type = ?,
                salary_band = ?,
                salary_max = ?,
                match_score = ?,
                interview_prob = ?,
                fit_band = ?,
                match_tier = ?,
                source = ?,
                source_label = ?,
                posted_date = ?,
                is_reposted = ?,
                reposted_date = ?,
                agent_executed_at = ?,
                linkedin_url = ?,
                direct_url = ?,
                search_landing_url = ?,
                why_matched = ?,
                top_skills = ?,
                gap_bridge = ?,
                package_action = ?,
                output_dir = ?,
                last_seen_at = ?
            WHERE id = ?
        """, (
            job_data.get("title", ""),
            job_data.get("employer", ""),
            job_data.get("department", ""),
            job_data.get("category", "ai_enablement"),
            job_data.get("location", ""),
            job_data.get("location_type", "remote"),
            job_data.get("salary_band", ""),
            int(job_data.get("salary_max", 0)),
            match_score,
            int(job_data.get("interview_prob", 0)),
            job_data.get("fit_band", "Strong Fit"),
            match_tier,
            source,
            source_label,
            posted_date,
            is_reposted,
            reposted_date,
            agent_executed_at,
            job_data.get("linkedin_url", ""),
            job_data.get("direct_url", ""),
            job_data.get("search_landing_url", ""),
            job_data.get("why_matched", ""),
            top_skills_str,
            job_data.get("gap_bridge", ""),
            job_data.get("package_action", ""),
            job_data.get("output_dir", ""),
            now_iso,
            job_id
        ))
        action_taken = "updated"
    else:
        status = job_data.get("status", "active")
        applied_at = job_data.get("applied_at", None)
        first_seen_at = now_iso

        cursor.execute("""
            INSERT INTO jobs (
                job_key, title, employer, department, category, location, location_type,
                salary_band, salary_max, match_score, interview_prob, fit_band, match_tier,
                source, source_label, posted_date, is_reposted, reposted_date, agent_executed_at,
                linkedin_url, direct_url, search_landing_url, why_matched, top_skills, gap_bridge,
                package_action, output_dir, status, applied_at, first_seen_at, last_seen_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job_key,
            job_data.get("title", ""),
            job_data.get("employer", ""),
            job_data.get("department", ""),
            job_data.get("category", "ai_enablement"),
            job_data.get("location", ""),
            job_data.get("location_type", "remote"),
            job_data.get("salary_band", ""),
            int(job_data.get("salary_max", 0)),
            match_score,
            int(job_data.get("interview_prob", 0)),
            job_data.get("fit_band", "Strong Fit"),
            match_tier,
            source,
            source_label,
            posted_date,
            is_reposted,
            reposted_date,
            agent_executed_at,
            job_data.get("linkedin_url", ""),
            job_data.get("direct_url", ""),
            job_data.get("search_landing_url", ""),
            job_data.get("why_matched", ""),
            top_skills_str,
            job_data.get("gap_bridge", ""),
            job_data.get("package_action", ""),
            job_data.get("output_dir", ""),
            status,
            applied_at,
            first_seen_at,
            now_iso
        ))
        job_id = cursor.lastrowid
        action_taken = "inserted"

    conn.commit()
    conn.close()
    return {"id": job_id, "action": action_taken, "status": status}

def update_job_status(job_id: int, status: str, applied_at: Optional[str] = None, db_path: Optional[Path] = None) -> bool:
    """Update status ('active', 'applied', 'deleted') of a job."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE jobs SET status = ?, applied_at = ? WHERE id = ?
    """, (status, applied_at, job_id))
    affected = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return affected

def get_all_jobs(min_score: int = 0, status: Optional[str] = None, tier: Optional[str] = None, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Retrieve jobs matching filters, ordered by match_score DESC."""
    init_db(db_path)
    conn = get_connection(db_path)
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE match_score >= ?"
    params = [min_score]

    if status:
        query += " AND status = ?"
        params.append(status)
    if tier and tier != "all":
        query += " AND match_tier = ?"
        params.append(tier)

    query += " ORDER BY match_score DESC, id ASC"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    results = []
    for r in rows:
        d = dict(r)
        try:
            d["top_skills"] = json.loads(d["top_skills"])
        except Exception:
            if isinstance(d["top_skills"], str):
                d["top_skills"] = [s.strip() for s in d["top_skills"].split(",") if s.strip()]
        results.append(d)

    conn.close()
    return results

def get_tier_counts(db_path: Optional[Path] = None) -> Dict[str, int]:
    """Return count of jobs grouped by match_tier."""
    init_db(db_path)
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT match_tier, count(*) as cnt FROM jobs WHERE status != 'deleted' GROUP BY match_tier")
    counts = {r["match_tier"]: r["cnt"] for r in cursor.fetchall()}
    conn.close()
    return counts
