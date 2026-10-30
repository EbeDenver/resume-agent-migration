# CU Boulder Interview Preparation Package
**Data Integration Analyst | University of Colorado Boulder | Requisition 75732**  
Candidate: Ebenezer J. Rolston (Denver, CO) • Prepared for CU Boulder IT & Data Architecture Interview Panel

---

## 1. CU Boulder & Data Integration Strategic Context

The University of Colorado Boulder is modernizing its enterprise data infrastructure, with a focus on integrating disparate campus systems into unified CRM and analytical platforms. The **Data Integration Analyst** is responsible for building and maintaining ETL/ELT pipelines, designing source-to-target mappings, ensuring data quality across the Salesforce ecosystem, and supporting data-driven decision making across enrollment, student services, advancement, and academic operations.

### Key Dimensions of the Role:
- **ETL/ELT Pipeline Development:** Building reliable data pipelines that extract data from legacy campus systems, transform it according to business rules, and load it into Salesforce and analytical platforms.
- **Source-to-Target Mapping:** Documenting detailed field-level mappings between source systems and target schemas, including transformation logic, data type conversions, and business rule enforcement.
- **CRM Data Architecture:** Working within the Salesforce ecosystem (Education Cloud, Data Cloud) to maintain clean, deduplicated, and well-governed student, prospect, and alumni records.
- **Data Quality & Governance:** Establishing monitoring, reconciliation, and audit processes to ensure ongoing data health and compliance with FERPA and university governance standards.
- **Stakeholder Collaboration:** Partnering with Data Architects, application teams, and business stakeholders to translate requirements into robust integration solutions.

---

## 2. 30-60-90 Day Strategic Onboarding Charter

### Days 1–30: Understand the Landscape
- **Map the Data Ecosystem:** Inventory all source systems, target platforms, existing ETL pipelines, and integration touchpoints across CU Boulder's IT environment.
- **Review Existing Source-to-Target Documentation:** Assess current data mapping artifacts, transformation logic documentation, and data lineage records for completeness and accuracy.
- **Understand Salesforce Data Model:** Deep-dive into CU Boulder's Salesforce Education Cloud configuration — object relationships, custom fields, data flows, and integration connectors.
- **Establish Relationships:** Meet key stakeholders across IT, enrollment, advancement, and academic affairs to understand their data consumption patterns and pain points.

### Days 31–60: Contribute and Build
- **Assume Pipeline Ownership:** Take ownership of assigned ETL/ELT pipelines, running validations, troubleshooting failures, and implementing fixes with full documentation.
- **Enhance Data Quality Monitoring:** Implement automated reconciliation checks and row-count/hash-based validation scripts to catch data drift, truncation, and duplication proactively.
- **Author Source-to-Target Mappings:** Produce detailed field-level mapping documents for new integration initiatives, including transformation rules, null handling, deduplication logic, and referential integrity constraints.
- **Introduce Schema-Governed Validation:** Pilot Pydantic-style contract validation for incoming data feeds, enforcing data type constraints and business rule checks at ingestion time.

### Days 61–90: Optimize and Scale
- **Optimize SQL & Pipeline Performance:** Profile existing queries and ETL jobs for performance bottlenecks; implement indexing improvements, query refactoring, and incremental load strategies.
- **Establish Operational Documentation:** Create and maintain runbooks, SOPs, and troubleshooting guides that enable the team to operate pipelines without single-person dependencies.
- **Deliver Stakeholder Training:** Conduct cross-functional training sessions on data integration best practices, data quality expectations, and self-service data request procedures.
- **Propose Pipeline Modernization:** Identify legacy batch processes that could benefit from event-driven or incremental architectures, presenting a prioritized modernization roadmap.

---

## 3. High-Probability Technical & Behavioral Scenarios (STAR Format)

### Scenario 1: Leading a Multi-System Enterprise Data Migration
* **Situation:** At the Department of the Interior, I was appointed Department ETL Architect for the FBMS enterprise data conversion — a Department-wide initiative to migrate fragmented legacy databases into a unified SAP S/4 platform across 4 federal agencies.
* **Task:** Design and execute end-to-end source-to-target mappings, transformation rules, data cleansing procedures, and validation test plans ensuring complete data fidelity and zero business disruption.
* **Action:** I authored detailed field-level source-to-target mappings documenting every transformation rule, data type conversion, null handling protocol, and business logic derivation. I built automated SQL reconciliation scripts that compared record counts, financial totals, and hash checksums between source and target systems at each migration stage. I established a multi-pass validation methodology: (1) structural validation (schema match), (2) quantitative validation (row counts and financial footing checks), and (3) semantic validation (business rule correctness sampling).
* **Result:** Successfully migrated all 4 agencies' data into the unified FBMS platform with zero unresolved data discrepancies. Received two Department of Interior Awards for Excellence. This experience directly transfers to CU Boulder's need to integrate disparate campus systems into Salesforce.

### Scenario 2: Building Automated Data Quality Reconciliation Frameworks
* **Situation:** During the FBMS migration, post-conversion data quality issues were detected by contracting officers who noticed financial totals that didn't match their legacy system records.
* **Task:** Design and implement an automated reconciliation framework that could systematically detect and flag data discrepancies between source and target systems.
* **Action:** I built SQL-based reconciliation scripts that performed: (1) row-count comparisons by entity type and date range, (2) financial footing checks verifying that detail-level transaction amounts summed exactly to reported control totals, (3) cross-reference validation ensuring referential integrity between related tables, and (4) hash-based change detection to identify records modified during the migration window. The framework ran automatically and generated exception reports highlighting discrepancies with their root causes.
* **Result:** The reconciliation framework resolved financial discrepancies that helped reclaim millions in government funds and became the standard validation methodology adopted across the Department. At CU Boulder, I would apply the identical framework pattern to validate Salesforce data loads, enrollment record migrations, and advancement data integrations.

### Scenario 3: Resolving Complex Data Quality Issues Across Interconnected Platforms
* **Situation:** At the Department of the Interior, I handled 5 to 10 mission-critical enterprise incidents daily, many of which involved data quality issues that cascaded across interconnected procurement, financial, and reporting systems.
* **Task:** Perform rapid root-cause analysis to determine whether data issues originated in source system extraction, transformation logic, loading procedures, or downstream reporting.
* **Action:** I developed a systematic triage methodology: (1) trace the data lineage backward from the reported error to identify the earliest point of corruption, (2) examine transformation logs for truncation, rounding, or character encoding issues, (3) compare source timestamps with load timestamps to detect race conditions or out-of-order processing, and (4) validate business rules at each transformation step. I documented each root cause and implemented preventive fixes to eliminate recurrence.
* **Result:** Systematically reduced recurring incident volume by eliminating root causes rather than repeatedly patching symptoms. At CU Boulder, this diagnostic methodology would be directly applicable to troubleshooting Salesforce data feed failures, duplicate record creation, and cross-system synchronization issues.

### Scenario 4: Training Users and Establishing Operational Documentation
* **Situation:** At DOI/IBC, I was responsible for training 85+ users across multiple agencies on enterprise system operations, data entry standards, and reporting procedures.
* **Task:** Design and deliver a comprehensive training program that reduced support tickets and eliminated knowledge silos.
* **Action:** I created structured cohort training sessions combining live demonstrations, hands-on exercises, and reference documentation. I authored Standard Operating Procedures covering common workflows, troubleshooting guides for frequent error patterns, and data dictionary documentation explaining field definitions and business rules. I established office hours for ongoing support and maintained living documentation that evolved with system updates.
* **Result:** Achieved measurable reduction in recurring support requests and eliminated single-person dependencies. At CU Boulder, I would apply this approach to cross-functional training on data integration processes, data quality expectations, and Salesforce data stewardship practices.

### Scenario 5: Designing Customer Data Integration Pipelines at Acxiom Scale
* **Situation:** At Acxiom, I partnered with Fortune 500 clients (Citibank, GE Money, ChoicePoint, Allstate) to design customer data integration and data warehouse pipelines processing millions of consumer records.
* **Task:** Design and implement ETL architectures that ingested, cleansed, deduplicated, and matched consumer records from dozens of disparate source files into a unified customer data platform.
* **Action:** I designed source-to-target mappings for complex multi-source ingestion, implementing entity resolution algorithms that linked consumer identities across inconsistent name spellings, address variations, and demographic discrepancies. I built relational data warehouse schemas (star and snowflake models) and optimized SQL queries for high-volume batch processing. I implemented data quality profiling and hygiene routines that flagged duplicate records, stale addresses, and orphaned relationships.
* **Result:** Delivered production-grade customer data platforms that powered precision marketing, cross-selling, and identity verification for the nation's largest financial institutions. The entity resolution and deduplication expertise directly applies to CU Boulder's need to maintain clean, unduplicated student and prospect records across the Salesforce ecosystem.

---

## 4. Technical Deep-Dive Questions & Prepared Responses

### Q: "Walk us through how you would design a source-to-target mapping for a new data feed."
**A:** I start by understanding the business context — what decisions will this data support? Then I obtain sample source data and the target schema documentation. I create a field-level mapping spreadsheet documenting: source field name, source data type, target field name, target data type, transformation rule (direct map, derivation, concatenation, lookup), null handling (default value, reject, flag), and validation rule (regex pattern, range check, referential integrity). I identify deduplication keys and matching logic. I include data volume estimates and update frequency. Before building the pipeline, I walk the mapping through a review with both the source system SME and the target system architect to catch misunderstandings early. Every mapping gets a corresponding validation test plan.

### Q: "How do you handle data quality issues you discover during a migration?"
**A:** I categorize issues by severity and source: (1) systemic issues (affecting all records — usually a transformation logic error), (2) pattern issues (affecting a subset — usually a data type or encoding issue in specific source files), and (3) isolated issues (individual records — usually source data quality problems). Systemic issues get immediate pipeline fixes. Pattern issues get targeted cleansing rules. Isolated issues go into an exception queue with the source system team for manual resolution. I never silently discard or default-fill problematic records — every exception must be explicitly handled and documented.

### Q: "What's your experience with Salesforce data architecture?"
**A:** My direct CRM data architecture experience comes from 11 years at Acxiom building Customer 360 platforms — entity resolution, identity matching, deduplication, and multi-source data integration for financial services and insurance clients. The underlying data architecture principles are identical to Salesforce: understanding multi-object relational models, managing many-to-many relationships through junction objects, handling record matching and merge operations, and maintaining referential integrity across related records. I'm transparent that Salesforce-specific configuration (object manager, flow builder, Data Cloud connectors) is the learnable delta — but the core ETL/integration architecture I bring is platform-agnostic and transfers directly.

---

## 5. Questions to Ask the CU Boulder Interview Panel

1. "What are the primary source systems feeding into CU Boulder's Salesforce environment today, and which integrations are the highest priority for improvement?"
2. "How is the team currently handling data deduplication and identity matching across student, prospect, and alumni records?"
3. "What's the current ETL/ELT technology stack — is CU Boulder using Salesforce Data Loader, MuleSoft, Informatica, or custom solutions?"
4. "How does the team manage data governance and FERPA compliance within the integration pipeline?"
5. "What does success look like for this role in the first 6 months?"
