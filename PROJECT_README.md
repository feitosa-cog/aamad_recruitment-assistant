# AI Recruitment Assistant

A multi-agent AI system that automates candidate sourcing, evaluation, and recommendation for small businesses. Built using the AAMAD framework with CrewAI.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Value Proposition](#value-proposition)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Next Steps](#next-steps-for-contributors)

---

## Project Overview

The **AI Recruitment Assistant** is a multi-agent system that automates the end-to-end recruitment process — from candidate sourcing to evaluation and recommendation.

### What It Does

1. **Parses job descriptions** into structured requirements
2. **Searches and sources candidates** using AI agents
3. **Evaluates resumes** against job criteria with match scoring
4. **Provides ranked recommendations** with clear rationale

### Target Users

| Persona | Description |
|---------|-------------|
| **Recruiters** | Solo or small team recruiters who need to find and evaluate candidates quickly |
| **Hiring Managers** | Department leads who need ranked, qualified candidate recommendations |

### Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | React + TypeScript |
| Backend | Python (FastAPI) |
| AI/ML | Google Gemini API |
| Multi-Agent Framework | CrewAI |
| Database | PostgreSQL |

---

## Problem Statement

Manual candidate sourcing and evaluation is highly inefficient for small businesses:

| Issue | Impact |
|-------|--------|
| **Time-Consuming Sourcing** | Recruiters spend 60-70% of time on manual sourcing tasks |
| **Inconsistent Evaluation** | Human bias leads to inconsistent candidate assessments |
| **High Volume Handling** | Unable to scale during peak hiring periods |
| **Poor Candidate Matching** | Missed qualified candidates due to manual screening limits |
| **Delayed Response Times** | Slow feedback loops cause top candidates to accept competing offers |

---

## Value Proposition

> **"Reduce time-to-hire by 80% with AI agents that source, evaluate, and recommend qualified candidates — without the enterprise price tag."**

### Success Metrics

| Metric | Target |
|--------|--------|
| Time to Source Candidates | < 1 hour (vs 15-20 hrs manual) |
| Candidate Match Accuracy | ≥ 85% |
| Recruiter Satisfaction | ≥ 4.5/5 |
| Resume Screening Speed | < 5 min per 100 resumes |

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Candidate Search** | AI agents search and source candidates based on job requirements |
| **Automated Evaluation** | Resume screening against job criteria with match scoring (0-100) |
| **Ranked Recommendations** | Sorted candidate list with match scores and rationale |
| **Job Description Parsing** | Natural language processing of job requirements |
| **Source Attribution** | Track and display candidate source channels |

### Out of Scope (v1)

- Full ATS integration
- Candidate communication automation
- Advanced analytics and reporting
- Job posting system integration
- Video interview platform
- Multi-language support

---

## Architecture

### Application Crew (AI Agents)

The system uses a **multi-agent crew architecture** with three specialized agents:

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI RECRUITMENT ASSISTANT                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐     ┌──────────────────┐                  │
│  │   USER INPUT    │────▶│  RESEARCHER      │                  │
│  │  (Job Description)    │  AGENT            │                  │
│  └──────────────────┘     └────────┬─────────┘                  │
│                                     │                            │
│                                     ▼                            │
│                            ┌──────────────────┐                  │
│                            │  EVALUATOR       │                  │
│                            │  AGENT           │                  │
│                            └────────┬─────────┘                  │
│                                     │                            │
│                                     ▼                            │
│                            ┌──────────────────┐                  │
│                            │  RECOMMENDER     │                  │
│                            │  AGENT           │                  │
│                            └────────┬─────────┘                  │
│                                     │                            │
│                                     ▼                            │
│  ┌──────────────────┐     ┌──────────────────┐                  │
│  │  RANKED          │◀────│  USER OUTPUT     │                  │
│  │  CANDIDATES     │     │  (Candidate List)│                  │
│  └──────────────────┘     └──────────────────┘                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Agent Roles

| Agent | Purpose | Capabilities |
|-------|---------|--------------|
| **Researcher Agent** | Searches and sources candidates | Parse job requirements, search multiple channels, aggregate profiles, deduplicate |
| **Evaluator Agent** | Evaluates candidates against job criteria | Score resumes (0-100), identify matching skills, generate match rationale |
| **Recommender Agent** | Provides ranked recommendations | Aggregate scores, rank by fit, generate summary reports |

### Development Crew

| Role | Responsibility |
|------|----------------|
| **Product Manager** (@product-mgr) | Requirements, PRD, MRD |
| **System Architect** (@system.arch) | SAD, SFS, architecture design |
| **Backend Engineer** (@backend.eng) | CrewAI implementation, agent logic |
| **Integration Engineer** (@integration.eng) | API integrations, frontend-backend |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 14+
- Google Gemini API key

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd recruitment-assistant

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```

### Configuration

1. **Backend**: Create `.env` file in `backend/`:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   DATABASE_URL=postgresql://user:pass@localhost:5432/recruitment
   ```

2. **Frontend**: Create `.env` file in `frontend/`:
   ```
   VITE_API_URL=http://localhost:8000
   ```

### Running the Application

```bash
# Backend
cd backend
uvicorn main:app --reload

# Frontend (new terminal)
cd frontend
npm run dev
```

### Usage

1. Open `http://localhost:5173` in your browser
2. Enter a job description in natural language
3. Click "Search Candidates"
4. View ranked results with match scores

---

## Project Structure

```
recruitment-assistant/
├── .github/
│   └── agents/              # Agent persona definitions
│       ├── product-mgr.agent.md
│       ├── system-arch.agent.md
│       ├── backend.eng.agent.md
│       └── integration.eng.agent.md
├── project-context/
│   ├── 1.define/            # Phase 1: Define artifacts
│   │   ├── mrd.md           # Market Research Document
│   │   ├── prd.md          # Product Requirements Document
│   │   └── handoff.md      # Handoff to System Architect
│   ├── 2.build/             # Phase 2: Build artifacts
│   └── 3.deliver/           # Phase 3: Delivery artifacts
├── backend/                  # Python/FastAPI backend
│   ├── agents/              # CrewAI agent definitions
│   ├── services/           # Business logic
│   └── main.py             # Application entry point
├── frontend/                 # React + TypeScript frontend
│   ├── src/
│   │   ├── components/     # UI components
│   │   ├── services/       # API calls
│   │   └── App.tsx         # Main application
│   └── package.json
└── PROJECT_README.md       # This file
```

---

## Next Steps for Contributors

### Current Phase

The project is in **Phase 1: Define** — requirements are complete.

### What's Next

| Step | Owner | Status |
|------|-------|--------|
| Create SAD (System Architecture Document) | @system.arch | Pending |
| Scaffold project structure | @project.mgr | Pending |
| Implement CrewAI backend | @backend.eng | Pending |
| Build React frontend | @frontend.eng | Pending |
| Integrate frontend and backend | @integration.eng | Pending |
| QA validation | @qa.eng | Pending |

### How to Contribute

1. **Review artifacts** in `project-context/1.define/`
2. **Pick a module** from the development crew mapping
3. **Follow AAMAD workflow** — Define → Build → Deliver

### Resources

- [PRD](project-context/1.define/prd.md) — Full product requirements
- [MRD](project-context/1.define/mrd.md) — Market research
- [AGENTS.md](./AGENTS.md) — Agent persona definitions

---

*Built with the AAMAD multi-agent framework*