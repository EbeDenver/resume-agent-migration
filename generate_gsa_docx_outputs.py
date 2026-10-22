"""Generate native Microsoft Word (.docx) documents for all 4 GSA Program Analyst (Data Analytics) deliverables.

Follows the approved visual reference system (resume-format-standard-2 / consultant-style):
- Candidate Name: Ebenezer J. Rolston (20pt/36hpt bold navy #17365D, Cambria)
- Target Role Subtitle: PROGRAM ANALYST (DATA ANALYTICS) — GS-0343-13 (11pt/22hpt light blue #5B9BD5, Cambria)
- Contact Line: Denver, CO • 501-307-3237 • eberolston@yahoo.com • LinkedIn • AI Guardians
  with embedded hyperlinks for LinkedIn and AI Guardians portal!
- Navy Section Headings with bottom border rule (#17365D)
- Shaded Role Title Bars (#EBF1F5 light blue background shading)
- Clean single-column ATS typography with 0.50" top/bottom and 0.62" left/right margins
- Standard candidate-first formatting
"""
import sys
from pathlib import Path
sys.path.insert(0, 'src')

from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = Path("/Volumes/SanDiskOne/AI Projects/Gumloop/resume-agent-migration/output/GSA_Program_Analyst_Data_Analytics")

def build_resume_docx():
    paragraphs = [
        # Candidate Header Name
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36, "font": "Cambria"}]},
        # Subtitle Line
        {"align": "center", "space_after": 40, "text_runs": [{"text": "PROGRAM ANALYST (DATA ANALYTICS) — GS-0343-13", "bold": True, "color": "5B9BD5", "size": 22, "font": "Cambria"}]},
        # Contact Line with Hyperlinks
        {
            "align": "center", "space_after": 40, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • 501-307-3237 • ", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": "eberolston@yahoo.com", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": " • ", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": "LinkedIn", "size": 18, "color": "17365D", "bold": True, "font": "Cambria", "url": "https://www.linkedin.com/in/ebenezer-rolston/"},
                {"text": " • ", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": "AI Guardians Portal", "size": 18, "color": "17365D", "bold": True, "font": "Cambria", "url": "https://portal.aiguardiansllc.us/"}
            ]
        },
        # Metadata banner
        {
            "align": "center", "space_after": 100,
            "text_runs": [
                {"text": "U.S. Citizen • Public Trust Eligible (Previously Held) • Preferred Location: Lakewood, CO (Open to All Listed)", "size": 17, "color": "4F4F4F", "font": "Times New Roman"}
            ]
        },

        # PROFESSIONAL SUMMARY
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {
            "space_after": 60,
            "text_runs": [{
                "text": "Results-driven Program Analyst (Data Analytics) with 20+ years of enterprise data analysis, business intelligence reporting, and operational transformation experience across federal acquisition and commercial financial environments. Proven GS-13-equivalent track record manipulating and processing large streams of operational and financial data within complex federal ERP systems (SAP S/4 / FBMS and Unison PRISM). Expert in designing SQL-based data queries, conducting structured financial reconciliations, performing helpdesk incident trend analytics, and delivering executive-ready decision-support reports that reclaimed $1M+ annually in deobligated contract funds. Bridges operational and analytical domains by combining rigorous Department of the Interior (DOI) acquisition data governance with advanced graduate-level training in AI strategy and exploratory data visualization. Experienced briefing senior leadership, Contracting Officers (COs), and Contracting Officer's Representatives (CORs) to streamline operations, enhance supplier and customer engagement, and drive mission-critical business transformation.",
                "size": 19, "color": "1F1F1F"
            }]
        },

        # CORE COMPETENCIES
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {
            "space_after": 30,
            "text_runs": [
                {"text": "Data Analytics & BI Reporting: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": "SQL Querying • SAP Financial Reporting (FBL1N, ME2M, FAGLL03, ZFI) • Operational Metrics • Trend Analysis", "size": 18}
            ]
        },
        {
            "space_after": 30,
            "text_runs": [
                {"text": "Decision-Support & Briefings: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": "Executive Briefings • Data-Driven Recommendations • Stakeholder Reporting • Leadership Dashboards", "size": 18}
            ]
        },
        {
            "space_after": 30,
            "text_runs": [
                {"text": "Operational Data Manipulation & ETL: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": "Complex Datasets • Data Harmonization • ETL Architecture • Discrepancy Reconciliation • Root-Cause Analysis", "size": 18}
            ]
        },
        {
            "space_after": 30,
            "text_runs": [
                {"text": "Federal Acquisition & Financial Systems: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": "Federal Business Management System (SAP S/4 / FBMS) • Unison PRISM • FPDS • GSA Schedules • IPP • IPAC", "size": 18}
            ]
        },
        {
            "space_after": 30,
            "text_runs": [
                {"text": "Lifecycle & Operational Performance: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": "Funds Realignment & Deobligation ($1M+ Reclaimed) • Remedy Incident Trend Analytics • Supplier/Vendor Data Review", "size": 18}
            ]
        },
        {
            "space_after": 30,
            "text_runs": [
                {"text": "Exploratory Analytics & Visualization: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": "Exploratory Data Analysis (Tableau) • Academic Data Visualization (Matplotlib, Python) • Advanced Excel (Pivot Tables, VLOOKUP)", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "Data Governance & Quality: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": "Federal Data Integrity Oversight • System Conversion Validation • Standard Operating Procedures (SOPs)", "size": 18}
            ]
        },

        # PROFESSIONAL EXPERIENCE
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},

        # Role 1: DOI
        {"bg_color": "EBF1F5", "space_before": 60, "space_after": 20, "text_runs": [
            {"text": "Program Analyst (Contracting Business Operations / Data Analytics)", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"},
            {"text": " | U.S. Department of the Interior • Denver, CO | 01/2025 – 09/2025", "bold": True, "color": "5B9BD5", "size": 19, "font": "Cambria"}
        ]},
        {"space_after": 30, "text_runs": [{"text": "Senior GS-13-equivalent operational and functional lead for Acquisition Directorate contracting operations; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Performed broad technical data analysis across Department-wide procurement and financial databases to evaluate program performance, streamline directorate operations, and enhance customer service for federal acquisition stakeholders.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Executed SQL and ERP queries across FBMS (SAP) to extract, validate, and analyze operational procurement metrics, identifying process bottlenecks across contract award and administration workflows.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Extracted and formatted SAP financial reports—including open commitment reports, purchase order history, and general ledger line items—to provide Contracting Officers (COs) and Contracting Officer's Representatives (CORs) with real-time financial performance analytics.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Analyzed operational incident data from Remedy ticketing systems, identifying recurring system failures, isolating root causes, and delivering data-backed recommendations to management that reduced repeat support tickets.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Provided expert technical advice and analytical guidance to acquisition leadership regarding data integrity standards, procurement system interfaces, and federal data governance compliance.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 80, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Delivered briefings to senior management on operational data trends, system reliability metrics, and user adoption rates across enterprise contracting applications.", "size": 19}]},

        # Role 2: ArkSolutions / DOI IBC
        {"bg_color": "EBF1F5", "space_before": 80, "space_after": 20, "text_runs": [
            {"text": "Senior Analyst Consultant / Data Analytics & Systems Specialist", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"},
            {"text": " | ArkSolutions (Client: DOI IBC Acquisition Directorate) • Denver, CO | 01/2011 – 01/2025", "bold": True, "color": "5B9BD5", "size": 19, "font": "Cambria"}
        ]},
        {"space_after": 30, "text_runs": [{"text": "14-year senior analytics and data transformation engagement for Department-wide acquisition platforms; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Architected and executed the end-to-end DOI FBMS data conversion as ETL Architect, extracting, cleansing, transforming, and validating millions of legacy procurement and financial records into a unified SAP S/4 enterprise platform (recognized with 2 DOI Department Awards).", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Generated, formatted, and analyzed SAP financial reports—specifically FBL1N (Vendor Line Items), ME2M (Purchasing Documents by Material/Service), FAGLL03 (G/L Account Line Items), and custom ZFI reports—tracking obligations, commitments, disbursements, and unliquidated obligations (UDOs).", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Reclaimed $1M+ in recurring annual government funds by designing rigorous deobligation tracking models and funds realignment reports that resolved multi-year financial discrepancies between contracting officials, program offices, and service providers.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Conducted operational data analysis on IPAC billing files, resolving complex vendor and aviation charge-card billing disputes through structured reconciliation between agency ledgers and vendor transaction records.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Led continuous incident trend analysis on 5 to 10 daily complex FBMS and Unison PRISM operational escalations, identifying workflow defects and authoring corrective data procedures that prevented system-wide transaction failures.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Administered Unison PRISM data integrity and access governance for 7 years, auditing procurement workflow data across contract solicitations, awards, modifications, and compliance feeds (FPDS/SAM).", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Evaluated procurement trends involving GSA schedule contracts and defense acquisitions, assisting contracting officials with obligation tracking, purchase requisitions, and compliance reporting under federal acquisition regulations.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Designed and delivered data-driven cohort training and operational reference documentation for 85+ end users, translating complex ERP transaction procedures into actionable workflows that boosted data entry accuracy.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 80, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Prepared and presented comprehensive analytical briefings to executive leadership and the FBMS Software Advocacy Leadership Team (FSALT), supporting major IT modernizations (including S/4 migration and Realignment Builder initiatives).", "size": 19}]},

        # Role 3: Acxiom
        {"bg_color": "EBF1F5", "space_before": 80, "space_after": 20, "text_runs": [
            {"text": "Solutions Developer / Solution Architect & Data Analyst", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"},
            {"text": " | Acxiom Corporation • Little Rock, AR & Remote | 01/1999 – 12/2010", "bold": True, "color": "5B9BD5", "size": 19, "font": "Cambria"}
        ]},
        {"space_after": 30, "text_runs": [{"text": "High-volume data analytics models, predictive algorithms, and relational data warehousing; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Engineered high-volume data analytics models, predictive algorithms, and relational data warehouse structures processing multi-million-record operational and consumer transaction streams.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Designed Citibank’s first Online Identity Scoring Model utilizing early statistical analytics and machine learning techniques, analyzing application pattern datasets in real time to stop millions of dollars in fraudulent account losses.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Applied advanced analytical methods, SQL scripting, and database programming languages to manipulate, profile, and aggregate large streams of customer and financial transactional data.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Built cross-sell predictive data models and enterprise data warehouse schemas as Lead Solution Architect & ETL Analyst for financial institutions including GE Money, ChoicePoint, and Citibank.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Directed senior technical developers in building, validating, and presenting data analysis architectures for the nation's first airline passenger-screening data system, delivering live analytical briefings to U.S. Congressional stakeholders.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 80, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Standardized data quality frameworks and software development lifecycle (SDLC) processes across the enterprise as an appointed specialist on the Acxiom Methodology Board.", "size": 19}]},

        # PORTFOLIO SECTION
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "DATA ANALYTICS, BUSINESS INTELLIGENCE & ACADEMIC PORTFOLIO", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [
            {"text": "AI Guardians Transformation & Analytics Toolkit — ", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"},
            {"text": "Developer / Researcher (", "size": 18},
            {"text": "portal.aiguardiansllc.us", "size": 18, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"},
            {"text": ")", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Developed a modular 11-tool business intelligence and decision-support toolkit covering organizational readiness assessments, risk scoring algorithms, and ROI financial modeling canvases.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 50, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Built data evaluation models that quantify projected operational cost savings, efficiency gains, and technology adoption feasibility for enterprise IT and analytical modernization programs.", "size": 19}]},

        {"space_after": 20, "text_runs": [
            {"text": "Academic Data Analytics & Visualizations — ", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"},
            {"text": "University of Denver · Harvard SEAS · UC Berkeley", "italic": True, "color": "4F4F4F", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Exploratory Data Analysis (Tableau): Utilized Tableau for exploratory data discovery, querying multi-variable datasets to uncover correlations, distribution anomalies, and operational trends.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Statistical Programming & Data Visualization (Python & Matplotlib): Developed programmatic data analysis scripts using Python (NumPy, Pandas) and generated statistical charts and visualizations using Matplotlib.", "size": 19}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 30, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Enterprise Strategic Roadmaps: Authored an end-to-end 3-year strategic business transformation roadmap for Mile High Logistics, evaluating operational data flows, financial forecasting, and enterprise decision-support architecture.", "size": 19}]},

        # EDUCATION & CREDENTIALS
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": " : University of Denver", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Master of Science (M.S.), Computer Science", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": " : St. Joseph's College", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Bachelor of Science (B.S.), Computer Science", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": " : St. Joseph's College", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Executive Certificate, LLM & Agentic AI", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": " : Harvard School of Engineering and Applied Sciences", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Professional Program in Machine Learning & Deep Learning", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": " : University of California, Berkeley", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "AI Governance Certification", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": " : AI Tech and Privacy Academy", "size": 18}]},
        {"space_after": 80, "text_runs": [{"text": "Honors & Awards: ", "bold": True, "color": "C00000", "size": 18}, {"text": "Interior Business Center (IBC) Award for Excellence · DOI FBMS Special Recognition Award", "size": 18}]},

        # TECHNICAL PROFICIENCIES
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "Data Analytics & Reporting: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": "SQL, Relational Querying, SAP Financial Reports (FBL1N, ME2M, FAGLL03, ZFI), Financial Reconciliation, Trend Analysis, Root-Cause Analysis, Metrics Tracking", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Business Intelligence & Visualization: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": "Tableau (Exploratory Data Analysis), Matplotlib (Academic/Coursework), Microsoft Excel (Pivot Tables, VLOOKUP, Advanced Modeling)", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Enterprise ERP & Federal Platforms: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": "Federal Business Management System (SAP S/4 / FBMS), Unison PRISM, FPDS, SAM, IPP, Remedy Incident Management", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Programming & Data Tools (Coursework & Portfolio): ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": "Python, PySpark, Apache Spark, NumPy, Pandas, PL/SQL, C, Git/GitHub", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "Methodologies: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"}, {"text": "Agile/Scrum, Business Process Reengineering, ETL Data Conversion, Data Governance, Lifecycle Performance Evaluation", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Ebenezer_Rolston_GSA_Program_Analyst_Resume.docx", paragraphs)

def build_cover_letter_docx():
    paragraphs = [
        {"align": "left", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36, "font": "Cambria"}]},
        {"align": "left", "space_after": 20, "text_runs": [{"text": "PROGRAM ANALYST (DATA ANALYTICS) CANDIDATE — GS-0343-13", "color": "5B9BD5", "bold": True, "size": 22, "font": "Cambria"}]},
        {
            "align": "left", "space_after": 100, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • 501-307-3237 • ", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": "eberolston@yahoo.com", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": " • ", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": "LinkedIn", "size": 18, "color": "17365D", "bold": True, "font": "Cambria", "url": "https://www.linkedin.com/in/ebenezer-rolston/"},
                {"text": " • ", "size": 18, "color": "17365D", "font": "Cambria"},
                {"text": "AI Guardians Portal", "size": 18, "color": "17365D", "bold": True, "font": "Cambria", "url": "https://portal.aiguardiansllc.us/"}
            ]
        },
        {"space_after": 100, "text_runs": [{"text": "2026-10-12", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Hiring Manager", "bold": True, "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "General Services Administration (GSA)", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{"text": "Federal Acquisition Service (FAS)", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 120, "text_runs": [{"text": "RE: Program Analyst (Data Analytics) — Control Number 887843500", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 100, "text_runs": [{"text": "Dear Hiring Manager,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{"text": "Thank you for considering my application for the Program Analyst (Data Analytics) position (GS-0343-13) within the General Services Administration’s Federal Acquisition Service (FAS). With over 20 years of experience in federal program analysis, data transformation, and business operations analysis—including recent GS-13-equivalent service supporting the Department of the Interior’s Acquisition Directorate in the Denver area—I offer a proven track record of analyzing complex procurement and financial datasets to drive operational excellence, optimize resources, and deliver actionable technical recommendations.", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 100, "text_runs": [{"text": "Throughout my 14 years supporting federal acquisition operations, I have delivered critical technical data analysis and reporting that enabled senior leadership and Contracting Officers to make data-driven decisions. In the Department of the Interior’s SAP-based Federal Business Management System (FBMS), I authored SQL queries and extracted and formatted complex financial reports (including FBL1N vendor ledger, ME2M purchase order tracking, FAGLL03 general ledger, and custom ZFI reports) to monitor obligations, track spend, and execute funds realignments that reclaimed over $1M annually in unliquidated obligations. Furthermore, as ETL Architect for the Department-wide FBMS data conversion, I analyzed legacy data structures and designed data conversion logic to migrate disparate databases into a unified federal platform. I also routinely conducted Remedy ticket trend analyses to identify recurring system pain points, evaluate operational workflows, and prepare executive briefings that guided process improvements across the acquisition lifecycle.", "size": 19, "color": "1F1F1F"}]},
        {
            "space_after": 100,
            "text_runs": [
                {"text": "While my federal data analytics background has centered on procurement, contracts, and financial management rather than direct fleet management, my analytical methodologies—tracking asset lifecycles, evaluating vendor and supplier performance, and auditing transactional data—directly transfer to FAS business transformation and vehicle lifecycle initiatives. In addition, my recent graduate certificate in AI Strategy and Applications in IT from the University of Denver positions me to bring forward-looking analytical frameworks to GSA, including AI maturity assessments, automated workflow design, and data-driven ROI modeling (as showcased on my portfolio portal, ", "size": 19, "color": "1F1F1F"},
                {"text": "AI Guardians", "size": 19, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"},
                {"text": "), ensuring analytical initiatives deliver measurable mission value.", "size": 19, "color": "1F1F1F"}
            ]
        },
        {"space_after": 120, "text_runs": [{"text": "As a Denver-area resident, I am especially excited about the opportunity to support FAS at the Lakewood, CO duty station, though I am fully open to any duty location listed for this announcement. I welcome the opportunity to discuss how my federal acquisition analytics background and technical rigor can support GSA’s data analytics initiatives, and I respectfully request feedback on my candidacy if another applicant is selected. Thank you for your time, consideration, and service.", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 80, "text_runs": [{"text": "Sincerely,", "size": 19, "color": "1F1F1F"}]},
        {"space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]}
    ]
    return create_docx(OUTPUT_DIR / "Cover_Letter_Ebenezer_Rolston_GSA_Program_Analyst.docx", paragraphs)

def build_analysis_docx():
    paragraphs = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Skill Gap Analysis: Program Analyst (Data Analytics)", "bold": True, "color": "17365D", "size": 26, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": "General Services Administration (GSA) — Federal Acquisition Service (FAS) | GS-0343-13", "color": "5B9BD5", "bold": True, "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": "Candidate: Ebenezer J. Rolston • Control Number: 887843500 • Date: 2026-10-12 (Post Fact-Finding)", "size": 18, "color": "4F4F4F"}]},

        # Section 1
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. FIT OVERVIEW & SCORES (POST FACT-FINDING)", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [
            {"text": "• Match Score: ", "bold": True, "color": "17365D", "size": 19},
            {"text": "85 / 100 (Strong Fit) — Increased from initial 78/100 following fact-finding", "bold": True, "color": "008000", "size": 19}
        ]},
        {"space_after": 40, "text_runs": [
            {"text": "• Interview Probability: ", "bold": True, "color": "17365D", "size": 19},
            {"text": "80 / 100 — Substantial direct evidence in SAP financial reporting and operational analytics", "bold": True, "color": "008000", "size": 19}
        ]},
        {"space_after": 80, "text_runs": [{
            "text": "Rationale: Fact-finding confirmed direct hands-on execution of SAP financial reports (FBL1N, ME2M, FAGLL03, ZFI), SQL query authoring for operational reports, Remedy helpdesk trend analytics, and multi-year funds reconciliation ($1M+ reclaimed annually). These are verified core data analytics deliverables that directly satisfy the JOA requirements. The remaining gap in fleet/vehicle lifecycle management is effectively bridged through parallel federal acquisition lifecycle methodologies.",
            "size": 19, "color": "1F1F1F"
        }]},

        # Section 2
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. SKILL MATCH MATRIX", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Data Analytics & Reporting: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct Evidence) — SAP financial reporting (FBL1N, ME2M, FAGLL03, ZFI) pulled/formatted for COs/CORs; SQL reporting.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Business Intelligence Dashboards: ", "bold": True, "color": "C00000", "size": 18},
            {"text": "PARTIAL (Exploratory/Academic) — Tableau exploratory data analysis; Matplotlib academic charts; Advanced Excel modeling.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Data Visualization for Leadership: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct Evidence) — Briefed COs/CORs, leadership on SAP financial data; Congressional-level demo at Acxiom.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Programming & Query Tools: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct + Coursework) — Production SQL/PL/SQL; Coursework in Python, PySpark, Spark, NumPy, Pandas.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Complex Dataset Analysis: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct Evidence) — ETL Architect for DOI FBMS conversion (millions of records); Acxiom relational models.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Federal Program Analysis (GS-13): ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct Evidence) — Program Analyst at DOI Acquisitions Directorate (GS-13 equivalent); 14-yr consulting lead.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Advisory & Guidance to Management: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct Evidence) — Senior escalation lead; FSALT advisory leadership; advised 3 major AQD IT modernizations.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Briefings to Senior Leadership: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct Evidence) — Executive briefings at DOI and FSALT; Congressional stakeholder presentations.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Financial Performance Reporting: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED (Direct Evidence) — Reclaimed $1M+ annually in funds deobligation; UDO tracking; FBL1N vendor ledger reconciliation.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Vehicle Lifecycle / Fleet Domain: ", "bold": True, "color": "C00000", "size": 18},
            {"text": "LEARNING BRIDGE — No direct fleet experience; bridged via federal capital asset and procurement lifecycle analytics.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [
            {"text": "• Supplier Management Analytics: ", "bold": True, "color": "008000", "size": 18},
            {"text": "TRANSFERABLE — IPAC vendor billing reconciliation; aviation contract vendor management; GSA Schedule analysis.", "size": 18}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 80, "text_runs": [
            {"text": "• Security Suitability / Public Trust: ", "bold": True, "color": "008000", "size": 18},
            {"text": "MATCHED — Previously held Public Trust (inactive); prior investigation facilitates smooth reinvestigation.", "size": 18}
        ]},

        # Section 3
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. GAP RESOLUTION & COMPETITIVE POSITIONING", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "Key Strengths: ", "bold": True, "color": "17365D", "size": 18}, {"text": "14 years of federal acquisition systems analysis at GS-13 level; hands-on SAP transaction reporting; $1M+ annual cost recovery; award-winning ETL data conversion; DU AI Strategy credential; Denver resident for Lakewood duty station.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "Honest Learning Bridges: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Fleet domain knowledge bridged via federal asset lifecycle models and Mile High Logistics coursework roadmap; Tableau framed honestly as exploratory discovery; Python framed as rapid prototyping and statistical analysis.", "size": 18}]}
    ]
    return create_docx(OUTPUT_DIR / "Analysis_GSA_Program_Analyst.docx", paragraphs)

def build_interview_prep_docx():
    paragraphs = [
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Interview Preparation Package: Program Analyst (Data Analytics)", "bold": True, "color": "17365D", "size": 24, "font": "Cambria"}]},
        {"align": "center", "space_after": 20, "text_runs": [{"text": "General Services Administration (GSA) — Federal Acquisition Service (FAS)", "bold": True, "color": "5B9BD5", "size": 20, "font": "Cambria"}]},
        {"align": "center", "space_after": 80, "bottom_border": True, "text_runs": [{"text": "Candidate: Ebenezer J. Rolston • Grade: GS-13 • Vacancy Control Number: 887843500 • Location: Lakewood, CO", "size": 18, "color": "4F4F4F"}]},

        # Section 1
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. ROLE, AGENCY & SECTOR BRIEF", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "• Agency Mission: ", "bold": True, "color": "008000", "size": 18}, {"text": "GSA Federal Acquisition Service (FAS) acquires over $100B in products and services annually across federal agencies.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "• GSA Fleet Context: ", "bold": True, "color": "008000", "size": 18}, {"text": "Manages 230,000+ non-tactical leased vehicles worldwide. Priorities: lifecycle cost reduction, telematics, supplier accountability, and the Zero-Emission Vehicle (ZEV) transition.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Key Modernization Drivers: ", "bold": True, "color": "008000", "size": 18}, {"text": "Transitioning from fragmented spreadsheets to integrated analytics pipelines, automated data anomaly detection, and executive BI dashboards.", "size": 18}]},

        # Section 2
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. CANDIDATE FIT NARRATIVE & POSITIONING STATEMENT", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 60, "text_runs": [{
            "text": "Ebenezer J. Rolston is a senior federal program analyst with 20+ years of experience across the Department of the Interior (DOI IBC) and commercial financial sectors. Operating at a GS-13 equivalent level, he combines deep expertise in federal ERP and procurement data (SAP FBMS, Unison PRISM, SQL) with a University of Denver Graduate Certificate in AI Strategy to deliver clean, auditable program intelligence and high-impact executive briefings.",
            "size": 19, "color": "1F1F1F"
        }]},

        # Section 3
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. ELEVATOR PITCH (60–90 SECONDS SPOKEN)", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {
            "space_after": 80,
            "text_runs": [{
                "text": "\"Good morning. I’m Ebenezer Rolston. Over the past 20 years, I’ve worked at the intersection of federal business systems, data analysis, and program operations—most notably spending 14 years supporting the Department of the Interior’s Acquisition Directorate right here in the Denver area. In that role, functioning at a GS-13 operational level, my core focus was transforming fragmented transactional data into clear, actionable program decisions. I pulled and analyzed SAP financial reports using transactions like FBL1N, ME2M, and FAGLL03, engineered custom SQL reconciliation queries, and systematically audited contract obligations. That work reclaimed over $1 million annually in idle government funds and resolved discrepancies between contracting officials, program managers, and vendors. I also served as the ETL Architect for DOI’s enterprise-wide FBMS conversion, harmonizing legacy databases across bureaus into a unified SAP system—earning two Interior Department awards. Recently, I paired that federal foundation with a Graduate Certificate in AI Strategy from the University of Denver, developing data roadmaps, risk governance models, and predictive analytics frameworks. I am drawn to GSA FAS and the Lakewood team because your mission touches every civilian agency. Whether analyzing vehicle lifecycle trends, evaluating supplier metrics, or optimizing program spend, I bring the data discipline, federal systems familiarity, and analytical integrity needed to deliver immediate value on day one.\"",
                "italic": True, "size": 19, "color": "1F1F1F"
            }]
        },

        # Section 4
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "4. HR & RECRUITER QUESTION BANK", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "• Q: Why GSA FAS? ", "bold": True, "color": "17365D", "size": 18}, {"text": "Scale of mission ($100B buying power, 230K vehicles), local Denver Federal Center presence, and strong alignment with federal data modernization goals.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "• Q: Salary Expectations: ", "bold": True, "color": "17365D", "size": 18}, {"text": "GS-13 scale ($108,173 - $172,980); competitive step placement commensurate with 14+ years GS-13-equivalent federal systems delivery and Denver locality.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "• Q: Location & Work Posture: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Lakewood, CO preferred (local resident); open to hybrid, telework, or full onsite schedules at the Denver Federal Center.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Q: Clearance Status: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Previously held Public Trust at DOI; background is clear and ready for immediate e-App / SF-85P processing.", "size": 18}]},

        # Section 5
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "5. DEEP TECHNICAL & STRATEGY QUESTION BANK", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "Q1: How do you approach analyzing complex datasets to support program decisions?", "bold": True, "color": "17365D", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Framework: 1) Define operational objectives with leadership; 2) Profile raw SQL/ERP tables for nulls and anomalies; 3) Standardize and cleanse data schemas; 4) Perform multi-dimensional exploratory slicing; 5) Synthesize findings into executive briefing decks with clear, risk-adjusted recommendations.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Q2: How would you structure a vehicle lifecycle metrics dashboard?", "bold": True, "color": "17365D", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Framework: Architecture organized around 4 stages: Procurement/Upfitting -> Operational Utilization (cost per mile, fuel/kWh) -> Mid-Life Maintenance -> End-of-Life Remarketing/Disposal. Connect underlying SQL pipelines to ensure reliable data refresh.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Q3: How do you handle poor or inconsistent source data?", "bold": True, "color": "17365D", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "Framework: Transparently flag data discrepancies early; run automated SQL assertion scripts (detecting negative mileage or orphaned PO lines); build crosswalk mapping tables to resolve issues systematically rather than through manual one-off edits.", "size": 18}]},

        # Section 6
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "6. CHALLENGE QUESTION BANK", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 30, "text_runs": [{"text": "Challenge: \"You don't have direct fleet or vehicle management experience.\"", "bold": True, "color": "C00000", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Answer: The analytical methodologies—tracking capital asset lifecycles, monitoring vendor SLAs, auditing maintenance costs, and evaluating deobligations—are identical to the 14 years of federal asset and contract analysis I performed at DOI. Furthermore, my DU logistics roadmap analyzed fleet routing and maintenance data streams. The core of a GS-13 analyst is data rigor and stakeholder alignment.", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Challenge: \"Your Tableau experience is exploratory rather than enterprise admin.\"", "bold": True, "color": "C00000", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "Answer: Exactly. My strength is foundational data engineering: writing the SQL queries, structuring clean relational tables, and validating data integrity before it reaches the BI layer. I build visual mockups and partner closely with BI developers to translate leadership requirements into production dashboards.", "size": 18}]},

        # Section 7
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "7. VERIFIED STAR STORY BANK", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [{"text": "Story 1: Remedy Ticket Trend Analysis & User Enablement", "bold": True, "color": "17365D", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Situation: Support team faced 5-10 escalations daily in PRISM/FBMS. Task: Isolate root causes. Action: Extracted months of Remedy ticket records, executed trend analysis, identified invoice routing confusion, and delivered cohort training for 85+ users. Result: Dramatically cut repeat ticket volume.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "Story 2: SAP Financial Reporting & $1M+ Annual Funds Reclamation", "bold": True, "color": "17365D", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Situation: Millions in unliquidated obligations sat dormant in FBMS. Task: Track obligations and recover funds. Action: Pulled SAP reports (FBL1N, ME2M, FAGLL03, ZFI), cross-matched PO lines against vendor IPAC files, and ran deobligations. Result: Reclaimed $1M+ annually in recurring government savings.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "Story 3: DOI FBMS Department-Wide Data Conversion (ETL Architect)", "bold": True, "color": "17365D", "size": 18}]},
        {"space_after": 30, "text_runs": [{"text": "Situation: Disparate legacy procurement databases across DOI bureaus. Task: Unify into SAP FBMS. Action: Built Oracle SQL translation rules, profiled historical records, and led cutover testing across bureaus. Result: Successful Department-wide conversion; earned 2 DOI awards.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "Story 4: Citibank Identity Scoring Model (Early AI/ML Analytics)", "bold": True, "color": "17365D", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "Situation: Citibank experienced credit application fraud. Task: Build real-time scoring model. Action: Engineered anomaly-detection algorithms evaluating relational application streams. Result: Stopped millions in fraudulent account losses and demonstrated system to Congress.", "size": 18}]},

        # Section 8
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "8. QUESTIONS CANDIDATE SHOULD ASK INTERVIEWER", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 20, "text_runs": [{"text": "1. ", "bold": True, "color": "17365D"}, {"text": "\"How is the GSA FAS data analytics team currently structured between operational ad-hoc reporting and long-term BI modernization?\"", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 20, "text_runs": [{"text": "2. ", "bold": True, "color": "17365D"}, {"text": "\"What are the primary data platforms and tools (e.g., GSA Fleet Drive-thru, FAS BI, Oracle, Tableau) this role interacts with most heavily?\"", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 20, "text_runs": [{"text": "3. ", "bold": True, "color": "17365D"}, {"text": "\"What are the top 1 or 2 operational data challenges currently facing the Lakewood analytics group—for instance, data latency or tracking the ZEV transition?\"", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 60, "text_runs": [{"text": "4. ", "bold": True, "color": "17365D"}, {"text": "\"How does leadership measure the success and impact of a GS-13 Program Analyst during their first 90 to 180 days?\"", "size": 18}]},

        # Section 9
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "9. 30 / 60 / 90-DAY ONBOARDING PLAN", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [{"text": "• Days 1–30 (Discovery & Systems): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Obtain GSA credentials; map FAS database tables; shadow senior analysts on current recurring report generation; catalog data sources.", "size": 18}]},
        {"space_after": 20, "text_runs": [{"text": "• Days 31–60 (Operational Delivery): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Assume ownership of scheduled operational data extracts; audit SQL scripts to optimize performance; deliver initial briefings to branch leadership.", "size": 18}]},
        {"space_after": 60, "text_runs": [{"text": "• Days 61–90 (Optimization & Modernization): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Implement automated SQL anomaly validation checks; propose dashboard prototypes for lifecycle milestones; deliver deep-dive analytical brief on fleet optimization.", "size": 18}]},

        # Section 10
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "10. PRACTICAL GUIDANCE & CURATED READING LIST", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [
            {"text": "• GSA Federal Acquisition Service: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "https://www.gsa.gov/about-us/organization/federal-acquisition-service", "size": 18, "url": "https://www.gsa.gov/about-us/organization/federal-acquisition-service"}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• GSA Fleet Management & Leasing: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "https://www.gsa.gov/buy-through-us/purchasing-programs/gsa-fleet", "size": 18, "url": "https://www.gsa.gov/buy-through-us/purchasing-programs/gsa-fleet"}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• GSA Data Strategy: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "https://www.gsa.gov/about-us/organization/office-of-the-chief-information-officer/gsa-data-strategy", "size": 18, "url": "https://www.gsa.gov/about-us/organization/office-of-the-chief-information-officer/gsa-data-strategy"}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• NIST AI Risk Management Framework: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "https://www.nist.gov/itl/ai-risk-management-framework", "size": 18, "url": "https://www.nist.gov/itl/ai-risk-management-framework"}
        ]},
        {"space_after": 40, "text_runs": [
            {"text": "• AI Guardians Portal: ", "bold": True, "color": "17365D", "size": 18},
            {"text": "https://portal.aiguardiansllc.us/", "size": 18, "url": "https://portal.aiguardiansllc.us/"}
        ]}
    ]
    return create_docx(OUTPUT_DIR / "Interview_Preparation_GSA_Program_Analyst.docx", paragraphs)

def build_bulleted_resume_docx():
    """Build the compact 1.5-page bulleted resume variant with zero repetition."""
    paragraphs = [
        # Candidate Header Name
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 34, "font": "Cambria"}]},
        # Subtitle Line
        {"align": "center", "space_after": 30, "text_runs": [{"text": "PROGRAM ANALYST (DATA ANALYTICS) — GS-0343-13", "bold": True, "color": "5B9BD5", "size": 20, "font": "Cambria"}]},
        # Contact Line with Hyperlinks
        {
            "align": "center", "space_after": 30, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • 501-307-3237 • ", "size": 17, "color": "17365D", "font": "Cambria"},
                {"text": "eberolston@yahoo.com", "size": 17, "color": "17365D", "font": "Cambria"},
                {"text": " • ", "size": 17, "color": "17365D", "font": "Cambria"},
                {"text": "LinkedIn", "size": 17, "color": "17365D", "bold": True, "font": "Cambria", "url": "https://www.linkedin.com/in/ebenezer-rolston/"},
                {"text": " • ", "size": 17, "color": "17365D", "font": "Cambria"},
                {"text": "AI Guardians Portal", "size": 17, "color": "17365D", "bold": True, "font": "Cambria", "url": "https://portal.aiguardiansllc.us/"}
            ]
        },
        # Metadata banner
        {
            "align": "center", "space_after": 60,
            "text_runs": [
                {"text": "U.S. Citizen • Public Trust Eligible (Previously Held) • Preferred Location: Lakewood, CO (Denver Federal Center)", "size": 16, "color": "4F4F4F", "font": "Times New Roman"}
            ]
        },

        # PROFESSIONAL SUMMARY
        {"space_before": 80, "space_after": 30, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {
            "space_after": 50,
            "text_runs": [{
                "text": "Results-driven Program Analyst (Data Analytics) with 20+ years of federal acquisition systems analysis, financial reconciliation, and business intelligence reporting across federal and financial environments. Proven GS-13-equivalent track record manipulating large streams of operational data within SAP FBMS and Unison PRISM to build decision-support reports, isolate workflow bottlenecks, and reclaim $1M+ annually in deobligated contract funds. Combines 14 years of Department of the Interior (DOI) acquisition data governance with Stanford University certification in Python data analysis and graduate training in AI strategy to deliver actionable, data-driven executive briefings.",
                "size": 18, "color": "1F1F1F"
            }]
        },

        # CORE COMPETENCIES
        {"space_before": 80, "space_after": 30, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {
            "space_after": 25,
            "text_runs": [
                {"text": "Data Analytics & BI Reporting: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
                {"text": "SQL Querying • SAP Financial Ledgers (FBL1N, ME2M, FAGLL03, ZFI) • Tableau (Exploratory EDA) • Helpdesk Trend Analysis • Executive Decision-Support Briefings", "size": 17}
            ]
        },
        {
            "space_after": 25,
            "text_runs": [
                {"text": "Federal Acquisition & Financial Systems: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
                {"text": "SAP S/4 (FBMS) • Unison PRISM Administration • IPAC Vendor Dispute Reconciliation • Funds Deobligation ($1M+ Reclaimed) • FAR & FPDS Compliance", "size": 17}
            ]
        },
        {
            "space_after": 60,
            "text_runs": [
                {"text": "Data Engineering & Modernization: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
                {"text": "Oracle PL/SQL & ETL Architecture • Python (Pandas, NumPy — Stanford Certified) • Enterprise Data Conversions • User Enablement (85+ Cohort Users)", "size": 17}
            ]
        },

        # PROFESSIONAL EXPERIENCE
        {"space_before": 80, "space_after": 30, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},

        # Role 1: DOI
        {"bg_color": "EBF1F5", "space_before": 40, "space_after": 15, "text_runs": [
            {"text": "Program Analyst (Contracting Business Operations / Data Analytics)", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
            {"text": " | U.S. Department of the Interior • Denver, CO | 01/2025 – 09/2025", "bold": True, "color": "5B9BD5", "size": 18, "font": "Cambria"}
        ]},
        {"space_after": 20, "text_runs": [{"text": "Senior GS-13-equivalent operational and functional lead for Acquisition Directorate contracting operations; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Extracted and formatted SAP financial reports—specifically FBL1N (vendor ledgers), ME2M (purchase order history), FAGLL03 (general ledger), and custom ZFI reports—to provide Contracting Officers (COs) and CORs with real-time financial tracking and commitment analytics.", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Analyzed operational incident data across thousands of Remedy ticketing records, identifying recurring system failure patterns, isolating root causes, and delivering data-backed recommendations that reduced repeat support tickets.", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 50, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Delivered briefings to senior acquisition leadership on procurement metrics, ERP transaction reliability, and federal data governance compliance across enterprise contracting applications.", "size": 18}]},

        # Role 2: ArkSolutions / DOI IBC
        {"bg_color": "EBF1F5", "space_before": 50, "space_after": 15, "text_runs": [
            {"text": "Senior Analyst Consultant / Data Analytics & Systems Specialist", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
            {"text": " | ArkSolutions (Client: DOI IBC Acquisition Directorate) • Denver, CO | 01/2011 – 01/2025", "bold": True, "color": "5B9BD5", "size": 18, "font": "Cambria"}
        ]},
        {"space_after": 20, "text_runs": [{"text": "14-year senior analytics and data transformation engagement for Department-wide acquisition platforms; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Architected and executed the Department-wide FBMS data conversion as ETL Architect, cleansing, transforming, and validating millions of legacy records into a unified SAP S/4 platform (honored with 2 Interior Department awards).", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Reclaimed $1M+ in recurring annual government funds by designing rigorous deobligation tracking models and funds realignment reports that resolved multi-year discrepancies between contracting officials and vendors.", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Administered Unison PRISM procurement workflows, data integrity, and role-based access for 7 years across contract solicitations, awards, modifications, and FPDS/SAM compliance feeds.", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 50, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Mediated complex aviation vendor charge-card and IPAC billing disputes through structured transaction ledger reconciliations, and designed operational cohort training for 85+ end users to boost data accuracy.", "size": 18}]},

        # Role 3: Acxiom
        {"bg_color": "EBF1F5", "space_before": 50, "space_after": 15, "text_runs": [
            {"text": "Solutions Developer / Solution Architect & Data Analyst", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
            {"text": " | Acxiom Corporation • Little Rock, AR & Remote | 01/1999 – 12/2010", "bold": True, "color": "5B9BD5", "size": 18, "font": "Cambria"}
        ]},
        {"space_after": 20, "text_runs": [{"text": "High-volume data analytics models, predictive algorithms, and relational data warehousing; 40 Hours/Week", "italic": True, "color": "4F4F4F", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Engineered Citibank's first Online Identity Scoring Model utilizing early statistical analytics and machine learning algorithms, analyzing real-time application streams to prevent millions of dollars in fraudulent account losses.", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 25, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Architected enterprise relational data warehouses and predictive cross-sell data models for Fortune 100 financial clients including GE Money, ChoicePoint, and Citibank.", "size": 18}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 50, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Standardized data quality frameworks on the Acxiom Methodology Board and directed senior technical developers in demonstrating airline passenger-screening data architectures to U.S. Congressional stakeholders.", "size": 18}]},

        # EDUCATION & CREDENTIALS
        {"space_before": 80, "space_after": 30, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [
            {"text": "• Data Analysis with Python", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : Stanford Continuing Studies (Taught by Matt Harrison — Pandas, NumPy, EDA)", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : University of Denver", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• Executive Certificate, Large Language Models: From Transformer Basics to Agentic AI", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : Harvard John A. Paulson School of Engineering and Applied Sciences", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "• Master of Science (M.S.) & Bachelor of Science (B.S.), Computer Science", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " : St. Joseph's College", "size": 17}
        ]},
        {"space_after": 50, "text_runs": [
            {"text": "• Honors & Awards: ", "bold": True, "color": "C00000", "size": 17},
            {"text": "Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award", "size": 17}
        ]},

        # TECHNICAL PROFICIENCIES
        {"space_before": 80, "space_after": 30, "bottom_border": True, "text_runs": [{"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 20, "font": "Cambria"}]},
        {"space_after": 20, "text_runs": [
            {"text": "Data Analytics & Reporting: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": "SQL, Relational Querying, SAP Financial Reports (FBL1N, ME2M, FAGLL03, ZFI), Financial Reconciliation, Trend Analysis, Advanced Excel (Pivot Tables, VLOOKUP)", "size": 17}
        ]},
        {"space_after": 20, "text_runs": [
            {"text": "Programming & Tools: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": "Python (Pandas, NumPy), Oracle PL/SQL, Apache Spark, Tableau (Exploratory), Remedy Incident Management, Git/GitHub", "size": 17}
        ]},
        {"space_after": 40, "text_runs": [
            {"text": "Federal & Enterprise Systems: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": "SAP S/4 (FBMS), Unison PRISM, FPDS, SAM, IPP, IPAC", "size": 17}
        ]}
    ]
    return create_docx(OUTPUT_DIR / "Ebenezer_Rolston_GSA_Program_Analyst_Resume_Bulleted_1.5Page.docx", paragraphs)

if __name__ == "__main__":
    r_path = build_resume_docx()
    c_path = build_cover_letter_docx()
    a_path = build_analysis_docx()
    i_path = build_interview_prep_docx()
    b_path = build_bulleted_resume_docx()
    print("ALL GSA NATIVE .DOCX APPLICATION DOCUMENTS GENERATED SUCCESSFULLY!")
    print(f"1. Standard Resume: {r_path}")
    print(f"2. Bulleted 1.5-Page Resume: {b_path}")
    print(f"3. Cover Letter: {c_path}")
    print(f"4. Analysis: {a_path}")
    print(f"5. Interview Prep: {i_path}")

