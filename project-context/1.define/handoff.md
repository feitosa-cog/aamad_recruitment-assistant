# Phase 1 Define — Handoff Summary

**Date:** April 25, 2026  
**From:** @product-mgr  
**To:** @system.arch

---

## Artifacts Produced

| Artifact | Location | Status |
|----------|----------|--------|
| Market Research Document (MRD) | `project-context/1.define/mrd.md` | ✅ Complete |
| Product Requirements Document (PRD) | `project-context/1.define/prd.md` | ✅ Complete |

---

## Project Summary

### Product
AI Recruitment Assistant — Scheduling Automation Module

### Target Market
- **Segment:** Small Business (1-50 employees)
- **Geography:** US-based initially

### Core Feature (MVP)
AI-powered multi-agent recruitment assistant that handles:
1. **Candidate Sourcing** — AI agents search and identify matching candidates
2. **Candidate Evaluation** — Resume screening and match scoring
3. **Interview Scheduling** — Natural language scheduling automation

### Key Requirements (Top 5)

1. **AI Candidate Sourcing** — Natural language job description → AI agents search and identify candidates
2. **Intelligent Resume Screening** — Automated evaluation against job requirements with match scoring
3. **Natural Language Scheduling** — Parse requests like "Schedule interview with John on Tuesday afternoon"
4. **Google Calendar Integration** — OAuth flow + availability detection
5. **Automated Candidate Communication** — Personalized messages at scale

### Technical Constraints

| Constraint | Detail |
|------------|--------|
| **Stack** | React + TypeScript (FE), Python FastAPI or Node.js (BE) |
| **AI** | Google Gemini API |
| **Database** | PostgreSQL |
| **Required Integrations** | Google Calendar API, Google OAuth, SendGrid, Google Meet |

### Out of Scope (MVP)

- ATS integration
- Video interview platform
- Multi-language support
- Advanced analytics
- Outlook integration

---

## Handoff Instructions

### For @system.arch

Create the **System Architecture Document (SAD)** using:

- **Input:** `project-context/1.define/mrd.md` and `project-context/1.define/prd.md`
- **Template:** Use `.cursor/templates/sad-template.md` (or create lean MVP version)
- **Output:** `project-context/1.define/sad.md`

### MVP Focus

Produce a lean SAD covering:
- Stakeholders and concerns
- Key architectural decisions
- Logical view (components)
- Process/runtime view (data flows)
- Deployment view
- Risks and assumptions

**Explicitly document:**
- What's included in MVP
- What's deferred to future phases
- Trade-offs made

---

## Next Steps

1. @system.arch creates SAD
2. SAD approved by stakeholders
3. Handoff to @project.mgr for project scaffolding

---

*This handoff is auditable and traceable to PRD user stories.*