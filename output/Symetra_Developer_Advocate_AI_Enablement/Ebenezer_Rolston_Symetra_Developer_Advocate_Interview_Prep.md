# Symetra Interview Preparation Package
**Developer Advocate / AI Enablement | Insurance AI Adoption | Requisition 446718944470**  
Candidate: Ebenezer J. Rolston (Denver, CO) • Prepared for Symetra Engineering Leadership & Developer Experience Panel

---

## 1. Symetra & AI Enablement Strategic Context

Symetra Financial Corporation is a diversified insurance company committed to modernizing its engineering culture through responsible AI adoption. The **Developer Advocate / AI Enablement** role is charged with accelerating enterprise-wide adoption of AI coding agents while maintaining insurance industry compliance, data privacy, and security standards.

### Key Dimensions of the Role:
- **AI Coding Agent Enablement:** Teaching engineers to use Codex, Claude, Cursor, and Antigravity effectively and safely for daily development workflows.
- **MCP & Enterprise Tool Integration:** Connecting AI agents to Symetra's internal systems (code repositories, design tools, ticketing, documentation) via Model Context Protocol.
- **Best Practices & Governance:** Creating prompting frameworks, quality gates, bounded execution guardrails, and security review processes for AI-assisted development.
- **Adoption Measurement:** Defining and tracking metrics that demonstrate AI productivity gains and quality improvements across engineering teams.
- **Office Hours & Training:** Running regular technical sessions, building demos, and creating documentation that bridges the gap between AI capabilities and day-to-day engineering practice.

---

## 2. 30-60-90 Day Strategic Onboarding Charter

### Days 1–30: Assess Current State & Establish Enablement Foundation
- **Survey Engineering Teams:** Conduct structured interviews and tool audits to assess current AI coding agent usage, pain points, adoption barriers, and security concerns across Symetra engineering teams.
- **Inventory Existing Tooling:** Map Symetra's current developer ecosystem (repos, CI/CD, design systems, documentation) to identify MCP integration opportunities.
- **Establish Office Hours:** Launch a weekly "AI Coding Agent Office Hours" cadence, starting with foundational Codex/Claude/Antigravity workflows and Plan Mode demonstrations.
- **Author AGENTS.md Standards:** Draft Symetra-specific AGENTS.md guidelines defining workspace context, tool permissions, and insurance compliance boundaries for AI agents.

### Days 31–60: Build & Deploy Enablement Infrastructure
- **Launch MCP Integrations:** Deploy Model Context Protocol servers connecting AI agents to Symetra's GitHub repositories, Atlassian ticketing, and internal documentation platforms.
- **Create Prompting Framework:** Deliver Symetra's enterprise prompting standard (Outcome, Constraints, Scope, Definition of Done, Verification Rules) as an onboarding guide for all engineering teams.
- **Develop Quality Gate Templates:** Implement evidence-based verification gates (build passes, lint clean, regression tests, diff reviews) replacing agent self-assessment with deterministic validation.
- **Introduce Harness Engineering Concepts:** Teach the 4-layer harness architecture and bounded execution principles to ensure agents operate within insurance compliance boundaries.

### Days 61–90: Measure Impact & Scale Adoption
- **Deploy 6-Dimension Scorecard:** Implement trajectory-based adoption metrics (Correctness, Grounding, Latency, Cost, Safety, Auditability) to replace subjective satisfaction surveys with evidence-based quality measurement.
- **Build Agent Security Playbook:** Author Symetra's AI agent security guidelines covering OWASP agent vulnerability awareness, bounded permissions, plugin vetting, and sandboxed execution for insurance data.
- **Scale Training Program:** Convert office hours learnings into self-serve documentation, recorded demos, and reusable skill templates that engineering teams can consume independently.
- **Present ROI Report:** Deliver an executive-ready report quantifying AI adoption gains across cycle time, defect reduction, and developer satisfaction.

---

## 3. High-Probability Technical & Behavioral Scenarios (STAR Format)

### Scenario 1: Designing an AI Enablement Program for a Skeptical Engineering Team
* **Situation:** At the Department of the Interior, I was responsible for driving adoption of a new enterprise system (FBMS/SAP S/4) across 85+ users who had established workflows and were resistant to change.
* **Task:** Design and deliver a comprehensive enablement program that moved users from skepticism to productive adoption with measurable reduction in support tickets.
* **Action:** I structured the program around three principles: (1) start with immediate productivity wins (show the tool solving a real daily pain point in the first 15 minutes), (2) provide evidence-based verification (don't trust the tool's self-assessment — require concrete output validation), and (3) create reusable reference materials (SOPs, quick-reference guides, office-hours recordings). I conducted hands-on cohort training sessions and established myself as the trusted technical escalation point.
* **Result:** Achieved full adoption across 85+ users, measurably reduced recurring support requests, and received two Department of Interior Awards for the transformation. At Symetra, I would apply the identical framework to AI coding agent adoption — starting with immediate productivity demos, enforcing evidence-based quality gates, and building a library of reusable skills and prompting templates.

### Scenario 2: Building Production-Grade Agent Governance for an Insurance Environment
* **Situation:** In the Packt Agentic AI for Finance intensive, I trained on harness engineering — the production architecture that separates non-deterministic model behavior from deterministic policy enforcement, specifically designed for regulated financial and insurance environments.
* **Task:** Design governance guardrails that allow Symetra engineers to use AI coding agents productively while preventing agents from accessing sensitive policyholder data, making unauthorized API calls, or generating non-compliant code.
* **Action:** I would implement a 4-layer harness framework:
  - **Layer 1 (Identity & Behavior):** AGENTS.md workspace directives defining Symetra's coding standards, insurance compliance boundaries, and prohibited operations.
  - **Layer 2 (Runtime):** Bounded execution budgets, sandboxed code execution, and MCP tool contracts with strict schema validation preventing agents from accessing production insurance databases.
  - **Layer 3 (Feedback Loop):** 4 mandatory termination conditions (success, budget, no-progress 2-turn oscillation, hard stop on policy breach) with 3-rung escalation ladders.
  - **Layer 4 (Governance):** OWASP agent vulnerability awareness training, third-party plugin security vetting, and human-in-the-loop approval gates for any state-changing operations touching policyholder data.
* **Result:** Provides Symetra a developer advocate who doesn't just teach "how to use Codex" but teaches "how to architect agent systems that the compliance team can approve."

### Scenario 3: Measuring AI Agent Quality Beyond Subjective Surveys
* **Situation:** In my AI Guardians work and Packt training, I learned that most organizations measure AI coding agent adoption through developer satisfaction surveys — which capture sentiment but not quality, safety, or cost effectiveness.
* **Task:** Design a quantitative adoption measurement framework for Symetra that provides executive-level evidence of AI coding agent value.
* **Action:** I would implement the 6-dimension evaluation scorecard adapted for developer tooling:
  - **Correctness:** Percentage of AI-generated code that passes build, lint, and test without manual intervention.
  - **Grounding:** Ratio of AI suggestions that accurately reference existing codebase patterns vs. hallucinated APIs or deprecated methods.
  - **Latency:** Developer wait time from prompt submission to usable code suggestion (p95).
  - **Cost:** Token consumption and API spend per developer per sprint.
  - **Safety:** Number of AI suggestions that would have introduced security vulnerabilities (detected by code scanning).
  - **Auditability:** Percentage of AI-assisted PRs with complete provenance (prompt, agent response, human review decision) logged.
  I would deploy golden-set evaluations — curated benchmark tasks representative of Symetra's codebase — to measure agent effectiveness on Symetra-specific code patterns rather than generic benchmarks.
* **Result:** Moves Symetra from "we think AI is helping" to "we can prove AI is helping, and here's how much."

### Scenario 4: Integrating MCP to Connect Symetra's Engineering Ecosystem
* **Situation:** At AI Guardians, I architected Model Context Protocol servers connecting Figma, GitHub, Atlassian, and Google Workspace, creating a unified agent context that linked design, code, tickets, and documentation in one workflow.
* **Task:** Design an MCP integration strategy for Symetra that gives AI coding agents the right context about Symetra's codebase, architecture decisions, and insurance domain knowledge without exposing sensitive data.
* **Action:** I would implement MCP servers with strict bounded permissions:
  - **GitHub MCP:** Read access to repository structure, file contents, and PR history; write access limited to PR comments and review suggestions (never direct commits without human approval).
  - **Atlassian MCP:** Read access to Jira ticket descriptions and acceptance criteria; enables AI agents to understand what they're building without accessing customer data.
  - **Documentation MCP:** Read access to internal engineering wikis and architecture decision records; gives agents Symetra-specific context.
  - **Zero-Trust Boundary:** All MCP connections route through a FastAPI backend that enforces path validation, prevents directory traversal, and logs every tool invocation for audit trails. Policyholder data stores are explicitly excluded from all MCP tool scopes.
* **Result:** Creates a "context-aware but compliance-safe" agent environment where AI tools understand Symetra's engineering culture without accessing regulated insurance data.

### Scenario 5: Teaching Engineers to Recognize and Prevent Agent Security Risks
* **Situation:** In the Packt intensive, I trained on the OWASP Top 15 Agent Vulnerabilities taxonomy, including Confused Deputy attacks (where an agent with legitimate system privileges is tricked by untrusted input into executing unauthorized actions) and Memory Poisoning (where malicious data injected into vector memory biases future agent behavior).
* **Task:** Design a security awareness training module for Symetra engineers that makes agent security tangible and actionable.
* **Action:** I would build a hands-on "Agent Red Team" workshop demonstrating:
  - How a Confused Deputy attack works: embedding malicious instructions in a customer support ticket that cause an AI agent with database access to execute unauthorized queries.
  - How Memory Poisoning works: injecting misleading code comments that bias AI code suggestions toward insecure patterns.
  - How to defend: Principle of Least Privilege (downscope agent permissions), separate proposing from committing (agents suggest, humans approve), sandbox code execution (Docker containers with dropped capabilities), and maintain provenance tracking on all AI-generated artifacts.
* **Result:** Transforms security from an abstract compliance checklist into a concrete, demonstrable engineering practice — building the security culture Symetra needs for responsible AI adoption.

---

## 4. Questions to Ask the Symetra Interview Panel

1. "What's the current baseline of AI coding agent adoption across Symetra's engineering teams, and what are the primary adoption barriers you've observed?"
2. "How does Symetra's compliance and information security team currently view AI coding agents — are there existing approved-tool lists or security review processes?"
3. "What engineering systems and toolchains would be the highest-priority MCP integration targets?"
4. "How does Symetra measure engineering productivity today, and is there appetite for moving from activity-based metrics to outcome-based metrics for AI adoption?"
5. "What's the relationship between this role and Symetra's existing developer experience or platform engineering teams?"
