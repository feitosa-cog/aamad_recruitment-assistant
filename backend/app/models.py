"""Data models for the recruitment assistant."""
from typing import List, Optional
from pydantic import BaseModel, Field


class CandidateProfile(BaseModel):
    """Candidate profile information."""
    name: str = Field(..., description="Candidate's full name")
    email: str = Field(..., description="Candidate's email address")
    skills: List[str] = Field(default_factory=list, description="List of candidate skills")
    experience_years: int = Field(..., description="Years of professional experience")
    education: str = Field(..., description="Highest education level")
    source: str = Field(..., description="Source of candidate (e.g., LinkedIn, Indeed)")


class EvaluatedCandidate(BaseModel):
    """Candidate with evaluation scores and reasoning."""
    profile: CandidateProfile
    match_score: float = Field(..., ge=0, le=100, description="Match score from 0-100")
    match_reasoning: str = Field(..., description="Explanation of why candidate matches")
    strengths: List[str] = Field(default_factory=list, description="Candidate's strengths")
    gaps: List[str] = Field(default_factory=list, description="Skill or experience gaps")


class RankedRecommendation(BaseModel):
    """Ranked list of candidate recommendations."""
    candidates: List[EvaluatedCandidate] = Field(..., description="Ranked list of candidates")
    total_searched: int = Field(..., description="Total candidates searched")
    processing_time_seconds: float = Field(..., description="Time taken to process")


class RecruitmentRequest(BaseModel):
    """Request model for starting recruitment pipeline."""
    job_description: str = Field(..., description="Job description text")
    max_candidates: int = Field(10, ge=1, le=50, description="Maximum candidates to return")


class RecruitmentResponse(BaseModel):
    """Response model for recruitment pipeline."""
    job_description: str
    recommendations: RankedRecommendation
    status: str = "completed"