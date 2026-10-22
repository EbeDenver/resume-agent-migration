"""Generate native Microsoft Word (.docx) document matching the exact version sent to Erin (VP LiveRamp).

Adheres strictly to:
- formatter2 visual styling (Navy #17365D, Light Blue #5B9BD5, Shaded Role Bars #EBF1F5)
- Reverse-chronological experience order: DOI (2025) -> ArkSolutions (2011-2025) -> Acxiom (1999-2009)
- Two-paragraph Professional Summary structure
- Title Case 'AI Transformation & Agent Engineering Portfolio' with horizontal rule
- Concise, high-impact bulleted portfolio items
- Clean, non-redundant Core Competencies and Credentials
- Replacement of Jira with 'Remedy Workflow Tracking, Federal Business Management System'
"""
import sys
from pathlib import Path

# Add project root src to path
ROOT_DIR = Path("/Volumes/SanDiskOne/AI Projects/Gumloop/resume-agent-migration")
sys.path.insert(0, str(ROOT_DIR / "src"))

from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = ROOT_DIR / "output" / "LiveRamp_Lead_Business_Transformation_Partner"

def build_liveramp_bulleted_resume_docx():
    paragraphs = [
        # Name
        {"align": "center", "space_after": 15, "text_runs": [
            {"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 30, "font": "Cambria"}
        ]},
        # Subtitle
        {"align": "center", "space_after": 25, "text_runs": [
            {"text": "LEAD BUSINESS TRANSFORMATION PARTNER | AI-ENABLED OPERATING MODELS • IDENTITY & DATA ARCHITECTURE", "bold": True, "color": "5B9BD5", "size": 16, "font": "Cambria"}
        ]},
        # Contact line with live links
        {
            "align": "center", "space_after": 60, "bottom_border": True,
            "text_runs": [
                {"text": "Denver, CO • Open to Hybrid / Travel • ", "size": 16, "color": "1F1F1F"},
                {"text": "501-307-3237", "size": 16, "color": "1F1F1F"},
                {"text": " • ", "size": 16, "color": "1F1F1F"},
                {"text": "eberolston@yahoo.com", "size": 16, "color": "1F1F1F"},
                {"text": " • ", "size": 16, "color": "1F1F1F"},
                {"text": "LinkedIn Profile", "size": 16, "color": "17365D", "bold": True, "url": "https://www.linkedin.com/in/ebenezer-rolston/"},
                {"text": " • ", "size": 16, "color": "1F1F1F"},
                {"text": "AI Guardians Portal", "size": 17, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"}
            ]
        },

        # PROFESSIONAL SUMMARY
        {"space_before": 60, "space_after": 20, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"}]},
        {
            "space_after": 20,
            "text_runs": [{
                "text": "Enterprise Business Transformation Leader and Solutions Architect with 20+ years driving cross-functional operating-model modernization, enterprise data platform migrations, and AI-enabled workflow innovation. Combines 10+ years of foundational engineering and architecture lineage from Acxiom Corporation—designing real-time identity scoring, address verification (AVS), and data warehousing systems directly foundational to LiveRamp's core data products—with 14 years modernizing large-scale public and private sector operational ecosystems ($1M+ annual recurring savings, enterprise ERP transformations).",
                "size": 17, "color": "1F1F1F"
            }]
        },
        {
            "space_after": 35,
            "text_runs": [{
                "text": "Over the past year (planned career sabbatical), engineered agentic AI workflows, LLM governance frameworks, and enterprise AI roadmaps backed by a University of Denver graduate certificate in AI Strategy and Harvard SEAS executive certification in LLMs & Agentic AI.",
                "size": 17, "color": "1F1F1F"
            }]
        },

        # CORE COMPETENCIES
        {"space_before": 60, "space_after": 20, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"}]},
        {
            "space_after": 15,
            "text_runs": [
                {"text": "Business Transformation & Operating Models: ", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
                {"text": "Workflow Redesign • Cross-Functional Process Mapping • Value Realization & ROI Baselines • Change Management & Enablement • Executive Strategy Briefings", "size": 16}
            ]
        },
        {
            "space_after": 15,
            "text_runs": [
                {"text": "AI Strategy: ", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
                {"text": "Enterprise AI Roadmaps • AI Center of Excellence Collaboration • LLM & Agentic AI Architecture • AI Governance, Privacy & Risk Mitigation • AI in Finance & Model Optimization", "size": 16}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Identity & Enterprise Data Architecture: ", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
                {"text": "Acxiom/LiveRamp Identity Resolution Lineage • Real-Time Identity Scoring • Relational Data Warehousing & ETL • Python Data Wrangling • Enterprise Systems Integration", "size": 16}
            ]
        },

        # AI Transformation & Agent Engineering Portfolio
        {"space_before": 60, "space_after": 20, "bottom_border": True, "text_runs": [{"text": "AI Transformation & Agent Engineering Portfolio", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"}]},
        {"space_after": 15, "text_runs": [{"text": "Planned Career Sabbatical & Professional Development | Denver, CO | 2025 – Present (Portfolio & Graduate Initiatives)", "italic": True, "color": "4F4F4F", "size": 16}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [
            {"text": "• Enterprise AI Strategy & Roadmapping: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": "Authored 3-year enterprise AI roadmap covering organizational maturity assessments, high-value opportunity prioritization, budgeting, ROI financial modeling, and executive strategy communication.", "size": 17}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [
            {"text": "• Auditable Multimodal Document Intelligence: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": "Designed an auditable extraction architecture for enterprise invoices and contracts, benchmarking Vision Language Models against Document Transformers and OCR baselines;", "size": 17}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [
            {"text": "• AI Governance & Healthcare Privacy Assessment: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": "Authored AI Compliance Plan for ChatGPT Health (University of Denver), operationalizing NIST AI RMF, GDPR Article 9, FTC Health Breach Notification Rule, and EU AI Act.", "size": 17}
        ]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 40, "text_runs": [
            {"text": "• Enterprise AI Transformation Tooling: ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": "Developed AI Guardians advisory tooling including enterprise AI readiness scorecards, use-case ROI calculators, vendor evaluation matrices, and agent loop oversight guards.", "size": 17}
        ]},

        # PROFESSIONAL EXPERIENCE
        {"space_before": 60, "space_after": 20, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"}]},

        # Role 1: DOI Acquisition Directorate (01/2025 – 09/2025)
        {"bg_color": "EBF1F5", "space_before": 30, "space_after": 12, "text_runs": [
            {"text": "Program Analyst (Business Operations / Data Analytics)", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " | U.S. Department of the Interior • Denver, CO | 01/2025 – 09/2025", "bold": True, "color": "5B9BD5", "size": 17, "font": "Cambria"}
        ]},
        {"space_after": 15, "text_runs": [{"text": "Cross-functional operating-model lead for Acquisition Directorate enterprise systems and business technology; GS-13 Equivalent", "italic": True, "color": "4F4F4F", "size": 16}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Led operational and cross-functional business analysis across enterprise procurement and financial platforms, mapping workflows to eliminate process bottlenecks and streamline coordination between commercial vendors, finance, and technical teams.", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Synthesized multi-source operational metrics across enterprise databases, delivering data-backed transformation briefings to executive leadership and establishing baseline KPIs for process cycle-time and data integrity.", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 35, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Performed root-cause incident trend analysis across thousands of operational Remedy ticketing records, translating recurring failure modes into prioritized technical enhancements and updated Standard Operating Procedures (SOPs).", "size": 17}]},

        # Role 2: ArkSolutions / DOI IBC (01/2011 – 01/2025)
        {"bg_color": "EBF1F5", "space_before": 30, "space_after": 12, "text_runs": [
            {"text": "Senior Analyst Consultant / Systems & Process Transformation Specialist", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " | ArkSolutions (Client: DOI IBC Acquisition Directorate) • Denver, CO | 01/2011 – 01/2025", "bold": True, "color": "5B9BD5", "size": 17, "font": "Cambria"}
        ]},
        {"space_after": 15, "text_runs": [{"text": "14-year enterprise business transformation, data platform migration, and change enablement engagement", "italic": True, "color": "4F4F4F", "size": 16}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Architected and executed Department-wide enterprise data conversion as ETL Architect, cleansing, migrating, and validating millions of legacy records into a unified SAP S/4 environment (recognized with 2 Department of the Interior awards).", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Reclaimed $1M+ in recurring annual enterprise savings by re-engineering deobligation tracking models and financial realignment workflows, resolving long-standing operational discrepancies across commercial service providers.", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Administered enterprise procurement workflows, data integrity, and role-based governance for 7 years across hundreds of stakeholders, ensuring regulatory compliance and seamless operational handoffs.", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 35, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Designed and delivered hands-on operational enablement and workflow training for 85+ cohort attendees, boosting user adoption, data accuracy, and significantly reducing support escalations.", "size": 17}]},

        # Role 3: Acxiom Corporation (01/1999 – 12/2009)
        {"bg_color": "EBF1F5", "space_before": 30, "space_after": 12, "text_runs": [
            {"text": "Solutions Developer / Solution Architect & Data Analyst", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": " | Acxiom Corporation • Little Rock, AR & Remote | 01/1999 – 12/2009", "bold": True, "color": "5B9BD5", "size": 17, "font": "Cambria"}
        ]},
        {"space_after": 15, "text_runs": [{"text": "Foundational identity resolution, predictive scoring, and data warehousing; corporate predecessor foundation of LiveRamp", "italic": True, "color": "4F4F4F", "size": 16}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Engineered Citibank's first real-time Online Identity Scoring Model and provided architecture support for the Application Verification System (AVS), developing algorithmic scoring engines that analyzed streaming consumer data in real time to prevent millions of dollars in fraudulent account losses.", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 18, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Architected scalable relational data warehouses, ETL integration pipelines, and predictive cross-sell data models for Fortune 100 enterprise clients including GE Money, ChoicePoint, and Citibank, processing multi-million-record customer transaction feeds.", "size": 17}]},
        {"left_indent": 288, "hanging_indent": 180, "space_after": 35, "text_runs": [{"text": "• ", "bold": True, "color": "17365D"}, {"text": "Standardized enterprise SDLC/SCM architecture frameworks on the Acxiom Methodology Board, and directed technical teams in designing and demonstrating large-scale data matching and passenger-screening data architectures to U.S. Congressional and corporate stakeholders.", "size": 17}]},

        # EDUCATION & CREDENTIALS
        {"space_before": 60, "space_after": 20, "bottom_border": True, "text_runs": [{"text": "EDUCATION & CREDENTIALS", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"}]},
        {"space_after": 15, "text_runs": [
            {"text": "• Executive Certificate, Large Language Models: From Transformer Basics to Agentic AI", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": " : Harvard John A. Paulson School of Engineering and Applied Sciences", "size": 16}
        ]},
        {"space_after": 15, "text_runs": [
            {"text": "• Graduate Certificate, AI Strategy & Applications in IT", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": " : University of Denver", "size": 16}
        ]},
        {"space_after": 15, "text_runs": [
            {"text": "• Data Analysis with Python", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": " : Stanford Continuing Studies", "size": 16}
        ]},
        {"space_after": 15, "text_runs": [
            {"text": "• Machine Learning", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": " : UC Berkeley Extension", "size": 16}
        ]},
        {"space_after": 15, "text_runs": [
            {"text": "• AI Governance", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": " : AI Tech and Privacy Academy", "size": 16}
        ]},
        {"space_after": 15, "text_runs": [
            {"text": "• Master of Science (M.S.) & Bachelor of Science (B.S.), Computer Science", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": " : St. Joseph's College", "size": 16}
        ]},
        {"space_after": 35, "text_runs": [
            {"text": "• Honors & Awards: ", "bold": True, "color": "C00000", "size": 16},
            {"text": "Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award", "size": 16}
        ]},

        # TECHNICAL PROFICIENCIES
        {"space_before": 60, "space_after": 20, "bottom_border": True, "text_runs": [{"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 19, "font": "Cambria"}]},
        {"space_after": 15, "text_runs": [
            {"text": "AI & LLMOps Stack: ", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": "Agentic AI Workflows, LLM Evaluation, RAG Architecture, Prompt Engineering & Caching, Context Compaction, Model Right-Sizing, AI Governance & Ethics Frameworks", "size": 16}
        ]},
        {"space_after": 15, "text_runs": [
            {"text": "Data & Analytics: ", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": "SQL, Python (Pandas, NumPy), Relational Data Warehousing, ETL Architecture, Exploratory Data Analysis (EDA), Advanced Excel (Data Modeling, Pivot Tables)", "size": 16}
        ]},
        {"space_after": 25, "text_runs": [
            {"text": "Enterprise Platforms & Operations: ", "bold": True, "color": "17365D", "size": 16, "font": "Cambria"},
            {"text": "SAP S/4 (FBMS), Unison PRISM, Identity Scoring Engines, Relational Databases (Oracle, SQL Server), Remedy Workflow Tracking, Federal Business Management System", "size": 16}
        ]}
    ]
    docx_path = OUTPUT_DIR / "Ebenezer_Rolston_LiveRamp_Lead_Business_Transformation_Partner_Resume_Bulleted_1.5Page.docx"
    return create_docx(docx_path, paragraphs)

if __name__ == "__main__":
    result = build_liveramp_bulleted_resume_docx()
    print(f"Generated LiveRamp Tailored Bulleted Resume DOCX: {result}")
