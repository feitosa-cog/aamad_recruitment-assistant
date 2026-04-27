"""Researcher agent for candidate sourcing."""
from crewai import Agent
from crewai.llm import LLM
import os


def create_researcher_agent() -> Agent:
    """Create the Researcher agent for candidate sourcing."""
    
    # Initialize the LLM using CrewAI's LLM class
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    
    researcher = Agent(
        role="Researcher",
        goal="Find qualified candidates matching job requirements",
        backstory=(
            "You are an expert recruiter with 10+ years of talent acquisition experience. "
            "You have successfully placed candidates in various industries including tech, "
            "finance, healthcare, and manufacturing. You know how to source candidates from "
            "multiple channels and identify the best talent for any role."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
    
    return researcher