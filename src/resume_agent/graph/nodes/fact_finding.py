"""Node for interactive fact finding."""

import json
import re
from langgraph.types import interrupt
from resume_agent.graph.state import AgentState

def fact_finding_node(state: AgentState, llm_service=None) -> AgentState:
    """
    Checks for missing or partial skills.
    Generates clarifying questions, interrupts for user input,
    and updates the master resume with new facts.
    """
    current_job_index = state.get("current_job_index", 0)
    jobs = state.get("jobs", [])
    if not jobs or current_job_index >= len(jobs):
        return state
    
    current_job = jobs[current_job_index]
    analysis = current_job.analysis
    if not analysis:
        return state
        
    missing = analysis.missing_skills
    partial = analysis.partial_skills
    
    if not missing and not partial:
        state["fact_finding_completed"] = True
        return state
        
    if not state.get("fact_finding_completed", False):
        user_answers = state.get("user_fact_finding_answers")
        if user_answers:
            # We have answers, process them
            formatted_facts = "\n\n### Additional Fact-Finding Verified Skills:\n"
            for q, a in user_answers.items():
                formatted_facts += f"- Q: {q}\n  A: {a}\n"
            
            master_text = state.get("master_resume_text", "")
            state["master_resume_text"] = master_text + formatted_facts
            state["fact_finding_completed"] = True
            return state
            
        else:
            # We need to generate questions and interrupt
            questions = []
            if llm_service:
                prompt = f"""
                The candidate has missing or partial skills for {current_job.posting.company} - {current_job.posting.job_title}.
                Missing skills: {[s.skill for s in missing]}
                Partial skills: {[s.skill for s in partial]}
                
                Generate 3-5 concise interviewer-style follow-up questions for the highest-value gap skills to see if the candidate has any transferable or direct experience not mentioned.
                Return ONLY a JSON list of strings, e.g., ["Question 1?", "Question 2?"].
                """
                try:
                    response_text = llm_service.generate_text(prompt)
                    json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
                    if json_match:
                        questions = json.loads(json_match.group(0))
                except Exception:
                    pass
            
            if not questions:
                # Fallback questions
                skill_names = [s.skill for s in missing + partial][:3]
                questions = [f"Do you have any experience with {skill} that isn't on your resume?" for skill in skill_names]
                
            state["fact_finding_questions"] = questions
            
            # Pause execution and request user input
            interrupt_data = {
                "questions": questions,
                "job": current_job.posting.company
            }
            # Attempt to interrupt, if environment supports it
            try:
                interrupt(interrupt_data)
            except Exception as e:
                # If interrupt not supported in this run, just mark completed
                state["fact_finding_completed"] = True
                
    return state
