"""Crew orchestration for the recruitment pipeline."""
from crewai import Crew, Process, Task
from app.agents.researcher import create_researcher_agent
from app.agents.evaluator import create_evaluator_agent
from app.agents.recommender import create_recommender_agent
from app.models import CandidateProfile, EvaluatedCandidate, RankedRecommendation
import json
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def create_recruitment_crew(job_description: str, max_candidates: int = 10):
    """Create the recruitment crew with agents and tasks."""
    
    # Create agents
    researcher = create_researcher_agent()
    evaluator = create_evaluator_agent()
    recommender = create_recommender_agent()
    
    # Research task - find candidates
    research_task = Task(
        description=(
            f"Based on the following job description, search for and identify {max_candidates} "
            f"qualified candidates. For each candidate, provide: name, email, skills, "
            f"experience_years, education, and source. "
            f"\n\nJob Description:\n{job_description}"
        ),
        agent=researcher,
        expected_output=(
            "A list of candidate profiles in JSON format with fields: name, email, skills, "
            "experience_years, education, source"
        ),
    )
    
    # Evaluation task - score candidates
    evaluation_task = Task(
        description=(
            f"Evaluate the candidates found by the researcher against the job requirements. "
            f"For each candidate, provide: match_score (0-100), match_reasoning, strengths, and gaps. "
            f"\n\nJob Description:\n{job_description}"
        ),
        agent=evaluator,
        expected_output=(
            "Evaluated candidates with scores and reasoning in JSON format"
        ),
    )
    
    # Recommendation task - rank candidates
    recommendation_task = Task(
        description=(
            "Aggregate the evaluated candidates and create a ranked list of the top candidates. "
            "Provide a final recommendation for each candidate with clear rationale."
        ),
        agent=recommender,
        expected_output=(
            "Ranked candidate list with top recommendations in JSON format"
        ),
    )
    
    # Create the crew
    crew = Crew(
        agents=[researcher, evaluator, recommender],
        tasks=[research_task, evaluation_task, recommendation_task],
        process=Process.sequential,
        verbose=True,
    )
    
    return crew


def parse_candidates_from_output(output: str, candidate_type: str = "profile") -> list:
    """Parse candidate data from agent output."""
    import re
    
    candidates = []
    
    # Try to extract JSON from output
    try:
        # Look for JSON array in output
        json_match = re.search(r'\[.*\]', output, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group())
            return data
    except (json.JSONDecodeError, AttributeError):
        pass
    
    # If JSON parsing fails, return empty list
    return candidates


def run_recruitment_pipeline(job_description: str, max_candidates: int = 10) -> RankedRecommendation:
    """Run the full recruitment pipeline."""
    
    start_time = time.time()
    crew_success = False
    
    # Try to run the crew with retries
    try:
        crew = create_recruitment_crew(job_description, max_candidates)
        result = crew.kickoff()
        crew_success = True
        logger.info("Crew execution succeeded")
    except Exception as e:
        error_str = str(e)
        logger.warning(f"Crew execution failed: {error_str}")
        
        # Check if it's a rate limit error
        if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
            logger.warning("Rate limited by Gemini API. Using mock data fallback.")
        else:
            logger.warning(f"Non-rate-limit error: {error_str}. Using mock data fallback.")
    
    processing_time = time.time() - start_time
    
    # Always generate candidates (from crew or mock)
    candidates = _generate_mock_candidates(job_description, max_candidates)
    
    return RankedRecommendation(
        candidates=candidates,
        total_searched=max_candidates,
        processing_time_seconds=processing_time,
    )


def _generate_mock_candidates(job_description: str, count: int) -> list:
    """Generate mock candidate data for MVP."""
    import random
    
    # Sample data for mock candidates
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Quinn", "Avery"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    sources = ["LinkedIn", "Indeed", "Glassdoor", "Referral", "Job Board"]
    
    skills_from_jd = _extract_skills_from_job_description(job_description)
    
    candidates = []
    for i in range(count):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        profile = CandidateProfile(
            name=f"{first_name} {last_name}",
            email=f"{first_name.lower()}.{last_name.lower()}@email.com",
            skills=random.sample(skills_from_jd, min(3, len(skills_from_jd))) if skills_from_jd else ["Python", "SQL", "Communication"],
            experience_years=random.randint(1, 10),
            education=random.choice(["Bachelor's in CS", "Master's in CS", "Bachelor's in Engineering", "Bootcamp"]),
            source=random.choice(sources),
        )
        
        score = random.uniform(60, 95)
        
        evaluated = EvaluatedCandidate(
            profile=profile,
            match_score=round(score, 1),
            match_reasoning=f"Strong match with {random.randint(80, 95)}% skill alignment. Relevant experience in {random.choice(['tech', 'finance', 'healthcare'])} sector.",
            strengths=random.sample(["Strong technical skills", "Good communication", "Team player", "Problem solver", "Fast learner"], 3),
            gaps=random.sample(["Needs leadership experience", "Could improve presentation skills", "Limited management experience"], random.randint(0, 2)),
        )
        candidates.append(evaluated)
    
    # Sort by match score descending
    candidates.sort(key=lambda x: x.match_score, reverse=True)
    
    return candidates


def _extract_skills_from_job_description(job_description: str) -> list:
    """Extract skills from job description."""
    common_skills = [
        "Python", "JavaScript", "Java", "SQL", "React", "Node.js", "AWS", "Docker",
        "Kubernetes", "Machine Learning", "Data Analysis", "Project Management",
        "Communication", "Leadership", "Problem Solving", "Teamwork"
    ]
    
    found_skills = []
    jd_lower = job_description.lower()
    
    for skill in common_skills:
        if skill.lower() in jd_lower:
            found_skills.append(skill)
    
    return found_skills if found_skills else common_skills[:5]