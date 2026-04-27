"""Recommender agent for ranked recommendations."""
from crewai import Agent
from crewai.llm import LLM
import os


def create_recommender_agent() -> Agent:
    """Create the Recommender agent for ranked recommendations."""
    
    # Initialize the LLM using CrewAI's LLM class
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    
    recommender = Agent(
        role="Recommender",
        goal="Aggregate scores and generate ranked candidate list",
        backstory=(
            "You are a career counselor helping candidates find ideal roles. "
            "You understand both employer needs and candidate aspirations, "
            "making you perfect for matching talent with the right opportunities. "
            "You provide clear, actionable recommendations with reasoning."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
    
    return recommender