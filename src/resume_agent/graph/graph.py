"""
Main graph orchestration for the Resume Agent.
"""

from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from resume_agent.state import AgentState
from resume_agent.nodes.load_context import load_context_node
from resume_agent.nodes.resolve_jobs import resolve_jobs_node
from resume_agent.nodes.gap_analysis import gap_analysis_node
from resume_agent.nodes.fact_finding import fact_finding_node
from resume_agent.nodes.generate_docs import generate_docs_node
from resume_agent.nodes.interview_prep import interview_prep_node
from resume_agent.nodes.update_tracker import update_tracker_node
from resume_agent.nodes.format_response import format_response_node


def should_do_fact_finding(state: AgentState) -> Literal["fact_finding", "generate_docs"]:
    """
    Determine whether to perform fact finding for the current job.
    """
    job_index = state.get("current_job_index", 0)
    jobs = state.get("jobs", [])
    
    if job_index >= len(jobs):
        return "generate_docs"
        
    job = jobs[job_index]
    missing_skills = job.get("missing_skills", [])
    partial_skills = job.get("partial_skills", [])
    
    needs_fact_finding = len(missing_skills) > 0 or len(partial_skills) > 0
    fact_finding_completed = job.get("fact_finding_completed", False)
    mode = state.get("mode", "generate_docs")
    
    if needs_fact_finding and not fact_finding_completed and mode == "fact_finding":
        return "fact_finding"
        
    return "generate_docs"


def has_more_jobs(state: AgentState) -> Literal["gap_analysis", "format_response"]:
    """
    Determine if there are more jobs to process.
    Note: current_job_index should be incremented by update_tracker_node prior to this.
    """
    job_index = state.get("current_job_index", 0)
    jobs = state.get("jobs", [])
    
    if job_index < len(jobs):
        return "gap_analysis"
    return "format_response"


def build_agent_graph(checkpointer=None):
    """
    Build and compile the LangGraph for the Resume Agent.
    """
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("load_context", load_context_node)
    workflow.add_node("resolve_jobs", resolve_jobs_node)
    workflow.add_node("gap_analysis", gap_analysis_node)
    workflow.add_node("fact_finding", fact_finding_node)
    workflow.add_node("generate_docs", generate_docs_node)
    workflow.add_node("interview_prep", interview_prep_node)
    workflow.add_node("update_tracker", update_tracker_node)
    workflow.add_node("format_response", format_response_node)
    
    # Add edges
    workflow.add_edge(START, "load_context")
    workflow.add_edge("load_context", "resolve_jobs")
    workflow.add_edge("resolve_jobs", "gap_analysis")
    
    workflow.add_conditional_edges(
        "gap_analysis",
        should_do_fact_finding,
        {
            "fact_finding": "fact_finding",
            "generate_docs": "generate_docs"
        }
    )
    
    workflow.add_edge("fact_finding", "generate_docs")
    workflow.add_edge("generate_docs", "interview_prep")
    workflow.add_edge("interview_prep", "update_tracker")
    
    workflow.add_conditional_edges(
        "update_tracker",
        has_more_jobs,
        {
            "gap_analysis": "gap_analysis",
            "format_response": "format_response"
        }
    )
    
    workflow.add_edge("format_response", END)
    
    if checkpointer is None:
        checkpointer = MemorySaver()
        
    return workflow.compile(checkpointer=checkpointer)


def run_pipeline(raw_jobs_input, config_path=None, thread_id="default", interrupt_before=None):
    """
    Helper function to run the pipeline.
    """
    graph = build_agent_graph()
    
    config = {"configurable": {"thread_id": thread_id}}
    
    initial_state = {
        "raw_jobs_input": raw_jobs_input,
        "config_path": config_path,
        "mode": "generate_docs",
        "jobs": [],
        "current_job_index": 0
    }
    
    if interrupt_before:
        return graph.invoke(initial_state, config=config, interrupt_before=interrupt_before)
    
    return graph.invoke(initial_state, config=config)
