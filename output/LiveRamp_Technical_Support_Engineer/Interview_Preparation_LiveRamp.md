# Comprehensive Interview Preparation Package: Technical Support Engineer — LiveRamp, Inc.

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
