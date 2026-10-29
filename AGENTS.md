# Workspace Directives: Resume Agent Migration

This workspace powers the **Resume Agent** for **Ebenezer J. Rolston**.

## Automatic Trigger Guidelines

Whenever the user provides a job URL (LinkedIn, Ashby, Workday, Greenhouse, SAP SuccessFactors, etc.) or requests application materials:
1. **Activate the Resume Agent Workflow** automatically.
2. **Perform Skill Gap Analysis** with 0–100 weighted fit score and interview probability.
3. **Conduct / Verify Fact-Finding** against the candidate baseline (Acxiom 1999–2010, DOI 2011–2025, University of Denver AI Strategy).
4. **Generate Native Deliverables** in `output/<Company_Role>/`:
   - Curated Resume (`.docx` & `.md`)
   - Tailored Cover Letter (`.docx` & `.md`)
   - Skill Gap Analysis (`.docx` & `.md`)
   - 13-Section Interview Preparation Package (`.docx` & `.md`)
5. **Enforce Design & Guardrail Standards (The Bulletted-Standard):**
   - Format Standard: Always use the **Bulletted-Standard** resume format (`skills/bulletted-standard/SKILL.md`) as the default for all future jobs (including AI Engineering, AI Transformation, and Data Analyst roles).
   - Single-column ATS 2-page layout in Canonical Navy (`#17365D`) with underlined section headers.
   - Clickable embedded hyperlinks for LinkedIn (`https://www.linkedin.com/in/ebenezer-rolston/`), GitHub (`https://github.com/EbeDenver`), and AI Guardians (`https://portal.aiguardiansllc.us/`).
   - Strictly date-free University of Denver credentialing.
   - Zero hallucination (do not invent employers, dates, or client production deployments).
   - **Zero Parentheses in Core Competencies:** Core Competencies must be a single dense inline block separated by square bullets (`▪` or `•`) strictly without parentheses `(...)`.
   - **Zero Test Harness Trivia:** Never include internal software test framework statistics or test counts such as `(pytest, 1,296+ Tests)` anywhere on the document.
   - Use standard library OpenXML generator: `src/resume_agent/utils/docx_writer.py` and `generate_bulletted_standard_package.py`.
