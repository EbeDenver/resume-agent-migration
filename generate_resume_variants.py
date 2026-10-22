"""Generate Option 1 (Executive Hybrid) and Option 3 (Matrix Callout) tailored resumes for KaiHonua Management Analyst.

Applies:
- De-cluttered, categorized Core Competencies (3 neat groupings)
- Tailored Professional Summary & Matrix featuring Federal Acquisition (DOI FBMS/PRISM), Acxiom Data Modeling & Identity Analytics, and DU AI Strategy Credentials
- Canonical Navy #17365D headers, light-blue #5B9BD5 accents, and hyperlinked LinkedIn and AI Guardians portal text
"""
import sys
import html
from pathlib import Path
sys.path.insert(0, 'src')

from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = Path("/Volumes/SanDiskOne/AI Projects/Gumloop/resume-agent-migration/output/KaiHonua_Management_Analyst")

def get_option1_paragraphs():
    """Option 1: Executive Hybrid Format (Summary Paragraph + 3 Impact Pillars)."""
    return [
        # Candidate Header Name
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36}]},
        # Subtitle Line
        {"align": "center", "space_after": 40, "text_runs": [{"text": "MANAGEMENT ANALYST | FEDERAL TRANSFORMATION & DATA ARCHITECTURE", "bold": True, "color": "17365D", "size": 19}]},
        # Contact Line with Hyperlinks
        {
            "align": "center", "space_after": 100, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • Open to Hybrid • ", "size": 18, "color": "1F1F1F"},
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
                "text": "Senior Management Analyst and Federal Transformation Lead with 20+ years of experience optimizing enterprise business operations, financial workflows, and data architecture across federal and commercial sectors. Proven track record managing GS-13-level contracting operations for the U.S. Department of the Interior, coupled with Acxiom data modeling experience and a University of Denver Graduate Certificate in AI Strategy to drive digital transformation, ROI modeling, and process automation.",
                "size": 19, "color": "1F1F1F"
            }]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Federal Operations & Systems Leadership: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "14 years as Senior Analyst Lead and Unison PRISM Administrator at the DOI IBC Acquisition Directorate; architected Department-wide FBMS data conversion migrating 12 legacy databases.", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Financial Realignment & Cost Recovery: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Reclaimed $1M+ in recurring annual savings through contract funds deobligation, executed funds realignment, and mediated vendor IPAC billing disputes.", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "• Data Analytics & AI Transformation: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Built Citibank's first Online Identity Scoring Model at Acxiom; authored enterprise AI roadmaps, healthcare LLM risk frameworks, and user training enabling 85+ cohort users.", "size": 18}
            ]
        },
        # CORE COMPETENCIES (Categorized Groupings for Clarity)
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Federal Acquisition & Operations: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Unison PRISM Admin • SAP FBMS Support • GS-13 Contracting Operations • Defense Award Exemptions • FAR & FPDS Compliance", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Data Engineering & Analytics: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Funds Realignment ($1M+ Reclaimed) • Oracle PL/SQL & ETL Architecture • SQL & Tableau Reporting • Acxiom Identity Data Modeling", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "AI Strategy & Transformation: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "DU AI Strategy Certificate • RAG & Agentic Workflows • LLM Risk & Governance • Cohort Training & User Enablement (85+ Trained)", "size": 18}
            ]
        },
        # AI STRATEGY & TRANSFORMATION PORTFOLIO
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "AI STRATEGY & TRANSFORMATION PORTFOLIO - Denver, CO | Sep 2025", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Internal AI enablement tooling: ", "size": 18, "bold": True}, {"text": "Career Advancement Agent * Gap Analysis SKILL, Fact Finding SubAgent", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• LLM risk assessment on ChatGPT Health: ", "size": 18, "bold": True}, {"text": "Privacy, governance, compliance, and ethical usage framing across 6 risk dimensions.", "size": 18}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• ", "size": 18},
                {"text": "AI Guardians", "size": 18, "bold": True, "color": "17365D", "url": "https://portal.aiguardiansllc.us/"},
                {"text": " AI Transformation Services: AI readiness, governance and risk, use-case prioritization, ROI, vendor evaluation, policy, Agent oversight.", "size": 18}
            ]
        },
        {"space_after": 40, "text_runs": [{"text": "• Enterprise AI roadmap: ", "size": 18, "bold": True}, {"text": "Authored 3-year enterprise AI strategy for Mile High Logistics covering maturity assessment, opportunity identification, budgeting, ROI modeling, and executive strategy communication.", "size": 18}]},
        # PROFESSIONAL EXPERIENCE
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 20}]},
        {"bg_color": "EBF1F5", "space_before": 60, "space_after": 40, "text_runs": [{"text": "PROGRAM ANALYST, ACQUISITIONS DIRECTORATE | U.S. DEPARTMENT OF THE INTERIOR\tDenver, CO | Jan–Sep 2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Senior operational and functional lead for the Acquisition Directorate's contracting business operations, serving as top escalation resource for mission-critical acquisition and financial systems in a GS-13-level environment.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Owned enterprise application support for mission-critical procurement and financial systems, keeping them compliant, secure, and available under strict federal data-governance requirements.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as senior escalation resource for system issues impacting contracting operations, coordinating incident resolution across technical and business teams to shorten time-to-resolution.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Delivered targeted user training and operational guidance that improved system adoption and reduced repeat support requests across the directorate.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SENIOR ANALYST CONSULTANT | ARKSOLUTIONS — CLIENT: IBC ACQUISITION DIRECTORATE\tDenver, CO | 2011–2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Architected DOI FBMS data conversion and translated complex business requirements into integrated enterprise workflows; recognized with two Department of the Interior awards.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Reclaimed $1M+ in recurring annual savings through government contract funds deobligation, executing funds realignment that resolved financial discrepancies between contracting officials and service providers.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as Unison PRISM administrator for seven years, overseeing access management, data integrity, procurement workflows, and stakeholder support across the Acquisition Directorate.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Resolved 5 to 10 mission-critical business issues daily through root-cause analysis, workflow correction, testing, and cross-functional coordination.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Designed and delivered operational training for 85+ users, improving adoption and reducing repeat support demand.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Chief POC for IPP Payment, Vendor Invoicing, Accounts Payable, and Core Financials Funds Management; mediated aviation vendor IPAC billing disputes.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Supported contracting officials with special FBMS defense award exemption procedures and assisted with DARPA project contract modifications.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SOLUTIONS DEVELOPER / SOLUTION ARCHITECT | ACXIOM CORPORATION\t1999–2010", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Built Citibank's first Online Identity Scoring Model (early AI/ML) and provided production support for the Application Verification System (AVS).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Supported customer identity-verification solutions for financial-services and insurance clients; gathered requirements, analyzed customer data needs, and designed Oracle data warehouses.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Standardized company-wide SDLC/SCM methodology and led cross-functional process-improvement teams.", "size": 18}]},
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 18}, {"text": " : University of Denver", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "M.S. & B.S., Computer Science", "bold": True, "color": "17365D", "size": 18}, {"text": " : St. Joseph's College", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "LLM & Agentic AI", "bold": True, "color": "17365D", "size": 18}, {"text": " : Harvard School of Engineering and Applied Sciences", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Awards: ", "bold": True, "color": "C00000", "size": 18}, {"text": "Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award", "size": 18}]},
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "AI Toolset: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Azure OpenAI APIs, Microsoft Copilot, RAG, agentic AI workflows, Claude, Cursor, Qdrant, REST APIs", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Data & Analytics: ", "bold": True, "color": "17365D", "size": 18}, {"text": "SQL, Python, PL/SQL, Apache Spark, PySpark, Tableau, Matplotlib, NumPy, Jupyter, ETL", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Enterprise & Systems: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Oracle, SQL Server, Sybase, SAP S/4, Unison PRISM, FBMS, IPP, Application Verification System", "size": 18}]}
    ]

def get_option3_paragraphs():
    """Option 3: Matrix Callout Format (Summary + 4 Key Contribution Areas)."""
    return [
        # Candidate Header Name
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36}]},
        # Subtitle Line
        {"align": "center", "space_after": 40, "text_runs": [{"text": "MANAGEMENT ANALYST | FEDERAL ACQUISITIONS & DATA ARCHITECTURE", "bold": True, "color": "17365D", "size": 19}]},
        # Contact Line with Hyperlinks
        {
            "align": "center", "space_after": 100, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • Open to Hybrid • ", "size": 18, "color": "1F1F1F"},
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
            "space_after": 80,
            "text_runs": [{
                "text": "High-impact Management Analyst offering 20+ years of expertise translating complex business, policy, and data priorities into streamlined federal acquisition, financial, and AI technology solutions. Proven GS-13-level operational lead adept at architecting enterprise system conversions, resolving daily escalations, building AI roadmaps, and aligning cross-functional stakeholders.",
                "size": 19, "color": "1F1F1F"
            }]
        },
        # MATRIX CALLOUTS (4 Key Contribution Areas)
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Federal Acquisition & Systems Admin: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "14-year Senior Analyst Lead at DOI IBC; 7-year Unison PRISM Administrator; defense award exemption lead.", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Financial Realignment & Cost Recovery: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Reclaimed $1M+ in recurring annual savings through contract funds deobligation; mediated IPAC billing disputes.", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Enterprise Data & Acxiom Analytics: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Architected DOI FBMS conversion (12 source DBs); built Citibank's first Online Identity Scoring Model at Acxiom.", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "• AI Strategy & User Enablement: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "DU AI Strategy Certificate; developed Mile High Logistics AI roadmap & cohort training for 85+ users.", "size": 18}
            ]
        },
        # CORE COMPETENCIES (Categorized Groupings for Clarity)
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Federal Acquisition & Operations: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Unison PRISM Admin • SAP FBMS Support • GS-13 Contracting Operations • Defense Award Exemptions • FAR & FPDS Compliance", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Data Engineering & Analytics: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Funds Realignment ($1M+ Reclaimed) • Oracle PL/SQL & ETL Architecture • SQL & Tableau Reporting • Acxiom Identity Data Modeling", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "AI Strategy & Transformation: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "DU AI Strategy Certificate • RAG & Agentic Workflows • LLM Risk & Governance • Cohort Training & User Enablement (85+ Trained)", "size": 18}
            ]
        },
        # AI STRATEGY & TRANSFORMATION PORTFOLIO
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "AI STRATEGY & TRANSFORMATION PORTFOLIO - Denver, CO | Sep 2025", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Internal AI enablement tooling: ", "size": 18, "bold": True}, {"text": "Career Advancement Agent * Gap Analysis SKILL, Fact Finding SubAgent", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• LLM risk assessment on ChatGPT Health: ", "size": 18, "bold": True}, {"text": "Privacy, governance, compliance, and ethical usage framing across 6 risk dimensions.", "size": 18}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• ", "size": 18},
                {"text": "AI Guardians", "size": 18, "bold": True, "color": "17365D", "url": "https://portal.aiguardiansllc.us/"},
                {"text": " AI Transformation Services: AI readiness, governance and risk, use-case prioritization, ROI, vendor evaluation, policy, Agent oversight.", "size": 18}
            ]
        },
        {"space_after": 40, "text_runs": [{"text": "• Enterprise AI roadmap: ", "size": 18, "bold": True}, {"text": "Authored 3-year enterprise AI strategy for Mile High Logistics covering maturity assessment, opportunity identification, budgeting, ROI modeling, and executive strategy communication.", "size": 18}]},
        # PROFESSIONAL EXPERIENCE
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 20}]},
        {"bg_color": "EBF1F5", "space_before": 60, "space_after": 40, "text_runs": [{"text": "PROGRAM ANALYST, ACQUISITIONS DIRECTORATE | U.S. DEPARTMENT OF THE INTERIOR\tDenver, CO | Jan–Sep 2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Senior operational and functional lead for the Acquisition Directorate's contracting business operations, serving as top escalation resource for mission-critical acquisition and financial systems in a GS-13-level environment.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Owned enterprise application support for mission-critical procurement and financial systems, keeping them compliant, secure, and available under strict federal data-governance requirements.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as senior escalation resource for system issues impacting contracting operations, coordinating incident resolution across technical and business teams to shorten time-to-resolution.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Delivered targeted user training and operational guidance that improved system adoption and reduced repeat support requests across the directorate.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SENIOR ANALYST CONSULTANT | ARKSOLUTIONS — CLIENT: IBC ACQUISITION DIRECTORATE\tDenver, CO | 2011–2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Architected DOI FBMS data conversion and translated complex business requirements into integrated enterprise workflows; recognized with two Department of the Interior awards.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Reclaimed $1M+ in recurring annual savings through government contract funds deobligation, executing funds realignment that resolved financial discrepancies between contracting officials and service providers.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as Unison PRISM administrator for seven years, overseeing access management, data integrity, procurement workflows, and stakeholder support across the Acquisition Directorate.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Resolved 5 to 10 mission-critical business issues daily through root-cause analysis, workflow correction, testing, and cross-functional coordination.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Designed and delivered operational training for 85+ users, improving adoption and reducing repeat support demand.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Chief POC for IPP Payment, Vendor Invoicing, Accounts Payable, and Core Financials Funds Management; mediated aviation vendor IPAC billing disputes.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Supported contracting officials with special FBMS defense award exemption procedures and assisted with DARPA project contract modifications.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SOLUTIONS DEVELOPER / SOLUTION ARCHITECT | ACXIOM CORPORATION\t1999–2010", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Built Citibank's first Online Identity Scoring Model (early AI/ML) and provided production support for the Application Verification System (AVS).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Supported customer identity-verification solutions for financial-services and insurance clients; gathered requirements, analyzed customer data needs, and designed Oracle data warehouses.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Standardized company-wide SDLC/SCM methodology and led cross-functional process-improvement teams.", "size": 18}]},
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 18}, {"text": " : University of Denver", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "M.S. & B.S., Computer Science", "bold": True, "color": "17365D", "size": 18}, {"text": " : St. Joseph's College", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "LLM & Agentic AI", "bold": True, "color": "17365D", "size": 18}, {"text": " : Harvard School of Engineering and Applied Sciences", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Awards: ", "bold": True, "color": "C00000", "size": 18}, {"text": "Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award", "size": 18}]},
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "AI Toolset: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Azure OpenAI APIs, Microsoft Copilot, RAG, agentic AI workflows, Claude, Cursor, Qdrant, REST APIs", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Data & Analytics: ", "bold": True, "color": "17365D", "size": 18}, {"text": "SQL, Python, PL/SQL, Apache Spark, PySpark, Tableau, Matplotlib, NumPy, Jupyter, ETL", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Enterprise & Systems: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Oracle, SQL Server, Sybase, SAP S/4, Unison PRISM, FBMS, IPP, Application Verification System", "size": 18}]}
    ]

if __name__ == "__main__":
    opt1_docx = create_docx(OUTPUT_DIR / "Ebenezer_Rolston_KaiHonua_Resume_Option1_ExecutiveHybrid.docx", get_option1_paragraphs())
    opt3_docx = create_docx(OUTPUT_DIR / "Ebenezer_Rolston_KaiHonua_Resume_Option3_MatrixCallout.docx", get_option3_paragraphs())
    print("SUCCESSFULLY GENERATED BOTH OPTION 1 AND OPTION 3 DOCX RESUMES!")
    print("Option 1 DOCX:", opt1_docx)
    print("Option 3 DOCX:", opt3_docx)
