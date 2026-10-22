#!/usr/bin/env python3
"""Build and assemble dashboard/index.html and artifact job_dashboard.html.

Includes:
- Multi-Source Integration (80,000 Hours, Ashby ATS, Greenhouse, LinkedIn, USAJobs)
- Date Stamps (Agent Executed, Employer Posted, Reposted Status)
- Incremental Match Tiers (90-100, 80-89, 70-79, 60-69, 50-59)
- Real-time SQLite state synchronization and local agent execution bridge
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOBS_FILE = PROJECT_ROOT / "dashboard" / "default_jobs.json"
OUTPUT_INDEX = PROJECT_ROOT / "dashboard" / "index.html"
ARTIFACT_INDEX = Path("/Users/eberolston/.gemini/antigravity/brain/617659e8-edc7-423a-a2a7-eef70ed53918/job_dashboard.html")

with open(JOBS_FILE, "r", encoding="utf-8") as f:
    jobs_json_str = f.read()

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Job Intelligence & Interview Ranking Dashboard | Ebenezer J. Rolston</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .badge-tier-90 { background-color: #ECFDF5; color: #065F46; border: 1px solid #A7F3D0; }
    .badge-tier-80 { background-color: #EFF6FF; color: #1E40AF; border: 1px solid #BFDBFE; }
    .badge-tier-70 { background-color: #FFFBEB; color: #92400E; border: 1px solid #FDE68A; }
    .badge-tier-60 { background-color: #EEF2FF; color: #3730A3; border: 1px solid #C7D2FE; }
    .badge-tier-50 { background-color: #F8FAFC; color: #475569; border: 1px solid #CBD5E1; }
    .badge-ai { background-color: #FAF5FF; color: #6B21A8; border: 1px solid #E9D5FF; }
    .badge-80k { background-color: #FFFBEB; color: #B45309; border: 1px solid #FCD34D; }
    .badge-ashby { background-color: #ECFEFF; color: #0E7490; border: 1px solid #A5F3FC; }
    .card-applied { border-color: #10B981 !important; background-color: #F0FDF4; }
  </style>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col">

  <!-- Top Navigation Header -->
  <header class="bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-blue-700 to-indigo-800 text-white flex items-center justify-center font-bold text-sm shadow">
          EJR
        </div>
        <div>
          <h1 class="text-base font-bold text-slate-900 leading-tight flex items-center gap-2">
            Job Intelligence & Interview Ranking Dashboard
            <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-blue-100 text-blue-800 border border-blue-200">Active Market Scan</span>
          </h1>
          <div class="flex items-center gap-2 text-xs text-slate-500 flex-wrap">
            <span>Candidate: <strong>Ebenezer J. Rolston</strong> • Denver, CO • Remote / Hybrid • Min Score: ≥60%</span>
            <span class="text-slate-300">•</span>
            <span class="font-mono text-slate-600 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">
              🕒 Last Agent Scan: <strong id="scanTimestampText">Oct 13, 2026</strong>
            </span>
          </div>
        </div>
      </div>

      <div class="flex items-center gap-2.5 flex-wrap">
        <!-- Database Badge -->
        <div class="flex items-center gap-1.5 text-xs bg-slate-100 text-slate-700 px-3 py-1.5 rounded-lg border border-slate-200" title="Persistent SQLite Database (data/jobs.db)">
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
          <span class="font-medium">DB: <code>data/jobs.db</code> (<span id="totalDbJobsCount">38</span> tracked)</span>
        </div>

        <!-- Local Server Bridge Status Indicator -->
        <div id="serverStatusPill" class="flex items-center gap-1.5 text-xs bg-slate-100 text-slate-600 px-3 py-1.5 rounded-lg border border-slate-200">
          <span id="serverStatusDot" class="w-2 h-2 rounded-full bg-slate-400"></span>
          <span id="serverStatusText" class="font-medium">Connecting...</span>
        </div>

        <!-- Trigger Job Search Button -->
        <button onclick="triggerJobSearch()" id="btnJobSearch" class="bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold px-3 py-1.5 rounded-lg shadow-sm transition flex items-center gap-1.5">
          <span>🔍</span> Run Job Search (≥60%)
        </button>

        <!-- Reset Button -->
        <button onclick="resetAllDefaults()" class="text-slate-500 hover:text-slate-700 text-xs font-medium px-2.5 py-1.5 rounded border border-slate-200 hover:bg-slate-100 transition">
          Reset View
        </button>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full space-y-6">

    <!-- KPI Metric Cards -->
    <section class="grid grid-cols-2 md:grid-cols-5 gap-3.5">
      <div class="bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm">
        <div class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Top Match Score</div>
        <div class="mt-1 flex items-baseline gap-2">
          <span class="text-2xl font-bold text-emerald-600">94%</span>
          <span class="text-xs text-slate-500 truncate">Matter Health (CTO)</span>
        </div>
      </div>
      <div class="bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm">
        <div class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Active Opportunities</div>
        <div class="mt-1 flex items-baseline gap-2">
          <span class="text-2xl font-bold text-blue-600" id="activeJobsCount">0</span>
          <span class="text-xs text-slate-500">Ready to Target</span>
        </div>
      </div>
      <div class="bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm">
        <div class="text-xs font-semibold text-slate-500 uppercase tracking-wider">AI Enablement Roles</div>
        <div class="mt-1 flex items-baseline gap-2">
          <span class="text-2xl font-bold text-purple-600" id="aiEnablementCountCard">18</span>
          <span class="text-xs text-slate-500">Technical Workflows</span>
        </div>
      </div>
      <div class="bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm">
        <div class="text-xs font-semibold text-slate-500 uppercase tracking-wider">80,000 Hours / Impact</div>
        <div class="mt-1 flex items-baseline gap-2">
          <span class="text-2xl font-bold text-amber-600" id="source80kCountCard">5</span>
          <span class="text-xs text-slate-500">AI Safety & Policy</span>
        </div>
      </div>
      <div class="bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm">
        <div class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Applied / In Progress</div>
        <div class="mt-1 flex items-baseline gap-2">
          <span class="text-2xl font-bold text-emerald-600" id="appliedJobsCount">0</span>
          <span class="text-xs text-slate-500">Submissions Logged</span>
        </div>
      </div>
    </section>

    <!-- Filter & Search Controls -->
    <section class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm space-y-3.5">
      <!-- Search Input & Sort -->
      <div class="flex flex-col md:flex-row gap-3 justify-between items-center">
        <div class="relative w-full md:w-96">
          <svg class="w-4 h-4 text-slate-400 absolute left-3 top-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          <input type="text" id="searchInput" placeholder="Search roles, skills, or companies (e.g. Matter Health, 80000 Hours, Prompt, LangGraph)..." 
                 class="w-full pl-9 pr-4 py-2 border border-slate-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
        </div>

        <div class="flex items-center gap-2 w-full md:w-auto">
          <span class="text-xs font-medium text-slate-500 whitespace-nowrap">Sort By:</span>
          <select id="sortSelect" class="border border-slate-300 rounded-lg px-3 py-2 text-sm bg-white text-slate-700 focus:outline-none focus:ring-2 focus:ring-blue-500">
            <option value="rank">Recommended Rank (Default)</option>
            <option value="posted">Employer Date Posted (Newest First)</option>
            <option value="probability">Highest Interview Probability</option>
            <option value="match">Highest Match Score</option>
            <option value="salary">Highest Base Salary</option>
          </select>
        </div>
      </div>

      <!-- MATCH TIER FILTER SELECTION (User Requested 50-59, 60-69, etc.) -->
      <div class="flex items-center gap-1.5 flex-wrap pt-2 border-t border-slate-100">
        <span class="text-xs font-bold text-slate-700 uppercase tracking-wider mr-1">Match Tier:</span>
        <button onclick="setTierFilter('all')" id="tier-all" class="tier-pill px-3 py-1 rounded-full text-xs font-bold bg-blue-600 text-white transition">All Tiers (≥60%)</button>
        <button onclick="setTierFilter('90-100')" id="tier-90-100" class="tier-pill px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-800 border border-emerald-300 hover:bg-emerald-100 transition">Tier 90–100% (<span id="tierCount90">7</span>)</button>
        <button onclick="setTierFilter('80-89')" id="tier-80-89" class="tier-pill px-2.5 py-1 rounded-full text-xs font-semibold bg-blue-50 text-blue-800 border border-blue-300 hover:bg-blue-100 transition">Tier 80–89% (<span id="tierCount80">19</span>)</button>
        <button onclick="setTierFilter('70-79')" id="tier-70-79" class="tier-pill px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-50 text-amber-800 border border-amber-300 hover:bg-amber-100 transition">Tier 70–79% (<span id="tierCount70">6</span>)</button>
        <button onclick="setTierFilter('60-69')" id="tier-60-69" class="tier-pill px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-50 text-indigo-800 border border-indigo-300 hover:bg-indigo-100 transition">Tier 60–69% (<span id="tierCount60">6</span>)</button>
        <button onclick="setTierFilter('50-59')" id="tier-50-59" class="tier-pill px-2.5 py-1 rounded-full text-xs font-semibold bg-slate-100 text-slate-500 border border-slate-300 hover:bg-slate-200 transition">Tier 50–59% (<span id="tierCount50">0</span>)</button>
      </div>

      <!-- Category & Source Filters -->
      <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-100">
        <button onclick="setFilter('active')" id="btn-active" class="filter-pill px-3 py-1 rounded-full text-xs font-semibold bg-blue-600 text-white transition">Active Positions</button>
        <button onclick="setFilter('ai_enablement')" id="btn-ai_enablement" class="filter-pill px-3 py-1 rounded-full text-xs font-semibold bg-purple-50 text-purple-700 border border-purple-200 hover:bg-purple-100 transition">🤖 AI Enablement (<span id="aiEnablementTabCount">18</span>)</button>
        <button onclick="setFilter('80000_hours')" id="btn-80000_hours" class="filter-pill px-3 py-1 rounded-full text-xs font-semibold bg-amber-50 text-amber-800 border border-amber-300 hover:bg-amber-100 transition">⏳ 80,000 Hours (<span id="source80kTabCount">5</span>)</button>
        <button onclick="setFilter('ats')" id="btn-ats" class="filter-pill px-3 py-1 rounded-full text-xs font-semibold bg-cyan-50 text-cyan-800 border border-cyan-300 hover:bg-cyan-100 transition">⚡ Ashby & Greenhouse ATS (<span id="sourceAtsTabCount">3</span>)</button>
        <button onclick="setFilter('federal')" id="btn-federal" class="filter-pill px-3 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-600 hover:bg-slate-200 transition">🏛️ Federal & Defense (7)</button>
        <button onclick="setFilter('ai_strategy')" id="btn-ai_strategy" class="filter-pill px-3 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-600 hover:bg-slate-200 transition">🧠 AI Strategy & Governance (8)</button>
        <button onclick="setFilter('enterprise')" id="btn-enterprise" class="filter-pill px-3 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-600 hover:bg-slate-200 transition">🏢 Enterprise Systems / ERP (5)</button>
        <button onclick="setFilter('applied')" id="btn-applied" class="filter-pill px-3 py-1 rounded-full text-xs font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 transition">✓ Applied (<span id="appliedTabCount">0</span>)</button>
        <button onclick="setFilter('deleted')" id="btn-deleted" class="filter-pill px-3 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-400 hover:bg-slate-200 transition">🗑️ Dismissed (<span id="trashTabCount">0</span>)</button>
      </div>
    </section>

    <!-- Notification Toast -->
    <div id="toast" class="hidden fixed bottom-6 right-6 z-50 bg-slate-900 text-white px-4 py-3 rounded-xl shadow-lg text-sm flex items-center gap-3">
      <span id="toastMsg">Action updated</span>
      <button id="toastUndoBtn" class="text-blue-400 font-semibold underline text-xs">Undo</button>
    </div>

    <!-- Agent Execution / Search Modal -->
    <div id="agentModal" class="hidden fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4">
      <div class="bg-white rounded-2xl max-w-2xl w-full p-6 shadow-2xl border border-slate-200 space-y-4">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3">
          <div class="flex items-center gap-3">
            <div id="modalSpinner" class="w-5 h-5 border-2 border-indigo-600 border-t-transparent rounded-full animate-spin"></div>
            <h3 id="modalTitle" class="text-base font-bold text-slate-900">Processing...</h3>
          </div>
          <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600 text-lg">✕</button>
        </div>

        <div id="modalStatusText" class="text-xs text-slate-600 font-medium">
          Connecting to pipeline...
        </div>

        <!-- Terminal Output Window -->
        <pre id="modalConsole" class="bg-slate-950 text-emerald-400 p-4 rounded-xl text-xs font-mono max-h-64 overflow-y-auto whitespace-pre-wrap leading-relaxed shadow-inner">Initializing...</pre>

        <div class="flex items-center justify-between pt-2">
          <button id="openFolderBtn" onclick="openOutputFolder()" class="hidden bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold px-4 py-2 rounded-lg border border-slate-300 transition flex items-center gap-2">
            <span>📁 Open Deliverables in Finder</span>
          </button>
          <button onclick="closeModal()" class="ml-auto bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold px-4 py-2 rounded-lg transition">
            Close
          </button>
        </div>
      </div>
    </div>

    <!-- Job Cards Feed Container -->
    <section id="jobsContainer" class="space-y-4">
      <!-- Rendered dynamically by JavaScript -->
    </section>

  </main>

  <!-- Footer -->
  <footer class="bg-white border-t border-slate-200 py-6 text-center text-xs text-slate-400 mt-auto">
    <p>Automated Resume Generator & Job Intelligence Pipeline • Built for Ebenezer J. Rolston • Denver, CO</p>
    <p class="mt-1">Tracks Ashby, Greenhouse, 80,000 Hours, USAJobs, and LinkedIn • Deduplicated SQLite Store</p>
  </footer>

  <script>
    // Embedded Data Set
    let defaultJobs = """ + jobs_json_str + """;

    // Application State
    const STORAGE_KEY = 'ejr_jobs_dashboard_state_v3';
    let state = {};
    let currentFilter = 'active';
    let currentTierFilter = 'all';
    let currentSearch = '';
    let currentSort = 'rank';
    let isServerConnected = false;
    let currentOutputDir = '';

    const SERVER_URL = 'http://localhost:8000';

    async function init() {
      state = loadState();
      // Render IMMEDIATELY from embedded data so cards appear with zero latency!
      renderJobs();

      // Background sync with local SQLite server bridge
      try {
        await checkServer();
        if (isServerConnected) {
          await fetchJobsFromDb();
          renderJobs();
        }
      } catch (err) {
        console.warn("Background server bridge notice:", err);
      }

      setInterval(async () => {
        await checkServer();
      }, 10000);
    }

    async function checkServer() {
      const dot = document.getElementById('serverStatusDot');
      const text = document.getElementById('serverStatusText');
      const pill = document.getElementById('serverStatusPill');

      try {
        const res = await fetch(`${SERVER_URL}/api/status`, { signal: AbortSignal.timeout(2000) });
        if (res.ok) {
          isServerConnected = true;
          dot.className = "w-2 h-2 rounded-full bg-emerald-500 animate-pulse";
          text.innerText = "Agent Bridge Live (Port 8000)";
          pill.className = "flex items-center gap-1.5 text-xs bg-emerald-50 text-emerald-700 px-3 py-1.5 rounded-lg border border-emerald-200";
          return;
        }
      } catch (err) {}

      isServerConnected = false;
      dot.className = "w-2 h-2 rounded-full bg-amber-500";
      text.innerText = "Bridge Standby (Offline)";
      pill.className = "flex items-center gap-1.5 text-xs bg-amber-50 text-amber-700 px-3 py-1.5 rounded-lg border border-amber-200";
    }

    async function fetchJobsFromDb() {
      if (!isServerConnected) return;
      try {
        const res = await fetch(`${SERVER_URL}/api/jobs`);
        if (res.ok) {
          const data = await res.json();
          if (data.jobs && data.jobs.length > 0) {
            defaultJobs = data.jobs.map((j, idx) => ({
              id: j.id,
              rank: idx + 1,
              title: j.title,
              employer: j.employer,
              department: j.department || '',
              category: j.category || 'ai_enablement',
              location: j.location || 'Denver, CO',
              locationType: j.location_type || 'remote',
              salaryBand: j.salary_band || '$100,000 – $140,000',
              salaryMax: j.salary_max || 140000,
              matchScore: j.match_score,
              interviewProb: j.interview_prob,
              fitBand: j.fit_band || 'Strong Fit',
              matchTier: j.match_tier || computeTier(j.match_score),
              source: j.source || 'linkedin',
              sourceLabel: j.source_label || (j.source === '80000_hours' ? '80,000 Hours' : 'LinkedIn'),
              postedDate: j.posted_date || 'Oct 2026',
              isReposted: Boolean(j.is_reposted),
              repostedDate: j.reposted_date || null,
              agentExecutedAt: j.agent_executed_at || j.last_seen_at || null,
              linkedinUrl: j.linkedin_url,
              directUrl: j.direct_url,
              searchLandingUrl: j.search_landing_url,
              whyMatched: j.why_matched || '',
              topSkills: Array.isArray(j.top_skills) ? j.top_skills : [],
              gapBridge: j.gap_bridge || '',
              packageAction: j.package_action || `python3 run_agent.py --job-id ${j.id}`,
              outputDir: j.output_dir || `output/Job_${j.id}`,
              status: j.status || 'active',
              appliedAt: j.applied_at || null
            }));

            // Sync server statuses into local state
            defaultJobs.forEach(j => {
              if (j.status && j.status !== 'active') {
                state[j.id] = { status: j.status, appliedAt: j.appliedAt };
              }
            });
            saveState();
            const dbCountEl = document.getElementById('totalDbJobsCount');
            if (dbCountEl) dbCountEl.innerText = defaultJobs.length;
          }
        }
      } catch (err) {
        console.warn("Could not fetch jobs from SQLite:", err);
      }
    }

    function computeTier(score) {
      if (score >= 90) return '90-100';
      if (score >= 80) return '80-89';
      if (score >= 70) return '70-79';
      if (score >= 60) return '60-69';
      if (score >= 50) return '50-59';
      return 'under-50';
    }

    function formatAgentTime(iso) {
      if (!iso) return 'Oct 13, 2026';
      try {
        const d = new Date(iso);
        if (isNaN(d.getTime())) return iso;
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) + ' ' + d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
      } catch (e) {
        return iso;
      }
    }

    function getSourceBadge(source, label) {
      if (source === '80000_hours') return '<span class="badge-80k px-2 py-0.5 rounded text-xs font-bold">⏳ 80,000 Hours</span>';
      if (source === 'ashby') return '<span class="badge-ashby px-2 py-0.5 rounded text-xs font-bold">⚡ Ashby ATS</span>';
      if (source === 'greenhouse') return '<span class="bg-emerald-50 text-emerald-700 border border-emerald-300 px-2 py-0.5 rounded text-xs font-bold">🌿 Greenhouse</span>';
      if (source === 'usajobs') return '<span class="bg-blue-50 text-blue-800 border border-blue-200 px-2 py-0.5 rounded text-xs font-bold">🏛️ USAJobs</span>';
      return `<span class="bg-slate-100 text-slate-700 border border-slate-300 px-2 py-0.5 rounded text-xs font-bold">💼 ${label || 'LinkedIn'}</span>`;
    }

    async function triggerJobSearch() {
      await checkServer();
      const modal = document.getElementById('agentModal');
      const title = document.getElementById('modalTitle');
      const consoleBox = document.getElementById('modalConsole');
      const spinner = document.getElementById('modalSpinner');
      const statusText = document.getElementById('modalStatusText');
      const folderBtn = document.getElementById('openFolderBtn');

      title.innerText = "Running Job Search & Deduplication Engine...";
      statusText.innerText = "Scanning 80,000 Hours, Ashby ATS, Greenhouse, LinkedIn & USAJobs...";
      consoleBox.innerText = `[INITIALIZING MULTI-SOURCE SEARCH]\\n$ python3 job_search_engine.py --min-score 60\\nConnecting to SQLite at ${SERVER_URL}...\\n`;
      spinner.classList.remove('hidden');
      folderBtn.classList.add('hidden');
      modal.classList.remove('hidden');

      if (!isServerConnected) {
        spinner.classList.add('hidden');
        title.innerText = "Bridge Offline — Command Available";
        statusText.innerText = "Copy command below to run directly in terminal:";
        consoleBox.innerText += "\\nTo run the live search engine, launch: python3 dashboard/server.py 8000";
        return;
      }

      try {
        const res = await fetch(`${SERVER_URL}/api/run-job-search`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ minScore: 60 })
        });
        const data = await res.json();
        spinner.classList.add('hidden');
        if (data.success) {
          title.innerText = "✓ Job Search Completed";
          statusText.innerText = `Search engine finished. SQLite database updated.`;
          consoleBox.innerText += `\\n[OUTPUT LOGS]:\\n` + data.output + `\\n\\n[STATUS: SUCCESS - Zero Repetitions]`;
          await fetchJobsFromDb();
          renderJobs();
        } else {
          title.innerText = "⚠️ Search Engine Notice";
          statusText.innerText = "Search completed with notice:";
          consoleBox.innerText += `\\n` + (data.output || data.error);
        }
      } catch (err) {
        spinner.classList.add('hidden');
        title.innerText = "Search Engine Error";
        consoleBox.innerText += `\\nNetwork error: ${err.message}`;
      }
    }

    async function runAgent(jobId) {
      const job = defaultJobs.find(j => j.id === jobId);
      if (!job) return;

      await checkServer();
      if (!isServerConnected) {
        navigator.clipboard.writeText(job.packageAction);
        showToast(`📋 Copied command for ${job.title}! Run in terminal: ${job.packageAction}`);
        return;
      }

      currentOutputDir = job.outputDir;
      const modal = document.getElementById('agentModal');
      const title = document.getElementById('modalTitle');
      const consoleBox = document.getElementById('modalConsole');
      const spinner = document.getElementById('modalSpinner');
      const statusText = document.getElementById('modalStatusText');
      const folderBtn = document.getElementById('openFolderBtn');

      title.innerText = `Running Agent: ${job.title}`;
      statusText.innerText = `Executing: ${job.packageAction}`;
      consoleBox.innerText = `[STARTING PIPELINE]\\n$ ${job.packageAction}\\nConnecting to agent engine at ${SERVER_URL}...\\n`;
      spinner.classList.remove('hidden');
      folderBtn.classList.add('hidden');
      modal.classList.remove('hidden');

      try {
        const response = await fetch(`${SERVER_URL}/api/run-agent`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            command: job.packageAction,
            jobTitle: job.title,
            outputDir: job.outputDir
          })
        });
        const res = await response.json();
        spinner.classList.add('hidden');
        if (res.success) {
          title.innerText = `✓ Completed: ${job.title}`;
          statusText.innerText = `All 4 tailored deliverables successfully created!`;
          consoleBox.innerText += `\\n[OUTPUT LOGS]:\\n` + res.output + `\\n\\n[STATUS: SUCCESS]`;
          folderBtn.classList.remove('hidden');
        } else {
          title.innerText = `⚠️ Agent Execution Notice`;
          statusText.innerText = `Execution output:`;
          consoleBox.innerText += `\\n` + res.output;
        }
      } catch (err) {
        spinner.classList.add('hidden');
        title.innerText = `Execution Error`;
        consoleBox.innerText += `\\nFailed to connect to local server: ${err.message}`;
      }
    }

    function openOutputFolder() {
      if (currentOutputDir && isServerConnected) {
        fetch(`${SERVER_URL}/api/open-folder`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ folder: currentOutputDir })
        });
      }
    }

    function closeModal() {
      document.getElementById('agentModal').classList.add('hidden');
    }

    function loadState() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
          const parsed = JSON.parse(saved);
          if (parsed && typeof parsed === 'object') {
            const normalized = {};
            for (const [k, v] of Object.entries(parsed)) {
              if (typeof v === 'string') {
                normalized[k] = { status: v, appliedAt: null };
              } else if (v && typeof v === 'object') {
                normalized[k] = { status: v.status || 'active', appliedAt: v.appliedAt || null };
              }
            }
            return normalized;
          }
        }
      } catch (e) {
        console.error("Failed to load state", e);
      }
      const initial = {};
      defaultJobs.forEach(j => {
        initial[j.id] = { status: j.status || 'active', appliedAt: j.appliedAt || null };
      });
      return initial;
    }

    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
      } catch (e) {
        console.error("Failed to save state", e);
      }
      updateCounts();
    }

    function updateCounts() {
      let active = 0, applied = 0, deleted = 0;
      let t90 = 0, t80 = 0, t70 = 0, t60 = 0, t50 = 0;
      let aiCount = 0, source80k = 0, sourceAts = 0;
      let latestAgentTime = null;

      defaultJobs.forEach(j => {
        const entry = state[j.id];
        const s = (entry && typeof entry === 'object') ? (entry.status || 'active') : (entry || j.status || 'active');
        if (s === 'active') active++;
        else if (s === 'applied') applied++;
        else if (s === 'deleted') deleted++;

        if (j.agentExecutedAt && (!latestAgentTime || j.agentExecutedAt > latestAgentTime)) {
          latestAgentTime = j.agentExecutedAt;
        }

        if (s !== 'deleted') {
          const tier = j.matchTier || computeTier(j.matchScore);
          if (tier === '90-100') t90++;
          else if (tier === '80-89') t80++;
          else if (tier === '70-79') t70++;
          else if (tier === '60-69') t60++;
          else if (tier === '50-59') t50++;

          if (j.category === 'ai_enablement') aiCount++;
          if (j.source === '80000_hours') source80k++;
          if (j.source === 'ashby' || j.source === 'greenhouse') sourceAts++;
        }
      });

      document.getElementById('activeJobsCount').innerText = active;
      document.getElementById('appliedJobsCount').innerText = applied;
      document.getElementById('deletedJobsCount').innerText = deleted;
      document.getElementById('appliedTabCount').innerText = applied;
      document.getElementById('trashTabCount').innerText = deleted;

      document.getElementById('aiEnablementCountCard').innerText = aiCount;
      document.getElementById('aiEnablementTabCount').innerText = aiCount;
      document.getElementById('source80kCountCard').innerText = source80k;
      document.getElementById('source80kTabCount').innerText = source80k;
      document.getElementById('sourceAtsTabCount').innerText = sourceAts;

      document.getElementById('tierCount90').innerText = t90;
      document.getElementById('tierCount80').innerText = t80;
      document.getElementById('tierCount70').innerText = t70;
      document.getElementById('tierCount60').innerText = t60;
      document.getElementById('tierCount50').innerText = t50;

      const dbCountEl = document.getElementById('totalDbJobsCount');
      if (dbCountEl) dbCountEl.innerText = defaultJobs.length;

      const scanTimeEl = document.getElementById('scanTimestampText');
      if (scanTimeEl && latestAgentTime) {
        scanTimeEl.innerText = formatAgentTime(latestAgentTime);
      }
    }

    async function toggleApplied(jobId) {
      const current = state[jobId] ? state[jobId].status : 'active';
      let newStatus, appliedAt;
      if (current === 'applied') {
        newStatus = 'active';
        appliedAt = null;
        state[jobId] = { status: 'active', appliedAt: null };
        showToast("Marked job as unapplied", jobId, 'active');
      } else {
        const now = new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
        newStatus = 'applied';
        appliedAt = now;
        state[jobId] = { status: 'applied', appliedAt: now };
        showToast("✓ Marked job as Applied (" + now + ")", jobId, 'applied');
      }
      saveState();
      renderJobs();

      if (isServerConnected) {
        try {
          fetch(`${SERVER_URL}/api/job-status`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: jobId, status: newStatus, appliedAt: appliedAt })
          });
        } catch(e) {}
      }
    }

    async function deleteJob(jobId) {
      const prev = state[jobId] || { status: 'active', appliedAt: null };
      state[jobId] = { status: 'deleted', appliedAt: prev.appliedAt };
      saveState();
      showToast("Job removed from active list", jobId, 'deleted', prev);
      renderJobs();

      if (isServerConnected) {
        try {
          fetch(`${SERVER_URL}/api/job-status`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: jobId, status: 'deleted', appliedAt: prev.appliedAt })
          });
        } catch(e) {}
      }
    }

    function restoreJob(jobId) {
      const prevApplied = state[jobId] && state[jobId].appliedAt;
      state[jobId] = { status: prevApplied ? 'applied' : 'active', appliedAt: prevApplied || null };
      saveState();
      showToast("Job restored to active list", jobId, 'restored');
      renderJobs();

      if (isServerConnected) {
        try {
          fetch(`${SERVER_URL}/api/job-status`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: jobId, status: prevApplied ? 'applied' : 'active', appliedAt: prevApplied || null })
          });
        } catch(e) {}
      }
    }

    function resetAllDefaults() {
      if (confirm("Reset all job filters and views? This will unhide dismissed opportunities.")) {
        localStorage.removeItem(STORAGE_KEY);
        state = {};
        defaultJobs.forEach(j => { state[j.id] = { status: 'active', appliedAt: null }; });
        saveState();
        renderJobs();
        showToast("Dashboard view reset");
      }
    }

    function showToast(msg, jobId = null, actionType = null, prevState = null) {
      const toast = document.getElementById('toast');
      const toastMsg = document.getElementById('toastMsg');
      const undoBtn = document.getElementById('toastUndoBtn');
      toastMsg.innerText = msg;
      
      if (jobId && prevState) {
        undoBtn.style.display = 'inline';
        undoBtn.onclick = () => {
          state[jobId] = prevState;
          saveState();
          renderJobs();
          toast.classList.add('hidden');
        };
      } else {
        undoBtn.style.display = 'none';
      }

      toast.classList.remove('hidden');
      setTimeout(() => { toast.classList.add('hidden'); }, 4000);
    }

    function setTierFilter(tier) {
      currentTierFilter = tier;
      document.querySelectorAll('.tier-pill').forEach(btn => {
        btn.className = "tier-pill px-2.5 py-1 rounded-full text-xs font-semibold bg-slate-100 text-slate-700 border border-slate-300 hover:bg-slate-200 transition";
      });
      const activeBtn = document.getElementById('tier-' + tier);
      if (activeBtn) {
        activeBtn.className = "tier-pill px-3 py-1 rounded-full text-xs font-bold bg-blue-600 text-white transition";
      }
      renderJobs();
    }

    function setFilter(filter) {
      currentFilter = filter;
      document.querySelectorAll('.filter-pill').forEach(btn => {
        btn.className = "filter-pill px-3 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-600 hover:bg-slate-200 transition";
      });
      const activeBtn = document.getElementById('btn-' + filter);
      if (activeBtn) {
        activeBtn.className = "filter-pill px-3 py-1 rounded-full text-xs font-bold bg-blue-600 text-white transition";
      }
      renderJobs();
    }

    function renderJobs() {
      updateCounts();
      const container = document.getElementById('jobsContainer');
      container.innerHTML = '';

      let list = defaultJobs.filter(job => {
        const entry = state[job.id];
        const status = (entry && typeof entry === 'object') ? (entry.status || 'active') : (entry || job.status || 'active');

        // Status / Category / Source Filter
        if (currentFilter === 'active') {
          if (status !== 'active') return false;
        } else if (currentFilter === 'applied') {
          if (status !== 'applied') return false;
        } else if (currentFilter === 'deleted') {
          if (status !== 'deleted') return false;
        } else {
          if (status === 'deleted') return false;
          if (currentFilter === 'ai_enablement' && job.category !== 'ai_enablement') return false;
          if (currentFilter === '80000_hours' && job.source !== '80000_hours') return false;
          if (currentFilter === 'ats' && job.source !== 'ashby' && job.source !== 'greenhouse') return false;
          if (currentFilter === 'federal' && job.category !== 'federal') return false;
          if (currentFilter === 'ai_strategy' && job.category !== 'ai_strategy') return false;
          if (currentFilter === 'enterprise' && job.category !== 'enterprise') return false;
        }

        // Match Tier Filter
        if (currentTierFilter !== 'all') {
          const tier = job.matchTier || computeTier(job.matchScore);
          if (tier !== currentTierFilter) return false;
        }

        // Search Query
        if (currentSearch) {
          const q = currentSearch.toLowerCase();
          const skillsText = Array.isArray(job.topSkills) ? job.topSkills.join(' ') : String(job.topSkills || '');
          const matchStr = ((job.title || '') + " " + (job.employer || '') + " " + (job.sourceLabel || '') + " " + (job.whyMatched || '') + " " + skillsText).toLowerCase();
          if (!matchStr.includes(q)) return false;
        }
        return true;
      });

      list.sort((a, b) => {
        if (currentSort === 'rank') return (a.rank || 0) - (b.rank || 0);
        if (currentSort === 'posted') {
          const da = new Date(a.postedDate || 0).getTime() || 0;
          const db = new Date(b.postedDate || 0).getTime() || 0;
          return db - da;
        }
        if (currentSort === 'probability') return (b.interviewProb || 0) - (a.interviewProb || 0);
        if (currentSort === 'match') return (b.matchScore || 0) - (a.matchScore || 0);
        if (currentSort === 'salary') return (b.salaryMax || 0) - (a.salaryMax || 0);
        return 0;
      });

      if (list.length === 0) {
        container.innerHTML = `
          <div class="bg-white p-12 rounded-xl border border-slate-200 text-center space-y-3">
            <div class="text-4xl">🔍</div>
            <div class="text-base font-semibold text-slate-700">No jobs match this filter combination</div>
            <p class="text-xs text-slate-500 max-w-md mx-auto">Try selecting 'All Tiers' or switching category pills above to view active opportunities.</p>
          </div>
        `;
        return;
      }

      list.forEach(job => {
        try {
          const entry = state[job.id];
          const isApplied = ((entry && typeof entry === 'object') ? entry.status : entry) === 'applied';
          const isDeleted = ((entry && typeof entry === 'object') ? entry.status : entry) === 'deleted';
          const appliedDate = (entry && typeof entry === 'object') ? (entry.appliedAt || '') : '';
          const tier = job.matchTier || computeTier(job.matchScore || 0);

          let tierBadgeClass = "badge-tier-80";
          if (tier === '90-100') tierBadgeClass = "badge-tier-90";
          else if (tier === '80-89') tierBadgeClass = "badge-tier-80";
          else if (tier === '70-79') tierBadgeClass = "badge-tier-70";
          else if (tier === '60-69') tierBadgeClass = "badge-tier-60";
          else tierBadgeClass = "badge-tier-50";

          const isAiEnablement = job.category === 'ai_enablement';

          const skillsArray = Array.isArray(job.topSkills) ? job.topSkills : 
            (typeof job.topSkills === 'string' ? job.topSkills.split(',').map(s => s.trim()).filter(Boolean) : []);

          const card = document.createElement('div');
          card.className = `bg-white rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition p-5 flex flex-col justify-between ${isApplied ? 'card-applied' : ''}`;

          card.innerHTML = `
            <div class="space-y-3">
              <div class="flex flex-wrap items-start justify-between gap-3">
                <div class="space-y-1">
                  <div class="flex items-center gap-2 flex-wrap">
                    <span class="w-6 h-6 rounded-full bg-slate-900 text-white text-xs font-bold flex items-center justify-center">#${job.rank || 1}</span>
                    <h2 class="text-base font-bold text-slate-900">${job.title || 'Untitled Role'}</h2>
                    <span class="px-2 py-0.5 rounded text-xs font-bold ${tierBadgeClass}">Tier ${tier}%</span>
                    ${isAiEnablement ? `<span class="px-2 py-0.5 rounded text-xs font-semibold badge-ai">🤖 AI Enablement</span>` : ''}
                    ${isApplied ? `<span class="bg-emerald-100 text-emerald-800 border border-emerald-300 text-xs font-bold px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Applied ${appliedDate}</span>` : ''}
                  </div>
                  <div class="text-sm text-slate-600 font-medium flex items-center gap-2 flex-wrap">
                    <span>🏢 ${job.employer || 'Employer'}</span>
                    ${job.department ? `<span class="text-slate-300">•</span><span class="text-xs text-slate-500">${job.department}</span>` : ''}
                  </div>
                </div>

                <div class="flex items-center gap-3">
                  <div class="text-right">
                    <div class="text-xs text-slate-400 font-medium">Interview Prob.</div>
                    <div class="text-sm font-bold text-blue-700">${job.interviewProb || 0}%</div>
                  </div>
                  <div class="px-2.5 py-1 rounded-lg text-xs font-bold ${tierBadgeClass}">
                    Match: ${job.matchScore || 0}%
                  </div>
                </div>
              </div>

              <!-- DATE STAMP & REPOST STATUS METADATA BAR -->
              <div class="flex flex-wrap items-center justify-between gap-2 text-xs bg-slate-50 border border-slate-200/90 rounded-lg px-3 py-2 text-slate-600">
                <div class="flex items-center gap-2 flex-wrap">
                  ${getSourceBadge(job.source, job.sourceLabel)}
                  <span class="text-slate-300">•</span>
                  <span class="inline-flex items-center gap-1" title="When the employer posted this role">
                    📅 <strong>Employer Posted:</strong> <span class="text-slate-800 font-semibold">${job.postedDate || 'Recent'}</span>
                  </span>
                  <span class="text-slate-300">•</span>
                  <span class="inline-flex items-center gap-1" title="Posting Freshness / Status">
                    ${job.isReposted ? 
                      `<span class="inline-flex items-center gap-1 text-amber-800 font-bold bg-amber-100 px-2 py-0.5 rounded border border-amber-300 text-[11px]">🔄 Reposted ${job.repostedDate ? '(' + job.repostedDate + ')' : ''}</span>` : 
                      `<span class="inline-flex items-center gap-1 text-emerald-800 font-bold bg-emerald-100 px-2 py-0.5 rounded border border-emerald-300 text-[11px]">✨ Original Posting</span>`
                    }
                  </span>
                </div>
                <div class="text-[11px] text-slate-500 font-mono flex items-center gap-1" title="When the automated agent executed the search and evaluated this job">
                  🕒 <strong>Agent Scanned:</strong> <span>${formatAgentTime(job.agentExecutedAt)}</span>
                </div>
              </div>

              <div class="flex flex-wrap gap-x-4 gap-y-1 text-xs text-slate-500 border-y border-slate-100 py-2.5">
                <div class="flex items-center gap-1">📍 <span>${job.location || 'Remote'}</span></div>
                <div class="flex items-center gap-1">💵 <span class="font-semibold text-slate-700">${job.salaryBand || 'Competitive'}</span></div>
                <div class="flex items-center gap-1">🎯 <span class="font-medium">${job.fitBand || 'Strong Fit'}</span></div>
              </div>

              <div class="text-xs text-slate-700 leading-relaxed">
                <strong>Why Matched:</strong> ${job.whyMatched || 'Direct technical skill and domain experience alignment.'}
              </div>

              <div class="space-y-1">
                <div class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Top Aligned Skills:</div>
                <div class="flex flex-wrap gap-1.5">
                  ${skillsArray.map(skill => `<span class="bg-slate-100 text-slate-700 px-2 py-0.5 rounded text-xs font-medium border border-slate-200">${skill}</span>`).join('')}
                </div>
              </div>

              <div class="bg-amber-50/70 border border-amber-200/60 rounded-lg p-2.5 text-xs text-amber-900 leading-relaxed">
                <strong>Strategic Value / Gap Bridge:</strong> ${job.gapBridge || 'Experienced background bridges cross-functional workflows.'}
              </div>
            </div>

            <div class="pt-4 mt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3">
              <div class="flex items-center gap-2 flex-wrap">
                ${job.directUrl ? `<a href="${job.directUrl}" target="_blank" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold px-3 py-1.5 rounded-lg border border-slate-300 transition flex items-center gap-1"><span>🔗</span> Direct Portal</a>` : ''}
                ${job.linkedinUrl ? `<a href="${job.linkedinUrl}" target="_blank" class="bg-blue-50 hover:bg-blue-100 text-blue-700 text-xs font-semibold px-3 py-1.5 rounded-lg border border-blue-200 transition flex items-center gap-1"><span>💼</span> LinkedIn Job</a>` : ''}
                ${job.searchLandingUrl ? `<a href="${job.searchLandingUrl}" target="_blank" class="bg-slate-50 hover:bg-slate-100 text-slate-500 text-xs px-2.5 py-1.5 rounded border border-slate-200 transition">Search Origin</a>` : ''}
              </div>

              <div class="flex items-center gap-2 ml-auto flex-wrap">
                ${!isDeleted ? `
                  <button onclick="runAgent(${job.id})" class="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-3.5 py-1.5 rounded-lg shadow-sm transition flex items-center gap-1.5">
                    <span>▶</span> Run Resume Agent
                  </button>
                  <button onclick="toggleApplied(${job.id})" class="${isApplied ? 'bg-emerald-600 text-white' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'} text-xs font-semibold px-3 py-1.5 rounded-lg border border-slate-300 transition">
                    ${isApplied ? '✓ Applied' : 'Mark as Applied'}
                  </button>
                  <button onclick="deleteJob(${job.id})" class="text-slate-400 hover:text-red-500 text-xs p-1.5 rounded hover:bg-slate-100 transition" title="Not Interested / Dismiss">
                    🗑️
                  </button>
                ` : `
                  <button onclick="restoreJob(${job.id})" class="bg-slate-800 hover:bg-slate-900 text-white text-xs font-semibold px-3 py-1.5 rounded-lg transition">
                    ↩ Restore Opportunity
                  </button>
                `}
              </div>
            </div>
          `;

          container.appendChild(card);
        } catch (cardErr) {
          console.error("Error creating job card", job.id, cardErr);
        }
      });
    }

    // Attach Search & Sort listeners
    document.getElementById('searchInput').addEventListener('input', (e) => {
      currentSearch = e.target.value.trim();
      renderJobs();
    });

    document.getElementById('sortSelect').addEventListener('change', (e) => {
      currentSort = e.target.value;
      renderJobs();
    });

    // Start App
    if (document.readyState === 'loading') {
      window.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  </script>
</body>
</html>"""

with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)
print(f"✓ Written {OUTPUT_INDEX}")

if ARTIFACT_INDEX.parent.exists():
    with open(ARTIFACT_INDEX, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"✓ Written {ARTIFACT_INDEX}")
