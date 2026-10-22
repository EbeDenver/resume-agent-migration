"""Phase 2 verification test suite for tool implementations and pipeline nodes."""
import sys
sys.path.insert(0, 'src')

from resume_agent.graph.state import AgentState
from resume_agent.graph.nodes.load_context import load_context_node
from resume_agent.graph.nodes.resolve_jobs import resolve_jobs_node
from resume_agent.graph.nodes.analyze_job import analyze_job_node
from resume_agent.graph.nodes.generate_docs import generate_docs_node
from resume_agent.graph.nodes.update_tracker import update_tracker_node
from resume_agent.graph.nodes.format_response import format_response_node

from resume_agent.tools.firecrawl_scraper import FirecrawlJobScraper
from resume_agent.tools.llm_client import GeminiLLMService
from resume_agent.tools.google_docs import GoogleDocsServiceImpl
from resume_agent.tools.google_sheets import GoogleSheetsServiceImpl
from resume_agent.models.job import JobRun, JobPosting, JobAnalysis, SkillMatch
from resume_agent.models.formatting import COLORS

def test_phase2_tools_and_nodes():
    # 1. Initialize State
    state: AgentState = {
        "config": {
            "google": {
                "account_email": "ebeDenver@gmail.com",
                "tracker_tab": "Tracker"
            },
            "timezone": "America/Denver"
        },
        "master_resume_text": "",
        "resume_instructions": "",
        "cover_letter_instructions": "",
        "raw_jobs_input": ["https://example.com/job/ai-strategist"],
        "jobs": [],
        "current_job_index": 0,
        "completed_jobs": [],
        "failed_jobs": [],
        "final_summary": "",
        "mode": "normal"
    }

    # 2. Test load_context_node
    docs_service = GoogleDocsServiceImpl(credentials=None)
    state = load_context_node(state, docs_service=docs_service)
    assert len(state["master_resume_text"]) > 0

    # 3. Test resolve_jobs_node
    scraper_service = FirecrawlJobScraper(api_key=None)
    state = resolve_jobs_node(state, scraper_service=scraper_service)
    assert len(state["jobs"]) == 1
    assert state["jobs"][0].posting.company != ""

    # 4. Test analyze_job_node
    llm_service = GeminiLLMService(api_key=None)
    state = analyze_job_node(state, llm_service=llm_service)
    job = state["jobs"][0]
    assert job.analysis is not None
    assert 0 <= job.analysis.match_score <= 100
    assert job.analysis.fit_band in ["strong", "solid", "partial", "weak", "poor"]

    # 5. Test generate_docs_node with #17365D Canonical Navy validation
    state = generate_docs_node(state, llm_service=llm_service, docs_service=docs_service)
    assert job.documents.analysis_doc_url is not None
    assert job.documents.resume_doc_url is not None
    assert job.documents.cover_letter_doc_url is not None
    assert COLORS.NAVY == "#17365D"

    # 6. Test update_tracker_node
    sheets_service = GoogleSheetsServiceImpl(credentials=None)
    state = update_tracker_node(state, sheets_service=sheets_service)
    assert job.status in ["completed", "partial", "error"]

    # 7. Test format_response_node
    state = format_response_node(state)
    assert "Job Application Processing Summary" in state["final_summary"]
    assert job.posting.company in state["final_summary"]

    print("SUCCESS: Phase 2 end-to-end pipeline nodes verification passed!")

if __name__ == "__main__":
    test_phase2_tools_and_nodes()
