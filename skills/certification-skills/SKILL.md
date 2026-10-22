---
name: certification-skills
description: Authoritative repository and query engine for Ebenezer J. Rolston's verified certifications, credentials, and technical skills. Automatically extracts and aligns credentials, tools, and achievement bullets based on target job requirements.
---

# Certification Skills Repository & Extraction Engine

This skill manages the verified credentials, certifications, and technical badges for **Ebenezer J. Rolston**, providing an intelligent extraction engine that maps job requirements to verified credentials, skills, tools, and resume bullets.

## Authoritative Repositories
- **JSON Structured Data:** `data/certifications_repository.json`
- **Markdown Reference:** `data/certifications_repository.md`
- **Master Resume:** `data/master_resume.md`

## Verified Credential Catalog Summary

| Credential ID | Official Title | Institution / Authority | Key Domain / Focus | Verification |
| :--- | :--- | :--- | :--- | :--- |
| `STANFORD-PYTHON-2025` | **Data Analysis with Python** | Stanford Continuing Studies (Matt Harrison) | Python, Pandas, NumPy, EDA, Data Wrangling | VeriX QR Code |
| `HARVARD-SEAS-LLM-2025` | **Large Language Models: From Transformer Basics to Agentic AI** | Harvard SEAS (ProfEd) | Transformers, LLMs, Agentic AI, RAG | CeDiD: `25TR-9XBP-E5NU` |
| `DU-AI-LITERACY-GOVERNANCE-2026` | **AI Literacy, Ethics, and Governance** | University of Denver (CPS) | AI Ethics, Governance, Bias Mitigation | Credly: `wIjGxM38` |
| `AI-TECH-PRIVACY-GOVERNANCE-2026` | **AI Governance Training** | AI, Tech & Privacy Academy (Dr. Luiza Jarovsky) | AI Governance, Privacy, Compliance, EU AI Act | Certificate of Completion |
| `AI-REALIST-STACK-OPTIMIZATION-2026` | **Learn to Optimise Your AI Stack** | AI Realist / AI Stack (Maria Sukhareva) | AI Cost Optimization, Prompt Caching, Loop Capping | Cert: `AIS-2026-010` (EU AI Act Art. 4) |
| `DU-GRAD-CERT-AI-STRATEGY-2025` | **Graduate Certificate, AI Strategy & Applications in IT** | University of Denver | AI Roadmaps, Maturity Assessments, ROI Modeling | Graduate Registrar |
| `UC-BERKELEY-ML-DL-2025` | **Professional Program in Machine Learning & Deep Learning** | UC Berkeley | ML, Deep Learning, Neural Networks | Professional Program |
| `ST-JOSEPH-MS-CS` | **M.S. & B.S., Computer Science** | St. Joseph's College | CS Fundamentals, Database Systems, Software Engineering | Academic Registrar |

---

## Extraction Engine Workflow

Whenever the Resume Generator, Cover Letter Writer, or Interview Prep agent processes a job description:

1. **Scan Job Requirements for Domain Keywords:**
   - **Data Analytics / Python:** Look for "Python", "Pandas", "NumPy", "data analysis", "reporting", "data wrangling", "BI".
     $\rightarrow$ Extract `STANFORD-PYTHON-2025`.
   - **LLMs / Agentic AI / Generative AI:** Look for "LLM", "Generative AI", "agentic", "agents", "RAG", "prompt engineering".
     $\rightarrow$ Extract `HARVARD-SEAS-LLM-2025`.
   - **AI Governance / Ethics / Privacy / Policy:** Look for "governance", "ethics", "compliance", "risk", "privacy", "responsible AI", "EU AI Act".
     $\rightarrow$ Extract `DU-AI-LITERACY-GOVERNANCE-2026` and `AI-TECH-PRIVACY-GOVERNANCE-2026`.
   - **AI FinOps / Cost Engineering / LLMOps:** Look for "cost", "optimization", "FinOps", "LLMOps", "prompt caching", "model evaluation".
     $\rightarrow$ Extract `AI-REALIST-STACK-OPTIMIZATION-2026`.
   - **AI Strategy / Transformation:** Look for "AI strategy", "transformation", "roadmap", "maturity", "ROI".
     $\rightarrow$ Extract `DU-GRAD-CERT-AI-STRATEGY-2025`.

2. **Populate Target Resume Sections:**
   - **Education & Credentials:** Order extracted credentials with the most relevant ones prominently listed.
   - **Core Competencies:** Add verified keywords from the extracted credentials.
   - **Technical Proficiencies:** Inject verified tools (e.g., Python Pandas/NumPy, Prompt Caching, RAG).
   - **Projects / Sabbatical:** Incorporate pre-drafted extractable achievement bullets.

3. **Enforce Display Rules & Anti-Hallucination Guardrails:**
   - Never add expected or graduation dates to the University of Denver Graduate Certificate.
   - Label workshop credentials (e.g. AI Realist) accurately as intensive technical workshops supporting AI literacy.
   - Distinguish academic/continuing studies coursework from enterprise client delivery.

---

## Instructions for Adding Future Certificates

When the user provides new certificates:
1. Append the record to `data/certifications_repository.json`.
2. Add the descriptive entry in `data/certifications_repository.md`.
3. Update this `SKILL.md` table.
4. Ensure the domain tags map to standard job requirement terms.
