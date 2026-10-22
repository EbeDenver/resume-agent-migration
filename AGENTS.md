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
5. **Enforce Design & Guardrail Standards:**
   - Single-column ATS layout in Canonical Navy (`#17365D`) and light blue role banners (`#EBF1F5`).
   - Clickable embedded hyperlinks for LinkedIn (`https://www.linkedin.com/in/ebenezer-rolston/`) and AI Guardians (`https://portal.aiguardiansllc.us/`).
   - Strictly date-free University of Denver credentialing.
   - Zero hallucination (do not invent employers, dates, or client production deployments).
   - Use standard library OpenXML generator: `src/resume_agent/utils/docx_writer.py`.
