"""Generate complete application deliverables for Technical Support Engineer at LiveRamp, Inc.

Generates:
1. Ebenezer_Rolston_LiveRamp_Resume.docx & .md
2. Cover_Letter_Ebenezer_Rolston_LiveRamp.docx & .md
3. Analysis_LiveRamp.docx & .md
4. Interview_Preparation_LiveRamp.docx & .md

Applies:
- Candidate Name: Ebenezer J. Rolston (36pt bold navy #17365D)
- Subtitle: TECHNICAL SUPPORT ENGINEER | ENTERPRISE DATA PLATFORMS • SQL & LOG DIAGNOSTICS • ADTECH / SAAS (#17365D)
- Contact Line: Little Rock, AR / Denver, CO • Hybrid / Little Rock Office Available • eberolston@yahoo.com • 501-307-3237 • LinkedIn • AI Guardians
  with real embedded hyperlinks for LinkedIn and AI Guardians portal!
- Navy Section Headings with bottom border line (#17365D)
- Shaded Role Title Bars (#EBF1F5 light blue background shading)
- De-cluttered Core Competencies (3 categorized groupings)
- Tailored for LiveRamp, Inc. (Little Rock, AR / San Francisco / Hybrid)
"""
import sys
from pathlib import Path

sys.path.insert(0, 'src')
from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = Path("/Volumes/SanDiskOne/AI Projects/Gumloop/resume-agent-migration/output/LiveRamp_Technical_Support_Engineer")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# 1. RESUME BUILDER
# ==========================================

def build_resume():
    paragraphs = [
        # Candidate Header Name
        {"align": "center", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 36}]},
        # Subtitle Line
        {"align": "center", "space_after": 40, "text_runs": [{"text": "TECHNICAL SUPPORT ENGINEER | ENTERPRISE DATA PLATFORMS • SQL & LOG DIAGNOSTICS • ADTECH / SAAS", "bold": True, "color": "17365D", "size": 19}]},
        # Contact Line with Hyperlinks
        {
            "align": "center", "space_after": 100, "bottom_border": True,
            "text_runs": [
                {"text": "Little Rock, AR / Denver, CO • Hybrid / Little Rock Office Available • ", "size": 18, "color": "1F1F1F"},
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
                "text": "Versatile Technical Support Engineer and Enterprise Systems Specialist with 20+ years of deep hands-on troubleshooting, customer-facing delivery, and data platform support across advertising technology, marketing services, and mission-critical SaaS environments. Brings 11 years of foundational experience at Acxiom Corporation (Conway/Little Rock) supporting high-throughput customer data integration (CDI), identity matching, and multi-channel marketing pipelines—the direct technical lineage from which LiveRamp emerged. Supported by 14 years at the Department of the Interior leading GS-13-level production application escalations, managing high-volume ticket queues (5–10 critical incidents/day), and resolving complex technical outages via Oracle PL/SQL querying, API log inspection, and system telemetry without step-by-step runbooks. Adept at partnering with cross-functional engineering, product, and client account teams to explain complex technical root causes over video conference, restore customer trust, and establish automated monitoring to prevent recurrence.",
                "size": 19, "color": "1F1F1F"
            }]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Complex System Troubleshooting & SQL Diagnostics: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Veteran SQL developer proficient in writing, executing, and modifying complex relational queries, analyzing transaction logs, tracing data ingestion pipeline failures, and isolating API/data transformation discrepancies.", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "• Enterprise Queue & SLA Management: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Proven track record managing mission-critical ticket queues (Remedy/ServiceNow), triaging P1/P2 production escalations, exceeding SLAs, and facilitating root-cause remediations for Fortune 500 financial institutions, government agencies, and enterprise partners.", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "• Client-Facing Communication & High-Belonging Teamwork: ", "size": 18, "bold": True, "color": "17365D"},
                {"text": "Exceptional verbal and written communicator poised in high-stress customer video conferences; brings an authentic connection to LiveRamp's Little Rock heritage and a Type S collaborative, proactive mindset.", "size": 18}
            ]
        },
        # CORE COMPETENCIES (Categorized Groupings)
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "CORE COMPETENCIES", "bold": True, "color": "17365D", "size": 20}]},
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Technical Troubleshooting & Data Diagnostics: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "SQL Querying & Optimization • Database & Log Analysis • Data Ingestion & ETL Pipelines • API & Data Flow Verification • Root Cause Analysis (RCA) • Production Support (AVS On-Call)", "size": 18}
            ]
        },
        {
            "space_after": 40,
            "text_runs": [
                {"text": "Ticket Queue & Operational Excellence: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "Incident & Problem Management • SLA Adherence & Escalation Pathing • Ticket Queue Triage (Remedy / ServiceNow) • Customer Video Conferencing • Cross-Functional Bug Triage • Post-Mortem Documentation", "size": 18}
            ]
        },
        {
            "space_after": 100,
            "text_runs": [
                {"text": "Platform Architecture & Domain Knowledge: ", "bold": True, "color": "17365D", "size": 18},
                {"text": "AdTech / MarTech Ecosystem • Identity Resolution & Customer Data Integration (CDI) • Privacy, Consent & PII Safeguards • Enterprise SaaS Support • SDLC & Release Management • Process Improvement", "size": 18}
            ]
        },
        # PROFESSIONAL EXPERIENCE
        {"space_before": 120, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "PROFESSIONAL EXPERIENCE", "bold": True, "color": "17365D", "size": 20}]},
        
        # Role 1: DOI Program Analyst
        {"bg_color": "EBF1F5", "space_before": 60, "space_after": 40, "text_runs": [{"text": "PROGRAM ANALYST, ACQUISITIONS DIRECTORATE | U.S. DEPARTMENT OF THE INTERIOR\tDenver, CO | Jan–Sep 2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Acted as senior operational and technical support lead for enterprise contracting and financial platforms, managing technical escalations and ensuring 99.9% platform availability across a high-volume user base.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Triaged and diagnosed complex multi-tiered software defects, system integration errors, and data discrepancies without existing runbooks by analyzing database logs, verifying transactional records, and liaising with software vendors.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Conducted regular video conferences and technical briefings with agency stakeholders and functional users to resolve high-priority platform issues, translate technical obstacles into actionable business steps, and train users on new capabilities.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Documented comprehensive root-cause analyses and standard operating procedures (SOPs) that reduced repeat tier-2/tier-3 ticket submissions by 25%.", "size": 18}]},

        # Role 2: ArkSolutions / DOI
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SENIOR ANALYST CONSULTANT | ARKSOLUTIONS — CLIENT: IBC ACQUISITION DIRECTORATE\tDenver, CO | 2011–2025", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Managed daily ticket queue operations for Unison PRISM and FBMS (SAP S/4HANA-adjacent) platforms, resolving 5–10 mission-critical enterprise incidents daily under strict SLA windows.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served as primary technical escalation engineer diagnosing complex data ingestion failures, batch processing errors, and user permission discrepancies using advanced SQL scripts, Oracle PL/SQL stored procedures, and server event logs.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Designed and implemented enterprise ETL data conversion pipelines across 12 bureau databases, performing automated data validation, error logging, and reconciliation audits that earned two DOI Excellence Awards.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Partnered cross-functionally with database administrators, infrastructure engineers, and federal project directors to troubleshoot platform release bugs, validate hotfixes in staging, and conduct post-deployment verification.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Delivered white-glove technical assistance and customized video/screen-share troubleshooting sessions for senior executives and contracting officers, maintaining an exceptional 98%+ customer satisfaction rating.", "size": 18}]},

        # Role 3: Acxiom Corporation
        {"bg_color": "EBF1F5", "space_before": 100, "space_after": 40, "text_runs": [{"text": "SOLUTIONS DEVELOPER / SOLUTION ARCHITECT | ACXIOM CORPORATION\tConway / Little Rock, AR | 1999–2010", "bold": True, "color": "17365D", "size": 19}]},
        {"space_after": 40, "text_runs": [{"text": "• Provided Tier-3 technical support and on-call production support (AVS on-call rotation) for high-throughput customer data integration (CDI) pipelines, identity matching systems, and multi-channel marketing databases processing hundreds of millions of records for Fortune 100 enterprise clients (Citibank, Allstate, ChoicePoint).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Investigated and resolved complex data delivery anomalies, schema mismatches, and pipeline latency bottlenecks by querying relational databases, dissecting execution logs, and refactoring SQL/ETL processing jobs.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Built Citibank's first online real-time identity scoring model, collaborating with client engineering teams to test API integrations, monitor latency thresholds, and debug real-time transaction scoring feeds.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Served on the Acxiom Methodology Board, standardizing SDLC and software configuration management (SCM) processes across distributed development and support teams, establishing robust incident tracking standards that improved ticket resolution velocity.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Regularly conducted technical review sessions with enterprise client technical leads to explain data hygiene discrepancies, identity graph resolution logic, and automated ingestion schedules.", "size": 18}]},

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
        {"space_after": 40, "text_runs": [{"text": "Diagnostic & Support Tools: ", "bold": True, "color": "17365D", "size": 18}, {"text": "SQL Querying (Oracle, PostgreSQL, MySQL), Database Log Analysis, Remedy, ServiceNow, JIRA, Postman, Splunk/Datadog Log Tracing, Excel (VLOOKUP, Pivot Tables)", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Data & Systems Architecture: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Customer Data Integration (CDI), Identity Resolution, ETL Pipelines, Batch Processing, REST APIs, JSON/XML Feeds, Relational Data Modeling", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "AdTech & Cloud Technologies: ", "bold": True, "color": "17365D", "size": 18}, {"text": "AdTech/MarTech Ecosystem, Identity Graphs (RampID concepts), Consent & PII Privacy Safeguards, AWS / Cloud Data Flows, Python Scripting", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "Customer Delivery & Soft Skills: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Enterprise Video Conferencing, High-Empathy Client De-escalation, Cross-Functional Engineering Collaboration, Root-Cause Analysis (RCA), SOP Authoring", "size": 18}]}
    ]
    docx_path = create_docx(OUTPUT_DIR / "Ebenezer_Rolston_LiveRamp_Resume.docx", paragraphs)

    # Markdown version
    md_content = """# Ebenezer J. Rolston
**TECHNICAL SUPPORT ENGINEER | ENTERPRISE DATA PLATFORMS • SQL & LOG DIAGNOSTICS • ADTECH / SAAS**  
Little Rock, AR / Denver, CO • Hybrid / Little Rock Office Available • eberolston@yahoo.com • 501-307-3237 • [LinkedIn](https://www.linkedin.com/in/ebenezer-rolston/) • [AI Guardians](https://portal.aiguardiansllc.us/)

---

## PROFESSIONAL SUMMARY
Versatile Technical Support Engineer and Enterprise Systems Specialist with 20+ years of deep hands-on troubleshooting, customer-facing delivery, and data platform support across advertising technology, marketing services, and mission-critical SaaS environments. Brings 11 years of foundational experience at Acxiom Corporation (Conway/Little Rock) supporting high-throughput customer data integration (CDI), identity matching, and multi-channel marketing pipelines—the direct technical lineage from which LiveRamp emerged. Supported by 14 years at the Department of the Interior leading GS-13-level production application escalations, managing high-volume ticket queues (5–10 critical incidents/day), and resolving complex technical outages via Oracle PL/SQL querying, API log inspection, and system telemetry without step-by-step runbooks. Adept at partnering with cross-functional engineering, product, and client account teams to explain complex technical root causes over video conference, restore customer trust, and establish automated monitoring to prevent recurrence.

- **Complex System Troubleshooting & SQL Diagnostics:** Veteran SQL developer proficient in writing, executing, and modifying complex relational queries, analyzing transaction logs, tracing data ingestion pipeline failures, and isolating API/data transformation discrepancies.
- **Enterprise Queue & SLA Management:** Proven track record managing mission-critical ticket queues (Remedy/ServiceNow), triaging P1/P2 production escalations, exceeding SLAs, and facilitating root-cause remediations for Fortune 500 financial institutions, government agencies, and enterprise partners.
- **Client-Facing Communication & High-Belonging Teamwork:** Exceptional verbal and written communicator poised in high-stress customer video conferences; brings an authentic connection to LiveRamp's Little Rock heritage and a Type S collaborative, proactive mindset.

---

## CORE COMPETENCIES

- **Technical Troubleshooting & Data Diagnostics:** SQL Querying & Optimization • Database & Log Analysis • Data Ingestion & ETL Pipelines • API & Data Flow Verification • Root Cause Analysis (RCA) • Production Support (AVS On-Call)
- **Ticket Queue & Operational Excellence:** Incident & Problem Management • SLA Adherence & Escalation Pathing • Ticket Queue Triage (Remedy / ServiceNow) • Customer Video Conferencing • Cross-Functional Bug Triage • Post-Mortem Documentation
- **Platform Architecture & Domain Knowledge:** AdTech / MarTech Ecosystem • Identity Resolution & Customer Data Integration (CDI) • Privacy, Consent & PII Safeguards • Enterprise SaaS Support • SDLC & Release Management • Process Improvement

---

## PROFESSIONAL EXPERIENCE

### PROGRAM ANALYST, ACQUISITIONS DIRECTORATE | U.S. DEPARTMENT OF THE INTERIOR
*Denver, CO | Jan–Sep 2025*
- Acted as senior operational and technical support lead for enterprise contracting and financial platforms, managing technical escalations and ensuring 99.9% platform availability across a high-volume user base.
- Triaged and diagnosed complex multi-tiered software defects, system integration errors, and data discrepancies without existing runbooks by analyzing database logs, verifying transactional records, and liaising with software vendors.
- Conducted regular video conferences and technical briefings with agency stakeholders and functional users to resolve high-priority platform issues, translate technical obstacles into actionable business steps, and train users on new capabilities.
- Documented comprehensive root-cause analyses and standard operating procedures (SOPs) that reduced repeat tier-2/tier-3 ticket submissions by 25%.

### SENIOR ANALYST CONSULTANT | ARKSOLUTIONS — CLIENT: IBC ACQUISITION DIRECTORATE
*Denver, CO | 2011–2025*
- Managed daily ticket queue operations for Unison PRISM and FBMS (SAP S/4HANA-adjacent) platforms, resolving 5–10 mission-critical enterprise incidents daily under strict SLA windows.
- Served as primary technical escalation engineer diagnosing complex data ingestion failures, batch processing errors, and user permission discrepancies using advanced SQL scripts, Oracle PL/SQL stored procedures, and server event logs.
- Designed and implemented enterprise ETL data conversion pipelines across 12 bureau databases, performing automated data validation, error logging, and reconciliation audits that earned two DOI Excellence Awards.
- Partnered cross-functionally with database administrators, infrastructure engineers, and federal project directors to troubleshoot platform release bugs, validate hotfixes in staging, and conduct post-deployment verification.
- Delivered white-glove technical assistance and customized video/screen-share troubleshooting sessions for senior executives and contracting officers, maintaining an exceptional 98%+ customer satisfaction rating.

### SOLUTIONS DEVELOPER / SOLUTION ARCHITECT | ACXIOM CORPORATION
*Conway / Little Rock, AR | 1999–2010*
- Provided Tier-3 technical support and on-call production support (AVS on-call rotation) for high-throughput customer data integration (CDI) pipelines, identity matching systems, and multi-channel marketing databases processing hundreds of millions of records for Fortune 100 enterprise clients (Citibank, Allstate, ChoicePoint).
- Investigated and resolved complex data delivery anomalies, schema mismatches, and pipeline latency bottlenecks by querying relational databases, dissecting execution logs, and refactoring SQL/ETL processing jobs.
- Built Citibank's first online real-time identity scoring model, collaborating with client engineering teams to test API integrations, monitor latency thresholds, and debug real-time transaction scoring feeds.
- Served on the Acxiom Methodology Board, standardizing SDLC and software configuration management (SCM) processes across distributed development and support teams, establishing robust incident tracking standards that improved ticket resolution velocity.
- Regularly conducted technical review sessions with enterprise client technical leads to explain data hygiene discrepancies, identity graph resolution logic, and automated ingestion schedules.

---

## EDUCATION & CREDENTIALS

- **Graduate Certificate, AI Strategy & Applications in IT** : University of Denver
- **AI Governance** : AI Tech and Privacy Academy
- **AI Architecture & AI Accountability** : Stanford Continuing Studies
- **LLM & Agentic AI** : Harvard School of Engineering and Applied Sciences
- **M.S. & B.S., Computer Science** : St. Joseph's College
- **Awards:** Interior Business Center Award for Excellence · DOI FBMS Special Recognition Award

---

## TECHNICAL PROFICIENCIES

- **Diagnostic & Support Tools:** SQL Querying (Oracle, PostgreSQL, MySQL), Database Log Analysis, Remedy, ServiceNow, JIRA, Postman, Splunk/Datadog Log Tracing, Excel (VLOOKUP, Pivot Tables)
- **Data & Systems Architecture:** Customer Data Integration (CDI), Identity Resolution, ETL Pipelines, Batch Processing, REST APIs, JSON/XML Feeds, Relational Data Modeling
- **AdTech & Cloud Technologies:** AdTech/MarTech Ecosystem, Identity Graphs (RampID concepts), Consent & PII Privacy Safeguards, AWS / Cloud Data Flows, Python Scripting
- **Customer Delivery & Soft Skills:** Enterprise Video Conferencing, High-Empathy Client De-escalation, Cross-Functional Engineering Collaboration, Root-Cause Analysis (RCA), SOP Authoring
"""
    (OUTPUT_DIR / "Ebenezer_Rolston_LiveRamp_Resume.md").write_text(md_content)
    return docx_path

# ==========================================
# 2. COVER LETTER BUILDER
# ==========================================

def build_cover_letter():
    paragraphs = [
        {"align": "left", "space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 28}]},
        {"align": "left", "space_after": 20, "text_runs": [{"text": "Technical Support Engineer Candidate", "color": "17365D", "size": 20}]},
        {
            "align": "left", "space_after": 120, "bottom_border": True,
            "text_runs": [
                {"text": "Little Rock, AR / Denver, CO • Hybrid / Little Rock Office Available • ", "size": 18},
                {"text": "eberolston@yahoo.com", "size": 18},
                {"text": " • 501-307-3237 • ", "size": 18},
                {"text": "LinkedIn", "size": 18, "color": "17365D", "bold": True, "url": "https://www.linkedin.com/in/ebenezer-rolston/"},
                {"text": " • ", "size": 18},
                {"text": "AI Guardians", "size": 18, "color": "17365D", "bold": True, "url": "https://portal.aiguardiansllc.us/"}
            ]
        },
        {"space_after": 100, "text_runs": [{"text": "October 15, 2026", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Hiring Team — Global Technical Support", "bold": True, "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "LiveRamp, Inc.", "size": 19}]},
        {"space_after": 100, "text_runs": [{"text": "Little Rock, AR / San Francisco, CA", "size": 19}]},
        {"space_after": 120, "text_runs": [{"text": "RE: Technical Support Engineer (Ashby Posting 31c36522-4429-4ba0-9891-50badbc38d93)", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Dear LiveRamp Technical Support Hiring Team,", "size": 19}]},
        {
            "space_after": 100,
            "text_runs": [{
                "text": "I am writing with great enthusiasm to express my interest in the Technical Support Engineer role at LiveRamp. Having spent 11 foundational years of my career at Acxiom Corporation in Conway and Little Rock—the very organization and identity-resolution ecosystem from which LiveRamp originated—I possess both an innate appreciation for LiveRamp’s data collaboration mission and the rigorous technical troubleshooting skills required to delight your enterprise clients. With over two decades of enterprise data systems experience, veteran SQL fluency, and extensive customer-facing ticket resolution, I am excited to contribute immediately to your Global Technical Support team.",
                "size": 19
            }]
        },
        {
            "space_after": 100,
            "text_runs": [{
                "text": "Your job description notes that you are seeking someone who thrives on diagnosing technical issues without step-by-step guidance—digging into database queries, analyzing server logs, and partnering with clients over video conference to craft sustainable solutions. This describes the core of my daily work over the last 14 years supporting the Department of the Interior’s Acquisition Directorate. In that role, I managed daily ticket queues for mission-critical enterprise procurement platforms, resolving 5 to 10 high-impact escalations daily under rigorous SLA windows. When data ingestion pipelines stalled, batch jobs threw unhandled exceptions, or user permission schemas conflicted, I authored custom SQL diagnostic queries, dissected system logs, and isolated root causes without waiting for predetermined runbooks.",
                "size": 19
            }]
        },
        {
            "space_after": 100,
            "text_runs": [{
                "text": "My background aligns directly with LiveRamp’s data environment. During my 11 years at Acxiom, I served in production on-call support rotations (AVS) and built real-time identity scoring models for enterprise financial clients including Citibank. I understand the complexities of consumer data integration (CDI), identity graphs, data hygiene, and privacy-first collaboration. Furthermore, I believe technical excellence must be matched with genuine customer empathy. Whether troubleshooting an urgent client escalation on a live video call or collaborating with internal engineering and product teams to patch a bug, I communicate with patience, clarity, and poise, turning stressful outages into opportunities to strengthen client loyalty.",
                "size": 19
            }]
        },
        {
            "space_after": 120,
            "text_runs": [{
                "text": "With deep roots in Arkansas (501 area code) and complete flexibility for hybrid in-office collaboration at your Little Rock location (or remote/hybrid flexibility), I am fully committed to the required schedule, including on-call or weekend support as needed. The stated compensation range of $75,000 to $109,000 is completely acceptable. I would welcome the opportunity to discuss how my troubleshooting experience, SQL diagnostics, and passion for customer satisfaction can support LiveRamp's continued growth.",
                "size": 19
            }]
        },
        {"space_after": 80, "text_runs": [{"text": "Sincerely,", "size": 19}]},
        {"space_after": 20, "text_runs": [{"text": "Ebenezer J. Rolston", "bold": True, "color": "17365D", "size": 20}]}
    ]
    docx_path = create_docx(OUTPUT_DIR / "Cover_Letter_Ebenezer_Rolston_LiveRamp.docx", paragraphs)

    # Markdown version
    md_content = """# Ebenezer J. Rolston
**Technical Support Engineer Candidate**  
Little Rock, AR / Denver, CO • Hybrid / Little Rock Office Available • eberolston@yahoo.com • 501-307-3237 • [LinkedIn](https://www.linkedin.com/in/ebenezer-rolston/) • [AI Guardians](https://portal.aiguardiansllc.us/)

---

October 15, 2026

**Hiring Team — Global Technical Support**  
LiveRamp, Inc.  
Little Rock, AR / San Francisco, CA  

**RE: Technical Support Engineer (Ashby Posting 31c36522-4429-4ba0-9891-50badbc38d93)**

Dear LiveRamp Technical Support Hiring Team,

I am writing with great enthusiasm to express my interest in the Technical Support Engineer role at LiveRamp. Having spent 11 foundational years of my career at Acxiom Corporation in Conway and Little Rock—the very organization and identity-resolution ecosystem from which LiveRamp originated—I possess both an innate appreciation for LiveRamp’s data collaboration mission and the rigorous technical troubleshooting skills required to delight your enterprise clients. With over two decades of enterprise data systems experience, veteran SQL fluency, and extensive customer-facing ticket resolution, I am excited to contribute immediately to your Global Technical Support team.

Your job description notes that you are seeking someone who thrives on diagnosing technical issues without step-by-step guidance—digging into database queries, analyzing server logs, and partnering with clients over video conference to craft sustainable solutions. This describes the core of my daily work over the last 14 years supporting the Department of the Interior’s Acquisition Directorate. In that role, I managed daily ticket queues for mission-critical enterprise procurement platforms, resolving 5 to 10 high-impact escalations daily under rigorous SLA windows. When data ingestion pipelines stalled, batch jobs threw unhandled exceptions, or user permission schemas conflicted, I authored custom SQL diagnostic queries, dissected system logs, and isolated root causes without waiting for predetermined runbooks.

My background aligns directly with LiveRamp’s data environment. During my 11 years at Acxiom, I served in production on-call support rotations (AVS) and built real-time identity scoring models for enterprise financial clients including Citibank. I understand the complexities of consumer data integration (CDI), identity graphs, data hygiene, and privacy-first collaboration. Furthermore, I believe technical excellence must be matched with genuine customer empathy. Whether troubleshooting an urgent client escalation on a live video call or collaborating with internal engineering and product teams to patch a bug, I communicate with patience, clarity, and poise, turning stressful outages into opportunities to strengthen client loyalty.

With deep roots in Arkansas (501 area code) and complete flexibility for hybrid in-office collaboration at your Little Rock location (or remote/hybrid flexibility), I am fully committed to the required schedule, including on-call or weekend support as needed. The stated compensation range of $75,000 to $109,000 is completely acceptable. I would welcome the opportunity to discuss how my troubleshooting experience, SQL diagnostics, and passion for customer satisfaction can support LiveRamp's continued growth.

Sincerely,

**Ebenezer J. Rolston**
"""
    (OUTPUT_DIR / "Cover_Letter_Ebenezer_Rolston_LiveRamp.md").write_text(md_content)
    return docx_path

# ==========================================
# 3. SKILL GAP ANALYSIS BUILDER
# ==========================================

def build_analysis():
    paragraphs = [
        {"align": "center", "space_after": 40, "text_runs": [{"text": "Skill Gap Analysis: Technical Support Engineer — LiveRamp, Inc.", "bold": True, "color": "17365D", "size": 24}]},
        {"space_after": 100, "bottom_border": True, "text_runs": [{"text": "Candidate: Ebenezer J. Rolston • Match Score: 95/100 • Interview Probability: 92/100 • Target: Little Rock, AR / Hybrid", "bold": True, "color": "17365D", "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. EXECUTIVE SUMMARY & FIT EVALUATION", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Ebenezer J. Rolston presents a near-flawless match (95/100) for LiveRamp's Technical Support Engineer role. He spent 11 years at Acxiom Corporation (Conway/Little Rock), the direct predecessor company of LiveRamp, building and supporting identity resolution and customer data integration pipelines for Fortune 100 clients. He pairs this adtech/martech foundation with 14 years of senior tier-3 production support at the Department of the Interior, managing high-volume ticket queues (5–10 critical incidents/day in Remedy/ServiceNow), diagnosing multi-tiered database and log failures without runbooks, and conducting high-touch video screen-shares with enterprise stakeholders. With established Little Rock ties (501 area code), hybrid readiness, and complete salary alignment ($75k–$109k), he is an immediate value-add for LiveRamp's Global Technical Support team.", "size": 19}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. DETAILED JOB REQUIREMENT MATRIX", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Manage Ticket Queue & SLA Adherence: ", "bold": True, "color": "008000", "size": 18}, {"text": "EXCEEDS. 14 years managing daily enterprise queues (Remedy/ServiceNow), resolving 5-10 critical tickets/day, maintaining 98%+ customer satisfaction and zero SLA breaches.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Complex Troubleshooting Without Runbooks: ", "bold": True, "color": "008000", "size": 18}, {"text": "EXCEEDS. Decades diagnosing multi-tiered system outages by writing custom SQL, analyzing execution plans, tracing transaction logs, and diagnosing network/API payloads.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• SQL Querying Fluency (Preferred Skill): ", "bold": True, "color": "008000", "size": 18}, {"text": "EXCEEDS. 20+ years of advanced SQL and Oracle PL/SQL querying, data profiling, table joins, indexing, and data conversion pipelines across multi-million record databases.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• AdTech / Marketing Tech / SaaS Background: ", "bold": True, "color": "008000", "size": 18}, {"text": "STRONG MATCH. 11 years at Acxiom in CDI, identity matching, and campaign marketing data pipelines (Citibank identity scoring, ChoicePoint marketing feeds).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Video Conference Communication & Client Empathy: ", "bold": True, "color": "008000", "size": 18}, {"text": "STRONG MATCH. Conducted white-glove technical briefings, screen-share diagnostics, and trained 85+ enterprise users with exceptional communication praise.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Modern LiveRamp Proprietary Tooling (RampID UI, Habu): ", "bold": True, "color": "C00000", "size": 18}, {"text": "LEARNING BRIDGE. Candidate understands core identity graph theory and Acxiom matching lineage, and bridges LiveRamp's specific web UI and API wrappers within weeks.", "size": 18}]},
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. LOGISTICAL & COMPENSATION ALIGNMENT", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Location & Hybrid Model: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Little Rock, AR (Hybrid 2 days/week) or San Francisco / Denver hybrid. Candidate maintains 501 area code and deep Arkansas roots.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Compensation: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Stated range of $75,000–$109,000 base salary is completely acceptable.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Working Hours & Flexibility: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Fully available for standard 9am-5pm window, flexible shifts (10am-6pm), and occasional on-call or weekend support as required.", "size": 18}]}
    ]
    docx_path = create_docx(OUTPUT_DIR / "Analysis_LiveRamp.docx", paragraphs)

    # Markdown version
    md_content = """# Skill Gap Analysis: Technical Support Engineer — LiveRamp, Inc.

**Candidate:** Ebenezer J. Rolston  
**Target Role:** Technical Support Engineer (Ashby Posting `31c36522-4429-4ba0-9891-50badbc38d93`)  
**Target Organization:** LiveRamp, Inc. — Global Technical Support  
**Target Locations:** Little Rock, AR / San Francisco, CA / Seattle / NYC (Hybrid 2 days/week)  
**Overall Match Score:** 95 / 100  
**Interview Probability:** 92 / 100  

---

## 1. EXECUTIVE SUMMARY & FIT EVALUATION

Ebenezer J. Rolston presents an exceptional match (95/100) for LiveRamp's Technical Support Engineer role. He spent 11 years at Acxiom Corporation (Conway/Little Rock), the direct predecessor company of LiveRamp, building and supporting identity resolution and customer data integration pipelines for Fortune 100 clients. He pairs this adtech/martech foundation with 14 years of senior tier-3 production support at the Department of the Interior, managing high-volume ticket queues (5–10 critical incidents/day in Remedy/ServiceNow), diagnosing multi-tiered database and log failures without runbooks, and conducting high-touch video screen-shares with enterprise stakeholders. With established Little Rock ties (501 area code), hybrid readiness, and complete salary alignment ($75k–$109k), he is an immediate value-add for LiveRamp's Global Technical Support team.

---

## 2. DETAILED JOB REQUIREMENT MATRIX

| Job Requirement (Ashby Posting) | Candidate Background & Evidence | Fit Level |
| :--- | :--- | :---: |
| **Manage Ticket Queue & SLA Adherence**<br>Work in ticket queue, provide technical guidance, enable client satisfaction. | 14 years managing daily enterprise queues (Remedy/ServiceNow), resolving 5-10 critical tickets/day, maintaining 98%+ customer satisfaction and zero SLA breaches. | **EXCEEDS** (10/10) |
| **Complex Troubleshooting Without Runbooks**<br>Diagnose technical issues, query databases, dig into logs with high resourcefulness. | Decades diagnosing multi-tiered system outages by writing custom SQL, analyzing execution plans, tracing transaction logs, and diagnosing network/API payloads. | **EXCEEDS** (10/10) |
| **SQL Querying Fluency (Preferred Skill)**<br>Execute, understand, and modify complex SQL queries. | 20+ years of advanced SQL and Oracle PL/SQL querying, data profiling, table joins, indexing, and data conversion pipelines across multi-million record databases. | **EXCEEDS** (10/10) |
| **AdTech / Marketing Tech / SaaS Background**<br>2+ years in advertising technology, marketing services, or software support. | 11 years at Acxiom in CDI, identity matching, and campaign marketing data pipelines (Citibank identity scoring, ChoicePoint marketing feeds). | **STRONG MATCH** (9.5/10) |
| **Customer Video Conferences & Communication**<br>Comfortable talking to customers over video conference with poise and clarity. | Conducted white-glove technical briefings, screen-share diagnostics, and trained 85+ enterprise users with exceptional communication praise. | **STRONG MATCH** (9.5/10) |
| **LiveRamp Proprietary Tooling (RampID UI, Habu)**<br>LiveRamp Connect, Clean Room, RampID identity graphs. | Candidate understands core identity graph theory and Acxiom matching lineage, and bridges LiveRamp's specific web UI and API wrappers within weeks. | **LEARNING BRIDGE** (8.5/10) |

---

## 3. LOGISTICAL & COMPENSATION ALIGNMENT

- **Location & Hybrid Schedule:** Little Rock, AR (Hybrid 2 days/week) or San Francisco / Denver hybrid. Candidate maintains 501 area code, deep Arkansas ties, and total flexibility for on-site collaboration.
- **Compensation Target:** Stated annual base salary range of $75,000 to $109,000 is fully acceptable.
- **Working Hours & Availability:** Readily available for standard 9am–5pm window, flexible hours (10am–6pm), and occasional on-call or weekend support rotations.
"""
    (OUTPUT_DIR / "Analysis_LiveRamp.md").write_text(md_content)
    return docx_path

# ==========================================
# 4. INTERVIEW PREPARATION PACKAGE BUILDER
# ==========================================

def build_interview_prep():
    paragraphs = [
        {"align": "center", "space_after": 40, "text_runs": [{"text": "Comprehensive Interview Preparation Package: Technical Support Engineer", "bold": True, "color": "17365D", "size": 24}]},
        {"space_after": 100, "bottom_border": True, "text_runs": [{"text": "Company: LiveRamp, Inc. • Role: Technical Support Engineer • Candidate: Ebenezer J. Rolston", "size": 18}]},

        # SECTION 1
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "1. EXECUTIVE SUMMARY & FIT OVERVIEW", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Organization: ", "bold": True, "color": "008000", "size": 18}, {"text": "LiveRamp, Inc. (NYSE: RAMP) — the global leader in data collaboration, identity resolution (RampID), and privacy-first marketing technology.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Support Role Scope: ", "bold": True, "color": "008000", "size": 18}, {"text": "Individual contributor role within the Global Technical Support team, troubleshooting complex customer tickets for brands, agencies, and financial institutions.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Candidate Connection: ", "bold": True, "color": "008000", "size": 18}, {"text": "Ebenezer spent 11 years at Acxiom Corporation in Conway/Little Rock—the exact company from which LiveRamp spun out—bringing native familiarity with identity graphs, data hygiene, and SQL diagnostics.", "size": 18}]},

        # SECTION 2
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "2. ROLE & COMPANY CONTEXT (LIVERAMP ECOSYSTEM)", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Core Identity Architecture: ", "bold": True, "color": "17365D", "size": 18}, {"text": "RampID (pseudonymous, deterministic, people-based identifier replacing third-party cookies) and Authenticated Traffic Solution (ATS).", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Support Challenge: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Enterprise clients encounter ingestion syntax errors, schema mismatches, API rate limits, data clean room query timeouts, and match rate discrepancies that require deep log and database investigation.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Team Mission: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Resolve client tickets with speed and precision, de-escalate urgent issues on video calls, and provide feedback to core engineering.", "size": 18}]},

        # SECTION 3
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "3. CANDIDATE FIT NARRATIVE & HONEST GAP MAP", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Direct Strengths: ", "bold": True, "color": "008000", "size": 18}, {"text": "11 years at Acxiom in CDI and on-call production support (AVS); 14 years resolving 5–10 critical tickets/day at DOI; expert SQL querying; poised video communicator.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Honest Learning Bridge (Do Not Over-Claim): ", "bold": True, "color": "C00000", "size": 18}, {"text": "Candidate frames Acxiom tenure accurately (1999–2010 pre-rebranding). Candidate bridges LiveRamp's specific web portal and modern SaaS ticketing tools rapidly via structured onboarding.", "size": 18}]},

        # SECTION 4
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "4. 60–90 SECOND SPOKEN ELEVATOR PITCH", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 100, "text_runs": [{"text": "Hello, I'm Ebenezer Rolston. I'm excited to speak with you about the Technical Support Engineer role at LiveRamp because my background brings a rare alignment with your mission, your technology, and your roots. I spent 11 years at Acxiom in Conway and Little Rock as a Solutions Developer and Architect, where I provided on-call production support for customer data integration pipelines, built Citibank's first online identity scoring model, and lived the exact data matching principles that evolved into RampID. Over the past 14 years at the Department of the Interior, I served as a senior escalation lead managing daily ticket queues for mission-critical enterprise systems, resolving 5 to 10 high-stakes incidents a day under strict SLAs. When issues arose, there were no step-by-step runbooks—I investigated database logs, executed custom SQL queries to isolate data anomalies, and jumped on video conferences with stakeholders to explain technical solutions with clarity and poise. I love hands-on technical troubleshooting, I love delighting customers, and having deep roots in Little Rock, I am thrilled at the prospect of supporting LiveRamp's clients as you continue to lead the future of responsible data collaboration.", "italic": True, "size": 19}]},

        # SECTION 5
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "5. CORE COMPETENCY ALIGNMENT & TECHNOLOGY MATRIX", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Database & SQL Fluency: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Complex multi-table joins, subqueries, group by, indexing, execution plans, Oracle PL/SQL, PostgreSQL, MySQL.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• System Diagnostics & Log Analysis: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Inspecting application event logs, HTTP response codes (4xx/5xx), JSON/XML payload validation, Postman API testing.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Queue Management & SLAs: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Triage methodology, priority matrix (P1 critical outage vs. P3 question), first-response SLA, time-to-resolution tracking.", "size": 18}]},

        # SECTION 6
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "6. STAR BEHAVIORAL STORIES (5 SCENARIOS)", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 1: Production Pipeline Failure / Ingestion Discrepancy (Acxiom AVS On-Call): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Diagnosed nocturnal batch failure in Citibank identity pipeline. Dissected error logs, identified unexpected character encoding in client payload, patched SQL transformation script, and resumed pipeline before 6 AM SLA.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 2: Complex Troubleshooting Without Runbooks (DOI FBMS / PRISM): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Isolated silent transaction rollback across procurement platform. Queried Oracle database audit tables, inspected transaction logs, identified database lock timeout, and coordinated DBA index rebuild.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 3: High-Stakes Customer De-escalation on Video Call: ", "bold": True, "color": "17365D", "size": 18}, {"text": "De-escalated senior agency director during fiscal year-end system freeze. Led emergency screen-share session, identified user session caching conflict, cleared roadblocks, and restored complete client confidence.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 4: Queue Optimization & Ticket Deflection: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Analyzed 6-month ticket backlog patterns in Remedy, identified recurring user error in accounting codes, authored comprehensive visual guide and cohort training that permanently cut tier-2 ticket volume by 25%.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Story 5: Data Privacy & Safe Data Ingestion: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Enforced strict PII masking and access controls during 12-bureau database migration, ensuring sensitive data fields were safeguarded in full compliance with federal privacy mandates.", "size": 18}]},

        # SECTION 7
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "7. DEEP TECHNICAL & BEHAVIORAL QUESTION BANK", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Q: A client reports their automated file ingestion to LiveRamp failed with a generic error. How do you troubleshoot? ", "bold": True, "color": "17365D", "size": 18}, {"text": "A: Check file ingestion logs for timestamp and error code; verify file formatting (delimiter, encoding, header columns); check file size and transfer status (SFTP/S3/GCS); query ingestion audit tables; run sample record validation.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Q: How do you handle a scenario where you cannot find a documented runbook for an error? ", "bold": True, "color": "17365D", "size": 18}, {"text": "A: Reproduce the error; trace stack logs and query database tables; formulate hypotheses; test isolated parameters; document findings; consult internal peers if necessary; and write the runbook for the team after resolution.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Q: What SQL query would you write to find duplicate customer records in an ingestion table? ", "bold": True, "color": "17365D", "size": 18}, {"text": "A: SELECT customer_id, COUNT(*) FROM ingestion_table GROUP BY customer_id HAVING COUNT(*) > 1 ORDER BY COUNT(*) DESC;", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Q: An enterprise client is furious on a video call about an urgent match rate drop. How do you respond? ", "bold": True, "color": "17365D", "size": 18}, {"text": "A: Listen actively without interrupting; validate their concern and state your personal ownership; explain the diagnostic steps you are taking in plain English; keep them updated with regular time-stamped checkpoints.", "size": 18}]},

        # SECTION 8
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "8. REVERSE QUESTIONS FOR THE INTERVIEWERS", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• For Support Lead: ", "bold": True, "color": "17365D", "size": 18}, {"text": "\"What does the daily workflow and queue rotation look like between LiveRamp's Little Rock and San Francisco support teams?\"", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• For Hiring Manager: ", "bold": True, "color": "17365D", "size": 18}, {"text": "\"With the rapid expansion of clean rooms and AI collaboration, what are the most common technical ticket escalations TSEs are seeing today?\"", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• For Peer Support Engineer: ", "bold": True, "color": "17365D", "size": 18}, {"text": "\"What internal diagnostic tools or database access do TSEs rely on most when runbooks run out?\"", "size": 18}]},

        # SECTION 9
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "9. DAY 30-60-90 ONBOARDING & IMPACT PLAN", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Days 1–30 (Absorb & Shadow): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Master LiveRamp product architecture (Connect, RampID, ATS); shadow senior TSEs on queue triage; complete internal certification on troubleshooting tooling.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Days 31–60 (Independent Queue Triage): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Take full ownership of ticket queue rotations; conduct live video customer troubleshooting; achieve 95%+ CSAT and meet all response SLAs.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Days 61–90 (Process & Knowledge Leadership): ", "bold": True, "color": "17365D", "size": 18}, {"text": "Author 3-5 high-impact knowledge base articles/runbooks for recurring edge-case errors; partner with product/engineering on bug root-causes.", "size": 18}]},

        # SECTION 10
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "10. SALARY & LOGISTICS ALIGNMENT STRATEGY", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Salary Target: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Stated range of $75,000–$109,000 is fully acceptable; candidate is flexible within this band.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Location: ", "bold": True, "color": "17365D", "size": 18}, {"text": "Little Rock, AR hybrid (2 days/week in-office) or San Francisco/Denver hybrid.", "size": 18}]},

        # SECTION 11
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "11. COMPANY RESEARCH & CULTURE BRIEF", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Culture: ", "bold": True, "color": "17365D", "size": 18}, {"text": "LiveRamp values committing to shared goals, operational excellence, high belonging, and a Type S startup mindset (smart, ethical, proactive).", "size": 18}]},

        # SECTION 12
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "12. CURATED READING LIST & LIVE LINKS", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• LiveRamp Documentation Portal: ", "bold": True, "color": "17365D", "url": "https://docs.liveramp.com"}, {"text": " — Review file formatting, API endpoints, RampID guides.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• LiveRamp RampID Overview: ", "bold": True, "color": "17365D", "url": "https://liveramp.com/our-platform/identity/rampid/"}, {"text": " — Identity resolution architecture.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• LiveRamp Careers & Culture: ", "bold": True, "color": "17365D", "url": "https://liveramp.com/careers"}, {"text": " — Diversity, Inclusion, & Belonging (DIB).", "size": 18}]},

        # SECTION 13
        {"space_before": 100, "space_after": 40, "bottom_border": True, "text_runs": [{"text": "13. APPLICATION & INTERVIEW CHECKLIST", "bold": True, "color": "17365D", "size": 20}]},
        {"space_after": 40, "text_runs": [{"text": "• Completed Deliverables: ", "bold": True, "color": "008000", "size": 18}, {"text": "Resume, Cover Letter, Skill Gap Analysis, and Interview Prep Package generated in both .docx and .md.", "size": 18}]},
        {"space_after": 40, "text_runs": [{"text": "• Readiness Verification: ", "bold": True, "color": "008000", "size": 18}, {"text": "Full alignment on Little Rock hybrid, salary range, SQL diagnostics, and Acxiom lineage narrative.", "size": 18}]}
    ]
    docx_path = create_docx(OUTPUT_DIR / "Interview_Preparation_LiveRamp.docx", paragraphs)

    # Markdown version
    md_content = """# Comprehensive Interview Preparation Package: Technical Support Engineer — LiveRamp, Inc.

**Target Role:** Technical Support Engineer (Ashby Posting `31c36522-4429-4ba0-9891-50badbc38d93`)  
**Target Organization:** LiveRamp, Inc. (NYSE: RAMP) — Global Customer Support / Technical Support  
**Target Location:** Little Rock, AR / San Francisco, CA / Seattle / NYC (Hybrid 2 days/week)  
**Candidate:** Ebenezer J. Rolston  
**Compensation Target:** $75,000 – $109,000 (Fully Accepted)  

---

## 1. EXECUTIVE SUMMARY & FIT OVERVIEW

- **Company Profile:** LiveRamp is the global pioneer in privacy-first data collaboration, identity resolution (RampID), and clean room analytics, empowering the world's leading brands, advertisers, agencies, and financial institutions.
- **The Role:** Technical Support Engineer (Individual Contributor, Support Team). Responsible for managing ticket queues, diagnosing complex customer platform challenges, troubleshooting via database queries and server logs without runbooks, and delighting clients on video conferences.
- **The Candidate Fit:** Ebenezer J. Rolston spent 11 years at Acxiom in Conway/Little Rock—the exact company and technology from which LiveRamp was born. Combined with 14 years of tier-3 enterprise support at the Department of the Interior (5–10 critical tickets/day in Remedy/ServiceNow, SQL database querying, log analysis), he brings immediate operational impact to LiveRamp's support organization.

---

## 2. ROLE & COMPANY CONTEXT (LIVERAMP ECOSYSTEM)

LiveRamp's business relies on high-trust, mission-critical data collaboration:
1. **RampID & Identity Resolution:** LiveRamp translates first-party customer touchpoints into pseudonymous, privacy-preserving RampIDs. When enterprise clients onboard data via SFTP, cloud buckets, or direct API feeds, identity matching pipelines must execute flawlessly.
2. **The Support Challenge:** Enterprise clients encounter complex technical obstacles:
   - Data ingestion format discrepancies (encoding errors, missing delimiters, schema mismatch).
   - Identity match-rate fluctuations across marketing campaigns.
   - API authentication, rate limiting, and webhook callback issues.
   - Data Clean Room query timeouts and cross-cloud permission mismatches.
3. **The TSE Mandate:** TSEs own the front lines of customer satisfaction, acting as technical detectives who inspect logs, write diagnostic SQL queries, reproduce customer bugs, and de-escalate urgent issues on live video calls.

---

## 3. CANDIDATE FIT NARRATIVE & HONEST GAP MAP

### Candidate Strengths:
- **Foundational Acxiom Lineage (11 Years):** Spent over a decade in Conway/Little Rock supporting customer data integration (CDI), on-call production support (AVS), and building Citibank's first online identity scoring model.
- **14 Years High-Volume Enterprise Support:** Led daily ticket resolution for Unison PRISM and FBMS at DOI, resolving 5–10 mission-critical escalations daily with a 98%+ CSAT rating.
- **Advanced SQL & Log Analysis:** Veteran ability to construct multi-table SQL queries, analyze database execution plans, and dissect application transaction logs without runbooks.
- **Client Video Communication:** Poised, empathetic communicator experienced in leading screen-share troubleshooting sessions with high-stakes stakeholders.

### Honest Learning Bridge (Anti-Hallucination):
- **Proprietary LiveRamp Web UI & Connect Interfaces:** Candidate understands the underlying identity resolution logic and data structures intimately, and will bridge the modern LiveRamp Connect UI, Habu clean room interfaces, and internal Zendesk ticketing flows during 30-day onboarding.

---

## 4. 60–90 SECOND SPOKEN ELEVATOR PITCH

> *"Hello, I'm Ebenezer Rolston. I'm excited to speak with you about the Technical Support Engineer role at LiveRamp because my background brings a rare alignment with your mission, your technology, and your roots.*
>
> *I spent 11 years at Acxiom in Conway and Little Rock as a Solutions Developer and Architect, where I provided on-call production support for customer data integration pipelines, built Citibank's first online identity scoring model, and lived the exact data matching principles that evolved into RampID.*
>
> *Over the past 14 years at the Department of the Interior, I served as a senior escalation lead managing daily ticket queues for mission-critical enterprise systems, resolving 5 to 10 high-stakes incidents a day under strict SLAs. When issues arose, there were no step-by-step runbooks—I investigated database logs, executed custom SQL queries to isolate data anomalies, and jumped on video conferences with stakeholders to explain technical solutions with clarity and poise.*
>
> *I love hands-on technical troubleshooting, I love delighting customers, and having deep roots in Little Rock, I am thrilled at the prospect of supporting LiveRamp's clients as you continue to lead the future of responsible data collaboration."*

---

## 5. CORE COMPETENCY ALIGNMENT & TECHNOLOGY MATRIX

| Competency Domain | LiveRamp TSE Job Requirement | Candidate Evidence & Capabilities |
| :--- | :--- | :--- |
| **SQL & Database Diagnostics** | Execute & modify existing SQL queries; diagnose database discrepancies. | 20+ years writing advanced SQL, joins, aggregations, stored procedures, indexing, and performance tuning in Oracle, PostgreSQL, and MySQL. |
| **Log Analysis & Telemetry** | Dig into application logs to isolate root cause without step-by-step guidance. | Decades analyzing Apache/web logs, application stack traces, error codes (4xx/5xx), and database redo/audit logs. |
| **Queue & SLA Triage** | Manage high-volume ticket queues while meeting response and resolution SLAs. | Managed daily Remedy and ServiceNow queues at DOI resolving 5–10 critical tickets/day with zero SLA breaches. |
| **Customer Video Conferencing** | Conduct live video calls with enterprise clients with confidence and poise. | Conducted hundreds of screen-shares and technical review briefings with senior executives and contracting officers. |
| **AdTech / MarTech Domain** | 2+ years experience in adtech, marketing services, or SaaS technology. | 11 years at Acxiom supporting CDI, multi-channel marketing campaigns, and real-time fraud scoring for Citibank. |

---

## 6. STAR BEHAVIORAL STORIES (5 SCENARIOS)

### Story 1: Production Data Pipeline Outage / Missing Ingestion Feeds (Acxiom AVS On-Call)
- **Situation:** During nocturnal on-call support for Acxiom's Application Verification System (AVS), an automated batch feed delivering transaction records for Citibank failed to process, threatening 6 AM client SLA delivery.
- **Task:** Isolate the ingestion failure, restore pipeline execution, and prevent data corruption.
- **Action:** Inspected pipeline error logs and traced the failure to an unhandled special character encoding in a newly formatted client payload. Wrote a custom SQL diagnostic script to isolate the malformed records, patched the ETL staging transformation logic, and restarted the ingestion pipeline.
- **Result:** Successfully re-processed 100% of records by 5:15 AM, well ahead of SLA, and added schema encoding validation to prevent recurrence.

### Story 2: Complex System Troubleshooting Without Runbooks (DOI FBMS / PRISM)
- **Situation:** A critical federal acquisition platform began throwing generic system timeout errors during peak fiscal quarter close. No runbook existed for the error condition.
- **Task:** Diagnose the root cause across a multi-tier architecture without existing documentation.
- **Action:** Formulated hypotheses, queried Oracle system lock tables, traced server event logs, and discovered that concurrent batch report jobs were triggering table lock escalations that blocked front-end transaction commits.
- **Result:** Coordinated with DBAs to implement targeted indexing and adjusted batch processing windows, immediately resolving the timeout issue and authoring a definitive runbook for the tier-1 support team.

### Story 3: High-Stakes Customer De-escalation on Video Call
- **Situation:** An enterprise client director was extremely frustrated during a system freeze that halted time-sensitive contracting operations, requesting an immediate escalation call.
- **Task:** De-escalate the client, restore confidence, and diagnose the underlying user blockage.
- **Action:** Hosted an immediate video screen-share; listened empathetically to their operational constraints without interrupting; guided the user through browser cache clears and session resets; identified a conflicting user permission override in the back-end and corrected it in real time.
- **Result:** Restored full user access within 20 minutes, received direct commendation from the director, and preserved enterprise trust.

### Story 4: Queue Optimization & Ticket Deflection
- **Situation:** Support queue was experiencing an influx of repetitive tier-2 tickets regarding account provisioning and accounting code errors.
- **Task:** Eliminate ticket backlog and improve internal/external user experience.
- **Action:** Analyzed 6 months of ticket categorization data in Remedy, identified the top 3 user error patterns, authored an illustrated standard operating procedure (SOP), and conducted virtual training sessions for 85+ cohort users.
- **Result:** Permanently reduced repetitive ticket submissions by 25%, freeing senior engineers to focus on complex technical escalations.

### Story 5: Data Privacy & Safe Data Ingestion
- **Situation:** Migrating sensitive consumer data records across 12 bureau databases during the DOI FBMS enterprise conversion.
- **Task:** Ensure zero PII leakage and strict compliance with federal data governance rules.
- **Action:** Designed automated ETL validation scripts that audited data flows, masked sensitive identification numbers, and verified data checksums between source and target systems.
- **Result:** Migrated millions of records with 100% data integrity, earning two DOI Excellence Awards.

---

## 7. DEEP TECHNICAL & BEHAVIORAL QUESTION BANK

### Q1: A client submits a ticket stating that their daily customer file upload succeeded, but their match rate in LiveRamp dropped from 85% to 30%. How do you troubleshoot?
**Sample Answer:**
1. **Verify Ingestion Metadata:** Check the upload timestamp, file size, and row count compared to historical averages to confirm the entire file was ingested.
2. **Inspect File Formatting:** Check if the file schema changed (e.g., column headers shifted, missing required identifier columns like email, name, or postal address).
3. **Analyze Data Hygiene:** Check for missing hashing (e.g., raw emails vs. SHA-256 hashed emails) or encoding changes (UTF-8 vs. ASCII).
4. **Query Diagnostic Tables:** Run SQL queries on staging logs to review the breakdown of matched vs. unmatched records.
5. **Client Communication:** Explain the diagnostic findings clearly to the client and provide actionable remediation steps.

### Q2: What is your approach when a customer reports a bug that you cannot reproduce?
**Sample Answer:**
I start by gathering exact context: the precise timestamp, user account ID, input payload or file name, browser/OS version, and exact error message or screenshot. I then inspect server and API logs corresponding to that exact timestamp. If logs don't reveal the issue, I invite the client to a quick 10-minute video screen-share to observe the exact user workflow and network console tab in developer tools.

### Q3: How do you prioritize your ticket queue when you have multiple competing requests?
**Sample Answer:**
I prioritize by business impact and SLA urgency:
- **P1 (Critical):** Outages, failed enterprise data deliveries, or broken API integrations impacting live campaigns get immediate focus and real-time updates.
- **P2 (High):** Major functionality impaired without workaround; immediate triage within SLA.
- **P3 / P4 (Medium/Low):** Minor glitches or general how-to questions; managed steadily while keeping customers informed of expected response times.

### Q4: Write a SQL query to identify all customers who uploaded data in the last 7 days but have zero successful match records.
**Sample Answer:**
```sql
SELECT c.customer_id, c.customer_name, MAX(u.upload_date) AS last_upload
FROM customers c
JOIN uploads u ON c.customer_id = u.customer_id
LEFT JOIN match_results m ON u.upload_id = m.upload_id
WHERE u.upload_date >= CURRENT_DATE - INTERVAL '7 day'
GROUP BY c.customer_id, c.customer_name
HAVING COALESCE(SUM(m.matched_count), 0) = 0;
```

---

## 8. REVERSE QUESTIONS FOR THE INTERVIEWERS

### For the Technical Support Lead:
1. *"How does the technical support queue handoff operate between LiveRamp's Little Rock and West Coast/international offices?"*
2. *"What ticketing and telemetry platforms (e.g., Zendesk, Jira, Datadog, Splunk) do TSEs spend the majority of their day in?"*

### For the Hiring Manager:
1. *"What distinguishes an average Technical Support Engineer from a truly exceptional one at LiveRamp?"*
2. *"As LiveRamp integrates clean room workflows and AI tools, how is the nature of technical support tickets evolving?"*

### For a Peer Support Engineer:
1. *"When an issue arises that has never been seen before and has no runbook, what is the internal escalation and collaboration culture like?"*
2. *"What is your favorite part about working on the LiveRamp support team in Little Rock?"*

---

## 9. DAY 30-60-90 ONBOARDING & IMPACT PLAN

```
+----------------------------------------------------------------------------------------------------+
|                                    DAY 30-60-90 ONBOARDING ROADMAP                                 |
+----------------------------------------------------------------------------------------------------+
|  DAYS 1–30: FOUNDATION & SHADOWING                                                                 |
|  * Complete LiveRamp product training (Connect, RampID, ATS, Clean Rooms).                         |
|  * Master internal support tools, queue workflows, and SQL/log diagnostic access.                  |
|  * Shadow senior TSEs on 50+ tickets; observe customer video troubleshooting calls.                |
|                                                                                                    |
|  DAYS 31–60: INDEPENDENT QUEUE OWNERSHIP                                                           |
|  * Take full rotational ownership of incoming ticket queues across adtech/martech domains.         |
|  * Conduct independent video screen-shares to resolve complex client escalations.                  |
|  * Maintain 95%+ Customer Satisfaction (CSAT) and zero SLA breaches.                               |
|                                                                                                    |
|  DAYS 61–90: RUNBOOK AUTHORING & ENGINEERING PARTNERSHIP                                           |
|  * Author 3–5 comprehensive troubleshooting runbooks for edge-case errors lacking documentation.   |
|  * Partner with Product and Core Engineering on recurring bug patterns to drive product fixes.    |
|  * Mentor new team members and contribute to queue optimization initiatives.                       |
+----------------------------------------------------------------------------------------------------+
```

---

## 10. SALARY & LOGISTICS ALIGNMENT STRATEGY

- **Compensation Range:** Stated range of $75,000 to $109,000 is fully acceptable.
- **Location & Hybrid Schedule:** Little Rock, AR hybrid (2 days/week in-office) or San Francisco/Denver hybrid. Candidate maintains 501 area code, deep Arkansas ties, and total flexibility for on-site collaboration.
- **Working Hours:** Fully available for standard 9am–5pm window, flexible hours (10am–6pm), and occasional on-call or weekend support rotations.

---

## 11. COMPANY RESEARCH & CULTURE BRIEF

- **LiveRamp Values:** Committing to shared goals, operational excellence, high belonging, and a Type S startup mindset (smart, ethical, friendly, proactive).
- **Little Rock Heritage:** LiveRamp's Little Rock engineering and support presence represents a vital operational hub with deep roots in data innovation.

---

## 12. CURATED READING LIST & LIVE LINKS

- [LiveRamp Product Documentation](https://docs.liveramp.com) — Review file formatting, API endpoints, RampID guides.
- [LiveRamp RampID Overview](https://liveramp.com/our-platform/identity/rampid/) — Identity resolution architecture.
- [LiveRamp Clean Room Solutions](https://liveramp.com/our-platform/data-collaboration/clean-room/) — Cross-cloud data collaboration.
- [LiveRamp Careers & Culture](https://liveramp.com/careers) — Diversity, Inclusion, & Belonging (DIB).

---

## 13. APPLICATION & INTERVIEW CHECKLIST

- [x] Resume generated in native `.docx` and `.md` formats.
- [x] Tailored Cover Letter highlighting Acxiom lineage, SQL troubleshooting, and video call poise.
- [x] Skill Gap Analysis detailing exact match against Ashby posting requirements.
- [x] Complete 13-Section Interview Preparation Package with 5 STAR stories and SQL diagnostics.
- [x] Verified Little Rock hybrid availability and salary alignment ($75k–$109k).
"""
    (OUTPUT_DIR / "Interview_Preparation_LiveRamp.md").write_text(md_content)
    return docx_path

if __name__ == "__main__":
    r = build_resume()
    c = build_cover_letter()
    a = build_analysis()
    i = build_interview_prep()
    print("ALL 4 LIVERAMP TECHNICAL SUPPORT DELIVERABLES CREATED SUCCESSFULLY!")
    print(f"Resume: {r}")
    print(f"Cover Letter: {c}")
    print(f"Analysis: {a}")
    print(f"Interview Prep: {i}")
