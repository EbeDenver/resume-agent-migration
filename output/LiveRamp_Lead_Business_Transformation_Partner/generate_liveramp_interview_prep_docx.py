"""Generate native Microsoft Word (.docx) for LiveRamp Interview Preparation Package.

Adheres strictly to:
- formatter2 visual styling (Navy #17365D, Light Blue #5B9BD5, Shaded Topic Bars #EBF1F5)
- Complete coverage of all 11 sections, including the Sequenced AI & Product Architecture Dashboard
- Live hyperlinks to verified sources
- Strict anti-hallucination guardrails (No Jira, verified candidate facts only)
"""
import sys
from pathlib import Path

# Add project root src to path
ROOT_DIR = Path("/Volumes/SanDiskOne/AI Projects/Gumloop/resume-agent-migration")
sys.path.insert(0, str(ROOT_DIR / "src"))

from resume_agent.utils.docx_writer import create_docx

OUTPUT_DIR = ROOT_DIR / "output" / "LiveRamp_Lead_Business_Transformation_Partner"

def build_interview_prep_docx():
    p = []

    def add_title(text):
        p.append({
            "align": "center", "space_before": 120, "space_after": 20,
            "text_runs": [{"text": text, "bold": True, "color": "17365D", "size": 32, "font": "Cambria"}]
        })

    def add_subtitle(text):
        p.append({
            "align": "center", "space_after": 40,
            "text_runs": [{"text": text, "bold": True, "color": "5B9BD5", "size": 18, "font": "Cambria"}]
        })

    def add_meta(line):
        p.append({
            "align": "center", "space_after": 60, "bottom_border": True,
            "text_runs": [{"text": line, "size": 17, "color": "4F4F4F"}]
        })

    def add_h1(text):
        p.append({
            "space_before": 140, "space_after": 25, "bottom_border": True,
            "text_runs": [{"text": text, "bold": True, "color": "17365D", "size": 22, "font": "Cambria"}]
        })

    def add_h2(text):
        p.append({
            "space_before": 80, "space_after": 15,
            "text_runs": [{"text": text, "bold": True, "color": "17365D", "size": 19, "font": "Cambria"}]
        })

    def add_h3(text):
        p.append({
            "space_before": 50, "space_after": 10,
            "text_runs": [{"text": text, "bold": True, "color": "2B579A", "size": 17, "font": "Cambria"}]
        })

    def add_body(text, italic=False, color="1F1F1F"):
        p.append({
            "space_after": 20,
            "text_runs": [{"text": text, "size": 17, "italic": italic, "color": color}]
        })

    def add_quote(text):
        p.append({
            "left_indent": 360, "space_before": 30, "space_after": 30, "bg_color": "F2F5F8",
            "text_runs": [{"text": text, "italic": True, "size": 17, "color": "17365D"}]
        })

    def add_bullet(lead, text, url=None):
        runs = [
            {"text": f"• {lead} ", "bold": True, "color": "17365D", "size": 17, "font": "Cambria"},
            {"text": text, "size": 17, "color": "1F1F1F"}
        ]
        if url:
            runs.append({"text": " [Link]", "url": url, "color": "17365D", "bold": True, "size": 16})
        p.append({
            "left_indent": 288, "hanging_indent": 180, "space_after": 15,
            "text_runs": runs
        })

    def add_topic_banner(seq, title, category):
        p.append({
            "space_before": 70, "space_after": 15, "bg_color": "EBF1F5",
            "text_runs": [
                {"text": f"{seq}: ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": f"{title} ", "bold": True, "color": "17365D", "size": 18, "font": "Cambria"},
                {"text": f"({category})", "italic": True, "color": "5B9BD5", "size": 16}
            ]
        })

    # Header
    add_title("LIVE RAMP INTERVIEW PREPARATION PACKAGE")
    add_subtitle("LEAD BUSINESS TRANSFORMATION PARTNER | STRATEGIC AI & PRODUCT ALIGNMENT")
    add_meta("Requisition JR162206 • Prepared for VP of Product Discussions • Candidate: Ebenezer J. Rolston • Denver, CO")

    # Section 1
    add_h1("1. Executive Brief: LiveRamp Product Ecosystem & VP of Product Context")
    add_h2("LiveRamp's Strategic Inflection Point")
    add_body("LiveRamp operates as the global leader in data collaboration, identity resolution, and privacy-first marketing infrastructure. The company is currently navigating an unprecedented market inflection driven by three macro forces:")
    add_bullet("1. Post-Cookie & Signal Deprecation:", "With third-party cookie deprecation, IP masking, and privacy mandates, brands require deterministic identity. LiveRamp's RampID and ATS (Authenticated Traffic Solution) serve as the industry benchmark.")
    add_bullet("2. Cross-Cloud Clean Room Explosion:", "Enterprises no longer centralize raw data; they collaborate where data lives. Bolstered by the 2024 acquisition of Habu, LiveRamp delivers a native cross-cloud clean room across Snowflake, Databricks, AWS, Azure, and Google Cloud BigQuery.")
    add_bullet("3. Generative & Agentic AI Evolution:", "Pioneering embedded GenAI helper bots in the LiveRamp Clean Room to automate queries and partner approval workflows, while acting as a secure intermediary for autonomous enterprise AI agents.")

    add_h2("The VP of Product's Strategic Agenda & Operational Pressures")
    add_body("When speaking with the VP of Product, discussion must align directly with their daily reality:")
    add_bullet("Product-Led Growth vs. Operational Friction:", "Product delivers cloud-native features and Snowflake Native Apps, but manual internal commercial onboarding, billing sync, or contract provisioning creates time-to-value drag.")
    add_bullet("Cross-Cloud Fragmentation:", "Merging Habu's SaaS layer across 5 hyperscalers requires standardized internal schemas, partner-specific integration playbooks, and support triage.")
    add_bullet("AI Governance & Brand Trust:", "LiveRamp's primary asset is trust. All internal and external AI workflows must strictly adhere to NIST AI RMF, GDPR Article 9, and FTC rules with zero data leakage.")
    add_bullet("Connecting Product to Internal Velocity:", "The VP of Product needs a strategic peer in Business Technology who understands data plumbing (matching keys, ETL, identity graphs) and can streamline operations.")

    # Section 2
    add_h1("2. Strategic Candidate Positioning & 'The Unfair Moat'")
    add_body("Ebenezer Rolston offers a unique, three-pillar competitive moat directly aligned with LiveRamp:")
    add_bullet("Pillar 1: Foundational Acxiom Lineage (LiveRamp's Genetic Code):", "10+ years at Acxiom (1999-2009) engineering Citibank's first Online Identity Scoring Model and AVS. Directly understands the entity resolution, match keys, and CDI lineage that evolved into AbiliTec and RampID.")
    add_bullet("Pillar 2: Enterprise Operating-Model Transformation (14 Years):", "14 years transforming enterprise operating models at DOI IBC Acquisition Directorate, reclaiming $1M+ annually, leading Department-wide SAP S/4 data conversions, and training 85+ cohort attendees with measurable ticket reduction.")
    add_bullet("Pillar 3: Auditable Agentic AI, Governance & FinOps:", "Harvard SEAS Executive Certificate in Agentic AI, University of Denver AI Strategy & Ethics, TECH 77 LangGraph document intelligence with prompt-injection defenses, and AI Stack Optimization (FinOps).")

    # Section 3
    add_h1("3. Spoken Elevator Pitch (60–90 Seconds Spoken Script)")
    add_quote(
        '"Good morning. I’m Ebenezer Rolston. I’m excited to speak with you because my career brings a very rare combination of deep identity architecture, enterprise operating-model transformation, and modern agentic AI governance.\n\n'
        'I actually know LiveRamp from the ground up: I spent 10 years at Acxiom as a Solution Architect, where I engineered Citibank’s first real-time Online Identity Scoring Model and worked on the core Application Verification System—the exact matching, CDI, and entity-resolution lineage that evolved into AbiliTec and RampID.\n\n'
        'Over the past 14 years, I operated in complex, multi-stakeholder enterprise ecosystems at the Department of the Interior’s Acquisition Directorate. In that role, I served as the ETL Architect migrating millions of records into unified SAP systems, analyzed Remedy incident ticketing trends across thousands of cases to eliminate operational failure modes, and re-engineered financial workflows to reclaim over $1 million annually in recurring funds.\n\n'
        'Over the past year, I dedicated myself to modern agentic AI engineering, earning credentials from Harvard SEAS in Agentic LLM Architectures and the University of Denver in AI Strategy and Governance. I’ve built auditable LangGraph document workflows with prompt-injection defenses and authored comprehensive AI compliance plans operationalizing the NIST AI Risk Management Framework.\n\n'
        'As LiveRamp scales the Data Collaboration Platform, integrates Habu’s clean rooms across Snowflake and Databricks, and rolls out AI helper bots, I want to partner with you and the Business Technology team as Lead Business Transformation Partner—ensuring our internal commercial, financial, and operational workflows match the speed, precision, and privacy standards of our world-class product."'
    )

    # Section 4: Sequenced AI Dashboard
    add_h1("4. Sequenced AI & Product Architecture Dashboard")
    add_body("The following sequenced dashboard maps LiveRamp's product capabilities directly to Business Technology operational applicability, candidate assets, and verified source materials.")

    topics_data = [
        ("Topic 01", "Core Identity Resolution & RampID Architecture", "Core Identity",
         "Deterministic & probabilistic entity resolution across online/offline touchpoints. Keyed pseudonymous RampIDs replacing cookies and raw PII.",
         "Serves as the identity backbone for LiveRamp Connect and cloud-native integrations. In Business Technology, this foundation governs internal customer master data, partner onboarding synchronization, and billing linkage.",
         "10+ years at Acxiom engineering Citibank's first Online Identity Scoring Model and AVS; direct CDI lineage ancestral to AbiliTec and RampID.",
         "https://liveramp.com/our-platform/identity/rampid/"),
        ("Topic 02", "Cross-Cloud Data Clean Rooms (Habu Integration)", "Clean Rooms",
         "Multi-party, cross-cloud collaboration across Snowflake, Databricks, AWS, Azure, and GCP without raw data movement.",
         "Following Habu acquisition, unified into LiveRamp Connect. Transformation requires standardizing partner provisioning, resolving cloud entitlement discrepancies, and harmonizing CRM/billing pipelines.",
         "14 years reconciling fragmented enterprise databases (DOI FBMS ETL conversion, SAP S/4), deobligation tracking reclaiming $1M+ annually, and cross-platform data hygiene.",
         "https://liveramp.com/our-platform/data-collaboration/clean-room/"),
        ("Topic 03", "Embedded Clean Room Generative AI & Natural Language Querying", "Generative AI",
         "AI Helper Bot predicting valuable cross-party analyses, generating governed SQL queries, drafting partner approval memos, and alerting on anomalies.",
         "Demonstrates product-led AI maturity. In Business Technology, similar generative interfaces can be operationalized internally for Commercial sales enablement, RFP generation, and usage summaries.",
         "Harvard SEAS LLM & Agentic AI credentials; Stanford Python exploratory data analysis; AI Guardians enterprise readiness frameworks.",
         "https://liveramp.com/blog/generative-ai-in-the-clean-room/"),
        ("Topic 04", "Agentic Orchestration & Secure Multi-Party Agent Workflows", "Agentic AI",
         "Clean rooms as secure context intermediaries for autonomous enterprise AI agents, enabling agents to query partner context without raw data leaks.",
         "High-growth frontier for LiveRamp Product. For internal operations, enables the AI CoE to deploy multi-agent workflows across Commercial, Legal, and Finance (e.g., automated contract review and schema validation).",
         "TECH 77 LangGraph auditable document intelligence: state machines, deterministic Pydantic schema validation, prompt-injection defense filters, and HITL routing.",
         "https://liveramp.com/blog/ai-agents-data-collaboration/"),
        ("Topic 05", "AI Governance, Privacy-Enhancing Technologies (PETs) & Risk", "Governance",
         "Differential privacy, zero-knowledge queries, cryptographic hashing, and adherence to NIST AI RMF 1.0, EU AI Act, GDPR Article 9, and FTC rules.",
         "LiveRamp brand rests on privacy and compliance. Internal AI deployments by the AI CoE must have formal risk gating, zero data-leakage controls, and audit logs to ensure enterprise compliance and protect customer trust.",
         "University of Denver ChatGPT Health Compliance Plan operationalizing NIST AI RMF, GDPR Art 9, and EU AI Act; AI Tech & Privacy Academy certification in AI Governance.",
         "https://liveramp.com/our-platform/privacy-and-data-ethics/"),
        ("Topic 06", "AI FinOps, Stack Optimization & Operational Cost Control", "FinOps",
         "Prompt caching, model right-sizing (SLMs vs. frontier LLMs), context compaction, and bounding agentic recursion loops to prevent runaway API spend.",
         "As LiveRamp expands internal AI adoption across hundreds of commercial and operations users, Business Technology must institute FinOps cost governance, cache-hit tracking, and ROI baselines.",
         "AI Realist 'Learn to Optimise Your AI Stack' credential; prompt caching, token cost modeling, and loop-capping architectural design.",
         "https://airealist.ai/"),
        ("Topic 07", "Business Technology Operating Model & Change Enablement", "Transformation",
         "Structuring the cross-functional bridge connecting Product, Engineering, Commercial (GTM), Finance, and Operations.",
         "The exact mandate of the Lead Business Transformation Partner: working with the AI CoE and business leaders across Commercial, Finance, and Customer Engagement to optimize operating models and workflows.",
         "14 years leading change enablement, Remedy incident trend analysis isolating recurring operational failure modes, and training 85+ cohort users with measurable ticket reductions.",
         "https://liveramp.com/careers/")
    ]

    for seq, title, cat, exp, app, cand, link in topics_data:
        add_topic_banner(seq, title, cat)
        add_bullet("Technical Foundation:", exp)
        add_bullet("LiveRamp Operations Applicability:", app)
        add_bullet("Candidate Moat & Experience:", cand)
        add_bullet("Verified Source Material:", link, url=link)

    # Section 5
    add_h1("5. VP of Product & Product Leadership Question Bank")
    add_h2("Q1: Scaling Habu Clean Rooms Across Clouds & Mitigating Operational Friction")
    add_body("Talking Points: Align cross-cloud entitlement and billing telemetry between SaaS Habu and Snowflake/Databricks native apps. Standardize partner onboarding playbooks to shorten time-to-first-query from weeks to 48 hours.")

    add_h2("Q2: Operationalizing Generative AI Internally Across Commercial & Support")
    add_body("Talking Points: Mirror external product AI helper bots internally. Deploy RAG-enabled solution engineering assistants to reduce RFP cycle times by 60%. Use AI-driven ticket categorization to provide structured feedback loops back to Product.")

    add_h2("Q3: Leveraging Acxiom Identity Lineage to Strengthen LiveRamp's Position")
    add_body("Talking Points: Acxiom pioneered offline identity, AVS, and CDI. LiveRamp transformed that into digital RampID. A clean room without identity resolution is just an empty database—LiveRamp's identity graph is the true moat.")

    add_h2("Q4: Collaborating with Product Management Without Overstepping Roadmaps")
    add_body("Talking Points: Product builds for the market; Business Technology builds for the enterprise. Act as an operational sensor, gathering telemetry from sales ops, partner provisioning, and customer tickets to surface friction back to Product.")

    add_h2("Q5: AI Governance & Risk Mitigation in Sensitive Workflows")
    add_body("Talking Points: Operationalize NIST AI RMF (Govern, Map, Measure, Manage). Enforce strict Pydantic schema validation, prompt-injection defense filters, and automated human-in-the-loop (HITL) gates.")

    add_h2("Q6: Evaluating Deterministic Rules vs. ETL vs. Agentic AI Workflows")
    add_body("Talking Points: Never use frontier AI when deterministic SQL/ETL suffices. Reserve agentic workflows for unstructured multi-step tasks, and enforce strict FinOps unit economics.")

    add_h2("Q7: Measuring Transformation Financial ROI & Business Impact")
    add_body("Talking Points: Three ROI buckets: direct funds recovery (reclaimed $1M+ annually at DOI), cycle-time compression (partner onboarding), and incident escalation reduction.")

    add_h2("Q8: Driving Cross-Functional Change Adoption & Overcoming Resistance")
    add_body("Talking Points: Empathy-driven user shadowing, hands-on cohort training (trained 85+ users at DOI), and continuous monitoring of support ticket trends to eliminate root-cause user errors.")

    # Section 6
    add_h1("6. Deep Technical & AI Architecture Question Bank")
    add_h2("Tech Q1: Clean Room Cross-Cloud Federated Architecture & PETs")
    add_body("Candidate Framework: RampID encryption envelopes at data ingestion; federated SQL push-down across Snowflake and Databricks; differential privacy mathematical noise addition; dual-custody approval workflows.")

    add_h2("Tech Q2: Auditable Agentic Partner Schema Validation Workflow (LangGraph)")
    add_body("Candidate Framework: LangGraph state machine: Node 1 (Profiling) -> Node 2 (Pydantic Schema Mapping) -> Node 3 (Prompt Injection Defense) -> Node 4 (Deterministic Verification) -> Node 5 (HITL Routing if confidence < 95%).")

    add_h2("Tech Q3: AI FinOps & Unit Economics Governance")
    add_body("Candidate Framework: Prompt caching for static prefixes (90% cost cut), model right-sizing (SLMs for extraction, frontier for reasoning), loop-capping (`max_iterations = 5`), and context compaction.")

    add_h2("Tech Q4: Embedded Identity in Snowflake/Databricks vs. Traditional Hosted")
    add_body("Candidate Framework: Native container apps (Snowpark) run matching logic inside customer VPC. Zero PII egress, native cloud scale, and compliance with data residency mandates.")

    # Section 7
    add_h1("7. Tough Challenge Questions & Objection Handling")
    add_h2("Challenge 1: Transitioning from Federal Systems Back to AdTech SaaS")
    add_body("Answer: Formative 10 years at Acxiom provided high-velocity commercial DNA. 14 years in federal systems added enterprise rigor, compliance discipline, and large-scale ERP transformation mastery.")

    add_h2("Challenge 2: Influencing Product Without Direct Management Authority")
    add_body("Answer: Lead through operational partnership and data evidence. Business Technology sees where customer handoffs fail first; partnering with Product ensures solutions are enterprise-scalable.")

    add_h2("Challenge 3: Tooling Adaptation & Negative Guardrails")
    add_body("Answer: Deep fluency across enterprise workflow engines (Remedy, SAP S/4, PRISM, custom portals). Focus on business process clarity, SLA governance, and rapid toolchain adaptability.")

    # Section 8
    add_h1("8. Candidate Verified STAR Story Bank (6 Core Pillars)")
    add_bullet("STAR 1 (Acxiom):", "Citibank Real-Time Online Identity Scoring Model: Designed scoring engine analyzing streaming application data in real time, preventing millions in fraud and establishing AbiliTec/RampID lineage.")
    add_bullet("STAR 2 (DOI IBC):", "Department-Wide SAP S/4 FBMS Conversion: ETL Architect consolidating 12 legacy databases into unified ERP, earning 2 Interior Department Awards.")
    add_bullet("STAR 3 (DOI IBC):", "Reclaiming $1M+ Annually via Financial Re-alignment: Designed automated SQL reconciliation models resolving contract deobligations and funds realignment.")
    add_bullet("STAR 4 (DOI IBC):", "Remedy Incident Trend Analysis & 85+ User Enablement: Analyzed thousands of helpdesk tickets, isolated recurring failure modes, and trained 85+ cohort users with measurable ticket reduction.")
    add_bullet("STAR 5 (TECH 77):", "Auditable Multimodal Document Intelligence with LangGraph: Built stateful multi-agent extraction with Pydantic schemas, prompt-injection defense, and HITL routing.")
    add_bullet("STAR 6 (DU):", "ChatGPT Health AI Privacy & Compliance Plan: Authored comprehensive governance plan operationalizing NIST AI RMF 1.0, GDPR Article 9, and FTC health breach rules.")

    # Section 9
    add_h1("9. Strategic Questions Candidate Should Ask the VP of Product")
    add_bullet("Q1:", "With Habu integrated into LiveRamp Connect, how are you addressing cross-cloud query latency across Snowflake Snowpark vs Databricks Delta Sharing?")
    add_bullet("Q2:", "What has enterprise client feedback been regarding the GenAI helper bot in clean rooms, and what is planned for autonomous agent collaboration?")
    add_bullet("Q3:", "As PETs mature, how is the product team balancing identity match rates with mathematical differential privacy guarantees?")
    add_bullet("Q4:", "From a Business Technology perspective, what internal operational bottleneck currently creates the most drag on product time-to-market?")
    add_bullet("Q5:", "How closely does Product collaborate with the internal AI CoE to pilot new AI capabilities internally before external rollout?")
    add_bullet("Q6:", "What does a successful first 12 months look like for this Lead Business Transformation Partner?")

    # Section 10
    add_h1("10. 30-60-90 Day Transformation & Enablement Plan")
    add_bullet("Days 1–30 (Discovery & Baselines):", "Shadow end-to-end partner onboarding from contract signature to live clean room query. Analyze support tickets and provisioning logs to baseline cycle times and recurring errors.")
    add_bullet("Days 31–60 (Rapid AI Enablement):", "Pilot high-impact agentic workflow with AI CoE (e.g., automated partner schema validation). Implement NIST AI RMF governance and FinOps prompt caching. Deliver cohort enablement sessions.")
    add_bullet("Days 61–90 (Scale & Strategy):", "Standardize self-service clean room provisioning templates, targeting 30–50% cycle time reduction. Deliver 12-Month Enterprise AI & Business Transformation Strategic Roadmap.")

    # Section 11
    add_h1("11. Grounded Source Material & Product Reference Directory")
    add_bullet("LiveRamp RampID Overview:", "https://liveramp.com/our-platform/identity/rampid/", url="https://liveramp.com/our-platform/identity/rampid/")
    add_bullet("LiveRamp Data Clean Room:", "https://liveramp.com/our-platform/data-collaboration/clean-room/", url="https://liveramp.com/our-platform/data-collaboration/clean-room/")
    add_bullet("LiveRamp GenAI in Clean Rooms:", "https://liveramp.com/blog/generative-ai-in-the-clean-room/", url="https://liveramp.com/blog/generative-ai-in-the-clean-room/")
    add_bullet("LiveRamp Acquires Habu:", "https://liveramp.com/blog/liveramp-acquires-habu/", url="https://liveramp.com/blog/liveramp-acquires-habu/")
    add_bullet("LiveRamp AI Agents & Collaboration:", "https://liveramp.com/blog/ai-agents-data-collaboration/", url="https://liveramp.com/blog/ai-agents-data-collaboration/")
    add_bullet("LiveRamp Privacy & Data Ethics:", "https://liveramp.com/our-platform/privacy-and-data-ethics/", url="https://liveramp.com/our-platform/privacy-and-data-ethics/")
    add_bullet("NIST AI Risk Management Framework:", "https://www.nist.gov/itl/ai-risk-management-framework", url="https://www.nist.gov/itl/ai-risk-management-framework")
    add_bullet("European Union AI Act Portal:", "https://artificialintelligenceact.eu/", url="https://artificialintelligenceact.eu/")
    add_bullet("LangGraph Orchestration Framework:", "https://www.langchain.com/langgraph", url="https://www.langchain.com/langgraph")
    add_bullet("AI Realist AI Stack Optimization:", "https://airealist.ai/", url="https://airealist.ai/")

    docx_path = OUTPUT_DIR / "Interview_Preparation_LiveRamp_Lead_Business_Transformation_Partner.docx"
    create_docx(docx_path, p)
    print(f"Successfully generated DOCX at {docx_path}")

if __name__ == "__main__":
    build_interview_prep_docx()
