# System Architecture Document (SAD)

**Project:** AI Recruitment Assistant  
**Version:** 1.0  
**Date:** April 27, 2026  
**Owner:** @system.arch  
**Adapter:** crewai

---

## 1. Executive Summary

The AI Recruitment Assistant is a multi-agent system built on CrewAI that automates candidate sourcing, evaluation, and recommendation for small businesses. The architecture follows a sequential agent pipeline where a Researcher agent discovers candidates, an Evaluator agent scores them against job requirements, and a Recommender agent produces ranked outputs.

### 1.1 Architecture Overview

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Next.js + assistant-ui | Chat interface for job input and results |
| **Backend** | FastAPI (Python) | CrewAI orchestration and API layer |
| **Agents** | CrewAI | Researcher, Evaluator, Recommender crew |
| **LLM** | Gemini API | Power all agent reasoning |

### 1.2 Core Value Delivery

> "Reduce time-to-hire by 80% with AI agents that source, evaluate, and recommend qualified candidates — without the enterprise price tag."

---

## 2. Stakeholders & Concerns

| Stakeholder | Primary Concern | Architecture Response |
|-------------|-----------------|----------------------|
| **Recruiter** | Quick candidate sourcing, accurate screening | Sequential agent pipeline delivers results in minutes |
| **Hiring Manager** | Ranked recommendations with clear rationale | Recommender agent provides scored, justified output |
| **Backend Engineer** | Clean CrewAI implementation | Modular agent definitions with clear tool interfaces |
| **Integration Engineer** | API-First design for frontend-backend | FastAPI exposes REST endpoints with streaming support |

---

## 3. Quality Attributes

| Attribute | Target | Implementation |
|-----------|--------|-----------------|
| **Response Time** | < 5 min for full pipeline | Async agent execution, streaming responses |
| **Match Accuracy** | ≥ 85% | Gemini-powered evaluation with structured scoring |
| **Availability** | 99.5% | Stateless backend, health check endpoints |
| **Scalability** | 10 concurrent users (MVP) | Horizontal-ready FastAPI, containerized deployment |

---

## 4. Architectural Decisions

| Decision | Rationale | Trade-off |
|----------|-----------|-----------|
| **CrewAI Sequential Process** | Ensures proper data flow: Research → Evaluate → Rank | Less parallelization, but simpler debugging |
| **FastAPI over Flask** | Native async support, better OpenAPI docs, type safety | Slightly larger footprint |
| **Next.js + assistant-ui** | Production-grade chat, streaming support | Requires React expertise |
| **Gemini API** | Cost-effective, strong reasoning capabilities | Rate limits, dependency on external API |
| **SQLite for MVP** | Zero-config, file-based, easy backup | Not suitable for high concurrency |

---

## 5. Logical View

### 5.1 Component Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend (Next.js)                       │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │  Chat Interface │    │  Results Display │    │  Dashboard  │ │
│  │  (assistant-ui)  │    │  (Candidate List) │    │  (Metrics)  │ │
│  └────────┬────────┘    └────────┬────────┘    └──────┬───────┘ │
└───────────┼──────────────────────┼───────────────────┼─────────┘
            │                      │                    │
            ▼                      ▼                    ▼
┌───────────────────────────────────────────────────────────────────┐
│                      Backend API (FastAPI)                        │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────────────┐  │
│  │  /search     │    │  /evaluate   │    │  /recommend        │  │
│  │  Endpoint    │    │  Endpoint    │    │  Endpoint          │  │
│  └──────┬───────┘    └──────┬───────┘    └─────────┬──────────┘  │
└─────────┼────────────────────┼─────────────────────┼─────────────┘
          │                    │                      │
          ▼                    ▼                      ▼
┌───────────────────────────────────────────────────────────────────┐
│                    CrewAI Orchestration Layer                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    RecruitmentCrew                          │  │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │  │
│  │  │  Researcher │───▶│  Evaluator  │───▶│  Recommender │     │  │
│  │  │   Agent     │    │   Agent     │    │   Agent      │     │  │
│  │  └─────────────┘    └─────────────┘    └─────────────┘     │  │
│  └─────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────────────────────────────────────┐
│                      External Services                             │
│  ┌─────────────────┐    ┌─────────────────────────────────────┐  │
│  │  Gemini API     │    │  Job Boards / Data Sources          │  │
│  │  (LLM Backend)  │    │  (Simulated for MVP)               │  │
│  └─────────────────┘    └─────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────┘
```

### 5.2 Agent Definitions

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

## 6. Process / Runtime View

### 6.1 User Interaction Flow

```
User Input (Job Description)
         │
         ▼
┌─────────────────────────────────────┐
│   Frontend (assistant-ui chat)      │
│   - Parse job description            │
│   - Send to /api/recruit endpoint   │
└─────────────────────────────────────┘
         │
         ▼ (HTTP POST with streaming)
┌─────────────────────────────────────┐
│   FastAPI Backend                   │
│   - Validate request                │
│   - Initialize RecruitmentCrew      │
└─────────────────────────────────────┘
         │
         ▼ (async agent.kickoff())
┌─────────────────────────────────────┐
│   CrewAI Execution                  │
│   1. Researcher searches candidates │
│   2. Evaluator scores each candidate │
│   3. Recommender ranks results       │
└─────────────────────────────────────┘
         │
         ▼ (streaming response)
┌─────────────────────────────────────┐
│   Frontend Display                  │
│   - Stream agent messages            │
│   - Display ranked results          │
└─────────────────────────────────────┘
         │
         ▼
User Output (Candidate Report)
```

### 6.2 API Endpoints

| Endpoint | Method | Purpose | Request Body |
|----------|--------|---------|---------------|
| `/api/recruit` | POST | Start recruitment pipeline | `{ job_description: string }` |
| `/api/health` | GET | Health check | N/A |
| `/api/candidates` | GET | List cached candidates | `{ job_id?: string }` |

### 6.3 Data Models

```python
# Request/Response Models
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

## 7. Deployment View

### 7.1 Development Environment

```
┌─────────────────────────────────────┐
│         Development Setup           │
│  ┌─────────────┐    ┌────────────┐ │
│  │  Next.js    │    │  FastAPI   │ │
│  │  Dev Server │    │  Uvicorn   │ │
│  │  :3000      │    │  :8000     │ │
│  └─────────────┘    └────────────┘ │
└─────────────────────────────────────┘
```

### 7.2 MVP Deployment (Local)

| Service | Port | Technology |
|---------|------|------------|
| Frontend | 3000 | Next.js 14+ |
| Backend | 8000 | FastAPI + Uvicorn |
| Database | N/A | SQLite (file-based) |

### 7.3 Container Configuration

```yaml
# docker-compose.yml (MVP)
services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://backend:8000

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - DATABASE_URL=sqlite:///recruitment.db
```

---

## 8. Data View

### 8.1 Database Schema (SQLite)

```sql
-- Candidates table
CREATE TABLE candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    skills TEXT,  -- JSON array
    experience_years INTEGER,
    education TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Jobs table
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    requirements TEXT,  -- JSON array
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Evaluations table
CREATE TABLE evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER REFERENCES candidates(id),
    job_id INTEGER REFERENCES jobs(id),
    match_score REAL,
    match_reasoning TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 8.2 Data Flow

| Stage | Data | Storage |
|-------|------|---------|
| Input | Job description | In-memory, not persisted |
| Research | Candidate profiles | SQLite (candidates table) |
| Evaluation | Scored candidates | SQLite (evaluations table) |
| Output | Ranked recommendations | JSON response |

---

## 9. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Gemini API rate limits** | High | Implement request queuing, caching |
| **Agent hallucination** | Medium | Validate outputs against job criteria |
| **No real candidate data** | High | Create mock candidate database for MVP |
| **Streaming latency** | Medium | Optimize agent verbose logging |
| **Frontend-backend integration** | Medium | Use shared TypeScript types |

---

## 10. Traceability Matrix

| SAD Section | PRD Reference |
|-------------|----------------|
| §5.1 Researcher Agent | PRD §5.1 |
| §5.2 Evaluator Agent | PRD §5.2 |
| §5.3 Recommender Agent | PRD §5.3 |
| §6.2 API Endpoints | PRD §4 (Core Features) |
| §8.1 Database Schema | PRD §6 (Out of Scope - deferring full ATS) |

---

## 11. Future Work (Out of Scope for MVP)

| Feature | Reason | Phase |
|---------|--------|-------|
| Full ATS Integration | Requires API partnerships | Phase 2+ |
| Candidate Communication | Regulatory complexity | Phase 2+ |
| Advanced Analytics | Defer for validation | Phase 2+ |
| Multi-language Support | English-only for v1 | Phase 2+ |
| Video Interview Platform | Out of scope | Future |

---

## 12. Acceptance Criteria

- [ ] Frontend chat interface loads and accepts job descriptions
- [ ] Backend exposes `/api/recruit` endpoint that triggers Crew pipeline
- [ ] Researcher agent produces candidate list from mock data
- [ ] Evaluator agent scores candidates 0-100 with reasoning
- [ ] Recommender agent ranks candidates and returns top 5
- [ ] Streaming responses display in frontend in real-time
- [ ] Health check endpoint returns 200 OK
- [ ] SQLite database stores candidate and evaluation data
- [ ] Docker Compose orchestrates frontend + backend services

---

**Document Version:** 1.0  
**Last Updated:** April 27, 2026  
**Author:** @system.arch