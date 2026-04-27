# Backend Implementation Plan

**Project:** AI Recruitment Assistant  
**Version:** 1.0  
**Date:** April 27, 2026  
**Owner:** @backend.eng

---

## 1. Overview

This document outlines the backend implementation for the AI Recruitment Assistant using CrewAI. The backend will orchestrate a multi-agent crew to source, evaluate, and recommend candidates based on job descriptions.

---

## 2. Application Crew Implementation

### 2.1 Crew Structure

```
RecruitmentCrew (Sequential Process)
├── Researcher Agent     → Outputs: List[CandidateProfile]
├── Evaluator Agent      → Outputs: List[EvaluatedCandidate]
└── Recommender Agent    → Outputs: RankedRecommendation
```

### 2.2 Agent Definitions

#### Researcher Agent
- **Role:** Search and source candidates from multiple channels
- **Goal:** Find qualified candidates matching job requirements
- **Backstory:** Expert recruiter with 10+ years of talent acquisition experience
- **Tools:** Web search, candidate database query
- **Output:** List of candidate profiles with source attribution

#### Evaluator Agent
- **Role:** Evaluate candidates against job criteria
- **Goal:** Score resumes against job requirements (0-100)
- **Backstory:** Senior hiring manager with technical screening expertise
- **Tools:** Resume parsing, skill matching, experience analysis
- **Output:** Evaluated candidates with scores and match reasoning

#### Recommender Agent
- **Role:** Provide ranked recommendations
- **Goal:** Aggregate scores and generate ranked candidate list
- **Backstory:** Career counselor helping candidates find ideal roles
- **Tools:** Score aggregation, ranking algorithm
- **Output:** Ranked candidate list with top 5 recommendations

---

## 3. API Endpoints

| Endpoint | Method | Purpose | Status |
|----------|--------|---------|--------|
| `/api/recruit` | POST | Start recruitment pipeline | Pending |
| `/api/health` | GET | Health check | Pending |
| `/api/candidates` | GET | List cached candidates | Pending |

---

## 4. Business Logic Components

### 4.1 Core Components

| Component | Description | Priority |
|-----------|-------------|----------|
| `crew.py` | CrewAI crew definition and orchestration | P0 |
| `agents/researcher.py` | Researcher agent implementation | P0 |
| `agents/evaluator.py` | Evaluator agent implementation | P0 |
| `agents/recommender.py` | Recommender agent implementation | P0 |
| `models.py` | Pydantic data models | P0 |
| `main.py` | FastAPI application and endpoints | P0 |
| `tools/` | Custom tools for agents | P1 |

### 4.2 Data Models

```python
class RecruitmentRequest(BaseModel):
    job_description: str
    max_candidates: int = 10

class CandidateProfile(BaseModel):
    name: str
    email: str
    skills: List[str]
    experience_years: int
    education: str
    source: str

class EvaluatedCandidate(BaseModel):
    profile: CandidateProfile
    match_score: float  # 0-100
    match_reasoning: str
    strengths: List[str]
    gaps: List[str]

class RankedRecommendation(BaseModel):
    candidates: List[EvaluatedCandidate]
    total_searched: int
    processing_time_seconds: float
```

---

## 5. Implementation Approach

### 5.1 Phase 1: Project Setup
- [ ] Create backend directory structure
- [ ] Set up Python virtual environment
- [ ] Install dependencies (crewai, fastapi, uvicorn, pydantic)
- [ ] Configure environment variables

### 5.2 Phase 2: Data Models
- [ ] Create `models.py` with Pydantic models
- [ ] Define request/response schemas

### 5.3 Phase 3: Agent Implementation
- [ ] Implement Researcher agent
- [ ] Implement Evaluator agent
- [ ] Implement Recommender agent
- [ ] Create RecruitmentCrew

### 5.4 Phase 4: API Implementation
- [ ] Set up FastAPI application
- [ ] Implement `/api/recruit` endpoint
- [ ] Implement `/api/health` endpoint
- [ ] Implement `/api/candidates` endpoint

### 5.5 Phase 5: Integration
- [ ] Connect frontend to backend
- [ ] Test full pipeline
- [ ] Document backend architecture

---

## 6. Status Tracking

| Task | Status | Notes |
|------|--------|-------|
| Create backend directory | ✅ Completed | Created backend/ directory |
| Set up Python environment | ⏳ Pending | Requires virtual environment setup |
| Install dependencies | ⏳ Pending | Run pip install -r requirements.txt |
| Create data models | ✅ Completed | app/models.py |
| Implement agents | ✅ Completed | researcher.py, evaluator.py, recommender.py |
| Implement API endpoints | ✅ Completed | main.py with FastAPI |
| Test integration | ⏳ Pending | Requires running the server |

---

## 7. Known Gaps (Non-MVP)

- Real job board integration (LinkedIn, Indeed)
- Persistent database (using in-memory for MVP)
- Streaming responses
- Authentication/authorization
- Candidate storage and retrieval