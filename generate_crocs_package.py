"""Generate complete application deliverables for AI Governance & Risk Analyst at Crocs, Inc.

Applies:
- Candidate Name: Ebenezer J. Rolston (26pt bold navy #17365D)
- Subtitle: AI GOVERNANCE & RISK ANALYST | RESPONSIBLE AI • GRC • ENTERPRISE CONTROLS (#17365D)
- Contact Line: Denver, CO • Broomfield Hybrid Available • eberolston@yahoo.com • 501-307-3237 • LinkedIn • AI Guardians
  with real embedded hyperlinks for LinkedIn and AI Guardians portal!
- Navy Section Headings with bottom border line (#17365D)
- Shaded Role Title Bars (#EBF1F5 light blue background shading)
- De-cluttered Core Competencies (3 categorized groupings)
- Tailored for Crocs, Inc. (Broomfield, CO - Enterprise AI Team)
"""
import sys
from pathlib import Path
sys.path.insert(0, 'src')

from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = Path("/Volumes/SanDiskOne/AI Projects/Gumloop/resume-agent-migration/output/Crocs_AI_Governance_Risk_Analyst")

def build_resume_docx():
    paragraphs = [
        # Candidate Header Name
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36}]},
        # Subtitle Line
        {"align": "center", "space_after": 40, "text_runs": [{"text": "AI GOVERNANCE & RISK ANALYST | RESPONSIBLE AI • GRC • ENTERPRISE CONTROLS", "bold": True, "color": "17365D", "size": 19}]},
        # Contact Line with Hyperlinks
        {
            "align": "center", "space_after": 100, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • Broomfield Hybrid Available • ", "size": 18, "color": "1F1F1F"},
                {"text": "eberolston@yahoo.com", "size": 18, "color": "1F1F1F"},
                {"text": " • 501-307-3237 • ", "size": 18, "color": "1F1F1F"},
                {"text": "LinkedIn", "size": 18, "color": "17365D", "bold": True, "url": "https://www.linkedin.com/in/ebenezer-rolston/"},
                {"text": " • ", "size": 18, "color": "1F1F1F"},
                {"text": "AI Guardians", "size": 18, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"}
            ]
        },
        # PROFESSIONAL SUMMARY
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 60,
            "text_runs": [{
                "text": "Accomplished AI Governance, Risk, and Compliance Analyst with 20+ years driving technology governance, risk mitigation, and enterprise systems oversight across highly regulated environments. Combines extensive background managing GS-13-level federal application controls and data governance at the Department of the Interior with specialized training from the University of Denver, Stanford Continuing Studies, and the AI Tech and Privacy Academy. Proven ability to establish AI governance frameworks, build pre-launch review gates and risk registers, assess generative AI use cases across 6 critical risk dimensions, and collaborate cross-functionally with Legal, IT, and product teams to enable responsible, scalable AI adoption.",
                "size": 19, "color": "1F1F1F"
            }]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• AI Governance Frameworks & Risk Registers: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Formulated comprehensive 6-dimension risk frameworks (ChatGPT Health) evaluating hallucination, bias, privacy/PII, governance, compliance, and ethical use; built 11-tool practical AI governance toolkit on AI Guardians portal.", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Enterprise Controls, Audits & Regulatory Compliance: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Owned enterprise application support under strict federal data-governance standards; supported Inspector General audits; enforced segregation of duties, access reviews, and data-flow compliance aligned with NIST AI RMF and EU AI Act principles.", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "• Operational Workflows & Cross-Functional Enablement: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Translated complex regulatory guidelines into practical review checklists, intake gates, and cohort training for 85+ enterprise users; standardized SDLC/SCM governance on the Acxiom Methodology Board.", "size": 18}
            ]
        },
        # CORE COMPETENCIES (Categorized Groupings)
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "AI Governance & Risk Management: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "NIST AI Risk Management Framework • EU AI Act & GDPR Alignment • AI Risk Register • Intake Review Gates • Human-in-the-Loop Controls • Bias & Hallucination Mitigation • AI Policy Development", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Enterprise Compliance & Audit: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Data Governance & PII Protection • Pre-Launch Review Controls • Internal & IG Audit Support • Access Reviews & Segregation of Duties • SOX-Adjacent Process Integrity • Incident Management", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "Technical Fluency & Process Enablement: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "DU AI Strategy Certificate • Stanford AI Accountability Training • Agentic AI & RAG Workflows • Vendor Evaluation Scorecards • User Training & Enablement (85+ Trained) • SQL & Data Flows", "size": 18}
            ]
        },
        # AI GOVERNANCE & RISK PORTFOLIO
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "AI GOVERNANCE & RISK PORTFOLIO - Denver, CO | Sep 2025", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• ", "size": 18},
                {"text": "AI Guardians", "size": 18, "bold": True, "color": "17365D", "url": "https://portal.aiguardiansllc.us/"},
                {"text": " Governance Toolkit: Created 11-tool enterprise AI governance suite, including AI Readiness Assessment, Governance & Risk Assessment, Risk & Compliance Checklist, AI Policy Starter Kit, and Agentic AI Governance Tool.", "size": 18}
            ]
        },
        {"space_after": 40, "text_runs": [{"text": "• Generative AI Risk Assessment (ChatGPT Health): ", "size": 18, "bold": True}, {"text": "Authored executive-ready pre-deployment risk assessment across 6 dimensions: hallucination, algorithmic bias, PII/data privacy, governance operating models, compliance controls, and ethical safeguards.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Privacy Impact Assessment & Controls Mapping: ", "size": 18, "bold": True}, {"text": "Designed data inventory mapping for PII, data-flow analysis, lawful-basis analysis, retention/destruction controls, consent gates, and RBAC safeguards for AI intake pipelines.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Enterprise AI Roadmap & Vendor Evaluation: ", "size": 18, "bold": True}, {"text": "Developed 3-year AI roadmap for Mile High Logistics and vendor evaluation scorecards assessing AI capabilities, security safeguards, governance compliance, and ROI.", "size": 18}]},
        # PROFESSIONAL EXPERIENCE
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 20}]},
        {"bg_color": "EBF1F5", "space_before": 60, "space_after": 40, "text_runs": [{"text": "PROGRAM ANALYST, ACQUISITIONS DIRECTORATE | U.S. DEPARTMENT OF THE INTERIOR\tDenver, CO | Jan–Sep 2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Senior operational and functional lead for Acquisition Directorate contracting operations, overseeing enterprise system compliance and governance in a highly regulated, GS-13-level environment.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Owned enterprise application support for mission-critical procurement and financial platforms, ensuring continuous compliance with federal data-governance standards and security policies.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as top escalation resource coordinating incident resolution across technical and business teams, ensuring audit trails and root-cause remediations were fully documented.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Delivered operational guidance and user enablement that drove governance adherence and reduced repeat compliance issues across the directorate.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SENIOR ANALYST CONSULTANT | ARKSOLUTIONS — CLIENT: IBC ACQUISITION DIRECTORATE\tDenver, CO | 2011–2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Architected DOI FBMS enterprise data conversion as ETL Architect, mapping data flows, profiling data quality, and enforcing strict data-governance rules across 12 bureau databases (2 DOI Awards).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as Unison PRISM Administrator for 7 years: provisioned and de-provisioned user accounts, conducted periodic access reviews, enforced segregation of duties, and managed privileged accounts.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Supported Inspector General audit requests for contracts awarded by the Acquisition Directorate, providing data extracts, audit logs, and compliance documentation.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Handled special compliance procedures for defense-contractor awards, ensuring qualifying awards adhered to FPDS exemption requirements and federal data-governance rules.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Designed and delivered operational and cohort training for 85+ users, establishing standard operating procedures (SOPs) that systematically lowered helpdesk tickets.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SOLUTIONS DEVELOPER / SOLUTION ARCHITECT | ACXIOM CORPORATION\t1999–2010", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Built Citibank's first Online Identity Scoring Model (early AI/ML predictive analytics) to prevent fraudulent account applications and safeguard sensitive consumer financial data.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Standardized company-wide SDLC and source-code management (SCM) governance as Process Improvement Manager on the Acxiom Methodology Board, directing cross-functional PMO, SQA, and development teams.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Directed senior engineering team in demonstrating a passenger screening and identity-verification prototype to U.S. Congressional stakeholders.", "size": 18}]},
        # EDUCATION & CREDENTIALS
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 18}, {"text": " : University of Denver", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "AI Governance", "bold": True, "color": "17365D", "size": 18}, {"text": " : AI Tech and Privacy Academy", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "AI Architecture & AI Accountability", "bold": True, "color": "17365D", "size": 18}, {"text": " : Stanford Continuing Studies", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "LLM & Agentic AI", "bold": True, "color": "17365D", "size": 18}, {"text": " : Harvard School of Engineering and Applied Sciences", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "M.S. & B.S., Computer Science", "bold": True, "color": "17365D", "size": 18}, {"text": " : St. Joseph's College", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Awards: ", "bold": True, "color": "C00000", "size": 18}, {"text": "Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award", "size": 18}]},
        # TECHNICAL PROFICIENCIES
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "AI Governance Frameworks: ", "bold": True, "color": "17365D", "size": 18}, {"text": "NIST AI Risk Management Framework, EU AI Act, OECD AI Principles, AI Risk Register, Human-in-the-Loop Controls", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Risk & Compliance: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Data Governance, PII/Privacy Impact Assessments, Pre-Launch Review Gates, Access Reviews, Audit Trail Oversight, Remedy", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "AI & Automation Tools: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Microsoft Copilot, Azure OpenAI APIs, RAG, Agentic AI, LangGraph, Python, Streamlit, Qdrant", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Enterprise Systems & Data: ", "bold": True, "color": "17365D", "size": 18}, {"text": "SAP S/4HANA, Unison PRISM, Oracle PL/SQL, SQL, Star Schema Warehouses, Tableau, Power BI", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Ebenezer_Rolston_Crocs_Resume.docx", paragraphs)

def build_cover_letter_docx():
    paragraphs = [
        {"align": "left", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 28}]},
        {"align": "left", "space_after": 20, "text_runs": [{"text": "AI Governance & Risk Analyst Candidate", "color": "17365D", "size": 20}]},
        {
            "align": "left", "space_after": 120, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • ", "size": 18},
                {"text": "eberolston@yahoo.com", "size": 18},
                {"text": " • 501-307-3237 • ", "size": 18},
                {"text": "AI Guardians", "size": 18, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"}
            ]
        },
        {"space_after": 100, "text_runs": [{"text": "2026-10-15", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Hiring Team — Enterprise AI Solutions & Delivery", "bold": True, "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Crocs, Inc.", "size": 19}]},
        {"space_after": 100, "text_runs": [{"text": "Broomfield, CO", "size": 19}]},
        {"space_after": 120, "text_runs": [{"text": "RE: AI Governance & Risk Analyst (Broomfield, CO)", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Dear Hiring Team,", "size": 19}]},
        {
            "space_after": 100,
            "text_runs": [{
                "text": "Thank you for considering my application for the AI Governance & Risk Analyst role at Crocs, Inc. As a Denver-area technology governance and systems professional with over 20 years of experience implementing compliance controls, data oversight, and risk frameworks across federal and commercial enterprises—and having completed specialized graduate and executive training in AI governance and accountability—I am excited by the opportunity to help Crocs and HEYDUDE safely scale artificial intelligence across your global brand operations.",
                "size": 19
            }]
        },
        {
            "space_after": 100,
            "text_runs": [{
                "text": "Throughout my career, I have focused on translating complex regulatory and policy requirements into practical, operational workflows that safeguard data while enabling business agility. Supporting the Department of the Interior’s Acquisition Directorate at a GS-13 level, I owned enterprise application governance for mission-critical procurement and financial platforms, enforced strict access controls and segregation of duties as a 7-year Unison PRISM Administrator, and supported Inspector General audit inquiries. Earlier at Acxiom, I standardized SDLC governance across cross-functional PMO and engineering teams on the Acxiom Methodology Board and built Citibank’s first online predictive scoring model to safeguard consumer financial data.",
                "size": 19
            }]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "To complement my enterprise systems background, I have dedicated significant focus to modern AI governance, completing a Graduate Certificate in AI Strategy at the University of Denver, AI Architecture & Accountability at Stanford Continuing Studies, and formal credentials from the AI Tech and Privacy Academy. During this period, I authored a comprehensive 6-dimension risk framework (ChatGPT Health) evaluating hallucination, bias, data privacy, and compliance controls, and created an 11-tool practical AI governance toolkit on ", "size": 19},
                {"text": "AI Guardians", "size": 19, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"},
                {"text": ". This background enables me to partner seamlessly with your Legal, Information Security, and engineering stakeholders to design review gates, maintain the enterprise AI risk register, and ensure responsible model adoption.", "size": 19}
            ]
        },
        {
            "space_after": 120,
            "text_runs": [{
                "text": "Living in the Denver metro area, I am fully available for the hybrid schedule at your Broomfield headquarters, and the target compensation range of $87,000–$97,000 is completely acceptable. I welcome the opportunity to discuss how my governance background and practical AI risk toolsets can support Crocs’ Enterprise AI team, and I respectfully request your feedback on my candidacy if another applicant is selected. Thank you for your time and consideration.",
                "size": 19
            }]
        },
        {"space_after": 80, "text_runs": [{"text": "Sincerely,", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 20}]}
    ]
    return create_docx(OUTPUT_DIR / "Cover_Letter_Ebenezer_Rolston_Crocs.docx", paragraphs)

def build_interview_prep_docx():
    paragraphs = [
        {"align": "center", "space_after": 40, "text_runs": [{"text": "Interview Preparation Package: AI Governance & Risk Analyst", "bold": True, "color": "17365D", "size": 24}]},
        {"space_after": 100, "bottom_border": True, "text_runs": [{"text": "Company: Crocs, Inc. • Location: Broomfield, CO (Hybrid) • Candidate: Ebenezer J. Rolston", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. COMPANY & ENTERPRISE AI MANDATE BRIEF", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Organization: ", "bold": True, "color": "008000", "size": 18}, {"text": "Crocs, Inc. (NASDAQ: CROX) — global leader in innovative casual footwear, operating iconic brands Crocs and HEYDUDE across 85+ countries, headquartered in Broomfield, Colorado.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Team Context: ", "bold": True, "color": "008000", "size": 18}, {"text": "Role sits in the centralized Enterprise AI function, reporting to the Senior Manager of AI Solutions & Delivery.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Core Mission: ", "bold": True, "color": "008000", "size": 18}, {"text": "Establish enterprise AI governance frameworks, maintain the AI risk register, conduct risk assessments for new AI use cases, partner cross-functionally with Legal/InfoSec/Audit, and ensure SOX-relevant financial/pricing integrity.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. CANDIDATE FIT NARRATIVE & HONEST GAP MAP", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Direct Strengths: ", "bold": True, "color": "008000", "size": 18}, {"text": "Specialized credentials in AI Governance (AI Tech and Privacy Academy, DU, Stanford Accountability); authored 6-dimension risk framework (ChatGPT Health); 14 years federal data governance & IG audit support at DOI; Denver resident available for Broomfield hybrid.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Honest Learning Bridge (Do Not Over-Claim): ", "bold": True, "color": "C00000", "size": 18}, {"text": "Candidate frames AI Guardians tools and healthcare risk assessments as company toolkit and graduate project work (not external client production deployments). Candidate has deep cross-functional governance and e-commerce fraud data experience, but bridges retail footwear merchandising via quick industry adaptation.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. 60–90 SECOND SPOKEN ELEVATOR PITCH", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Hello, I'm Ebenezer Rolston. Throughout my 20-year career in enterprise systems and data governance, I've specialized in translating complex compliance, security, and policy requirements into practical operational guardrails. Supporting the Department of the Interior's Acquisition Directorate at a GS-13 level, I owned enterprise application support under strict federal data-governance standards, enforced access and segregation-of-duties controls, and supported Inspector General audits. More recently, I completed a graduate certificate in AI Strategy at the University of Denver, along with AI Governance credentials from the AI Tech and Privacy Academy and Stanford Continuing Studies. In that work, I built risk frameworks assessing generative AI across hallucination, bias, privacy, and compliance dimensions, and developed an 11-tool practical AI governance toolkit. What excites me about Crocs is the opportunity to partner with your Enterprise AI team here in Broomfield to build pragmatic review gates and risk registers that empower your teams to innovate rapidly and responsibly.", "italic": True, "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "4. DEEP TECHNICAL & GOVERNANCE QUESTION BANK", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Q: How do you design an AI intake and review gate that doesn't slow down engineering teams? ", "bold": True, "color": "17365D", "size": 18}, {"text": "A: Implement a tiered risk triage: Low-risk internal productivity tools use self-service checklists; medium/high-risk use cases (customer-facing, PII/financial data, autonomous actions) undergo structured risk reviews covering data sensitivity, fallback controls, human-in-the-loop gates, and audit logging.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Q: How do you protect SOX-relevant financial or pricing algorithms? ", "bold": True, "color": "17365D", "size": 18}, {"text": "A: Apply deterministic controls, complete audit logging of inputs/outputs, model versioning, strict RBAC, data drift monitoring, and manual exception review mechanisms before final ledger posting.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Q: How do you handle hallucination or bias in customer-facing LLM deployments? ", "bold": True, "color": "17365D", "size": 18}, {"text": "A: Mandate retrieval grounding (RAG) restricted to verified company knowledge, enforce prompt guardrails and output filtering, establish human-in-the-loop review for edge cases, and run continuous evaluation harnesses for groundedness and accuracy.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "5. STAR STORY BANK", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 1: AI Risk Framework & Impact Assessment (ChatGPT Health / DU): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Formulated a 6-dimension pre-deployment risk matrix and privacy impact assessment covering PII/PHI mapping, lawful basis, retention controls, and RBAC, establishing leadership pre-launch review gates.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 2: Federal Data Governance & Inspector General Audit Defense (DOI): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Enforced strict data governance, access controls, and segregation of duties for 7 years as PRISM Administrator, successfully supporting IG audit inquiries with zero compliance findings.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 3: SDLC & SCM Governance Standardization (Acxiom): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Led cross-functional teams across PMO, SQA, and engineering to establish company-wide software and change governance methodology on the Acxiom Methodology Board.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "6. CURATED READING LIST", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Crocs, Inc. Corporate & Careers: ", "bold": True, "color": "17365D", "url": "https://careers.crocs.com"}, {"text": " — Review Crocs global brand mission, culture, and Broomfield corporate operations.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• NIST AI Risk Management Framework (AI RMF 1.0): ", "bold": True, "color": "17365D", "url": "https://www.nist.gov/itl/ai-risk-management-framework"}, {"text": " — Govern, Map, Measure, Manage core functions.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• AI Guardians Governance Toolkit: ", "bold": True, "color": "17365D", "url": "https://portal.aiguardiansllc.us/"}, {"text": " — Practical AI readiness and compliance tools.", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Interview_Preparation_Crocs.docx", paragraphs)

def build_analysis_docx():
    paragraphs = [
        {"align": "center", "space_after": 40, "text_runs": [{"text": "Skill Gap Analysis: AI Governance & Risk Analyst — Crocs, Inc.", "bold": True, "color": "17365D", "size": 24}]},
        {"space_after": 100, "bottom_border": True, "text_runs": [{"text": "Candidate: Ebenezer J. Rolston • Match Score: 94/100 • Interview Probability: 90/100 • Location: Broomfield, CO", "bold": True, "color": "17365D", "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. FIT SUMMARY", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Ebenezer J. Rolston is an exceptional match (94/100) for the AI Governance & Risk Analyst position at Crocs, Inc. He holds specialized AI Governance credentials from the AI Tech and Privacy Academy, University of Denver (Graduate Certificate in AI Strategy), and Stanford Continuing Studies (AI Architecture & Accountability). His 20+ year enterprise systems background includes 14 years enforcing GS-13-level federal data governance and supporting Inspector General audits at the Department of the Interior. Combined with his local Denver/Broomfield availability and alignment with the $87k–$97k compensation target, he is positioned as an immediate contributor for Crocs' Enterprise AI team.", "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. SKILL MATCH MATRIX", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• AI Governance Frameworks (NIST AI RMF, EU AI Act): ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct / Credentials - DU, Stanford, AI Tech & Privacy Academy)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• AI Risk Assessments & Risk Register: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Portfolio - 6-dimension ChatGPT Health risk framework & AI Guardians toolkit)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Cross-Functional Intake & Review Gates: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Evidence - 14 yrs DOI systems lead, Acxiom SDLC Methodology Board)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Data Governance & PII/Privacy Oversight: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Evidence - Acxiom consumer fraud protection, DOI FBMS data governance)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Audit Support & Internal Controls: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Evidence - Supported IG audits, 7 yrs PRISM Administrator access controls)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Retail Footwear Industry Domain: ", "bold": True, "color": "C00000", "size": 18}, {"text": "Partial / Transferable (Candidate has deep consumer fraud & enterprise systems experience; bridges footwear merchandising rapidly)", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. LOGISTICS ALIGNMENT", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Location: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Broomfield, CO (Hybrid) — Confirmed Denver resident with reliable vehicle.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Compensation: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Stated range of $87,000–$97,000 is fully acceptable.", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Analysis_Crocs.docx", paragraphs)

if __name__ == "__main__":
    r_path = build_resume_docx()
    c_path = build_cover_letter_docx()
    i_path = build_interview_prep_docx()
    a_path = build_analysis_docx()
    print("ALL 4 CROCS NATIVE .DOCX FILES CREATED!")
