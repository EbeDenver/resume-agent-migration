"""Generate the authoritative Bulletted-Standard Format Resume in native DOCX and Markdown.

Matches the official 2-page Bulletted-Standard format for Ebenezer J. Rolston:
- Centered Header with 3-Pillar Tagline and Active Hyperlinks (LinkedIn, GitHub, AI Guardians)
- Underlined Navy #17365D Section Headers
- Two-Paragraph Professional Summary + Award Callout
- Dense Inline Core Competencies (Strict Zero-Parentheses Rule)
- 4 Chronological Roles with Italicized Context Subtitles
- 4 AI Engineering Portfolio Projects
- Date-Free Education & Credentials
- 5 Categorized Technical Proficiencies Clusters
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = Path(__file__).parent / "output" / "Bulleted_Standard"

def build_bulletted_standard_docx_paragraphs():
    p = []

    # 1. Candidate Name
    p.append({
        "align": "center",
        "space_before": 0,
        "space_after": 20,
        "text_runs": [
            {"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36, "font": "Times New Roman"}
        ]
    })

    # Subtitle
    p.append({
        "align": "center",
        "space_before": 0,
        "space_after": 30,
        "text_runs": [
            {"text": "Identity Analytics • Customer Data Integration • Business Management System", "bold": True, "color": "17365D", "size": 19, "font": "Times New Roman"}
        ]
    })

    # Contact Line
    p.append({
        "align": "center",
        "space_before": 0,
        "space_after": 80,
        "text_runs": [
            {"text": "Denver, CO • ", "size": 18, "color": "1F1F1F"},
            {"text": "eberolston@yahoo.com", "size": 18, "color": "1F1F1F"},
            {"text": " • 501-307-3237 • ", "size": 18, "color": "1F1F1F"},
            {"text": "LinkedIn", "size": 18, "color": "17365D", "bold": True, "url": "https://www.linkedin.com/in/ebenezer-rolston/"},
            {"text": " • ", "size": 18, "color": "1F1F1F"},
            {"text": "GitHub", "size": 18, "color": "17365D", "bold": True, "url": "https://github.com/EbeDenver"},
            {"text": " • ", "size": 18, "color": "1F1F1F"},
            {"text": "AI Guardians", "size": 18, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"}
        ]
    })

    # 2. PROFESSIONAL SUMMARY
    p.append({
        "space_before": 100,
        "space_after": 40,
        "bottom_border": True,
        "text_runs": [
            {"text": "PROFESSIONAL SUMMARY", "bold": True, "color": "17365D", "size": 20, "font": "Times New Roman"}
        ]
    })
    p.append({
        "space_before": 40,
        "space_after": 40,
        "text_runs": [
            {
                "text": "Enterprise Data and Identity Analytics professional and Solutions Architect with 20+ years of experience in customer data integration, enterprise systems modernization, business analytics, and data transformation. Brings 11 years of solutions engineering and architecture experience at Acxiom Corporation, developing real-time identity scoring, application verification, and customer data solutions for major financial services and insurance clients. Led enterprise data integration, reconciliation, and operational analytics initiatives supporting the U.S. Department of the Interior, including data conversions for 4 agencies.",
                "size": 18,
                "color": "1F1F1F"
            }
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 30,
        "text_runs": [
            {
                "text": "Combines this experience with recent hands-on AI engineering and workflow development, supported by a University of Denver graduate certificate in AI Strategy and a Harvard SEAS executive certificate in LLMs and Agentic AI.",
                "size": 18,
                "color": "1F1F1F"
            }
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 60,
        "text_runs": [
            {"text": "Winner of two Department of Interior Awards", "italic": True, "bold": True, "color": "8B0000", "size": 18}
        ]
    })

    # 3. CORE COMPETENCIES
    p.append({
        "space_before": 100,
        "space_after": 40,
        "bottom_border": True,
        "text_runs": [
            {"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 20, "font": "Times New Roman"}
        ]
    })
    p.append({
        "space_before": 30,
        "space_after": 60,
        "text_runs": [
            {
                "text": "▪ Customer Data Integration & Entity Resolution ▪ Identity Scoring Models & Algorithmic Scoring ▪ Identity Data Quality, Profiling & Hygiene ▪ Identity Match Reach & Quality KPIs ▪ Relational Schema Design ▪ Advanced SQL ▪ Privacy, Regulatory & AI Governance ▪ Python Data Analysis ▪ Enterprise ETL Architecture & Conversion ▪ Automated Validation & Testing ▪ Cross-Functional Stakeholder Relationship ▪ User Enablement & Mentorship",
                "size": 17,
                "color": "1F1F1F"
            }
        ]
    })

    # 4. PROFESSIONAL EXPERIENCE
    p.append({
        "space_before": 100,
        "space_after": 40,
        "bottom_border": True,
        "text_runs": [
            {"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 20, "font": "Times New Roman"}
        ]
    })

    # Role 1: AI Guardians
    p.append({
        "space_before": 40,
        "space_after": 10,
        "text_runs": [
            {"text": "AI Engineering & Enablement | AI Guardians LLC ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Denver, CO | Jan 2026–Present", "italic": True, "size": 18, "color": "17365D"}
        ]
    })
    for b in [
        "Engineered autonomous multi-agent workflows and custom TOML/markdown agents using OpenAI Codex and Google Antigravity with runtime hooks, Plan Mode trade-off analysis, and automated build–test–fix loops.",
        "Integrated enterprise toolchains (Figma, GitHub, Atlassian, Google Workspace) via Model Context Protocol (MCP) servers and plugins; standardized agent context via AGENTS.md and reusable skill lifecycles.",
        "Formulated enterprise prompting methodologies (Outcome, Constraints, Definition of Done) and evidence-based verification gates replacing agent self-assessment with deterministic testing.",
        "Designed AI transformation toolkits, AI maturity assessments, use-case prioritization canvases, and governance guardrails based on NIST AI RMF 1.0 and ISO 42001."
    ]:
        p.append({
            "space_before": 0,
            "space_after": 20,
            "left_indent": 360,
            "hanging_indent": 180,
            "text_runs": [{"text": f"• {b}", "size": 18}]
        })

    # Role 2: DOI
    p.append({
        "space_before": 40,
        "space_after": 10,
        "text_runs": [
            {"text": "Program Analyst, Acquisition Directorate | U.S. Department of the Interior, ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Denver, CO | Jan–Sep 2025", "italic": True, "size": 18, "color": "17365D"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 20,
        "text_runs": [
            {"text": "Cross-functional Analyst lead for Acquisition Directorate enterprise systems and business technology; GS-13", "italic": True, "size": 17, "color": "4A4A4A"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 20,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Senior Analyst for Acquisition Directorate enterprise financial system, managing business workflow, assuring data integrity, and ensuring business & functional reliability in federal environment.", "size": 18}]
    })
    p.append({
        "space_before": 0,
        "space_after": 20,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Resolved client & platform vendor defects and contractual billing disputes.", "size": 18}]
    })
    p.append({
        "space_before": 0,
        "space_after": 40,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Triaged enterprise system defects.", "size": 18}]
    })

    # Role 3: ARK Solutions
    p.append({
        "space_before": 40,
        "space_after": 10,
        "text_runs": [
            {"text": "Senior Analyst Consultant | ARK Solutions — Client : IBC Acquisition Directorate ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Denver, CO | 2011–2025", "italic": True, "size": 18, "color": "17365D"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 20,
        "text_runs": [
            {"text": "14-year enterprise business support, data migration, vendor support & client training", "italic": True, "size": 17, "color": "4A4A4A"}
        ]
    })
    for b in [
        "Department ETL Architect for the FBMS enterprise data conversion for 4 agencies, migrating, cleansing, and validating bureau databases into SAP S/4.",
        "Served as Senior escalation lead handling enterprise incidents and Aviation payment negotiations",
        "Member of DOI Special Interest Group - FPDS reporting, Exemption & security compliance",
        "Implemented framework to resolve financial discrepancies through realignment process",
        "PRISM system administration, role-based access, procurement compliance, schema updates.",
        "Delivered agency-wide cohort enablement and client system training.",
        "Performed DataAct Audit Analytics"
    ]:
        p.append({
            "space_before": 0,
            "space_after": 20,
            "left_indent": 360,
            "hanging_indent": 180,
            "text_runs": [{"text": f"• {b}", "size": 18}]
        })

    # Role 4: Acxiom Corporation
    p.append({
        "space_before": 40,
        "space_after": 10,
        "text_runs": [
            {"text": "Solutions Developer / Architect | Acxiom Corporation ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Little Rock, AR | 1999–2009", "italic": True, "size": 18, "color": "17365D"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 20,
        "text_runs": [
            {"text": "Identity resolution, predictive scoring algorithms, and relational data warehousing; foundation of LiveRamp", "italic": True, "size": 17, "color": "4A4A4A"}
        ]
    })
    for b in [
        "Worked with commercial enterprise clients (Citibank, GE Money, ChoicePoint, Allstate) deploying customer verification pipeline and marketing data solutions.",
        "Built and supported customer recognition, precision marketing and cross-selling solutions",
        "Built Citibank's online identity scoring model, real-time scoring algorithms for fraud prevention.",
        "Provided business and technical support for Application Verification System, SLA compliance",
        "SME on the Software Methodology Board, established SDLC governance."
    ]:
        p.append({
            "space_before": 0,
            "space_after": 20,
            "left_indent": 360,
            "hanging_indent": 180,
            "text_runs": [{"text": f"• {b}", "size": 18}]
        })

    # 5. AI Engineering Portfolio
    p.append({
        "space_before": 100,
        "space_after": 40,
        "bottom_border": True,
        "text_runs": [
            {"text": "AI Engineering Portfolio", "bold": True, "color": "17365D", "size": 20, "font": "Times New Roman"}
        ]
    })

    # Project 1: Trading Copilot
    p.append({
        "space_before": 30,
        "space_after": 10,
        "text_runs": [
            {"text": "Trading Copilot — Governed Multi-Agent Research Platform ", "bold": True, "color": "17365D", "size": 18},
            {"text": "AI in Finance Nicole Koenigstein 2026", "italic": True, "size": 17, "color": "4A4A4A"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 30,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Architected multi-agent equities research pipelines with supervisory layer, automated risk verification and deterministic execution bounds.", "size": 18}]
    })

    # Project 2: Rental Housing Law Navigator
    p.append({
        "space_before": 30,
        "space_after": 10,
        "text_runs": [
            {"text": "Rental Housing Law Navigator — Regulatory Decision-Support Application ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Global AI Hackathon 2026", "italic": True, "size": 17, "color": "4A4A4A"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 30,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Engineered full-stack regulatory decision application linking Lovable frontend, Google Cloud Run, Python/FastAPI backend.", "size": 18}]
    })

    # Project 3: AI Incident Monitor
    p.append({
        "space_before": 30,
        "space_after": 10,
        "text_runs": [
            {"text": "AI Incident Monitor — AI Risk Intelligence Platform ", "bold": True, "color": "17365D", "size": 18},
            {"text": "AI Guardians LLC | 2026", "italic": True, "size": 17, "color": "4A4A4A"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 30,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Architected Explainable AI incident severity scoring and compliance taxonomy mapping based on NIST AI RMF 1.0", "size": 18}]
    })

    # Project 4: Multimodal Document Intelligence
    p.append({
        "space_before": 30,
        "space_after": 10,
        "text_runs": [
            {"text": "Multimodal Document Intelligence — Auditable Data Extraction Pipeline ", "bold": True, "color": "17365D", "size": 18},
            {"text": "Stanford | 2026", "italic": True, "size": 17, "color": "4A4A4A"}
        ]
    })
    p.append({
        "space_before": 0,
        "space_after": 15,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Built an auditable document intelligence pipeline using LangGraph StateGraph & OCR parsing.", "size": 18}]
    })
    p.append({
        "space_before": 0,
        "space_after": 40,
        "left_indent": 360,
        "hanging_indent": 180,
        "text_runs": [{"text": "• Enforced Pydantic contract validation, confidence scoring, and semantic retrieval.", "size": 18}]
    })

    # 6. EDUCATION & PROFESSIONAL DEVELOPMENT
    p.append({
        "space_before": 100,
        "space_after": 40,
        "bottom_border": True,
        "text_runs": [
            {"text": "EDUCATION & PROFESSIONAL DEVELOPMENT", "bold": True, "color": "17365D", "size": 20, "font": "Times New Roman"}
        ]
    })
    edu_items = [
        [{"text": "OpenAI Codex Bootcamps: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Completed 7 Bootcamps across Fundamentals, 201, and 301 (Agent Orchestration, MCP Integration, Context Engineering)", "size": 18}],
        [{"text": "UC Berkeley Extension: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Machine Learning and Deep Learning.", "size": 18}],
        [{"text": "University of Denver : ", "bold": True, "color": "17365D", "size": 18}, {"text": "Graduate Certificate, AI Strategy & Applications in IT", "size": 18}],
        [{"text": "Stanford Continuing Studies: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Data Analysis with Python • Modern AI Architectures • AI Accountability", "size": 18}],
        [{"text": "Harvard John A. Paulson SEAS: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Executive Certificate — LLMs: Transformer to Agentic AI", "size": 18}],
        [{"text": "M.S. & B.S., Computer Science: ", "bold": True, "color": "17365D", "size": 18}, {"text": "St. Joseph's College", "size": 18}],
        [{"text": "Honors & Awards: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Interior Business Center Award for Excellence • DOI FBMS Special Recognition", "size": 18}],
        [{"text": "AI Tech and Privacy Academy: ", "bold": True, "color": "17365D", "size": 18}, {"text": "AI Governance & Privacy Frameworks", "size": 18}],
    ]
    for runs in edu_items:
        p.append({
            "space_before": 0,
            "space_after": 15,
            "text_runs": runs
        })

    # 7. TECHNICAL PROFICIENCIES
    p.append({
        "space_before": 100,
        "space_after": 40,
        "bottom_border": True,
        "text_runs": [
            {"text": "TECHNICAL PROFICIENCIES", "bold": True, "color": "17365D", "size": 20, "font": "Times New Roman"}
        ]
    })
    prof_items = [
        ("Identity Analytics & Predictive Systems: ", "Customer Data Integration • Identity Resolution & Entity Matching • Real-Time Identity Scoring • Algorithmic Scoring Models • Predictive Cross-Sell Models • Deep Learning & Neural Networks"),
        ("Data Engineering & Big Data Platforms: ", "Acxiom Hive, AbiliTec Links, Apache Spark • Oracle, PostgreSQL, SQL Server • ETL/ELT Architectures • Relational Data Modeling • Schema Normalization • Data Quality, Deduplication & Profiling"),
        ("Software Engineering & Analytical Workflows: ", "Python • pandas & NumPy • FastAPI • Pydantic • SQLAlchemy • RESTful API Contracts • JSON Schema • pytest • GitHub • Cloud Deployment (Google Cloud Run, Vercel)"),
        ("Enterprise Platforms, Privacy & Governance: ", "SAP S/4HANA Federal Business Management System • Unison PRISM • Remedy"),
        ("AI Engineering & LLMOps: ", "Agentic AI Workflows • Multi-Agent Orchestration • Model Context Protocol (MCP) • OpenAI Codex (CLI, IDE, App) • Google Antigravity • Context Engineering (AGENTS.md) • Retrieval-Augmented Generation • LLM Evaluation & Observability • AI Governance & Responsible AI • NIST AI RMF 1.0 • ISO 42001 • Bounded Execution Guardrails • Prompt Engineering Frameworks • Qdrant Vector Search • Codex, Antigravity, Cursor, OpenAI")
    ]
    for label, text in prof_items:
        p.append({
            "space_before": 0,
            "space_after": 20,
            "text_runs": [
                {"text": label, "bold": True, "color": "17365D", "size": 18},
                {"text": text, "size": 18, "color": "1F1F1F"}
            ]
        })

    return p

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    docx_path = OUTPUT_DIR / "Ebenezer_Rolston_Bulleted_Standard_Resume.docx"
    md_path = OUTPUT_DIR / "Ebenezer_Rolston_Bulleted_Standard_Resume.md"

    # Build DOCX
    paragraphs = build_bulletted_standard_docx_paragraphs()
    create_docx(docx_path, paragraphs)
    print(f"Generated DOCX: {docx_path}")

    # Copy / Write MD from data/bulletted_standard_master_resume.md
    master_md = Path(__file__).parent / "data" / "bulletted_standard_master_resume.md"
    if master_md.exists():
        md_content = master_md.read_text(encoding="utf-8")
        md_path.write_text(md_content, encoding="utf-8")
        print(f"Generated MD: {md_path}")

if __name__ == "__main__":
    main()
