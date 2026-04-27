"""Evaluator agent for candidate assessment."""
from crewai import Agent
from crewai.llm import LLM
import os


def create_evaluator_agent() -> Agent:
    """Create the Evaluator agent for candidate assessment."""
    
    # Initialize the LLM using CrewAI's LLM class
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    
    evaluator = Agent(
        role="Evaluator",
        goal="Score resumes against job requirements (0-100)",
        backstory=(
            "You are a senior hiring manager with technical screening expertise. "
            "You have screened thousands of candidates and can quickly identify the "
            "best matches for any position. You provide objective, data-driven evaluations "
            "that help hiring managers make informed decisions."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
    
    return evaluator