# Symetra Interview Preparation Package
**Developer Advocate, AI Enablement (Remote) | Requisition 446718944470 / 9427**  
Candidate: Ebenezer J. Rolston • Prepared for Symetra AI Enablement & Data Analytics Leadership

---

## 1. Symetra Company Profile & AI Enablement Team Context

Symetra Financial Corporation is a premier national financial services company headquartered in Bellevue, WA, providing life insurance, retirement annuities, and employee benefits (including Stop Loss) to millions of customers. The company is anchored on principles of Value, Transparency, and Sustainability.

Symetra's **AI Enablement Team** operates as a high-velocity builders group inside the Data Analytics organization. Rather than functioning as an isolated research lab, the team is embedded with operational stakeholders to accelerate AI adoption across two distinct fronts:
- **Shared Platforms & Tooling:** Building patterns, MCP servers, and secure scaffolding that enable other software teams to integrate AI into existing systems.
- **Production AI Applications:** Deploying modular applications like **docstream**—Symetra's flagship document-processing platform currently supporting multiple back-end operational processes.
- **Why the First Developer Advocate?** Until now, the team has been engineering tools and platforms. They need a credible, high-empathy technical advocate to bridge the human divide—coaching non-technical underwriters and business users on ChatGPT/Claude while leading developer office hours on AI coding agents (Claude Code, Codex) and MCP integrations.

---

## 2. The First 30-60-90 Day Strategic Charter

### Days 1–30: Listen, Baseline & Build Trust
- **Audit Current AI Workflows:** Interview software engineers, COE leads, and business operations staff to assess existing usage of ChatGPT, Claude, and IDE extensions; map tool satisfaction and friction points.
- **Establish Developer Office Hours:** Launch bi-weekly developer office hours focused on practical AI-assisted development (e.g. Plan Mode, test loops, prompt boundaries).
- **Deep Dive into docstream:** Partner with the docstream engineering team to understand the modular architecture, pipeline bottlenecks, and user feedback from back-end operations.

### Days 31–60: Standardize Tooling & Deploy MCP Pilots
- **Roll Out Enterprise Prompting Framework:** Publish an intuitive 5-point prompting guide (Outcome, Constraints, Scope, Definition of Done, Verification) for business teams, packaged with reusable prompt templates.
- **Pilot Model Context Protocol (MCP) Servers:** Collaborate with an engineering team to deploy their first MCP server, connecting Claude or Codex securely to an internal repository or ticketing system (e.g., GitHub, Atlassian).
- **Launch 'docstream Super-Users':** Host targeted cohort enablement sessions for business operations teams utilizing docstream, measuring error rate reductions and throughput increases.

### Days 61–90: Scale, Measure & Institutionalize
- **Establish AI Adoption Dashboard:** Define and publish objective adoption KPIs: active weekly prompt volume, agentic PR review velocity, MCP tool invocations, and business process turnaround times.
- **Create Video & Written Demo Library:** Record bite-sized walkthrough videos and practical code samples showing how to build custom TOML agents, write robust test harnesses, and prevent hallucination.
- **Cross-Pollinate Innovation COE:** Partner with the Innovation Community and Cloud Office Hours to host a company-wide 'AI Builder Showcase' highlighting successful employee-led AI workflows.

---

## 3. Core Technical Deep Dives for Symetra Discussions

### Topic A: AI Coding Agents (Claude Code, OpenAI Codex, Antigravity)
Engineers often resist AI when it feels like an unreliable autocomplete. An effective Developer Advocate demonstrates disciplined agent engineering: using Plan Mode to evaluate architecture before code is written, leveraging parallel Git worktrees to isolate experimental branches, and establishing automated build–test–fix loops with regression verification so agents never self-certify unverified changes.

### Topic B: Model Context Protocol (MCP) Server Architecture
MCP standardizes how generative models interact with external enterprise data and tools without hard-coding proprietary API bridges. In an insurer like Symetra, setting up MCP servers allows AI coding assistants to query schema metadata, fetch pull request diffs, or inspect ticketing queues within bounded security sandboxes that enforce read-only boundaries and mandatory human approvals.

### Topic C: docstream Synergy — Modular Document Intelligence
Symetra's docstream platform processes unstructured insurance documents, claims, and underwriting files. In your Stanford TECH 77 project, you evaluated Vision Language Models vs. Document Transformers vs. OCR baselines, implementing LangGraph StateGraph conditional routing with Pydantic validation and prompt-injection anomaly gating. This gives you immediate peer-level credibility with the docstream builders.

---

## 4. Key Behavioral & Technical Interview Scenarios (STAR Method)

### Q1: How do you convince skeptical senior software engineers to adopt AI coding assistants without alienating them?
* **Strategic Intent:** Demonstrates technical humility, respect for engineering craft, and proof-based advocacy rather than buzzword cheerleading.
* **Response (STAR):**
  - **Situation:** Experienced engineers are rightfully protective of code quality and skeptical of hallucinated AI solutions.
  - **Task:** In my enablement work, my goal is never to tell senior developers how to code, but to demonstrate where AI coding agents save them mundane friction.
  - **Action:** I introduce agents not as code writers, but as junior research partners. I demonstrate practical workflows: using Plan Mode to explore three architectural trade-offs, spinning up parallel Git worktrees for safe experimentation, and running automated build–test–fix loops with strict regression testing. I emphasize the principle: *"start deterministic, add agents only when variability warrants it."*
  - **Result:** Engineers realize AI isn't replacing their judgment; it's eliminating boilerplate, catching edge cases, and speeding up unit test creation. Skepticism turns into curious engagement during office hours.

### Q2: How do you teach non-technical business teams to use ChatGPT and Claude effectively while maintaining security and accuracy?
* **Strategic Intent:** Demonstrates structured curriculum design, patient communication, and enterprise risk guardrails.
* **Response (STAR):**
  - **Situation:** Business users in operations, HR, and underwriting often treat LLMs like Google search or magical black boxes, resulting in vague prompts or privacy concerns.
  - **Task:** Teach business teams to generate high-value, auditable outputs.
  - **Action:** I established a structured 5-part prompting methodology: (1) Goal/Outcome, (2) Explicit Constraints, (3) Context & Scope, (4) Definition of Done, and (5) Verification Step. In cohort training sessions, I walk through real-world transformations—turning unstructured meeting notes or spreadsheet columns into executive project briefs. Crucially, I teach evidence-based verification: never trust an agent's self-assessment; verify numbers and citations.
  - **Result:** Teams cut down prompt iterations by over 50%, eliminated accidental data exposure, and packaged successful prompts into reusable skills for their departments.

### Q3: Can you describe your experience setting up Model Context Protocol (MCP) servers or tool integrations?
* **Strategic Intent:** Demonstrates hands-on architectural competency with the exact protocol highlighted in Symetra's job description.
* **Response (STAR):**
  - **Situation:** Coding agents cannot deliver deep organizational value in a silo; they need structured access to enterprise context.
  - **Task:** Connect agentic environments to external toolchains safely.
  - **Action:** I architected MCP server implementations connecting agent runtimes to Figma for design specifications, GitHub for repository oversight, Atlassian for issue tracking, and Google Workspace for documentation. I enforced strict security boundaries: read-only access for research and discovery, explicit schema validation with Pydantic, and mandatory human approval gates before executing state-changing API calls.
  - **Result:** The agent workflows bridged design, tickets, and code reviews into a unified loop, dramatically reducing context switching for developers.

### Q4: Symetra has docstream in production for document processing. How would you support and advocate for that platform?
* **Strategic Intent:** Demonstrates immediate relevance to Symetra's core product, highlighting the Stanford document intelligence project.
* **Response (STAR):**
  - **Situation:** An internal platform like docstream needs ongoing advocacy to encourage operational teams to trust it with increasingly complex document types.
  - **Task:** Act as the technical and educational liaison between the docstream engineering team and business users.
  - **Action:** Having built an auditable document intelligence pipeline during my Stanford TECH 77 project—benchmarking VLMs, Document Transformers, and OCR with LangGraph StateGraph routing and Pydantic validation—I understand the technical underpinnings of document extraction. I would host "docstream Office Hours" where operational users bring difficult, low-confidence documents. I would show users how confidence scoring and human-in-the-loop review work, while feeding edge-case failure modes directly back to the engineering team as structured test cases.
  - **Result:** Increased user trust, faster turnaround times, and continuous product improvement driven by real user telemetry.

### Q5: How do you measure whether AI enablement is actually working, beyond vanity metrics like total logins?
* **Strategic Intent:** Demonstrates executive maturity and alignment with Symetra's "knack for driving adoption and measuring what works."
* **Response (STAR):**
  - **Situation:** Organizations frequently measure AI adoption by licenses allocated or queries typed, which fails to capture business impact.
  - **Task:** Establish meaningful, value-driven AI adoption KPIs.
  - **Action:** I track metrics across three distinct dimensions:
    1. *Adoption Depth:* Weekly active prompt chains, adoption of structured prompting frameworks, and frequency of reusable skill executions.
    2. *Engineering Velocity:* PR cycle time reductions, automated test coverage generated, and MCP tool call frequency.
    3. *Business Value:* Error reduction in processed operational forms (e.g., via docstream), time saved on manual document synthesis, and reduced support tickets.
  - **Result:** Leadership receives empirical, ROI-backed evidence showing where AI creates tangible leverage and where workflows need recalibration.

---

## 5. High-Impact Questions to Ask the Symetra Interview Panel

### For the Hiring Manager / Head of AI Enablement:
1. *"As Symetra's first Developer Advocate, what does success look like at the 6-month mark? Is it measured more by engineering toolchain integration (like MCP and coding agents) or by business process adoption across operational units?"*
2. *"docstream is in production supporting back-end operational processes. What is the biggest hurdle in expanding docstream to other lines of business—is it data heterogeneity, user trust, or integration bandwidth?"*

### For Lead Software Engineers / Architects:
1. *"How are Symetra's engineering teams currently experimenting with coding assistants like Claude Code or GitHub Copilot? Are you looking for standardized MCP servers across repositories, or are teams currently setting up local configurations?"*
2. *"In my engineering lab, I operate under the rule: 'start deterministic, add agents only when variability warrants it.' How does the AI Enablement team balance deterministic microservices with agentic workflows in docstream and future platforms?"*

### For Business Operations / Cross-Functional Partners:
1. *"Symetra has an active innovation community and COE. What has been the most effective forum so far for sharing AI discoveries across departments, and where do business teams feel the most friction when trying to use tools like ChatGPT or Claude?"*
