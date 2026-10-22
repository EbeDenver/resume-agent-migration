"""Generate complete application deliverables for Business Process Technology Senior Analyst at Black & Veatch.

Applies:
- Candidate Name: Ebenezer J. Rolston (26pt bold navy #17365D)
- Subtitle: BUSINESS PROCESS TECHNOLOGY SENIOR ANALYST | WORKFLOW & DATA AUTOMATION (#17365D)
- Contact Line: Denver, CO • Open to Hybrid/Onsite (Greenwood Village, CO) • eberolston@yahoo.com • 501-307-3237 • LinkedIn • AI Guardians
  with real embedded hyperlinks for LinkedIn and AI Guardians portal!
- Navy Section Headings with bottom border line (#17365D)
- Shaded Role Title Bars (#EBF1F5 light blue background shading)
- De-cluttered Core Competencies (3 categorized groupings)
- Tailored for Black & Veatch Req ID 117315
"""
import sys
from pathlib import Path
sys.path.insert(0, 'src')

from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = Path("/Volumes/SanDiskOne/AI Projects/Gumloop/resume-agent-migration/output/Black_Veatch_Business_Process_Technology_Senior_Analyst")

def build_resume_docx():
    paragraphs = [
        # Candidate Header Name
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36}]},
        # Subtitle Line
        {"align": "center", "space_after": 40, "text_runs": [{"text": "BUSINESS PROCESS TECHNOLOGY SENIOR ANALYST | WORKFLOW & DATA AUTOMATION", "bold": True, "color": "17365D", "size": 19}]},
        # Contact Line with Hyperlinks
        {
            "align": "center", "space_after": 100, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • Greenwood Village Onsite Available • ", "size": 18, "color": "1F1F1F"},
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
                "text": "Accomplished Business Process Technology Senior Analyst with 20+ years translating complex operational requirements into scalable data, reporting, and workflow automation solutions across federal and commercial enterprises. Proven track record architecting Department-wide system data conversions, building Power BI and Tableau operational dashboards, and automating business workflows. Pairs deep SQL, Oracle PL/SQL, and ERP systems experience with a University of Denver Graduate Certificate in AI Strategy to design modern process improvements, evaluate emerging technologies, and deliver high-adoption user enablement.",
                "size": 19, "color": "1F1F1F"
            }]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Business Process & Requirements Translation: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "20+ years partnering with business stakeholders to map current-state workflows, define functional specifications, and implement technology solutions across 12 legacy databases at DOI and Acxiom.", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Reporting, Dashboards & Analytics: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Built Power BI reports on contracting status, obligations, and financials; connected Tableau with calculated fields to enterprise ERP data sources; strong SQL and relational data modeling proficiency.", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "• Workflow Automation & User Enablement: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Created browser-based automation tools on the AI Guardians portal; designed cohort training programs for 85+ users that measurably reduced recurring support tickets; evaluated RPA and AI tool adoption.", "size": 18}
            ]
        },
        # CORE COMPETENCIES (Categorized Groupings)
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Business Process & Solution Analysis: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Requirements Elicitation • Process Workflow Reengineering • Functional Specifications • SDLC / Agile Delivery • Stakeholder Collaboration", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Data Analytics & Enterprise Reporting: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Power BI Reporting • Tableau Dashboards • SQL & Oracle PL/SQL • Relational Data Modeling • ETL Pipelines • Star Schema Warehousing", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "Technology Enablement & Modernization: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "DU AI Strategy Certificate • Emerging AI Evaluation & Roadmapping • User Training & Cohort Enablement (85+ Trained) • Remedy Incident Management", "size": 18}
            ]
        },
        # AI & TECHNOLOGY TRANSFORMATION PORTFOLIO
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "TECHNOLOGY & PROCESS AUTOMATION PORTFOLIO - Denver, CO | Sep 2025", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• ", "size": 18},
                {"text": "AI Guardians", "size": 18, "bold": True, "color": "17365D", "url": "https://portal.aiguardiansllc.us/"},
                {"text": " Process Planning Tools: Built browser-based planning tools including Use-Case Prioritization Canvas, AI ROI / Cost Estimator, and Vendor Evaluation Scorecard.", "size": 18}
            ]
        },
        {"space_after": 40, "text_runs": [{"text": "• Enterprise Technology Roadmap: ", "size": 18, "bold": True}, {"text": "Authored 3-year enterprise technology and AI strategy for Mile High Logistics covering maturity assessment, readiness analysis, budgeting, and ROI modeling.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Document Extraction & Automation MVP: ", "size": 18, "bold": True}, {"text": "Built multimodal document processing and structured extraction workflow using Python, Pydantic schemas, and LangGraph conditional routing.", "size": 18}]},
        # PROFESSIONAL EXPERIENCE
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 20}]},
        {"bg_color": "EBF1F5", "space_before": 60, "space_after": 40, "text_runs": [{"text": "PROGRAM ANALYST, ACQUISITIONS DIRECTORATE | U.S. DEPARTMENT OF THE INTERIOR\tDenver, CO | Jan–Sep 2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Senior operational and functional lead analyzing business process workflows and translating policy needs into technical improvements in a highly regulated environment.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Built Power BI reports tracking contracting status, invoices, obligations, and core financials, giving leadership clear visibility into operational performance.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Coordinated incident resolution between technical and business teams, analyzing root causes to optimize business systems and shorten resolution times.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Delivered operational guidance and user enablement that drove system adoption and lowered repeat support requests across the directorate.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SENIOR ANALYST CONSULTANT | ARKSOLUTIONS — CLIENT: IBC ACQUISITION DIRECTORATE\tDenver, CO | 2011–2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Architected DOI FBMS enterprise data conversion as ETL Architect, gathering requirements across 12 bureau databases and translating them into integrated system workflows (awarded 2 DOI Excellence Awards).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Developed and maintained Tableau dashboards with calculated fields connected directly to FBMS enterprise ERP data sources for executive reporting.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Designed and delivered operational and cohort training for 85+ users, creating documentation and training materials that significantly reduced Remedy helpdesk tickets.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Reclaimed $1M+ in recurring annual savings through contract funds deobligation, and performed funds realignment resolving complex financial discrepancies between contracting officials and vendors.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as Unison PRISM administrator for 7 years, managing user access, data integrity oversight, and workflow administration.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Participated in user testing of a robotic process automation (RPA) solution and tested SAP S/4 and PRISM system enhancements.", "size": 18}]},
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SOLUTIONS DEVELOPER / SOLUTION ARCHITECT | ACXIOM CORPORATION\t1999–2010", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Interviewed financial-services and insurance clients (Citibank, Allstate) to gather business requirements, analyze customer prospecting needs, and architect customized data solutions.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Designed Oracle data warehouses, ETL data pipelines, relational data models, and star schemas behind multichannel marketing and fraud verification platforms.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Standardized company-wide SDLC/SCM methodology as a process-improvement specialist on the Acxiom Methodology Board, leading cross-functional teams across PMO, project managers, and technical SMEs.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Built Citibank's first Online Identity Scoring Model and directed senior developers in building and demonstrating the nation's first airline passenger-screening prototype to Congress.", "size": 18}]},
        # EDUCATION & CREDENTIALS
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 18}, {"text": " : University of Denver", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "M.S. & B.S., Computer Science", "bold": True, "color": "17365D", "size": 18}, {"text": " : St. Joseph's College", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "LLM & Agentic AI", "bold": True, "color": "17365D", "size": 18}, {"text": " : Harvard School of Engineering and Applied Sciences", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Machine Learning & Deep Learning", "bold": True, "color": "17365D", "size": 18}, {"text": " : UC Berkeley", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Awards: ", "bold": True, "color": "C00000", "size": 18}, {"text": "Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award", "size": 18}]},
        # TECHNICAL PROFICIENCIES
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "Data & Reporting: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Power BI (reporting & dashboards), Tableau (calculated fields & ERP connections), SQL, Oracle PL/SQL, Excel (VLOOKUP, Macros)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Process & Automation: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Requirements Gathering, Workflow Reengineering, SDLC, Agile/Scrum, RPA Testing, Streamlit, LangGraph", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Enterprise Systems: ", "bold": True, "color": "17365D", "size": 18}, {"text": "SAP S/4HANA (modules & reporting), Unison PRISM, Oracle DB, SQL Server, Remedy Incident Management", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "AI & Emerging Tech: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Microsoft Copilot, Azure OpenAI APIs, RAG, Agentic AI, AI Maturity Roadmapping, LLM Risk Assessment", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Ebenezer_Rolston_Black_Veatch_Resume.docx", paragraphs)

def build_cover_letter_docx():
    paragraphs = [
        {"align": "left", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 28}]},
        {"align": "left", "space_after": 20, "text_runs": [{"text": "Business Process Technology Senior Analyst Candidate", "color": "17365D", "size": 20}]},
        {
            "align": "left", "space_after": 120, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • ", "size": 18},
                {"text": "eberolston@yahoo.com", "size": 18},
                {"text": " • 501-307-3237 • ", "size": 18},
                {"text": "AI Guardians", "size": 18, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"}
            ]
        },
        {"space_after": 100, "text_runs": [{"text": "2026-10-12", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Hiring Team", "bold": True, "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Black & Veatch Family of Companies", "size": 19}]},
        {"space_after": 100, "text_runs": [{"text": "Greenwood Village, CO", "size": 19}]},
        {"space_after": 120, "text_runs": [{"text": "RE: Business Process Technology Senior Analyst (Req ID: 117315)", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Dear Hiring Team,", "size": 19}]},
        {
            "space_after": 100,
            "text_runs": [{
                "text": "Thank you for considering my application for the Business Process Technology Senior Analyst role at the Black & Veatch Family of Companies. With over 20 years of experience translating complex business and operational needs into technology-enabled solutions across enterprise data architectures, reporting dashboards, and automated workflows—and as a Denver-area resident available to work on-site in Greenwood Village—I am eager to contribute to Black & Veatch’s employee-owned culture and continuous process improvement initiatives.",
                "size": 19
            }]
        },
        {
            "space_after": 100,
            "text_runs": [{
                "text": "Throughout my career as a Senior Analyst Lead supporting federal acquisition and enterprise financial operations, I have specialized in bridging the gap between business stakeholders and technical execution. At the Department of the Interior’s Acquisition Directorate, I architected the Department-wide FBMS data conversion across 12 legacy databases, built operational Power BI and Tableau dashboards for contracting obligations and financials, and analyzed complex workflows to eliminate bottlenecks. Earlier at Acxiom, I led cross-functional process improvement initiatives on the Acxiom Methodology Board, gathered requirements from financial-services clients to design Oracle data warehouses, and built predictive analytics models that prevented significant fraud.",
                "size": 19
            }]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "In addition to core data and process analysis, I recently completed a graduate certificate in AI Strategy at the University of Denver, where I formulated enterprise technology roadmaps, ROI business cases, and workflow automation frameworks—including practical web tools for my small business project, ", "size": 19},
                {"text": "AI Guardians", "size": 19, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"},
                {"text": ". Combined with my background designing cohort training for 85+ users that measurably reduced helpdesk ticket volume, I am well-prepared to evaluate emerging business technologies and drive high-adoption solution rollouts for Black & Veatch teams.", "size": 19}
            ]
        },
        {
            "space_after": 120,
            "text_runs": [{
                "text": "I am fully available to work on-site in Greenwood Village, CO, and the stated Colorado salary range of $95,612–$167,332 is completely acceptable. I look forward to discussing how my enterprise process reengineering, data analysis, and user enablement experience align with Black & Veatch’s priorities, and I respectfully request your feedback on my candidacy if another applicant is chosen. Thank you for your consideration.",
                "size": 19
            }]
        },
        {"space_after": 80, "text_runs": [{"text": "Sincerely,", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 20}]}
    ]
    return create_docx(OUTPUT_DIR / "Cover_Letter_Ebenezer_Rolston_Black_Veatch.docx", paragraphs)

def build_interview_prep_docx():
    paragraphs = [
        {"align": "center", "space_after": 40, "text_runs": [{"text": "Interview Preparation Package: Business Process Technology Senior Analyst", "bold": True, "color": "17365D", "size": 24}]},
        {"space_after": 100, "bottom_border": True, "text_runs": [{"text": "Company: Black & Veatch • Req ID: 117315 • Location: Greenwood Village, CO • Candidate: Ebenezer J. Rolston", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. COMPANY & ROLE BRIEF", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Company Profile: ", "bold": True, "color": "008000", "size": 18}, {"text": "Black & Veatch is a 100% employee-owned global engineering, procurement, consulting, and construction (EPC) company founded in 1915, specializing in critical human infrastructure (power, water, telecommunications, government services).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• ESOP Culture: ", "bold": True, "color": "008000", "size": 18}, {"text": "As an employee-owned enterprise, accountability, stewardship, long-term sustainability, and collaborative continuous improvement are core organizational values.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Role Focus: ", "bold": True, "color": "008000", "size": 18}, {"text": "Partner with business stakeholders to formulate systems scope, translate business needs into technology solutions (Power BI, SQL, workflows), and guide less-experienced analysts.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. CANDIDATE FIT NARRATIVE & GAP MAP", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Direct Strengths: ", "bold": True, "color": "008000", "size": 18}, {"text": "20+ years requirements elicitation and workflow analysis; Power BI & Tableau reporting on enterprise data; Oracle PL/SQL & ETL data modeling; cohort training for 85+ users with measured ticket reduction; Denver-area resident available onsite in Greenwood Village, CO.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Honest Learning Bridge (Do Not Over-Claim): ", "bold": True, "color": "C00000", "size": 18}, {"text": "Candidate has strong Power BI reporting and SQL experience, but does NOT claim advanced DAX or Power Platform canvas apps (Power Apps/Power Automate). Candidate frames automation strength through Python/LangGraph workflows, browser-based AI planning tools, and willingness to adapt to Black & Veatch's preferred low-code toolchain.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. 60–90 SECOND SPOKEN ELEVATOR PITCH", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Hello, I'm Ebenezer Rolston. Over the past 20 years, I've specialized in translating complex business operations and data requirements into streamlined enterprise solutions. In my recent roles supporting the Department of the Interior's Acquisition Directorate, I led business process analysis, built operational Power BI and Tableau dashboards for financial obligations, and architected an enterprise data conversion across 12 legacy databases. I also recently completed a graduate certificate in AI Strategy at the University of Denver, where I formulated enterprise technology roadmaps and workflow automation tools. What excites me about Black & Veatch is your collaborative, employee-owned culture and the opportunity to help your Greenwood Village teams optimize business processes through modern data, reporting, and automation capabilities.", "italic": True, "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "4. STAR STORY BANK", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 1: Enterprise Data Conversion & Process Mapping (DOI FBMS): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Gathered functional requirements across 12 bureaus, defined translation rules, and migrated legacy systems into a unified ERP platform, winning 2 Interior Department Awards.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 2: Reporting Dashboards & Metric Optimization (Power BI & Tableau): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Built Power BI reports on contracting status and invoices; connected Tableau to FBMS data sources, resolving financial discrepancies and reclaiming $1M+ annually.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 3: User Training & Helpdesk Ticket Reduction: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Designed cohort training for 85+ users; analyzed Remedy ticket patterns to target user confusion, resulting in measurable drops in recurring support volume.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "5. CURATED READING LIST", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Black & Veatch Company Profile & ESOP: ", "bold": True, "color": "17365D", "url": "https://www.bv.com"}, {"text": " — Review company mission, 100% employee ownership model, and global infrastructure projects.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• AI Guardians Planning Tools: ", "bold": True, "color": "17365D", "url": "https://portal.aiguardiansllc.us/"}, {"text": " — Practical AI transformation and workflow planning toolset.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• B&V Sustainability & Technology Report: ", "bold": True, "color": "17365D", "url": "https://www.bv.com/about-us/sustainability"}, {"text": " — Connect process technology improvements to corporate ESG and digital delivery goals.", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Interview_Preparation_Black_Veatch.docx", paragraphs)

def build_analysis_docx():
    paragraphs = [
        {"align": "center", "space_after": 40, "text_runs": [{"text": "Skill Gap Analysis: Business Process Technology Senior Analyst — Black & Veatch", "bold": True, "color": "17365D", "size": 24}]},
        {"space_after": 100, "bottom_border": True, "text_runs": [{"text": "Candidate: Ebenezer J. Rolston • Match Score: 85/100 • Interview Probability: 82/100 • Location: Greenwood Village, CO", "bold": True, "color": "17365D", "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. FIT SUMMARY", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Ebenezer J. Rolston offers 20+ years of senior business process analysis, requirements translation, and data solution delivery experience. His demonstrated capability building Power BI and Tableau operational reports, architecting enterprise data conversions (12 legacy databases to ERP), training 85+ cohort users, and applying University of Denver AI Strategy frameworks aligns strongly with Black & Veatch's Business Process Technology Senior Analyst mandate in Greenwood Village, CO.", "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. SKILL MATCH MATRIX", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Business Process & Requirements Analysis: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Evidence - 20+ years across DOI FBMS & Acxiom SDLC Board)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• SQL & Relational Database Concepts: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Evidence - SQL, Oracle PL/SQL, ETL data pipelines, star schemas)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Power BI & Operational Dashboards: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Evidence - Built Power BI status/invoice reports & Tableau calculated fields)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• User Enablement & Training: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Direct Evidence - Trained 85+ users; measurably lowered Remedy helpdesk tickets)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Emerging Technology & AI Fluency: ", "bold": True, "color": "008000", "size": 18}, {"text": "Matched (Graduate Portfolio - DU AI Strategy Certificate, AI planning tools, Copilot user)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Power Automate / Power Apps Canvas Apps: ", "bold": True, "color": "C00000", "size": 18}, {"text": "Partial / Honest Learning Bridge (Candidate does not claim Power Apps/DAX; bridges via Python/LangGraph automation and fast adaptability)", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. LOGISTICS ALIGNMENT", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Onsite Availability: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Confirmed available to work on-site in Greenwood Village, CO for the first 90 days.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Background & Checks: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Background check, drug screen, and motor-vehicle records check ready.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Compensation: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Stated Colorado range of $95,612–$167,332 is fully acceptable.", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Analysis_Black_Veatch.docx", paragraphs)

if __name__ == "__main__":
    r_path = build_resume_docx()
    c_path = build_cover_letter_docx()
    i_path = build_interview_prep_docx()
    a_path = build_analysis_docx()
    print("ALL 4 BLACK & VEATCH NATIVE .DOCX FILES CREATED!")
