# Architecture Implementation Plan

**Project:** AI Recruitment Assistant  
**Version:** 1.0  
**Date:** April 27, 2026  
**Owner:** @system.arch

---

## 1. Overview

This document outlines the implementation approach for the AI Recruitment Assistant system architecture. It provides a phased implementation plan with clear milestones, dependencies, and status tracking.

---

## 2. Implementation Phases

### Phase 1: Foundation (Week 1-2)

| Task | Description | Status |
|------|-------------|--------|
| **P1.1** | Set up FastAPI backend with basic endpoints | Not Started |
| **P1.2** | Configure Gemini API client | Not Started |
| **P1.3** | Create SQLite database schema | Not Started |
| **P1.4** | Implement basic health check endpoint | Not Started |

**Deliverables:**
- FastAPI application running on port 8000
- Database initialized with schema
- Health endpoint at `/api/health`

### Phase 2: CrewAI Integration (Week 2-3)

| Task | Description | Status |
|------|-------------|--------|
| **P2.1** | Define Researcher agent with mock data tool | Not Started |
| **P2.2** | Define Evaluator agent with scoring logic | Not Started |
| **P2.3** | Define Recommender agent with ranking | Not Started |
| **P2.4** | Create RecruitmentCrew with sequential process | Not Started |
| **P2.5** | Implement `/api/recruit` endpoint | Not Started |

**Deliverables:**
- Three configured CrewAI agents
- RecruitmentCrew orchestrating the pipeline
- API endpoint accepting job descriptions

### Phase 3: Frontend Setup (Week 3-4)

| Task | Description | Status |
|------|-------------|--------|
| **P3.1** | Initialize Next.js project with TypeScript | Not Started |
| **P3.2** | Install assistant-ui and shadcn/ui | Not Started |
| **P3.3** | Create chat interface component | Not Started |
| **P3.4** | Implement streaming API client | Not Started |
| **P3.5** | Build results display component | Not Started |

**Deliverables:**
- Next.js application on port 3000
- Functional chat interface
- Results display with candidate cards

### Phase 4: Integration (Week 4-5)

| Task | Description | Status |
|------|-------------|--------|
| **P4.1** | Connect frontend to backend API | Not Started |
| **P4.2** | Implement streaming response handling | Not Started |
| **P4.3** | Add error handling and loading states | Not Started |
| **P4.4** | Configure CORS and environment variables | Not Started |

**Deliverables:**
- Fully integrated frontend-backend
- Real-time streaming of agent outputs
- Proper error messages and loading UI

### Phase 5: Testing & Deployment (Week 5-6)

| Task | Description | Status |
|------|-------------|--------|
| **P5.1** | Write unit tests for agents | Not Started |
| **P5.2** | Write integration tests for API | Not Started |
| **P5.3** | Create Docker Compose configuration | Not Started |
| **P5.4** | Document setup and run instructions | Not Started |

**Deliverables:**
- Test suite with >80% coverage
- Docker Compose for local development
- README with setup instructions

---

## 3. Technical Dependencies

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Phase 1   │────▶│   Phase 2   │────▶│   Phase 3   │
│ Foundation  │     │ CrewAI      │     │ Frontend    │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Phase 5   │◀────│   Phase 4   │◀────│   Phase 4   │
│ Testing     │     │ Integration │     │ Integration │
└─────────────┘     └─────────────┘     └─────────────┘
```

### Dependency Details

| From | To | Dependency Type |
|------|----|-----------------|
| P1.1 | P2.1 | FastAPI must be running before agent definition |
| P2.4 | P3.4 | Crew must exist before frontend streaming |
| P3.3 | P4.2 | Chat component needed for streaming |
| P4.1 | P5.3 | Integration complete before Docker config |

---

## 4. File Structure

```
recruitment-assistant/
├── frontend/                    # Next.js application
│   ├── app/
│   │   ├── api/                # API routes (if needed)
│   │   ├── page.tsx           # Main chat page
│   │   └── layout.tsx         # Root layout
│   ├── components/
│   │   ├── chat-interface.tsx
│   │   └── candidate-card.tsx
│   ├── lib/
│   │   └── api.ts             # API client
│   └── package.json
│
├── backend/                    # FastAPI application
│   ├── agents/
│   │   ├── researcher.py      # Researcher agent
│   │   ├── evaluator.py       # Evaluator agent
│   │   └── recommender.py     # Recommender agent
│   ├── crew/
│   │   └── recruitment_crew.py
│   ├── api/
│   │   └── routes.py          # API endpoints
│   ├── models/
│   │   └── schemas.py         # Pydantic models
│   ├── db/
│   │   └── database.py        # SQLite setup
│   ├── main.py                # FastAPI app
│   └── requirements.txt
│
├── docker-compose.yml
├── .env
└── README.md
```

---

## 5. Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | Yes | Google Gemini API key for LLM |
| `DATABASE_URL` | No | SQLite path (default: recruitment.db) |
| `API_URL` | Frontend only | Backend URL (default: http://localhost:8000) |
| `NEXT_PUBLIC_API_URL` | Frontend only | Public-facing API URL |

---

## 6. Success Criteria

| Phase | Criterion | Validation Method |
|-------|-----------|-------------------|
| P1 | Backend responds on port 8000 | `curl http://localhost:8000/api/health` |
| P2 | `/api/recruit` returns ranked candidates | POST job description, receive JSON |
| P3 | Frontend loads at localhost:3000 | Browser access, no console errors |
| P4 | Full pipeline executes end-to-end | Submit job, receive candidate recommendations |
| P5 | `docker-compose up` works | All services start without errors |

---

## 7. Known Constraints

| Constraint | Impact | Mitigation |
|------------|--------|------------|
| No real job board APIs | Cannot source real candidates | Use mock candidate database |
| Gemini rate limits | May throttle during testing | Implement caching, queue requests |
| Single developer | Limited parallelization | Prioritize core flow first |
| Timeboxed (6 weeks) | May not complete all features | Focus on MVP only |

---

## 8. Next Steps

1. **Immediate:** @project.mgr to scaffold project structure
2. **Week 1:** @backend.eng to implement Phase 1 (Foundation)
3. **Week 2:** @backend.eng to implement Phase 2 (CrewAI)
4. **Week 3:** @frontend.eng to implement Phase 3 (Frontend)
5. **Week 4:** @integration.eng to implement Phase 4 (Integration)
6. **Week 5:** @qa.eng to implement Phase 5 (Testing)

---

**Document Version:** 1.0  
**Last Updated:** April 27, 2026  
**Author:** @system.arch