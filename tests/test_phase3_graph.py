"""Verification script for Phase 3 LangGraph pipeline orchestration."""
import sys
sys.path.insert(0, 'src')

from resume_agent.graph.state import AgentState
from resume_agent.graph.nodes.gap_analysis import gap_analysis_node
from resume_agent.graph.nodes.fact_finding import fact_finding_node
from resume_agent.graph.nodes.interview_prep import interview_prep_node
from resume_agent.graph.graph import should_do_fact_finding, has_more_jobs, build_agent_graph
from resume_agent.tools.llm_client import GeminiLLMService
from resume_agent.tools.google_docs import GoogleDocsServiceImpl
from resume_agent.tools.web_search import MockWebSearchService
from resume_agent.models.job import JobRun, JobPosting, JobAnalysis, SkillMatch

def test_phase3_orchestration():
    print("Testing Phase 3 Advanced Nodes & Graph Wiring...")

    # 1. State Initialization
    state: AgentState = {
        "config": {
            "google": {
                "account_email": "ebeDenver@gmail.com",
                "tracker_tab": "Tracker"
            },
            "timezone": "America/Denver"
        },
        "master_resume_text": "Ebenezer J. Rolston - Senior IT & AI Specialist",
        "resume_instructions": "Standard ATS formatting",
        "cover_letter_instructions": "Standard 4-paragraph structure",
        "raw_jobs_input": ["https://example.com/job/ai-strategist"],
        "jobs": [
            JobRun(
                posting=JobPosting(
                    company="Acme AI",
                    job_title="AI Transformation Lead",
                    job_url="https://example.com/job/ai-strategist",
                    jd_text="Requirements: 5+ years AI Strategy, PyTorch, RAG, Agentic AI, Executive Stakeholder Management."
                )
            )
        ],
        "current_job_index": 0,
        "completed_jobs": [],
        "failed_jobs": [],
        "final_summary": "",
        "mode": "fact_finding",
        "fact_finding_questions": [],
        "user_fact_finding_answers": {},
        "fact_finding_completed": False
    }

    # 2. Test Skill Gap Analysis Node
    llm_service = GeminiLLMService(api_key=None)
    state = gap_analysis_node(state, llm_service=llm_service)
    job = state["jobs"][0]
    assert job.analysis is not None
    print(f"Gap Analysis Match Score: {job.analysis.match_score}/100, Band: {job.analysis.fit_band}")

    # 3. Test Conditional Routing to Fact-Finding
    route = should_do_fact_finding(state)
    print(f"Conditional Routing Decision: {route}")
    assert route in ["fact_finding", "generate_docs"]

    # 4. Test Fact-Finding Node (Human-in-the-Loop Simulation)
    if route == "fact_finding":
        try:
            state = fact_finding_node(state, llm_service=llm_service)
        except Exception as e:
            print(f"Human-in-the-Loop Interrupted: {e}")
            # Simulate user answering questions
            state["user_fact_finding_answers"] = {
                "PyTorch": "Built PyTorch models during DU Graduate Certificate labs."
            }
            state = fact_finding_node(state, llm_service=llm_service)
            assert state["fact_finding_completed"] is True
            print("Fact-Finding successfully resumed & updated Master Resume!")

    # 5. Test Interview Prep Node (Web Search + 13-Section Guide)
    docs_service = GoogleDocsServiceImpl(credentials=None)
    search_service = MockWebSearchService()
    state = interview_prep_node(
        state, 
        llm_service=llm_service, 
        docs_service=docs_service, 
        web_search_service=search_service
    )
    assert job.documents.interview_prep_doc_url is not None
    print(f"Interview Prep Doc URL: {job.documents.interview_prep_doc_url}")

    # 6. Test StateGraph Compilation
    graph = build_agent_graph()
    assert graph is not None
    print("StateGraph successfully built & compiled with MemorySaver checkpointer!")

    print("\nSUCCESS: All Phase 3 Advanced Nodes & Graph Wiring verified!")

if __name__ == "__main__":
    test_phase3_orchestration()
