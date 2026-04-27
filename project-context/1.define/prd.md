# Product Requirements Document (PRD)

**Project:** AI Recruitment Assistant  
**Version:** 1.0  
**Date:** April 25, 2026  
**Owner:** @product-mgr

---

## 1. Product Overview

### 1.1 High-Level Description

The AI Recruitment Assistant is a multi-agent system that automates candidate sourcing, evaluation, and recommendation for small businesses. Using specialized AI agents, it searches for candidates, evaluates them against job requirements, and provides ranked recommendations to recruiters and hiring managers.

### 1.2 Core Value Proposition

> "Reduce time-to-hire by 80% with AI agents that source, evaluate, and recommend qualified candidates — without the enterprise price tag."

### 1.3 Product Vision

Build an AI-powered multi-agent recruitment assistant that helps small businesses automate the end-to-end recruitment process — from candidate sourcing and evaluation to interview scheduling — reducing time-to-hire, eliminating manual effort, and providing a seamless candidate experience.

### 1.4 Problem Statement

Manual candidate sourcing and evaluation is highly inefficient:
- Recruiters spend 60-70% of time on manual sourcing
- Inconsistent evaluation due to human bias
- Unable to scale during high-volume hiring
- Delayed response times cause losing top candidates

---

## 2. Goals & Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Time to Source Candidates** | < 1 hour (vs 15-20 hrs manual) | Time from job description to candidate list |
| **Candidate Match Accuracy** | ≥ 85% | % of recommended candidates that pass interview |
| **Recruiter Satisfaction** | ≥ 4.5/5 | Post-use survey score |
| **Resume Screening Speed** | < 5 min per 100 resumes | Automated vs manual comparison |
| **Candidate Response Rate** | > 70% | Response to AI-initiated outreach |

---

## 3. User Personas

| Persona | Type | Description | Primary Need |
|---------|------|-------------|--------------|
| **Recruiter** | Primary | Solo or small team recruiter | Find and evaluate candidates quickly |
| **Hiring Manager** | Secondary | Department lead needing talent | Receive ranked, qualified candidate recommendations |

### 3.1 Primary Persona: Recruiter

- **Role:** Handles day-to-day recruitment tasks
- **Needs:** Quick candidate sourcing, accurate screening, minimal manual effort
- **Pain Points:** Manual sourcing takes 15-20 hrs/week, inconsistent screening

### 3.2 Secondary Persona: Hiring Manager

- **Role:** Makes hiring decisions, conducts interviews
- **Needs:** Ranked candidate recommendations, clear match rationale
- **Pain Points:** Receive unqualified candidates, waste interview time

---

## 4. Core Features

| Feature | Description | Priority |
|---------|-------------|----------|
| **Candidate Search** | AI agents search and source candidates based on job requirements | P0 |
| **Automated Evaluation** | Resume screening against job criteria with match scoring | P0 |
| **Ranked Recommendations** | Sorted candidate list with match scores and rationale | P0 |
| **Job Description Parsing** | Natural language processing of job requirements | P0 |
| **Source Attribution** | Track and display candidate source channels | P1 |

---

## 5. Application Crew Definition

The recruitment assistant uses a multi-agent crew architecture:

### 5.1 Researcher Agent

- **Purpose:** Searches and sources candidates from multiple channels
- **Capabilities:**
  - Parse job requirements into search criteria
  - Search job boards, LinkedIn, and other sources
  - Aggregate and deduplicate candidate profiles
  - Output: List of candidate profiles with source attribution

### 5.2 Evaluator Agent

- **Purpose:** Evaluates candidates against job criteria
- **Capabilities:**
  - Score resumes against job requirements (0-100)
  - Identify matching skills and experience
  - Generate match rationale for each candidate
  - Output: Evaluated candidates with scores and reasoning

### 5.3 Recommender Agent

- **Purpose:** Provides ranked recommendations
- **Capabilities:**
  - Aggregate scores from Evaluator
  - Rank candidates by fit score
  - Generate summary recommendations
  - Output: Ranked candidate list with top recommendations

### 5.4 Agent Communication Flow

```
User Input (Job Description)
         ↓
   [Researcher Agent] → Candidate List
         ↓
   [Evaluator Agent] → Scored Candidates
         ↓
   [Recommender Agent] → Ranked Recommendations
         ↓
   User Output (Candidate Report)
```

---

## 6. Development Crew Mapping

| Role | Responsibility | Module |
|------|----------------|--------|
| **Product Manager** (@product-mgr) | Requirements, PRD, MRD | This phase |
| **System Architect** (@system.arch) | SAD, SFS, architecture design | Module 06 |
| **Backend Engineer** (@backend.eng) | CrewAI implementation, agent logic | Module 06 |
| **Integration Engineer** (@integration.eng) | API integrations, frontend-backend | Module 06 |

---
## 8. Out of Scope (Mini-Project)

The following are explicitly out of scope for this mini-project:

| Feature | Reason |
|---------|--------|
| **Full ATS Integration** | Requires complex API partnerships |
| **Candidate Communication Automation** | Email/SMS automation adds regulatory complexity |
| **Advanced Analytics and Reporting** | Defer to future phase |
| **Job Posting System Integration** | Optional for mini-project |
| **Video Interview Platform** | Out of scope |
| **Multi-language Support** | English-only for v1 |

---

## 10. User Stories & Requirements

### 10.1 Epic: Candidate Sourcing

| ID | User Story | Priority | Acceptance Criteria |
|----|------------|----------|---------------------|
| US-001 | As a recruiter, I want to describe ideal candidate profile in natural language so that AI agents search and identify matching candidates | P0 | System parses profile description → searches multiple channels → returns candidate list |
| US-002 | As a recruiter, I want to see candidate sources so I know where candidates were found | P0 | Each candidate shows source channels (job boards, LinkedIn, etc.) |
| US-003 | As a hiring manager, I want to receive daily candidate recommendations so I can review qualified candidates | P1 | System sends digest with top 5-10 candidates matching open roles |

### 10.2 Epic: Candidate Evaluation

| ID | User Story | Priority | Acceptance Criteria |
|----|------------|----------|---------------------|
| US-004 | As a recruiter, I want resumes automatically screened so I only review qualified candidates | P0 | AI evaluates each resume against job requirements → assigns match score (0-100) |
| US-005 | As a hiring manager, I want to see why a candidate matched so I can validate AI recommendations | P0 | Match score includes specific reasons (skills, experience, keywords matched) |
| US-006 | As a recruiter, I want to filter candidates by score threshold so I focus on top matches | P1 | Filter candidates by minimum match score (configurable) |

### 10.3 Epic: Ranked Recommendations

| ID | User Story | Priority | Acceptance Criteria |
|----|------------|----------|---------------------|
| US-007 | As a hiring manager, I want candidates ranked by fit so I can focus on top matches | P0 | Candidates sorted by match score, highest first |
| US-008 | As a recruiter, I want a summary report of top candidates for each job | P0 | Report includes top 5 candidates with scores and rationale |

---

## 11. Functional Requirements

### 11.1 Core Features

#### 11.1.1 Job Description Parser

| FR-ID | Requirement | Description |
|-------|-------------|--------------|
| FR-001 | Natural Language Parsing | Parse job descriptions into structured requirements (skills, experience, education) |
| FR-002 | Skills Extraction | Identify required skills, years of experience, education level |
| FR-003 | Keyword Identification | Extract important keywords for matching |

#### 11.1.2 Candidate Search (Researcher Agent)

| FR-ID | Requirement | Description |
|-------|-------------|--------------|
| FR-004 | Multi-Channel Search | Search across job boards and candidate databases |
| FR-005 | Profile Aggregation | Combine candidate info from multiple sources |
| FR-006 | Deduplication | Remove duplicate candidate profiles |

#### 11.1.3 Candidate Evaluation (Evaluator Agent)

| FR-ID | Requirement | Description |
|-------|-------------|--------------|
| FR-007 | Resume Scoring | Score resumes against job requirements (0-100) |
| FR-008 | Skills Matching | Match candidate skills to job requirements |
| FR-009 | Experience Analysis | Evaluate years of experience vs required |
| FR-010 | Match Rationale | Generate human-readable explanation of match |

#### 11.1.4 Recommendation (Recommender Agent)

| FR-ID | Requirement | Description |
|-------|-------------|--------------|
| FR-011 | Ranking Algorithm | Sort candidates by composite match score |
| FR-012 | Top-N Selection | Return top 5-10 candidates by default |
| FR-013 | Summary Generation | Create concise summary for each candidate |

### 11.2 Non-Functional Requirements

| NFR-ID | Requirement | Target |
|--------|-------------|--------|
| NFR-001 | Response Time | < 30 seconds for full candidate pipeline |
| NFR-002 | Availability | 99.5% uptime |
| NFR-003 | Data Security | SOC 2 compliant (future) |
| NFR-004 | Privacy | GDPR compliant (future) |

---

## 12. Technical Constraints

### 12.1 Technology Stack (Recommended)

| Layer | Technology |
|-------|------------|
| **Frontend** | React + TypeScript |
| **Backend** | Python (FastAPI) |
| **AI/ML** | Google Gemini API |
| **Multi-Agent Framework** | CrewAI |
| **Database** | PostgreSQL |

### 12.2 Integration Requirements

| Integration | Method | Priority |
|-------------|--------|----------|
| Job Board APIs | REST API | Required (mock for MVP) |
| Gemini API | Google AI Studio | Required |
| Database | PostgreSQL | Required |

---

## 13. UI/UX Guidelines

### 13.1 Key Screens

1. **Landing/Onboarding** — Simple sign-up
2. **Dashboard** — View open jobs and candidate status
3. **Job Input** — Natural language job description input
4. **Candidate Results** — Ranked candidate list with scores
5. **Candidate Detail** — Individual candidate profile with match rationale

### 13.2 Design Principles

- **Minimal** — Single-purpose interface, no clutter
- **Fast** — Under 3 clicks to complete any action
- **Transparent** — Show AI reasoning, not black box

---

## 14. Success Metrics (KPIs)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Time to Source | < 1 hour (vs 15-20 hrs manual) | Job description to candidate list |
| Match Accuracy | ≥ 85% | Candidates passing interview / total recommended |
| Recruiter Satisfaction | ≥ 4.5/5 | Post-use survey |
| Resume Processing | < 5 min per 100 resumes | Automated vs manual |

---

## 15. Roadmap

### Phase 1 (MVP) — v1.0
- [x] Job description parsing
- [x] Candidate search (Researcher Agent)
- [x] Candidate evaluation (Evaluator Agent)
- [x] Ranked recommendations (Recommender Agent)

### Phase 2 — v1.1
- [ ] Multi-channel sourcing expansion
- [ ] Advanced filtering options
- [ ] Candidate database persistence

### Phase 3 — v2.0
- [ ] Scheduling automation
- [ ] Candidate communication
- [ ] Analytics dashboard

---

## 16. Appendix

### Glossary

| Term | Definition |
|------|------------|
| **Crew** | Multi-agent system working collaboratively |
| **Agent** | AI-powered autonomous unit with specific role |
| **Match Score** | 0-100 score indicating candidate-job fit |
| **Sourcing** | Process of finding and attracting candidates |

### References

- MRD document: `project-context/1.define/mrd.md`
- Technical constraints subject to @system.arch review

---

*Document Status: Draft for Architecture Review*  
*Next: Handoff to @system.arch for SAD creation*