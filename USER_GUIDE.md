# Resume Agent: User Guide & Antigravity Prompting Reference

## 1. Overview & Mission

The **Resume Agent** is an automated, AI-driven career application pipeline built for **Ebenezer J. Rolston**. It turns raw job postings (URLs or pasted descriptions) into rigorous skill gap evaluations, tailored application documents, and executive-level interview preparation packages.

For every targeted role, the agent produces:
1. **Curated Resume** (Native `.docx` and clean `.md`)
2. **Tailored Cover Letter** (Native `.docx` and clean `.md`)
3. **Skill Gap Analysis** (Native `.docx` and clean `.md`)
4. **13-Section Interview Preparation Package** (Native `.docx` and clean `.md`)
5. **Google Sheet Job Tracker Row** (14-column CSV A–N)
6. **Consolidated Interactive Artifact** in Antigravity for instant review

All documents adhere strictly to ATS single-column formatting, the **Canonical Navy (`#17365D`)** design system, and verified candidate ground-truth.

---

## 2. How to Invoke via Antigravity Prompts

You can invoke the Resume Agent directly within Antigravity using any of the following natural language prompts:

### Prompt A: Standard End-to-End Workflow (Recommended)
> `"Assess the skill gaps for this job description and ask fact finding questions. After completion of fact-finding, generate the cover letter, resume, updated skill gap analysis and complete interview prep package: <JOB_URL>"`

### Prompt B: Fast-Track Generation (Auto Fact-Finding)
> `"Process this job posting and generate the complete application package (resume, cover letter, gap analysis, and interview prep in both .docx and .md): <JOB_URL>"`

### Prompt C: From Pasted Text / Offline Job Description
> `"Here is a job description for [Company Name] - [Job Title]. Please run the Resume Agent workflow to analyze skill gaps and generate all deliverables: [PASTE JOB DESCRIPTION]"`

### Prompt D: Regenerate or Polish a Document
> `"Update the resume and cover letter for [Company Name] to emphasize [Specific Skill / Acxiom Experience / SQL diagnostics]. Ensure both .docx and .md files are regenerated."`

---

## 3. End-to-End Execution Workflow

```
+-----------------------------------------------------------------------------+
|                            RESUME AGENT PIPELINE                            |
+-----------------------------------------------------------------------------+
|                                                                             |
|  1. INGESTION & PARSING                                                     |
|     * Fetch live posting via URL (Ashby, LinkedIn, Workday, Greenhouse)      |
|     * Extract requirements, company culture, salary band, and location      |
|                                                                             |
|  2. WEIGHTED FIT ANALYSIS (0–100 Scoring)                                   |
|     * Must-Have Skills (40%) • Experience & Domain (25%)                    |
|     * Stack / Tools (15%) • Education / Credentials (10%) • Extras (10%)     |
|     * Classify requirements: Matched / Partial / Missing                    |
|                                                                             |
|  3. FACT-FINDING CHECK                                                      |
|     * Validate candidate evidence against Master Resume baseline             |
|     * Offer fact-finding clarifications for any identified gaps             |
|                                                                             |
|  4. NATIVE DOCUMENT GENERATION                                              |
|     * Create native OpenXML .docx using src/resume_agent/utils/docx_writer.py|
|     * Create markdown .md counterparts in output/<Company_Role>/            |
|                                                                             |
|  5. 13-SECTION INTERVIEW PREP PACKAGE                                       |
|     * Spoken 60-90s pitch, 5 STAR stories, 12 technical Q&As, reverse Qs,   |
|       30-60-90 day roadmap, culture brief, curated reading links            |
|                                                                             |
|  6. TRACKER & ARTIFACT DELIVERY                                             |
|     * Emit 14-column Google Sheet tracker row                               |
|     * Publish interactive Antigravity artifact with one-click feedback      |
+-----------------------------------------------------------------------------+
```

---

## 4. Visual Standards & Document Specifications

All Microsoft Word (`.docx`) documents are generated using `src/resume_agent/utils/docx_writer.py` (Python standard library `zipfile` + `xml.etree`):

- **Typography & Layout:** Clean single-column ATS layout (Times New Roman / Calibri).
- **Candidate Name Header:** 36pt / 18pt bold in Canonical Navy (`#17365D`).
- **Section Headers:** Navy with bottom accent rule (`#17365D`).
- **Role Title Bars:** Light blue background shading (`#EBF1F5`).
- **Core Competencies:** De-cluttered into 3 distinct functional categories.
- **Embedded Hyperlinks:** Active clickable links for:
  - [LinkedIn Profile](https://www.linkedin.com/in/ebenezer-rolston/)
  - [AI Guardians Portal](https://portal.aiguardiansllc.us/)
- **Education Formatting:** Date-free University of Denver credentialing:  
  `Graduate Certificate, AI Strategy & Applications in IT : University of Denver`

---

## 5. Candidate Ground-Truth & Anti-Hallucination Guardrails

The agent strictly enforces candidate authenticity across all outputs:

1. **Acxiom Tenure (1999–2010):**
   - 11 years as Solutions Developer / Solution Architect in Conway & Little Rock, AR.
   - Built Citibank's first Online Identity Scoring Model; provided on-call production support (AVS); served on Acxiom Methodology Board.
   - Accurately state Acxiom lineage without overclaiming post-2018 corporate legal entity names.
2. **Department of the Interior (2011–2025):**
   - 14 years supporting the IBC Acquisition Directorate at a GS-13 level.
   - Resolved 5–10 mission-critical escalations daily via Remedy and ServiceNow.
   - 7 years as Unison PRISM Administrator; ETL Architect for FBMS enterprise data conversion (2 DOI Awards).
3. **AI Guardians & Project Labeling:**
   - AI Guardians tools and healthcare risk assessments (ChatGPT Health) are framed as internal company toolkit and graduate project work (never external enterprise client deployments).
4. **No Fabrication Rule:**
   - Never invent employers, dates, titles, production deployments, or unearned certifications.

---

## 6. Directory Structure & Deliverable Locations

```
resume-agent-migration/
├── output/
│   ├── Crocs_AI_Governance_Risk_Analyst/
│   ├── Black_Veatch_Business_Process_Technology_Senior_Analyst/
│   ├── LiveRamp_Technical_Support_Engineer/
│   │   ├── Ebenezer_Rolston_LiveRamp_Resume.docx
│   │   ├── Ebenezer_Rolston_LiveRamp_Resume.md
│   │   ├── Cover_Letter_Ebenezer_Rolston_LiveRamp.docx
│   │   ├── Cover_Letter_Ebenezer_Rolston_LiveRamp.md
│   │   ├── Analysis_LiveRamp.docx
│   │   ├── Analysis_LiveRamp.md
│   │   ├── Interview_Preparation_LiveRamp.docx
│   │   └── Interview_Preparation_LiveRamp.md
│   └── KaiHonua_Management_Analyst/
├── skills/
│   └── resume-generator/SKILL.md
├── .agents/
│   └── skills/
│       └── resume-agent/SKILL.md
├── src/
│   └── resume_agent/
│       └── utils/
│           └── docx_writer.py
├── AGENTS.md
└── USER_GUIDE.md
```

---

## 7. Troubleshooting & Verification

To verify that generated `.docx` files are valid OpenXML archives:
```bash
python3 -c "
import zipfile, xml.etree.ElementTree as ET
from pathlib import Path

for f in Path('output').glob('*/*.docx'):
    with zipfile.ZipFile(f) as z:
        ET.fromstring(z.read('word/document.xml'))
        print(f'[VALID] {f.name}')
"
```
