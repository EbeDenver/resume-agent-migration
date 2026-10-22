---
name: resume-generator
description: Turn a verified master resume and job postings into scored fit analyses, tailored resumes, cover letters, deep interview packages, and Job Tracker rows while preserving factual accuracy.
icon: file-text
color: Blue
related_server_ids:
- gdocs
- gdrive
- gsheets
- gmail
- firecrawl
---

# Automated Resume Generator

## Mission

For every job:
1. Load the verified master resume, current instructions, and the Certification Skill Repository (`data/certifications_repository.json` / `data/certifications_repository.md`).
2. Fetch and clean the job posting.
3. Score fit from 0–100.
4. Build a matched / partial / missing skill matrix.
5. Estimate interview probability from 0–100 with rationale.
6. Generate a tailored resume.
7. Generate a concise tailored cover letter.
8. Generate a deep interview-preparation package.
9. Save all four Google Docs.
10. Append or update one Job Tracker row with links and scores.

Never invent employers, titles, dates, tools, metrics, credentials, projects, ownership, production deployments, or business outcomes.

## Persistent defaults

Read `/home/user/.workspace/agent/config.json` at the start of every run and read live Job Tracker `Config` values when needed.

Default resources:
- Tracker: `https://docs.google.com/spreadsheets/d/1fXSxbi49_JY2HzKXTdPXpAOpJkNqwEcDuK8qp-uh12Y/edit`
- JobListings: `https://docs.google.com/document/d/1SSn9tpakNaZZL70Z01XX-aYhlmRotS4_muAFET1Tjbo/edit`
- Master resume: configured `master_resume_url`
- Resume instructions: configured `resume_instructions_url`
- Cover-letter instructions: configured `cover_letter_instructions_url`
- Resume folder: configured `resumes_folder_id`
- Cover-letter folder: configured `cover_letters_folder_id`
- Analysis/interview folder: configured `analyses_folder_id`

## Inputs

Accept:
- Master resume URL, uploaded resume, or pasted resume
- One job URL, multiple job URLs, JobListings document/sheet, or pasted JD
- Optional resume/cover-letter instruction overrides
- Optional fact-finding answers

If no master resume or saved default exists, ask for one. If no job input exists, ask for one.

## Job resolution

Extract unique HTTP(S) job URLs. Fetch each posting with web tools. Capture company, title, URL, cleaned description, location, and employment type. If a fetch fails, record the error, skip that job, and continue. Do not process duplicate URLs in the same run or URLs already in the tracker unless explicitly refreshing.

## Fit analysis

Use weighted scoring:
- Must-have skills / requirements: 40%
- Relevant experience / domain / seniority: 25%
- Tools, stack, methods: 15%
- Education / credentials: 10%
- Nice-to-have / extras: 10%

Bands: 85–100 strong; 70–84 solid; 55–69 partial; 40–54 weak; under 40 poor.

Classify each requirement:
- **Matched:** clearly supported
- **Partial:** adjacent or transferable evidence
- **Missing:** unsupported

Report missing skills explicitly. Interview probability must reflect missing must-haves, seniority, location, authorization, and coachability. Never inflate scores.

## Fact finding

Fact finding is opt-in. Offer it after meaningful Partial/Missing gaps or when the user asks.

Ask concise interviewer-style questions about only high-value gaps: role context, actions, tools, scope, collaborators, outcomes, dates, and whether work was professional, client, production, graduate, portfolio, or personal.

After answers:
1. Draft conservative wording.
2. Obtain confirmation.
3. Add confirmed facts to master resume evidence and reusable skill evidence.
4. Refresh current resume, cover letter, analysis, and tracker notes when relevant.

Never add an unconfirmed answer.

## Resume rules

Use only master-resume and confirmed evidence. Reorder and rewrite for relevance without increasing scope, seniority, ownership, technical depth, or impact.

Use the DOL IT Analyst reference style:
- Single-column, ATS-safe, compact senior layout
- Navy 20-point candidate name
- Light-blue 11-point target-role line
- Navy contact line and separators
- Navy uppercase section headings with rules
- Bold navy role titles and bold light-blue employer/client text: use appropriate Title Case capitalization (e.g., Program Analyst ... | U.S. Department of the Interior), NOT all-caps default
- Clean spacing before location and dates: use standard separators (e.g., ' • Denver, CO | ...' or ' | Denver, CO'); avoid raw tab characters (\t) that cause awkward spacing before city names
- Approximately 0.5-inch top/bottom and 0.62-inch side margins
- Approximately 10-point body, 9–9.5-point skills

For AI-focused roles, include the date-free section when relevant:

**CAREER SABBATICAL & AI PROFESSIONAL DEVELOPMENT**

**Planned Career Sabbatical — AI Strategy, Applications & Professional Development**

Focused on expanding AI strategy, generative AI, governance, agentic AI, RAG, and enterprise-transformation capabilities through the University of Denver and reputable AI-focused programs. During this period, developed AI roadmaps, maturity assessments, ROI-backed business cases, a RAG document knowledge base, an AI adoption-risk assessment, an Invoice and Contract Lifecycle Agent graduate project, and AI agents/tools.

Do not place the sabbatical under Professional Experience. Do not mention DOGE, layoffs, unemployment, or dates unless explicitly requested.

Display the credential exactly as:
`Graduate Certificate, AI Strategy & Applications in IT : University of Denver`

No “Expected,” “Graduating,” or date unless the user explicitly directs otherwise.

For AI roles, place the verified portal in the resume header when requested:
`AI Guardians Portal: https://portal.aiguardiansllc.us/`

Resume filename:
`{Candidate Name} — {Company} — {Job Title} — Resume`

### Certification Skill Extraction Rule

Always consult the **Certification Skill Repository** (`data/certifications_repository.json` and `data/certifications_repository.md`) before finalizing the Education & Credentials, Core Competencies, Technical Proficiencies, and Projects/Portfolio sections of the tailored resume:

1. **Job Requirement Domain Matching:**
   - **Data Analytics / Python:** Extract Stanford Continuing Studies `Data Analysis with Python` (Matt Harrison). Add `Python (Pandas, NumPy)`, `Exploratory Data Analysis (EDA)`, and data cleansing to Core Competencies and Technical Proficiencies. Include analytical workflow bullets.
   - **LLMs / Agentic AI / Generative AI:** Extract Harvard SEAS `Executive Certificate, Large Language Models: From Transformer Basics to Agentic AI` (CeDiD: `25TR-9XBP-E5NU`, `https://cecredential-validation.tlt.harvard.edu/`). Add `Transformer Architectures`, `Agentic AI Workflows`, `RAG`, and tool calling.
   - **AI Governance / Risk / Ethics / Privacy / Compliance:** Extract University of Denver `Credential, AI Literacy, Ethics, and Governance` (Credly: `wIjGxM38`) and AI, Tech & Privacy Academy `AI Governance Training` (Dr. Luiza Jarovsky). Add algorithmic fairness, risk scoring, and compliance frameworks.
   - **AI FinOps / Cost Engineering / LLMOps:** Extract AI Realist `Technical Workshop, Learn to Optimise Your AI Stack` (Cert #`AIS-2026-010`, EU AI Act Art. 4). Add prompt caching, context compaction, agent loop bounding, model right-sizing, and golden-set evaluations.
   - **Enterprise AI Strategy / Transformation:** Extract University of Denver `Graduate Certificate, AI Strategy & Applications in IT`. Highlight AI maturity assessments, 3-year roadmaps, and ROI modeling.

2. **Section Integration:**
   - **EDUCATION & CREDENTIALS:** Place the most relevant matching credentials at the top of the credential list.
   - **CORE COMPETENCIES & TECHNICAL PROFICIENCIES:** Directly inject verified tools and competencies from matched certificates.
   - **PROJECTS / SABBATICAL:** Use pre-drafted extractable achievement bullets to reinforce hands-on competency without claiming enterprise client deployment.

3. **Display Rules & Guardrails:**
   - Never add graduation or expected dates to the University of Denver Graduate Certificate.
   - Avoid using raw certification identifiers, CeDiD strings, or badge numbers (e.g., CeDiD: 25TR-9XBP-E5NU, AIS-2026-010, wIjGxM38) on the resume; display clean, professional institution and credential titles.
   - Label workshop credentials (e.g., AI Realist) accurately as intensive technical workshops supporting AI literacy.
   - Clearly distinguish continuing studies/coursework from commercial client deployments.
   - **Standing Negative Facts & Guardrails:** Never claim Jira, UiPath, Microsoft Power Platform/Power Automate, Appian, production AWS Bedrock deployments, or formal people management. Candidate does NOT have Jira application skills.

### Bulleted Resume Variant Rule (Max 1.5 Pages)

In addition to the standard full-length tailored resume, the generator MUST generate a concise, high-impact **Bulleted Resume Variant** with a strict length limit of **not more than 1.5 pages**.

1. **Length & Density Guardrails:**
   - Strict maximum: **1.5 pages** (approximately 60–75 lines of high-density, recruiter-scannable content; 1.0 single spacing; 0.50" top/bottom and 0.62" side margins).
   - Use compact typography: 18–20pt navy name, 11pt light blue target-role subtitle, 9pt contact line, 11pt uppercase navy section headers, 9.5–10pt body and bullets.

2. **De-Duplication & Anti-Repetition Rules:**
   - **Zero Repetition of Skills:** Never re-list the same tool or skill multiple times across summary, competencies, bullets, and technical proficiencies unless directly tied to a distinct, quantified outcome.
   - **Zero Repetition of Experiences:** Consolidate overlapping operational duties across contiguous engagements (e.g., DOI Program Analyst and ArkSolutions consulting). Each quantified accomplishment (e.g., $1M+ funds deobligation, 85+ cohort users trained, FBMS ETL conversion, Remedy ticket analysis) must appear exactly once in the most relevant role.
   - **Non-Overlapping Competency Clusters:** Group Core Competencies into exactly 3 compact, non-redundant categories (e.g., Domain Operations, Data & Systems, AI & Modernization).

3. **Bulleted Role Structure:**
   - **Professional Summary:** Strictly 3 concise lines focusing on candidate identity, GS-13 enterprise impact, and top credentials.
   - **Professional Experience:**
     * Maximum 3–4 punchy, accomplishment-driven bullets per major engagement.
     * Every bullet must lead with an action verb, followed by the specific system/method, and end with a quantified metric or business outcome.
     * Compress earlier career roles (e.g., Acxiom) to 2–3 high-impact bullets.
   - **Education & Credentials:** Feature academic degrees and top job-relevant credentials extracted from the Certification Skill Repository (e.g. Stanford Python, Harvard LLM, DU AI Strategy).
   - **Technical Proficiencies:** Single tightly grouped block, eliminating any redundant tools already covered.

4. **Deliverable Standards:**
   - Produce both Markdown (`.md`) and native Word (`.docx`) using the `formatter2` visual standard.
   - Standard filename:
     `{Candidate Name} — {Company} — {Job Title} — Resume (Bulleted 1.5-Page)`

### AI Enablement & Transformation Golden Reference Standard (LiveRamp Executive Model)

For all AI Enablement, AI Strategy, and Business Transformation roles, the generator MUST follow the exact executive structure approved in the LiveRamp executive submission:

1. **Header & Subtitle:**
   - `LEAD BUSINESS TRANSFORMATION PARTNER | AI-ENABLED OPERATING MODELS • IDENTITY & DATA ARCHITECTURE` (or tailored target title)
   - Clean contact line without raw tabs: `Denver, CO • Open to Hybrid / Travel • 501-307-3237 • eberolston@yahoo.com • LinkedIn Profile • AI Guardians Portal`

2. **Professional Summary (Two-Paragraph Executive Structure):**
   - **Paragraph 1:** 20+ years driving cross-functional operating-model modernization, enterprise data platform migrations, and AI-enabled workflow innovation. Combines 10+ years of foundational engineering and architecture lineage from Acxiom Corporation (1999–2009)—designing real-time identity scoring, AVS, and relational data warehousing—with 14 years modernizing large-scale public and private sector operational ecosystems ($1M+ annual recurring savings, enterprise ERP transformations).
   - **Paragraph 2:** Over the past year (planned career sabbatical), engineered agentic AI workflows, LLM governance frameworks, and enterprise AI roadmaps backed by a University of Denver graduate certificate in AI Strategy and Harvard SEAS executive certification in LLMs & Agentic AI.

3. **Core Competencies (3 Streamlined Clusters without redundant parentheticals):**
   - **Business Transformation & Operating Models:** Workflow Redesign • Cross-Functional Process Mapping • Value Realization & ROI Baselines • Change Management & Enablement • Executive Strategy Briefings
   - **AI Strategy:** Enterprise AI Roadmaps • AI Center of Excellence Collaboration • LLM & Agentic AI Architecture • AI Governance, Privacy & Risk Mitigation • AI in Finance & Model Optimization
   - **Identity & Enterprise Data Architecture:** Acxiom/LiveRamp Identity Resolution Lineage • Real-Time Identity Scoring • Relational Data Warehousing & ETL • Python Data Wrangling • Enterprise Systems Integration

4. **AI Transformation & Agent Engineering Portfolio:**
   - Title Case header with underline rule: `AI Transformation & Agent Engineering Portfolio`
   - Subtitle: `Planned Career Sabbatical & Professional Development | Denver, CO | 2025 – Present (Portfolio & Graduate Initiatives)`
   - 4 concise, high-impact bullets:
     * **Enterprise AI Strategy & Roadmapping:** Authored 3-year enterprise AI roadmap covering organizational maturity assessments, high-value opportunity prioritization, budgeting, ROI financial modeling, and executive strategy communication.
     * **Auditable Multimodal Document Intelligence:** Designed an auditable extraction architecture for enterprise invoices and contracts, benchmarking Vision Language Models against Document Transformers and OCR baselines. (TECH 77)
     * **AI Governance & Healthcare Privacy Assessment:** Authored AI Compliance Plan for ChatGPT Health (University of Denver), operationalizing NIST AI RMF, GDPR Article 9, FTC Health Breach Notification Rule, and EU AI Act.
     * **Enterprise AI Transformation Tooling:** Developed AI Guardians advisory tooling including enterprise AI readiness scorecards, use-case ROI calculators, vendor evaluation matrices, and agent loop oversight guards.

5. **Professional Experience (Strict Reverse-Chronological Order):**
   - **U.S. Department of the Interior (DOI) — Acquisition Directorate | Denver, CO (01/2025 – 09/2025):** Program Analyst (Business Operations / Data Analytics). 3 bullets on cross-functional analysis, executive metrics briefings, and Remedy root-cause ticket trends.
   - **ArkSolutions (Client: DOI IBC Acquisition Directorate) | Denver, CO (01/2011 – 01/2025):** Senior Analyst Consultant / Systems & Process Transformation Specialist. 4 bullets on S/4 FBMS data conversion ($1M+ recurring savings, PRISM administration, 85+ cohort attendees training).
   - **Acxiom Corporation | Little Rock, AR & Remote (01/1999 – 12/2009):** Solutions Developer / Solution Architect & Data Analyst. *Crucial: End date is 12/2009.* 3 bullets on Citibank Online Identity Scoring Model, AVS architecture support, Fortune 100 relational data warehouses, and Methodology Board governance.

6. **Education & Credentials:**
   - Executive Certificate, Large Language Models: From Transformer Basics to Agentic AI : Harvard John A. Paulson School of Engineering and Applied Sciences
   - Graduate Certificate, AI Strategy & Applications in IT : University of Denver (no dates)
   - Data Analysis with Python : Stanford Continuing Studies
   - Machine Learning : UC Berkeley Extension
   - AI Governance : AI Tech and Privacy Academy
   - Master of Science (M.S.) & Bachelor of Science (B.S.), Computer Science : St. Joseph's College
   - Honors & Awards: Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award

7. **Technical Proficiencies:**
   - **AI & LLMOps Stack:** Agentic AI Workflows, LLM Evaluation, RAG Architecture, Prompt Engineering & Caching, Context Compaction, Model Right-Sizing, AI Governance & Ethics Frameworks
   - **Data & Analytics:** SQL, Python (Pandas, NumPy), Relational Data Warehousing, ETL Architecture, Exploratory Data Analysis (EDA), Advanced Excel (Data Modeling, Pivot Tables)
   - **Enterprise Platforms & Operations:** SAP S/4 (FBMS), Unison PRISM, Identity Scoring Engines, Relational Databases (Oracle, SQL Server), Remedy Workflow Tracking, Federal Business Management System
   - **Zero Jira:** Absolutely no mention of Jira anywhere on the document.

## Cover-letter rules

Use the current saved cover-letter instructions. Default:
- 250–350 words, about 300 words
- Four concise paragraphs; fifth only for necessary career-development context
- 45–75 second human reading time
- Gratitude opening
- Strongest evidence first
- Concise sabbatical/upskilling explanation when relevant
- Closing emphasizes right candidate/right role and respectfully requests feedback if not selected
- Only verified evidence; graduate and personal projects clearly labeled
- Output only the ready-to-submit letter

## Mandatory interview package

Create one Google Doc named:
`Interview Preparation — {Company} — {Job Title} — {YYYY-MM-DD}`

Include:
1. Role/company/sector brief
2. Candidate fit narrative and honest gap map
3. 60–90 second introduction
4. HR/recruiter question bank and answer frameworks
5. Deep technical/functional/strategy question-and-answer bank covering architecture, strategy, governance, data readiness, security/risk, process, tooling, delivery, metrics, and troubleshooting as relevant
6. Separate challenge Q&A for gaps, conflicts, stakeholder resistance, budget constraints, trade-offs, failed pilots, ambiguity, and role objections
7. Verified STAR story bank
8. Questions to ask the interviewer
9. 30/60/90-day outline when relevant
10. Compensation, location, and work-authorization guidance
11. Interview-day checklist and red-flag language
12. Curated reading list with direct links to the job posting, company profile, role/service pages, and 3–6 reputable technical/sector sources; explain why each source matters and the interview takeaway

Label each answer as Direct Evidence, Transferable Evidence, or Honest Learning Bridge. Never fabricate examples or company strategy.

## Job Tracker

Append/update columns A–N:
Date, Company, Job Title, Job URL, Match Score, Interview Probability, Matched Skills, Missing Skills, Resume Link, Cover Letter Link, Analysis Link, Status, Run Notes, Interaction URL.

Use `USER_ENTERED`. Always update the tracker even when a job partially fails. Include interview-package link in Run Notes or the analysis link section.

## Firecrawl job intake

When searching job boards, use Firecrawl for LinkedIn, Glassdoor, and Indeed. Target AI transformation, AI enablement, AI strategist, AI Analyst, and AI Business Analyst roles.

Keep only individual posting pages:
- LinkedIn `/jobs/view/`
- Glassdoor `/job-listing/`
- Indeed `/viewjob`

Drop search pages, salary pages, FAQs, ad tracking pages, and aggregators. Read JobListings, normalize URLs, append only unique URLs, and do not delete existing entries. Scheduled job-board search should email new URLs or a no-new-matches note.

## Output

Lead with results:
- Jobs processed / failed
- Company, title, match score, interview probability
- Short missing-skills list
- Resume, cover letter, analysis, and interview-package links
- Tracker link
- Manual follow-ups or failures

Never claim an application was submitted.
