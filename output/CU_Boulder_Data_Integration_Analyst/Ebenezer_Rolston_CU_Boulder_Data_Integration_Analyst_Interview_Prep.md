# CU Boulder Interview Preparation Package
**Data & Integration Analyst | OIT Enterprise CRM | Requisition 75732**  
Candidate: Ebenezer J. Rolston (Denver, CO) • Prepared for CU Boulder Search Committee & CRM Data Architect

---

## 1. CU Boulder OIT & Enterprise CRM Context

The University of Colorado Boulder's Office of Information Technology (OIT) serves over 36,000 students, 9,000 faculty and staff, and dozens of academic and auxiliary departments. The Enterprise CRM team is modernizing campus-wide engagement across student recruitment, advising, alumni relations, and student success using Salesforce platforms (Education Cloud, Sales/Service Cloud, and Salesforce Data Cloud / Data 360).

### Key Team Dynamics & The Single-Person Dependency Challenge:
- **Partnership with the CRM Data Architect:** The Data Architect currently carries heavy architectural design, mapping, and operational load. OIT created this role to serve as the Architect's direct implementation partner and operational backup.
- **Cross-Functional Coordination:** You will sit at the nexus of the Salesforce DevOps team, product managers, business analysts, data stewards from academic departments, and University Information Systems (UIS) integration teams.
- **Core Strategic Imperatives:** Execute high-integrity data migrations, create source-to-target mapping artifacts, develop automated reconciliation test plans, and support Data Cloud ingestion patterns.

---

## 2. 30-60-90 Day Strategic Onboarding Charter

### Days 1–30: Discover, Shadow & Inventory Assets
- **Shadow the CRM Data Architect:** Gain deep understanding of the existing Salesforce data model, active integration pipelines (UIS, SIS, downstream warehouses), and known operational pain points.
- **Catalog Source-to-Target Mappings:** Review current mapping documentation, identify undocumented business rules, and establish standardized mapping templates with clear data lineage.
- **Engage Data Stewards & DevOps:** Meet with campus data stewards across admissions, registrar, and advising to understand data governance protocols and data steward approval workflows.

### Days 31–60: Standardize Mappings & Implement Reconciliation Tests
- **Take Ownership of Migration Specifications:** Lead the development of detailed source-to-target mapping specs for upcoming CRM releases, documenting transformations and validation rules.
- **Deploy Automated Reconciliation Frameworks:** Write SQL-based validation scripts comparing source system extracts against target CRM staging tables, automating pre- and post-load reconciliation.
- **Support Salesforce Data Cloud Ingestion:** Assist in mapping enterprise data streams into Data Cloud data lake objects (DLOs) and data model objects (DMOs), establishing identity resolution rules.

### Days 61–90: Eliminate Dependencies & Institutionalize Standards
- **Serve as Confident Operational Backup:** Assume full day-to-day operational support for CRM data migrations, release testing, and integration incident triage, allowing the Data Architect to focus on strategic roadmap items.
- **Publish Standard Operating Procedures (SOPs):** Document standard procedures for data quality monitoring, defect root-cause analysis, and integration error handling.
- **Lead Cross-Functional Knowledge Transfer:** Host technical walkthroughs for business analysts and campus partners to demystify integration flows and promote data quality at the point of entry.

---

## 3. Core Technical Topics for the Search Committee

### Topic A: Source-to-Target Mapping & Data Lineage Best Practices
A rigorous source-to-target mapping document is not just a column-to-column spreadsheet; it is an executable contract. It specifies source table/field definitions, data types, business transformation logic, default values, nullability rules, primary/foreign key mappings, and audit logging triggers. Clear documentation prevents ambiguity between business analysts, developers, and data stewards.

### Topic B: Data Reconciliation & Automated Quality Assurance
Reconciliation must go beyond row counts. In high-stakes migrations, three levels of reconciliation are required:
1. *Record-level counts and volume matching* (ensuring no drop-offs during extraction).
2. *Hash-total or financial sum reconciliation* on critical numeric attributes.
3. *Boundary and anomaly checks* verifying that coded enumerations (e.g., student residency status, enrollment codes) map to valid target domain values.

### Topic C: Bridging Acxiom Customer 360 with Salesforce Data Cloud
Salesforce Data Cloud / Data 360 operates on principles identical to enterprise identity resolution platforms: ingesting high-volume disparate records, normalizing them into a canonical data model, applying deterministic or probabilistic match rules to create a unified profile, and exposing that unified record for analytics and engagement. Your Acxiom and ETL architecture background directly translates to Data Cloud modeling.

---

## 4. Key Behavioral & Technical Interview Scenarios (STAR Method)

### Q1: Can you describe your experience leading or supporting large-scale enterprise data migrations?
* **Strategic Intent:** Demonstrates Department-level technical leadership, risk mitigation, and end-to-end ETL execution.
* **Response (STAR):**
  - **Situation:** At the U.S. Department of the Interior, four distinct federal bureau agencies operated fragmented legacy databases that needed conversion into a single, unified SAP S/4 Federal Business Management System.
  - **Task:** As Department ETL Architect, I was responsible for the end-to-end data conversion—cleansing, transforming, validating, and migrating millions of enterprise procurement and financial records.
  - **Action:** I designed detailed source-to-target mappings, created business transformation rules in collaboration with data stewards, and engineered automated pre- and post-load reconciliation scripts. I instituted strict validation test gates before any mock cutover.
  - **Result:** Successfully completed the Department-wide migration without disruption to ongoing acquisition operations, recognized with two Department of the Interior Awards for Excellence.

### Q2: How do you approach creating source-to-target mappings when legacy documentation is incomplete or outdated?
* **Strategic Intent:** Demonstrates proactive discovery, technical detective work, and stakeholder elicitation.
* **Response (STAR):**
  - **Situation:** In long-standing enterprise environments, legacy documentation often diverges from actual system reality.
  - **Task:** Create accurate, audit-compliant source-to-target mappings for integration.
  - **Action:** I employ a three-step methodology: (1) *Data Profiling:* I run exploratory SQL queries directly against source relational databases to profile actual data distributions, null percentages, distinct value sets, and edge cases. (2) *Business Discovery:* I sit down with data stewards and operational end-users to understand how they actually use specific fields, rather than how the legacy spec was written years ago. (3) *Living Documentation:* I capture transformations, business logic, and boundary conditions in a centralized mapping document, obtaining sign-off from both technical leads and business stewards before development begins.
  - **Result:** Eliminated downstream migration rework and established clean data lineage that persisted across subsequent releases.

### Q3: This role serves as an operational backup to our CRM Data Architect to reduce single-person dependencies. How do you approach this dynamic?
* **Strategic Intent:** Demonstrates professional humility, collaborative reliability, and immediate operational value.
* **Response (STAR):**
  - **Situation:** In many growing IT organizations, lead data architects become overwhelmed by balancing strategic design with day-to-day operational support and data requests.
  - **Task:** Act as a force multiplier and operational backup, absorbing day-to-day data operations without needing micromanagement.
  - **Action:** During my 14 years supporting the Department of the Interior and 11 years at Acxiom, I frequently served as the senior escalation point alongside lead architects. I establish rapid trust by mastering the existing architecture, meticulously documenting operational procedures, and taking ownership of integration test plans, mapping updates, and defect triage.
  - **Result:** The Data Architect gains freedom to focus on strategic roadmap architecture, knowing that data operations, stakeholder requests, and release validations are handled with absolute technical rigor.

### Q4: Tell me about a time you identified a critical data discrepancy and how you resolved it through root cause analysis.
* **Strategic Intent:** Demonstrates deep analytical troubleshooting, SQL forensics, and systemic problem solving.
* **Response (STAR):**
  - **Situation:** During contract and financial operations in FBMS, discrepancies arose between federal financial obligations and vendor platform records, causing billing disputes and blocking year-end close.
  - **Task:** Identify root causes and implement a durable reconciliation mechanism.
  - **Action:** I conducted forensic SQL analysis across relational transaction logs, tracing data lineage from original PRISM procurement records through interface staging tables into SAP general ledger tables. I discovered that a legacy interface was dropping specific status flags during batch updates. I implemented a data realignment framework that reconciled historical mismatches, corrected interface transformation logic, and built an automated monitoring query to alert on unaligned records.
  - **Result:** Resolved the recurring discrepancies, reclaimed over $1M in annual contract funds, and established a permanent reconciliation routine.

### Q5: How do you collaborate with non-technical campus partners and data stewards who may not understand relational database schemas?
* **Strategic Intent:** Demonstrates empathy, clear technical translation, and consultative communication.
* **Response (STAR):**
  - **Situation:** Academic advisors, admissions officers, and department coordinators care deeply about student outcomes and business rules, but do not speak SQL or entity-relationship diagrams.
  - **Task:** Elicit accurate business requirements and validate data integration rules with non-technical stakeholders.
  - **Action:** I avoid technical jargon and frame discussions around real-world student and operational lifecycles: *"When a student changes majors, what should the advisor see on Day 1?"* I translate database fields into business concepts and use mock data outputs or side-by-side comparison tables during discovery sessions. When presenting validation results, I provide clear summary dashboards highlighting discrepancies in business terms.
  - **Result:** Campus partners felt heard and trusted, data steward approvals were secured on schedule, and the resulting CRM data models accurately mirrored campus operational needs.

---

## 5. High-Impact Reverse Questions for the CU Boulder Search Committee

### For the CRM Data Architect / Technical Lead:
1. *"The job description explicitly emphasizes reducing single-person dependencies across CRM data architecture and operations. From your perspective, where are the biggest operational bottlenecks right now, and what can I take off your plate in the first 90 days?"*
2. *"How far along is CU Boulder in deploying Salesforce Data Cloud / Data 360? Are you currently in the initial data ingestion and identity resolution phase, or are you already building downstream activation pipelines for student engagement?"*

### For the Hiring Manager / OIT Leadership:
1. *"OIT serves a decentralized campus environment across multiple colleges and institutes. How mature are the data governance and data stewardship processes across departments, and where does OIT see the greatest opportunity for standardizing CRM data exchange?"*
2. *"What does outstanding performance look like for this role after 6 months? Is it measured by the successful cutover of a specific CRM migration phase, the completeness of integration documentation, or the stability of operational data flows?"*

### For DevOps & Integration Partners (UIS):
1. *"How do the campus CRM integration flows coordinate with University Information Systems (UIS) central data engineering? What integration middleware (e.g., Boomi, MuleSoft, custom APIs) is primarily leveraged for cross-system data exchange?"*
