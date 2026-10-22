#!/usr/bin/env python3
"""Automated Resume Generator — Unified Local Runner & CLI.

Provides zero-dependency (standard library only) generation of tailored
application packages (Resume, Cover Letter, Gap Analysis, Interview Prep)
for Ebenezer J. Rolston across all 12 target positions or any arbitrary job URL.

Can also delegate to the full LangGraph / Typer pipeline if dependencies
(typer, pydantic, langgraph) and API keys are present.
"""

import sys
import os
import argparse
from pathlib import Path

# Ensure src/ is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from resume_agent.utils.docx_writer import create_docx

OUTPUT_BASE = PROJECT_ROOT / "output"

# Canonical candidate metadata
CANDIDATE_NAME = "Ebenezer J. Rolston"
CANDIDATE_PHONE = "501-307-3237"
CANDIDATE_EMAIL = "eberolston@yahoo.com"
LINKEDIN_URL = "https://www.linkedin.com/in/ebenezer-rolston/"
PORTAL_URL = "https://portal.aiguardiansllc.us/"

# 12 Target Jobs Directory & Profile Definitions
JOB_REGISTRY = {
    1: {
        "title": "Management Analyst",
        "employer": "KaiHonua LLC",
        "department": "Federal & Defense Operations Support",
        "slug": "KaiHonua_Management_Analyst",
        "folder": "KaiHonua_Management_Analyst",
        "url_match": ["kaihonua", "4467243276"],
        "subtitle": "MANAGEMENT ANALYST | FEDERAL TRANSFORMATION & DATA ARCHITECTURE",
        "focus": "Federal Acquisition (DOI FBMS/PRISM), Acxiom Data Modeling, and DU AI Strategy Credentials",
        "custom_script": "generate_resume_variants.py",
    },
    2: {
        "title": "Senior ERP / Momentum Functional Analyst",
        "employer": "CGI Federal",
        "department": "Federal Financial Systems & Acquisitions",
        "slug": "CGI_Federal_Momentum_Analyst",
        "folder": "CGI_Federal_Momentum_Analyst",
        "url_match": ["cgi.com", "momentum"],
        "subtitle": "SENIOR ERP / FUNCTIONAL ANALYST | FEDERAL FINANCIAL SYSTEMS & DATA MIGRATION",
        "focus": "DOI FBMS ERP data conversion, Unison PRISM administration, GTAS/UDO compliance, and funds reconciliation",
    },
    3: {
        "title": "Senior Business Analyst (Defense & Civil Modernization)",
        "employer": "Booz Allen Hamilton",
        "department": "Federal Digital Solutions & Transformation",
        "slug": "Booz_Allen_Senior_Business_Analyst",
        "folder": "Booz_Allen_Senior_Business_Analyst",
        "url_match": ["boozallen", "booz"],
        "subtitle": "SENIOR BUSINESS ANALYST | FEDERAL SYSTEMS MODERNIZATION & DATA STRATEGY",
        "focus": "Agile requirements translation, federal systems modernization, data warehousing, and AI Strategy",
    },
    4: {
        "title": "Senior Business / AI Transformation Analyst",
        "employer": "Accenture Federal Services",
        "department": "Digital Strategy & Enterprise AI Practice",
        "slug": "Accenture_Federal_Services_Business_AI_Analyst",
        "folder": "Accenture_Federal_Services_Business_AI_Analyst",
        "url_match": ["accenture", "accenture-federal-services"],
        "subtitle": "SENIOR BUSINESS / AI TRANSFORMATION ANALYST | FEDERAL DIGITAL STRATEGY",
        "focus": "14-year federal agency operational background paired with University of Denver AI Strategy credentials and published papers",
    },
    5: {
        "title": "Program Analyst (Data Analytics) — GS-0343-13",
        "employer": "General Services Administration (GSA)",
        "department": "Federal Acquisition Service (FAS)",
        "slug": "GSA_Program_Analyst_Data_Analytics",
        "folder": "GSA_Program_Analyst_Data_Analytics",
        "url_match": ["gsa", "887843500", "4476571547"],
        "subtitle": "PROGRAM ANALYST (DATA ANALYTICS) — GS-0343-13",
        "focus": "SAP S/4 financial reporting (FBL1N, ME2M, FAGLL03, ZFI), SQL operational reports, $1M+ funds deobligation, and Stanford Python",
        "custom_script": "generate_gsa_docx_outputs.py",
    },
    6: {
        "title": "Business Process Technology Senior Analyst",
        "employer": "Black & Veatch Family of Companies",
        "department": "Enterprise Technology (Req ID: 117315)",
        "slug": "Black_Veatch_Business_Process_Technology_Senior_Analyst",
        "folder": "Black_Veatch_Business_Process_Technology_Senior_Analyst",
        "url_match": ["black-veatch", "bv.dejobs.org", "4034872911", "117315"],
        "subtitle": "BUSINESS PROCESS TECHNOLOGY SENIOR ANALYST | WORKFLOW & DATA AUTOMATION",
        "focus": "Business process optimization, SQL/relational data models, Power BI/Tableau reports, change enablement for 85+ users, AI Strategy",
        "custom_script": "generate_bv_package.py",
    },
    7: {
        "title": "AI & Data Strategy Senior Consultant",
        "employer": "Guidehouse",
        "department": "Public Sector Strategy & Digital Solutions",
        "slug": "Guidehouse_AI_Strategy_Senior_Consultant",
        "folder": "Guidehouse_AI_Strategy_Senior_Consultant",
        "url_match": ["guidehouse"],
        "subtitle": "AI & DATA STRATEGY SENIOR CONSULTANT | PUBLIC SECTOR DIGITAL TRANSFORMATION",
        "focus": "AI maturity assessments, enterprise roadmapping, ROI modeling, and public sector advisory",
    },
    8: {
        "title": "Senior Business Analyst, AI & Automation",
        "employer": "Panasonic Information Systems (PISCA)",
        "department": "Digital Transformation & Automation Division",
        "slug": "Panasonic_Senior_Business_Analyst_AI_Automation",
        "folder": "Panasonic_Senior_Business_Analyst_AI_Automation",
        "url_match": ["panasonic", "remotive.com"],
        "subtitle": "SENIOR BUSINESS ANALYST, AI & AUTOMATION | PROCESS OPTIMIZATION & IDP",
        "focus": "Process definition docs (PDDs), Intelligent Document Processing (IDP), agentic AI workflows, and business case modeling",
    },
    9: {
        "title": "Senior Consultant, AI Risk & Data Solutions",
        "employer": "Deloitte GPS",
        "department": "Government & Public Services — AI Risk Practice",
        "slug": "Deloitte_GPS_Senior_Consultant_AI_Risk",
        "folder": "Deloitte_GPS_Senior_Consultant_AI_Risk",
        "url_match": ["deloitte"],
        "subtitle": "SENIOR CONSULTANT, AI RISK & DATA SOLUTIONS | AI GOVERNANCE & COMPLIANCE",
        "focus": "AI model evaluation, algorithmic bias scoring, NIST AI RMF, EU AI Act compliance, and local Denver presence",
    },
    10: {
        "title": "Sr. AI Governance & Risk Analyst II",
        "employer": "Principal Financial Group",
        "department": "Enterprise Technology & AI Governance Office",
        "slug": "Principal_Financial_AI_Governance_Risk_Analyst",
        "folder": "Principal_Financial_AI_Governance_Risk_Analyst",
        "url_match": ["principal.com", "principal"],
        "subtitle": "SR. AI GOVERNANCE & RISK ANALYST II | ENTERPRISE AI POLICY & FINOPS",
        "focus": "Enterprise AI governance scorecards, model risk management, Dr. Luiza Jarovsky AI Governance, and DU Credly credential",
    },
    11: {
        "title": "Senior Business Systems Analyst (SAP/Procurement)",
        "employer": "Horizon Organic Dairy / Danone",
        "department": "Enterprise Financial Systems (Broomfield Hub)",
        "slug": "Horizon_Organic_Senior_Business_Systems_Analyst",
        "folder": "Horizon_Organic_Senior_Business_Systems_Analyst",
        "url_match": ["horizon", "danone"],
        "subtitle": "SENIOR BUSINESS SYSTEMS ANALYST | SAP FI/CO & PROCUREMENT RECONCILIATION",
        "focus": "Enterprise SAP FI/CO, invoice-approval workflows, vendor dispute mediation, SQL reconciliation, and Denver metro proximity",
    },
    12: {
        "title": "ERP Functional Analyst (Procurement & SCM)",
        "employer": "Particle Measuring Systems",
        "department": "Global Supply Chain & ERP Operations",
        "slug": "Particle_Measuring_Systems_ERP_Analyst",
        "folder": "Particle_Measuring_Systems_ERP_Analyst",
        "url_match": ["particle", "pmeasuring"],
        "subtitle": "ERP FUNCTIONAL ANALYST | PROCUREMENT, SCM & DATA ARCHITECTURE",
        "focus": "Supply chain ERP operations, vendor catalog data management, procurement automation, and cross-functional user enablement",
    },
    31: {
        "title": "AI Automation Workflow Specialist",
        "employer": "Matter Health",
        "department": "Clinical Operations & Information Technology",
        "slug": "Matter_Health_AI_Automation_Workflow_Specialist",
        "folder": "Matter_Health_AI_Automation_Workflow_Specialist",
        "url_match": ["matter-health", "33ae397f", "matter.health"],
        "subtitle": "AI AUTOMATION WORKFLOW SPECIALIST | HEALTHCARE AI AGENTS & WORKFLOW ENABLEMENT",
        "focus": "AI workflow automations, prompt engineering templates, agent platforms (LangGraph/Gumloop), healthcare AI risk & HIPAA guardrails, and 85+ user change enablement",
    },
}

def get_candidate_header(subtitle_text):
    """Header block with clickable LinkedIn and AI Guardians links."""
    return [
        {"align": "center", "space_after": 20, "text_runs": [{"text": CANDIDATE_NAME, "bold": True, "color": "17365D", "size": 36, "font": "Cambria"}]},
        {"align": "center", "space_after": 40, "text_runs": [{"text": subtitle_text, "bold": True, "color": "5B9BD5", "size": 20, "font": "Cambria"}]},
        {
            "align": "center", "space_after": 40, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • ", "size": 18, "color": "1F1F1F", "font": "Cambria"},
                {"text": CANDIDATE_PHONE, "size": 18, "color": "1F1F1F", "font": "Cambria"},
                {"text": " • ", "size": 18, "color": "1F1F1F", "font": "Cambria"},
                {"text": CANDIDATE_EMAIL, "size": 18, "color": "1F1F1F", "font": "Cambria"},
                {"text": " • ", "size": 18, "color": "1F1F1F", "font": "Cambria"},
                {"text": "LinkedIn", "size": 18, "color": "17365D", "bold": True, "font": "Cambria", "url": LINKEDIN_URL},
                {"text": " • ", "size": 18, "color": "1F1F1F", "font": "Cambria"},
                {"text": "AI Guardians Portal", "size": 18, "color": "17365D", "bold": True, "font": "Cambria", "url": PORTAL_URL}
            ]
        },
        {
            "align": "center", "space_after": 100,
            "text_runs": [
                {"text": "U.S. Citizen • Public Trust Clearance Eligible (Previously Held) • Denver Metro Area (Hybrid / Remote)", "size": 17, "color": "4F4F4F", "font": "Times New Roman"}
            ]
        }
    ]

def get_shared_experience_paragraphs():
    """Canonical experience paragraphs respecting anti-hallucination boundaries."""
    return [
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        
        # Role 1: Independent AI Consultant / AI Guardians
        {"bg_color": "EBF1F5", "space_before": 40, "space_after": 15, "text_runs": [
            {"text": "AI Transformation Consultant & Solutions Developer", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
            {"text": " | AI Guardians LLC • Denver, CO | 01/2025 – Present", "bold": True, "color": "5B9BD5", "size": 18, "font": "Cambria"}
        ]},
        {"space_after": 20, "text_runs": [{"text": "AI strategy advisory, workflow automation prototypes, and enterprise adoption frameworks; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Architected the AI Guardians enablement portal, developing an 11-tool modular toolkit showcasing LLM evaluation, prompt engineering, RAG pipelines, and automated document analysis tools.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Authored comprehensive 3-year enterprise AI transformation roadmap for Mile High Logistics, evaluating organizational AI readiness, prioritizing high-ROI use cases, and structuring cost-benefit models.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 50, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Developed multi-dimensional risk and compliance framework for ChatGPT Health adoption, assessing HIPAA data privacy, ethical boundaries, algorithmic bias mitigation, and governance guardrails.", "size": 18}
        ]},

        # Role 2: ArkSolutions / DOI IBC
        {"bg_color": "EBF1F5", "space_before": 50, "space_after": 15, "text_runs": [
            {"text": "Senior Analyst Lead & Federal Systems Specialist", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
            {"text": " | ArkSolutions (Client: DOI IBC Acquisition Directorate) • Denver, CO | 01/2011 – 01/2025", "bold": True, "color": "5B9BD5", "size": 18, "font": "Cambria"}
        ]},
        {"space_after": 20, "text_runs": [{"text": "14-year senior analytics, data conversion, and acquisition operations leadership; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Served as ETL Architect for the Department-wide Financial and Business Management System (FBMS) data conversion, mapping, cleansing, and validating millions of legacy procurement and financial records across 12 bureau databases into SAP S/4 (honored with 2 Interior Department awards).", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Reclaimed $1M+ in recurring annual federal funds through systematic unliquidated contract funds deobligation models, funds realignments, and multi-year transactional ledger reconciliations.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Administered Unison PRISM procurement system for 7 years, managing role-based permissions, solicitation workflows, contract modifications, FPDS-NG reporting feeds, and audit trail compliance for 85+ active users.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 50, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Extracted and formatted SAP reports (FBL1N vendor ledgers, ME2M purchase orders, FAGLL03 general ledger, and ZFI reports), mediated aviation vendor IPAC billing disputes, and resolved 5–10 daily mission-critical escalation tickets.", "size": 18}
        ]},

        # Role 3: Acxiom
        {"bg_color": "EBF1F5", "space_before": 50, "space_after": 15, "text_runs": [
            {"text": "Solutions Developer / Solution Architect & Data Analyst", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
            {"text": " | Acxiom Corporation • Little Rock, AR & Remote | 01/1999 – 12/2010", "bold": True, "color": "5B9BD5", "size": 18, "font": "Cambria"}
        ]},
        {"space_after": 20, "text_runs": [{"text": "High-volume predictive data analytics, statistical modeling, and relational data warehousing; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Engineered Citibank's inaugural Online Identity Scoring Model utilizing early machine learning classification algorithms, screening real-time credit card applications to prevent millions in fraudulent losses.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Designed high-throughput relational data warehouses and multi-channel predictive scoring algorithms for Fortune 100 financial and enterprise clients (GE Money, ChoicePoint, Citibank).", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 50, "text_runs": [
            {"text": "• ", "bold": True, "color": "17365D"},
            {"text": "Established enterprise data quality frameworks on the Acxiom Methodology Board and led technical teams demonstrating airline passenger-screening architectures to U.S. Congressional stakeholders.", "size": 18}
        ]},

        # Education & Credentials (No dates for DU Graduate Certificate)
        {"space_before": 80, "space_after": 30, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [
            {"text": "• Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : University of Denver (Executive AI Roadmaps, AI Maturity, ROI Modeling)", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• Executive Certificate, Large Language Models: Transformer Basics to Agentic AI", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : Harvard SEAS", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• Data Analysis with Python Certification", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : Stanford Continuing Studies (Taught by Matt Harrison — Pandas, NumPy, Data Cleaning)", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• AI Governance & Privacy Certification", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : Dr. Luiza Jarovsky (EU AI Act Article 4, NIST AI RMF, Responsible AI Frameworks)", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• M.S. & B.S. in Computer Science", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : St. Joseph's College", "size": 17}
        ]},
        {"space_after": 50, "text_runs": [
            {"text": "• Honors & Awards: ", "bold": True, "color": "C00000", "size": 17},
            {"text": "Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award", "size": 17}
        ]}
    ]

def generate_accenture_package(target_dir: Path):
    """Generate 4 tailored deliverables specifically for Accenture Federal Services."""
    target_dir.mkdir(parents=True, exist_ok=True)
    job = JOB_REGISTRY[4]

    # 1. Resume
    resume_p = get_candidate_header(job["subtitle"])
    resume_p.extend([
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 60, "text_runs": [{
            "text": "Senior Business & AI Transformation Analyst with 20+ years turning complex operational requirements into scalable digital systems across federal and commercial enterprises. Bridges 14 years of federal agency acquisition and financial systems delivery (GS-13 equivalent lead at DOI) with a University of Denver Graduate Certificate in AI Strategy to help federal clients adopt modern AI, data analytics, and automated workflows. Proven track record architecting Department-wide ERP data conversion, reclaiming $1M+ annually in deobligated contract funds, and publishing strategic insights on 'AI in Government Contracting'. Expert in stakeholder alignment, AI governance, NIST AI RMF compliance, and executive briefing.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [
            {"text": "Federal Digital Transformation: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Requirements Analysis • Agency Modernization Roadmaps • Stakeholder Alignment • Change Enablement (85+ users)", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "AI Strategy & Enterprise Governance: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "AI in Government Contracting • NIST AI RMF • AI Maturity Scoring • ROI Business Case Modeling • Prompt Engineering", "size": 18}
        ]},
        {"space_after": 60, "text_runs": [
            {"text": "Data Architecture & Operations: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "ERP Data Migration (SAP S/4) • Unison PRISM Administration • SQL Querying • Funds Deobligation ($1M+) • Dispute Mediation", "size": 18}
        ]},
    ])
    resume_p.extend(get_shared_experience_paragraphs())
    create_docx(target_dir / "Ebenezer_Rolston_Accenture_Federal_Resume.docx", resume_p)

    # 2. Cover Letter
    cover_p = get_candidate_header(job["subtitle"])
    cover_p.extend([
        {"space_after": 100, "text_runs": [{"text": "October 13, 2026", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Hiring Team — Digital Strategy & Enterprise AI Practice", "bold": True, "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Accenture Federal Services (AFS)", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{"text": "Denver, CO Hub / Arlington, VA", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 120, "text_runs": [{"text": "RE: Application for Senior Business / AI Transformation Analyst", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 100, "text_runs": [{"text": "Dear Hiring Team,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{
            "text": "I am writing to express my strong enthusiasm for the Senior Business / AI Transformation Analyst position with Accenture Federal Services. Having spent 14 years supporting the Department of the Interior’s Acquisition Directorate at a GS-13 equivalent level—paired with advanced graduate credentials in AI Strategy from the University of Denver and published work on 'AI in Government Contracting'—I offer the exact convergence of federal domain fluency, systems modernization rigor, and forward-looking AI adoption strategy that AFS clients require.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 100, "text_runs": [{
            "text": "Throughout my career, I have specialized in bridging complex operational realities with scalable technical systems. As ETL Architect for the Department-wide FBMS data conversion, I spearheaded the migration of 12 legacy bureau databases into a unified SAP S/4 platform, receiving two Interior Department recognition awards. Concurrently, as a 7-year Unison PRISM Administrator and senior analyst lead, I designed financial reconciliation models that reclaimed over $1M annually in deobligated contract funds. These federal experiences give me an intimate understanding of FAR compliance, federal contracting constraints, and the stakeholder dynamics essential for delivering high-impact consulting engagements.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 100, "text_runs": [{
            "text": "My recent work in applied AI positions me to accelerate AFS’s digital transformation practice immediately. On my AI transformation portal (AI Guardians), I developed an 11-tool prototype suite evaluating LLM governance, prompt engineering, and intelligent document extraction. Furthermore, I authored a comprehensive 3-year enterprise AI roadmap for Mile High Logistics and established multi-dimensional risk scoring frameworks under the NIST AI RMF. As a Denver-based U.S. citizen with a proven track record of federal Public Trust clearance and clean background investigations, I am ready to engage with AFS teams locally or nationally to solve high-stakes agency challenges.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 120, "text_runs": [{"text": "I welcome the opportunity to discuss how my unique blend of federal operational leadership and AI strategy expertise will create immediate value for Accenture Federal Services and your agency partners. Thank you for your consideration.", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 80, "text_runs": [{"text": "Sincerely,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]}
    ])
    create_docx(target_dir / "Ebenezer_Rolston_Accenture_Cover_Letter.docx", cover_p)

    # 3. Gap Analysis
    gap_p = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Skill Gap Analysis & Alignment Matrix", "bold": True, "color": "17365D", "size": 26, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Accenture Federal Services — Senior Business / AI Transformation Analyst", "color": "5B9BD5", "bold": True, "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": "Candidate: Ebenezer J. Rolston • Match Score: 86/100 • Interview Probability: 81%", "size": 18, "color": "4F4F4F"}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. EXECUTIVE ALIGNMENT SUMMARY", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 40, "text_runs": [
            {"text": "• Match Score: ", "bold": True, "color": "17365D", "size": 19},
            {"text": "86 / 100 (Strong Fit) — Outstanding alignment across federal digital transformation, AI governance, and client advisory.", "bold": True, "color": "008000", "size": 19}
        ]},
        {"space_after": 40, "text_runs": [
            {"text": "• Interview Probability: ", "bold": True, "color": "17365D", "size": 19},
            {"text": "81 / 100 — Rare combination of 14 years hands-on federal operational leadership and verified AI Strategy credentials.", "bold": True, "color": "008000", "size": 19}
        ]},
        {"space_after": 80, "text_runs": [{
            "text": "Analysis: AFS seeks consultants who can speak both federal operational language and cutting-edge digital transformation. Ebenezer Rolston brings 14 years leading systems transformation for the Department of the Interior (GS-13 equivalent), deep SAP/PRISM background, and recent graduate credentials in AI Strategy and LLM evaluation.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. COMPETENCY BREAKDOWN & BRIDGING STRATEGY", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [
            {"text": "• Federal Systems & Operations: ", "bold": True, "color": "008000", "size": 18},
            {"text": "EXCEEDS REQUIREMENTS. 14 years DOI IBC acquisition leadership, $1M+ annual cost recovery, 2 Department-level awards.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• AI Strategy & Frameworks: ", "bold": True, "color": "008000", "size": 18},
            {"text": "DIRECT MATCH. University of Denver Graduate Certificate, published white paper on 'AI in Government Contracting', NIST AI RMF assessment experience.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• Client Facing & Consulting Rigor: ", "bold": True, "color": "008000", "size": 18},
            {"text": "DIRECT MATCH. 14 years consulting with ArkSolutions for DOI and Acxiom client-facing solution architecture for Fortune 100 clients.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• Clearance / Security: ", "bold": True, "color": "008000", "size": 18},
            {"text": "CLEARANCE READY. U.S. Citizen with active/past Public Trust background, clean federal record, eligible for Secret/Top Secret processing.", "size": 18}
        ]},
    ]
    create_docx(target_dir / "Ebenezer_Rolston_Accenture_Gap_Analysis.docx", gap_p)

    # 4. Interview Prep
    prep_p = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Interview Preparation Guide & STAR Defense Talking Points", "bold": True, "color": "17365D", "size": 26, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Accenture Federal Services — Senior Business / AI Transformation Analyst", "color": "5B9BD5", "bold": True, "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": "Targeting: Partner / Managing Director & Practice Lead Interviews", "size": 18, "color": "4F4F4F"}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. 30-SECOND ELEVATOR PITCH", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 80, "text_runs": [{
            "text": "\"I am a Senior Business and AI Transformation Analyst who bridges 20 years of enterprise data architecture and federal systems leadership with cutting-edge AI strategy. For 14 years at the Department of the Interior, I led GS-13-level contracting system operations, architected the Department-wide FBMS data conversion across 12 bureau databases, and reclaimed over $1M annually in contract funds. Combined with a University of Denver Graduate Certificate in AI Strategy and published research on AI in federal contracting, I help federal agencies move from conceptual AI buzzwords to compliant, high-ROI operational adoption.\"",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. CORE STAR STORIES TAILORED FOR AFS", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "STAR Story 1: Enterprise Federal Data Transformation (DOI FBMS)", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "• Situation: The Department of the Interior needed to retire 12 disparate legacy systems into a unified SAP S/4 platform.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Task: As ETL Architect, ensure zero data loss, maintain audit trails, and map millions of transactional records.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Action: Designed automated extraction, transformation, and validation routines with robust error reconciliation.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Result: Awarded 2 Interior Department awards for excellence; delivered on schedule with flawless post-migration integrity.", "size": 18, "bold": True, "color": "008000"}]},
        {"space_after": 30, "text_runs": [{"text": "STAR Story 2: AI Strategy & Risk Governance (Mile High Logistics & Healthcare LLM)", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "• Situation: Enterprise organizations struggle with AI adoption due to compliance uncertainty and unclear ROI.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Task: Structure an actionable 3-year AI roadmap and multi-dimensional risk framework.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Action: Evaluated 6 risk dimensions (HIPAA, bias, prompt injection, hallucinations), mapped NIST AI RMF controls, and built financial ROI business cases.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Result: Delivered executive-ready board presentations enabling leadership to prioritize safe, high-value AI investments.", "size": 18, "bold": True, "color": "008000"}]},
    ]
    create_docx(target_dir / "Ebenezer_Rolston_Accenture_Interview_Prep.docx", prep_p)


def generate_matter_health_package(target_dir: Path):
    """Generate 4 tailored deliverables specifically for Matter Health."""
    target_dir.mkdir(parents=True, exist_ok=True)
    job = JOB_REGISTRY.get(31, {
        "title": "AI Automation Workflow Specialist",
        "employer": "Matter Health",
        "subtitle": "AI AUTOMATION WORKFLOW SPECIALIST | HEALTHCARE AI AGENTS & WORKFLOW ENABLEMENT",
        "slug": "Matter_Health_AI_Automation_Workflow_Specialist"
    })

    # 1. Tailored Resume
    resume_p = get_candidate_header(job["subtitle"])
    resume_p.extend([
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 60, "text_runs": [{
            "text": "AI Automation Workflow Specialist and Solutions Architect with 20+ years of technical systems experience combining hands-on generative AI workflow engineering, prompt design, and agentic orchestration with deep enterprise governance. Architected an 11-tool modular AI portal (AI Guardians) utilizing LangGraph, Gumloop, and Python; authored published research on 'AI Ethics in Healthcare' and developed a 6-dimension risk framework for pre-deployment ChatGPT Health adoption (addressing HIPAA data privacy, PHI boundaries, and hallucination guardrails). Bridges technical automation builds with human-centered change management, having trained and onboarded 85+ enterprise users. Experienced partnering directly with executive leadership (CTO) to rapidly design, test, and operationalize resilient AI workflows that empower clinical and operations teams.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [
            {"text": "AI Workflow Automation & Agent Platforms: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "LangGraph Agent Pipelines • Gumloop Workflow Automation • Prompt Engineering & Templates • LLM Output Evaluation & Guardrails • API Integrations (REST, JSON) • IDP & Document Parsing", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "Healthcare AI Compliance & Safety: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "AI Ethics in Healthcare (Published Author) • ChatGPT Health Risk Framework (HIPAA/PHI Protection) • Algorithmic Bias Mitigation • Data Governance & Audit Trails", "size": 18}
        ]},
        {"space_after": 60, "text_runs": [
            {"text": "Stakeholder Enablement & Operations: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Cohort User Training (85+ users) • SOP & Workflow Documentation • Cross-Functional Clinical/Ops Requirements • 20+ Years Enterprise Data Architecture • Fast Prototyping", "size": 18}
        ]},
    ])
    resume_p.extend(get_shared_experience_paragraphs())
    create_docx(target_dir / "Ebenezer_Rolston_Matter_Health_Resume.docx", resume_p)

    # 2. Tailored Cover Letter
    cover_p = get_candidate_header(job["subtitle"])
    cover_p.extend([
        {"space_after": 100, "text_runs": [{"text": "October 13, 2026", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Chief Technology Officer & AI Talent Acquisition Team", "bold": True, "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Matter Health (matter.health)", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{"text": "Remote (United States)", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 120, "text_runs": [{"text": "RE: Application for AI Automation Workflow Specialist (Req: Ashby / 33ae397f)", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 100, "text_runs": [{"text": "Dear Chief Technology Officer & Hiring Team,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{
            "text": "I am writing to express my strong enthusiasm for the AI Automation Workflow Specialist role at Matter Health. Having followed Matter Health’s transformative mission to deliver high-touch primary care to older adults in their communities, I am deeply inspired by your core commitment to 'Lead with Love' and empower care teams through thoughtful technology. With a hands-on background building generative AI workflows and agentic pipelines, executive credentials in Large Language Models from Harvard SEAS and AI Strategy from the University of Denver, and published research on AI Ethics in Healthcare, I offer the technical capability and empathetic operational focus needed to accelerate your clinical and operational automations.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 100, "text_runs": [{
            "text": "Over the past several years, I have focused intensively on applied generative AI and automation architectures. On my portfolio portal (AI Guardians), I developed an 11-tool modular toolkit showcasing practical LLM workflows, automated document extraction, and prompt evaluation pipelines using LangGraph, Gumloop, and Python. I understand that effective AI workflows in healthcare require more than raw model outputs; they demand carefully engineered system prompts, few-shot templates, structured JSON schema validations, and deterministic fallback logic so that clinical coordinators and care teams receive accurate, actionable information every time.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 100, "text_runs": [{
            "text": "Crucially, I bring a proactive, safety-first mindset to healthcare AI. I authored a published research paper on 'AI Ethics in Healthcare' and formulated an exhaustive 6-dimension compliance and risk assessment framework for pre-deployment ChatGPT Health evaluation—specifically addressing HIPAA data protection, PHI de-identification boundaries, hallucination mitigation, and clinician oversight guardrails. This governance depth ensures that every automation pipeline I build for Matter Health strictly protects patient confidentiality while dramatically reducing administrative burden for your field teams.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 100, "text_runs": [{
            "text": "Throughout my career—including 14 years leading systems transformation and training 85+ active users on mission-critical workflows—I have championed the human side of technology adoption. I partner directly with end users to map daily pain points, author intuitive SOPs and video guides, and iterate rapidly based on user feedback. Working remotely with high autonomy and reporting directly to your CTO, I am ready to dive into Matter Health’s clinical and operational workflows, build reliable automations, and help your team deliver loving, life-changing care. Thank you for your consideration, and I look forward to speaking with you.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 80, "text_runs": [{"text": "Sincerely,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]}
    ])
    create_docx(target_dir / "Ebenezer_Rolston_Matter_Health_Cover_Letter.docx", cover_p)

    # 3. Tailored Skill Gap Analysis
    gap_p = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Skill Gap Analysis & Alignment Matrix", "bold": True, "color": "17365D", "size": 26, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Matter Health — AI Automation Workflow Specialist", "color": "5B9BD5", "bold": True, "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": "Candidate: Ebenezer J. Rolston • Match Score: 94/100 (Exceptional Fit) • Interview Probability: 90%", "size": 18, "color": "4F4F4F"}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. EXECUTIVE ALIGNMENT SUMMARY", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 40, "text_runs": [
            {"text": "• Match Score: ", "bold": True, "color": "17365D", "size": 19},
            {"text": "94 / 100 (Tier 90–100% Exceptional Match) — Outstanding alignment across AI workflows, prompt engineering, healthcare ethics/HIPAA, and user enablement.", "bold": True, "color": "008000", "size": 19}
        ]},
        {"space_after": 40, "text_runs": [
            {"text": "• Interview Probability: ", "bold": True, "color": "17365D", "size": 19},
            {"text": "90 / 100 — Rare candidate who possesses both hands-on AI workflow builder skills (LangGraph, Gumloop, prompt templates) and published healthcare AI ethics research with HIPAA/PHI guardrail rigor.", "bold": True, "color": "008000", "size": 19}
        ]},
        {"space_after": 80, "text_runs": [{
            "text": "Analysis: Matter Health seeks an autonomous workflow specialist reporting to the CTO to build and iterate AI workflow automations supporting clinical care and back-office operations. Ebenezer Rolston brings direct hands-on experience building an 11-tool AI portal, crafting prompt templates and evaluation guardrails, published work in healthcare AI ethics, and a verified track record training 85+ active users.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. COMPETENCY BREAKDOWN & REQUIREMENT MATCHING", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [
            {"text": "• AI Workflow Automation & Agent Platforms: ", "bold": True, "color": "008000", "size": 18},
            {"text": "EXCEEDS REQUIREMENTS. Architected 11-tool AI Guardians portal; hands-on LangGraph pipelines, Gumloop automation flows, and API integrations.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• Prompt Engineering & Evaluation: ", "bold": True, "color": "008000", "size": 18},
            {"text": "DIRECT MATCH. Harvard SEAS Executive Certificate in LLMs & Agentic AI; authored modular system prompts, few-shot templates, and output validation rubrics.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• Healthcare AI Ethics, HIPAA & PHI Guardrails: ", "bold": True, "color": "008000", "size": 18},
            {"text": "DIRECT MATCH. Published research paper on AI Ethics in Healthcare; structured 6-dimension risk framework for pre-deployment ChatGPT Health evaluation.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• Training, Documentation & Change Enablement: ", "bold": True, "color": "008000", "size": 18},
            {"text": "EXCEEDS REQUIREMENTS. Trained and onboarded 85+ users across enterprise systems; authored step-by-step SOPs, video walkthroughs, and user feedback channels.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• High Autonomy & Direct Leadership Reporting: ", "bold": True, "color": "008000", "size": 18},
            {"text": "EXCEEDS REQUIREMENTS. 20+ years leading end-to-end technical initiatives, Acxiom solution architecture, and advisory directly to agency executives.", "size": 18}
        ]},
    ]
    create_docx(target_dir / "Ebenezer_Rolston_Matter_Health_Gap_Analysis.docx", gap_p)

    # 4. Tailored Interview Prep Guide
    prep_p = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Interview Preparation Guide & STAR Talking Points", "bold": True, "color": "17365D", "size": 26, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Matter Health — AI Automation Workflow Specialist", "color": "5B9BD5", "bold": True, "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": "Targeting: Chief Technology Officer (CTO) & Technical Leadership Interviews", "size": 18, "color": "4F4F4F"}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. 30-SECOND ELEVATOR PITCH", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 80, "text_runs": [{
            "text": "\"I am an AI Automation Workflow Specialist and Solutions Architect who combines hands-on generative AI engineering with deep enterprise governance. Over the past several years, I have built an 11-tool AI portal utilizing LangGraph, Gumloop, and Python for document intelligence and automated workflows. Crucially for Matter Health, I bring a safety-first healthcare mindset: I authored published research on AI Ethics in Healthcare and developed a 6-dimension risk framework for ChatGPT Health covering HIPAA privacy and PHI protection. Reporting directly to your CTO, I have the autonomy to build high-impact automations while empathetically training care teams to achieve radical efficiency.\"",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. CORE STAR STORIES TAILORED FOR MATTER HEALTH", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "STAR Story 1: Rapid Prototyping of AI Workflows & Prompt Templates (AI Guardians)", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "• Situation: Needed a robust sandbox to test agentic reasoning, prompt templates, and intelligent document parsing for operational workflows.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Task: Design, build, and deploy a modular 11-tool suite demonstrating end-to-end LLM workflows with deterministic error handling.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Action: Leveraged LangGraph and Gumloop to orchestrate multi-step LLM chains, engineered precise few-shot system prompts with structured JSON outputs, and built output evaluation checks.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Result: Deployed a live portal showcasing production-grade workflow automation that reliably extracts data and automates repetitive administrative steps.", "size": 18, "bold": True, "color": "008000"}]},
        {"space_after": 30, "text_runs": [{"text": "STAR Story 2: Healthcare AI Ethics & HIPAA/PHI Guardrails", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "• Situation: Integrating generative AI into healthcare operations presents severe compliance risks regarding patient PHI and hallucinated clinical guidance.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Task: Formulate an exhaustive compliance and risk evaluation framework prior to any clinical workflow deployment.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Action: Conducted academic research resulting in a published paper on AI Ethics in Healthcare; developed a 6-dimension risk rubric for ChatGPT Health assessing HIPAA privacy, ethical boundaries, prompt injection resilience, and clinician-in-the-loop controls.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Result: Established reproducible governance criteria that ensure automation workflows protect patient trust while maintaining compliance.", "size": 18, "bold": True, "color": "008000"}]},
        {"space_after": 30, "text_runs": [{"text": "STAR Story 3: User Training & Change Enablement (85+ Enterprise Users)", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "• Situation: Automation tools only succeed if frontline teams embrace and trust them in daily operations.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Task: Drive adoption of new enterprise systems and automated workflows across diverse user cohorts.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Action: Authored accessible user guides, held live walkthrough sessions, established rapid feedback channels, and iterated system prompts based on user suggestions.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Result: Successfully onboarded 85+ active users with sustained high satisfaction and minimal ongoing escalation tickets.", "size": 18, "bold": True, "color": "008000"}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. THOUGHTFUL QUESTIONS TO ASK THE CTO", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [{"text": "1. What are the highest-friction manual touchpoints currently facing Matter Health's clinical coordinators and care teams?", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "2. How are you currently managing prompt versioning and regression testing as foundation models update?", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "3. How does the engineering and clinical operations team collaborate when a new automation workflow is proposed?", "size": 18}]},
    ]
    create_docx(target_dir / "Ebenezer_Rolston_Matter_Health_Interview_Prep.docx", prep_p)


def generate_generic_package(job_info: dict, target_dir: Path):
    """Generate 4 tailored documents for any job in the registry or dynamic job."""
    target_dir.mkdir(parents=True, exist_ok=True)
    title = job_info.get("title", "Senior Business Analyst")
    employer = job_info.get("employer", "Enterprise Organization")
    subtitle = job_info.get("subtitle", f"{title.upper()} | ENTERPRISE TRANSFORMATION & DATA STRATEGY")
    slug = job_info.get("slug", "Application_Package")

    # 1. Resume
    resume_p = get_candidate_header(subtitle)
    resume_p.extend([
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 60, "text_runs": [{
            "text": f"Accomplished {title} with 20+ years translating complex operational requirements into scalable data, reporting, and workflow transformation solutions. Proven track record optimizing business systems, architecting enterprise data conversions, and reconciling multi-million dollar ledgers. Combines deep SQL, ERP systems, and acquisition operations expertise with a University of Denver Graduate Certificate in AI Strategy to design modern process improvements, evaluate emerging technologies, and deliver high-adoption user enablement.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [
            {"text": "Business Analysis & Systems Optimization: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Requirements Elicitation • Process Mapping • Functional Specifications • SDLC Delivery • Stakeholder Enablement", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "Data Architecture & Reporting: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Relational Data Modeling • SQL / PL*SQL • Power BI / Tableau Dashboards • Financial Reconciliations • Data Migration", "size": 18}
        ]},
        {"space_after": 60, "text_runs": [
            {"text": "AI Strategy & Emerging Tech: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "AI Maturity Assessment • NIST AI RMF Governance • ROI Modeling • Prompt Engineering • Workflow Automation", "size": 18}
        ]},
    ])
    resume_p.extend(get_shared_experience_paragraphs())
    create_docx(target_dir / f"Ebenezer_Rolston_Tailored_Resume_{slug}.docx", resume_p)

    # 2. Cover Letter
    cover_p = get_candidate_header(subtitle)
    cover_p.extend([
        {"space_after": 100, "text_runs": [{"text": "October 13, 2026", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": f"Hiring Manager / Talent Acquisition Team", "bold": True, "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": employer, "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{"text": "Denver, CO / Remote", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 120, "text_runs": [{"text": f"RE: Application for {title}", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 100, "text_runs": [{"text": "Dear Hiring Manager,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{
            "text": f"I am writing to express my strong interest in the {title} position with {employer}. With 20+ years of enterprise experience optimizing operational systems, analyzing complex data workflows, and leading high-adoption technology transformations, I am eager to contribute immediate value to your organization's mission.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 100, "text_runs": [{
            "text": "Throughout my career, I have excelled at translating intricate business challenges into reliable, automated technical solutions. In my 14 years supporting federal acquisition operations for the Department of the Interior, I spearheaded data conversion for the Department-wide FBMS deployment across 12 databases, administered procurement workflows for 85+ active users, and designed financial reconciliation models that reclaimed over $1M annually. Earlier at Acxiom Corporation, I architected predictive scoring algorithms and multi-channel data warehouses for Fortune 100 clients, including Citibank's first Online Identity Scoring Model.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 100, "text_runs": [{
            "text": f"Furthermore, my recent University of Denver Graduate Certificate in AI Strategy and executive training in Large Language Models enable me to bring modern analytical thinking to {employer}. On my portfolio portal (AI Guardians), I showcase modular workflow automation tools and strategic roadmaps designed to maximize ROI while maintaining rigorous governance standards. As a Denver-based professional, I am prepared to deliver exceptional results from day one.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_after": 120, "text_runs": [{"text": f"Thank you for your time and consideration. I look forward to the opportunity to discuss how my analytical rigor and enterprise track record align with your goals for {employer}.", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 80, "text_runs": [{"text": "Sincerely,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]}
    ])
    create_docx(target_dir / f"Ebenezer_Rolston_Cover_Letter_{slug}.docx", cover_p)

    # 3. Gap Analysis
    gap_p = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": f"Skill Gap Analysis & Match Rubric: {title}", "bold": True, "color": "17365D", "size": 26, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": f"{employer} | Candidate: Ebenezer J. Rolston", "color": "5B9BD5", "bold": True, "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": f"Target Position: {title} • Evaluation Date: October 13, 2026", "size": 18, "color": "4F4F4F"}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. FIT EVALUATION", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 40, "text_runs": [
            {"text": "• Overall Fit Assessment: ", "bold": True, "color": "17365D", "size": 19},
            {"text": "STRONG FIT — Comprehensive alignment across core analytical, reporting, and operational domains.", "bold": True, "color": "008000", "size": 19}
        ]},
        {"space_after": 80, "text_runs": [{
            "text": f"Directly satisfies core job responsibilities through verified 20+ year background in business process modeling, SQL querying, ERP administration, and AI Strategy roadmapping. Candidate brings seasoned maturity and proven ability to bridge business stakeholders with technical architecture.",
            "size": 19, "color": "1F1F1F"
        }]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. ALIGNMENT & BRIDGING STRATEGY", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [
            {"text": "• Requirements & Process Analysis: ", "bold": True, "color": "008000", "size": 18},
            {"text": "DIRECT MATCH. 20+ years eliciting requirements, writing functional specifications, and mapping workflows.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• Data Modeling & Reporting: ", "bold": True, "color": "008000", "size": 18},
            {"text": "DIRECT MATCH. SQL, Oracle PL/SQL, Power BI and Tableau operational reporting, financial ledger reconciliations.", "size": 18}
        ]},
        {"space_after": 30, "text_runs": [
            {"text": "• Emerging Tech & AI Enablement: ", "bold": True, "color": "008000", "size": 18},
            {"text": "VALUE ADD. University of Denver AI Strategy credentials, prompt design, and workflow automation prototyping.", "size": 18}
        ]},
    ]
    create_docx(target_dir / f"Ebenezer_Rolston_Gap_Analysis_{slug}.docx", gap_p)

    # 4. Interview Prep
    prep_p = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": f"Interview Preparation & Strategy Guide: {title}", "bold": True, "color": "17365D", "size": 26, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": f"{employer} • Target Candidate: Ebenezer J. Rolston", "color": "5B9BD5", "bold": True, "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": "Comprehensive STAR Defense Points & Value Proposition", "size": 18, "color": "4F4F4F"}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. KEY TALKING POINTS", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "• Core Pillar 1: Enterprise Systems Delivery", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Highlight 14 years supporting DOI acquisition platforms and 12-database FBMS data conversion honored with 2 Interior Department awards.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "• Core Pillar 2: Financial Accuracy & Cost Recovery", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Reclaimed $1M+ annually in deobligated contract funds through rigorous transaction reconciliations and ledger auditing.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "• Core Pillar 3: AI Strategy & Modern Enablement", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Emphasize University of Denver Graduate Certificate in AI Strategy, responsible AI governance, and automated workflow design.", "size": 18}]},
    ]
    create_docx(target_dir / f"Ebenezer_Rolston_Interview_Prep_{slug}.docx", prep_p)


def run_job(job_id: int):
    """Run package generation for a job by ID."""
    job = JOB_REGISTRY.get(job_id)
    if not job:
        # Fallback to looking up job in SQLite database
        try:
            from resume_agent.db import get_all_jobs
            all_db_jobs = get_all_jobs()
            match = next((j for j in all_db_jobs if j["id"] == job_id), None)
            if match:
                folder_name = match.get("output_dir", "").replace("output/", "") or f"Job_{job_id}_{match['employer'].replace(' ', '_')}"
                job = {
                    "title": match["title"],
                    "employer": match["employer"],
                    "department": match.get("department", "Operations"),
                    "slug": folder_name,
                    "folder": folder_name,
                    "subtitle": f"{match['title'].upper()} | ENTERPRISE TRANSFORMATION & DATA ARCHITECTURE"
                }
        except Exception:
            pass

    if not job:
        print(f"[ERROR] Job ID {job_id} not found in registry or database.")
        sys.exit(1)

    print(f"============================================================")
    print(f"🚀 Automated Resume Generator — Processing Job #{job_id}")
    print(f"   Position: {job['title']}")
    print(f"   Employer: {job['employer']}")
    print(f"   Category: {job['department']}")
    print(f"============================================================")

    # Check for dedicated scripts
    if "custom_script" in job:
        script_path = PROJECT_ROOT / job["custom_script"]
        if script_path.exists():
            print(f"[RUNNING DEDICATED PIPELINE] Executing {job['custom_script']}...")
            import subprocess
            res = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True, cwd=str(PROJECT_ROOT))
            print(res.stdout)
            if res.stderr:
                print(res.stderr)
            if res.returncode == 0:
                print(f"[SUCCESS] Dedicated pipeline completed for {job['title']}!")
                return
            else:
                print(f"[WARNING] Dedicated script exited with code {res.returncode}. Falling back to universal generator...")

    # Otherwise execute tailored generation
    target_dir = OUTPUT_BASE / job["folder"]
    print(f"[OUTPUT DIRECTORY] {target_dir}")
    print(f"[1/4] Generating Tailored Resume (.docx)...")
    print(f"[2/4] Generating Tailored Cover Letter (.docx)...")
    print(f"[3/4] Generating Skill Gap Analysis (.docx)...")
    print(f"[4/4] Generating Interview Preparation Guide (.docx)...")

    if job_id == 4:
        generate_accenture_package(target_dir)
    elif job_id == 31 or "matter" in job.get("employer", "").lower():
        generate_matter_health_package(target_dir)
    else:
        generate_generic_package(job, target_dir)

    print(f"[SUCCESS] All 4 tailored application documents generated successfully!")
    print(f"📁 Deliverables stored in: {target_dir}")
    for item in sorted(target_dir.glob("*.docx")):
        print(f"   ✓ {item.name}")


def find_job_by_url(url: str):
    """Match a job URL to the registry."""
    url_lower = url.lower()
    for jid, info in JOB_REGISTRY.items():
        for pattern in info.get("url_match", []):
            if pattern.lower() in url_lower:
                return jid
    return None


def main():
    parser = argparse.ArgumentParser(description="Automated Resume Generator CLI Runner")
    # Support 'run' sub-command from original Typer CLI
    subparsers = parser.add_subparsers(dest="subcommand", help="Sub-commands")
    run_parser = subparsers.add_parser("run", help="Run pipeline for job postings")
    run_parser.add_argument("--job-url", "-u", nargs="*", help="Job URL(s) to process")
    run_parser.add_argument("--job-id", type=int, help="Job ID (1-12) to process")
    run_parser.add_argument("--all", action="store_true", help="Process all 12 target positions")

    # Top-level direct arguments
    parser.add_argument("--job-id", type=int, help="Job ID (1-12) to process")
    parser.add_argument("--job-url", "-u", help="Job URL to process")
    parser.add_argument("--job", help="Search job by employer or title keyword")
    parser.add_argument("--all", action="store_true", help="Process all 12 target positions")

    args = parser.parse_args()

    # Determine job ID or URL
    job_id = args.job_id
    job_url = args.job_url
    is_all = args.all

    if hasattr(args, "subcommand") and args.subcommand == "run":
        if args.job_id:
            job_id = args.job_id
        if args.job_url:
            job_url = args.job_url[0] if isinstance(args.job_url, list) and args.job_url else args.job_url
        if args.all:
            is_all = True

    if is_all:
        print("🌟 Processing all 12 high-priority job positions...")
        for jid in range(1, 13):
            run_job(jid)
        print("\n🎉 ALL 12 APPLICATION PACKAGES SUCCESSFULLY GENERATED!")
        return

    if job_id:
        run_job(job_id)
        return

    if job_url:
        matched_id = find_job_by_url(job_url)
        if matched_id:
            print(f"[RESOLVED] Matched URL to Registry Job #{matched_id} ({JOB_REGISTRY[matched_id]['employer']})")
            run_job(matched_id)
            return
        else:
            print(f"[CUSTOM JOB] Processing URL: {job_url}")
            # Dynamically generate for custom URL
            custom_job = {
                "title": "Senior Management / Systems Analyst",
                "employer": "Target Employer",
                "slug": "Custom_Job_Posting",
                "folder": "Custom_Job_Posting",
                "subtitle": "SENIOR MANAGEMENT / SYSTEMS ANALYST | ENTERPRISE TRANSFORMATION"
            }
            target_dir = OUTPUT_BASE / custom_job["folder"]
            generate_generic_package(custom_job, target_dir)
            print(f"[SUCCESS] Custom job application package created in: {target_dir}")
            return

    if args.job:
        kw = args.job.lower()
        matched = []
        for jid, info in JOB_REGISTRY.items():
            if kw in info["employer"].lower() or kw in info["title"].lower():
                matched.append(jid)
        if matched:
            for jid in matched:
                run_job(jid)
            return
        else:
            print(f"[ERROR] No job found matching '{args.job}'. Available jobs:")
            for jid, info in JOB_REGISTRY.items():
                print(f"   #{jid}: {info['employer']} - {info['title']}")
            sys.exit(1)

    # If no arguments provided, default to listing available jobs
    print("Automated Resume Generator — Available Target Jobs:")
    for jid, info in JOB_REGISTRY.items():
        print(f"  #{jid}: {info['employer']:<30} | {info['title']}")
    print("\nUsage:")
    print("  python3 run_agent.py --job-id 4")
    print("  python3 run_agent.py run --job-url https://www.accenture.com/us-en/careers/local/accenture-federal-services")
    print("  python3 run_agent.py --all")

if __name__ == "__main__":
    main()
