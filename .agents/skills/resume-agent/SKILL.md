---
name: resume-agent
description: Turn job postings into scored skill gap analyses, tailored resumes, cover letters, and 13-section interview preparation packages for Ebenezer J. Rolston. Triggers when a job URL is provided or application tailoring is requested.
---

# Resume Agent Workflow

This skill is automatically activated when the user asks to process a job description, assess skill gaps, or generate resumes, cover letters, and interview preparation packages for Ebenezer J. Rolston.

## Core Directives

1. **Candidate Identity & Baseline:**
   - Candidate: Ebenezer J. Rolston (`eberolston@yahoo.com`, `501-307-3237`, Denver, CO / Little Rock, AR roots).
   - Portfolios: [LinkedIn](https://www.linkedin.com/in/ebenezer-rolston/) and [AI Guardians](https://portal.aiguardiansllc.us/).
   - 11 Years Acxiom Corporation (1999–2010): CDI, AVS production support, Citibank scoring, SDLC on Methodology Board.
   - 14 Years Department of the Interior (2011–2025): Senior escalation lead (GS-13), 5–10 critical tickets/day in Remedy/ServiceNow, Oracle PL/SQL, ETL Architect (2 DOI awards).
   - Education: Date-free formatting (`Graduate Certificate, AI Strategy & Applications in IT : University of Denver`).

2. **Standard Workflow Steps:**
   - **Step 1:** Fetch & clean job description from URL.
   - **Step 2:** Execute weighted skill gap analysis (Must-haves 40%, Experience 25%, Tools 15%, Education 10%, Extras 10%).
   - **Step 3:** Offer / verify fact-finding against master resume logs.
   - **Step 4:** Generate 4 pairs of files in `output/<Company_Role>/` using `src/resume_agent/utils/docx_writer.py` and markdown:
     - `Ebenezer_Rolston_<Company>_Resume.docx` & `.md`
     - `Cover_Letter_Ebenezer_Rolston_<Company>.docx` & `.md`
     - `Analysis_<Company>.docx` & `.md`
     - `Interview_Preparation_<Company>.docx` & `.md` (complete 13-section package)
   - **Step 5:** Emit 14-column Google Sheet tracker row (A–N).
   - **Step 6:** Create interactive markdown artifact in Antigravity brain directory with `RequestFeedback: true`.

3. **Styling & Standards:**
   - Visual System: Canonical Navy (`#17365D`), light blue banners (`#EBF1F5`), ATS single-column layout, 3 categorized Core Competencies.
   - Zero Hallucination: Never invent employers, dates, titles, or unearned certifications.
