"""FastAPI application for the recruitment assistant."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
import time
from dotenv import load_dotenv

from app.models import (
    RecruitmentRequest,
    RecruitmentResponse,
    RankedRecommendation,
    CandidateProfile,
    EvaluatedCandidate,
)
from app.crew import run_recruitment_pipeline

# Load environment variables
load_dotenv()

# Store for cached candidates (MVP - in-memory storage)
candidate_cache = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Startup
    print("Starting AI Recruitment Assistant Backend...")
    print(f"Gemini API Key configured: {bool(os.getenv('GEMINI_API_KEY'))}")
    yield
    # Shutdown
    print("Shutting down AI Recruitment Assistant Backend...")


# Create FastAPI app
app = FastAPI(
    title="AI Recruitment Assistant",
    description="Multi-agent recruitment system using CrewAI",
    version="1.0.0",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "AI Recruitment Assistant",
        "version": "1.0.0",
    }


@app.post("/api/recruit")
async def recruit_candidates(request: RecruitmentRequest):
    """
    Start the recruitment pipeline.
    
    Takes a job description and returns ranked candidate recommendations.
    """
    try:
        start_time = time.time()
        
        # Run the recruitment pipeline
        recommendations = run_recruitment_pipeline(
            job_description=request.job_description,
            max_candidates=request.max_candidates,
        )
        
        processing_time = time.time() - start_time
        
        # Cache the results
        job_id = f"job_{int(processing_time * 1000)}"
        candidate_cache[job_id] = {
            "job_description": request.job_description,
            "recommendations": recommendations,
            "timestamp": time.time(),
        }
        
        # Return format matching frontend expectations
        return {
            "candidates": recommendations.candidates,
            "total_searched": recommendations.total_searched,
            "processing_time_seconds": processing_time,
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error running recruitment pipeline: {str(e)}",
        )


@app.get("/api/candidates")
async def list_candidates(job_id: str = None):
    """
    List cached candidates.
    
    If job_id is provided, return candidates for that job.
    Otherwise, return all cached jobs.
    """
    if job_id:
        if job_id in candidate_cache:
            return candidate_cache[job_id]
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Job {job_id} not found",
            )
    else:
        # Return all cached jobs
        return {
            "jobs": [
                {
                    "job_id": job_id,
                    "job_description": data["job_description"],
                    "timestamp": data["timestamp"],
                    "candidate_count": len(data["recommendations"].candidates),
                }
                for job_id, data in candidate_cache.items()
            ]
        }


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "8000"))
    debug = os.getenv("DEBUG", "true").lower() == "true"
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug,
    )