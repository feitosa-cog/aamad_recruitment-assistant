# Frontend Implementation Plan

**Project:** AI Recruitment Assistant  
**Version:** 1.0  
**Date:** April 27, 2026  
**Owner:** @frontend.eng

---

## 1. Overview

This document outlines the frontend implementation approach for the AI Recruitment Assistant. Based on the SAD, the frontend will be a Next.js + assistant-ui application that provides a chat interface for job input and displays ranked candidate recommendations.

---

## 2. UI Components to Build

### 2.1 Core Components (MVP)

| Component | Description | Priority |
|-----------|-------------|----------|
| **ChatInterface** | Main chat input for job descriptions | P0 |
| **MessageBubble** | Display user and AI messages | P0 |
| **CandidateCard** | Display candidate profile with scores | P0 |
| **ResultsList** | Ranked list of candidate recommendations | P0 |
| **LoadingIndicator** | Show agent progress during processing | P0 |

### 2.2 Placeholder Components (Future)

| Component | Description | Status |
|-----------|-------------|--------|
| **Dashboard** | Metrics and analytics display | Placeholder |
| **SettingsPanel** | API configuration | Placeholder |
| **HistoryPanel** | Past job searches | Placeholder |

---

## 3. User Interaction Flows

### 3.1 Primary Flow: Submit Job Description

```
1. User enters job description in chat input
2. User clicks "Submit" or presses Enter
3. Frontend displays loading state with agent progress
4. Backend processes through CrewAI pipeline:
   - Researcher searches candidates
   - Evaluator scores candidates
   - Recommender ranks results
5. Frontend displays ranked candidate cards
6. User can click candidate for detailed view
```

### 3.2 Secondary Flows

| Flow | Description |
|------|-------------|
| **View Candidate Details** | Click card to expand full profile |
| **Copy Candidate Info** | Copy email/contact to clipboard |
| **New Search** | Clear chat and start fresh |

---

## 4. API Integration Points

### 4.1 Backend Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/recruit` | POST | Submit job description, get recommendations |
| `/api/health` | GET | Check backend availability |
| `/api/candidates` | GET | List cached candidates (optional) |

### 4.2 Request/Response Format

```typescript
// Request
interface RecruitmentRequest {
  job_description: string;
  max_candidates?: number;
}

// Response
interface RecruitmentResponse {
  candidates: EvaluatedCandidate[];
  total_searched: number;
  processing_time_seconds: number;
}

interface EvaluatedCandidate {
  profile: {
    name: string;
    email: string;
    skills: string[];
    experience_years: number;
    education: string;
    source: string;
  };
  match_score: number;
  match_reasoning: string;
  strengths: string[];
  gaps: string[];
}
```

---

## 5. Implementation Approach

### 5.1 Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| **Framework** | Next.js | 14+ |
| **UI Library** | React + Tailwind CSS | 18+ / 3.x |
| **State** | React useState/useReducer | - |
| **HTTP** | Fetch API | - |

### 5.2 File Structure

```
frontend/
├── app/
│   ├── page.tsx          # Main chat page
│   └── layout.tsx        # Root layout
├── components/
│   ├── ChatInterface.tsx
│   ├── MessageBubble.tsx
│   ├── CandidateCard.tsx
│   ├── ResultsList.tsx
│   └── LoadingIndicator.tsx
├── lib/
│   └── api.ts            # API client functions
├── styles/
│   └── globals.css       # Global styles
└── package.json
```

### 5.3 Implementation Phases

| Phase | Tasks | Status |
|-------|-------|--------|
| **F1** | Set up Next.js project with TypeScript | Not Started |
| **F2** | Create chat interface component | Not Started |
| **F3** | Implement API client | Not Started |
| **F4** | Build candidate card component | Not Started |
| **F5** | Add loading states and error handling | Not Started |
| **F6** | Style with Tailwind CSS | Not Started |

---

## 6. Status Tracking

| Task | Description | Status |
|------|-------------|--------|
| F1.1 | Initialize Next.js project | ✅ Complete |
| F1.2 | Configure Tailwind CSS | ✅ Complete |
| F2.1 | Create chat input component | ✅ Complete |
| F2.2 | Create message display area | ✅ Complete |
| F3.1 | Implement API client for /api/recruit | ✅ Complete |
| F3.2 | Add error handling for API calls | ✅ Complete |
| F4.1 | Create CandidateCard component | ✅ Complete |
| F4.2 | Create ResultsList component | ✅ Complete |
| F5.1 | Add loading spinner component | ✅ Complete |
| F5.2 | Add error message display | ✅ Complete |
| F6.1 | Apply Tailwind styling | ✅ Complete |
| F6.2 | Make responsive for mobile | ✅ Complete |

---

## 7. Implementation Summary

### Files Created

```
frontend/
├── app/
│   ├── layout.tsx          # Root layout with header
│   └── page.tsx            # Main page with chat + sidebar
├── components/
│   ├── ChatInterface.tsx   # Main chat component
│   ├── MessageBubble.tsx   # Message display
│   ├── CandidateCard.tsx   # Candidate profile card
│   ├── ResultsList.tsx     # Ranked results list
│   └── LoadingIndicator.tsx # Loading animation
├── lib/
│   └── api.ts              # API client + types
├── styles/
│   └── globals.css         # Global Tailwind styles
├── package.json            # Dependencies
├── tsconfig.json           # TypeScript config
├── next.config.js          # Next.js config
├── tailwind.config.js      # Tailwind config
└── postcss.config.js       # PostCSS config
```

### Components Implemented

| Component | Features |
|-----------|-----------|
| **ChatInterface** | Job description input, message history, backend health check, loading states |
| **MessageBubble** | User/assistant message styling, responsive |
| **CandidateCard** | Rank, name, score (color-coded), skills, strengths, gaps, contact info |
| **ResultsList** | Ranked candidate display, empty state handling |
| **LoadingIndicator** | Animated dots for processing state |

### API Integration

- `/api/recruit` - POST job description, get candidates
- `/api/health` - GET backend availability
- TypeScript types for request/response

---

## 7. Acceptance Criteria

- [x] Chat interface accepts job description input
- [x] Submit button triggers API call to backend
- [x] Loading state displays during processing
- [x] Candidate cards show name, score, skills, reasoning
- [x] ResultsList displays ranked candidates (best match first)
- [x] Error messages display on API failure
- [x] Responsive design works on mobile and desktop
- [ ] Health check verifies backend connectivity (requires backend)

---

## 8. Dependencies

| Dependency | Required By | Notes |
|------------|-------------|-------|
| Backend running on port 8000 | F3 (API client) | Must be available |
| SAD specification | All components | Design reference |
| PRD user personas | F2, F4 | UX decisions |

---

**Document Version:** 1.0  
**Last Updated:** April 27, 2026  
**Author:** @frontend.eng