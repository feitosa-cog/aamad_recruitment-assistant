// Types for the recruitment assistant API

export interface CandidateProfile {
  name: string;
  email: string;
  skills: string[];
  experience_years: number;
  education: string;
  source: string;
}

export interface EvaluatedCandidate {
  profile: CandidateProfile;
  match_score: number;
  match_reasoning: string;
  strengths: string[];
  gaps: string[];
}

export interface RecruitmentRequest {
  job_description: string;
  max_candidates?: number;
}

export interface RecruitmentResponse {
  candidates: EvaluatedCandidate[];
  total_searched: number;
  processing_time_seconds: number;
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  candidates?: EvaluatedCandidate[];
  isLoading?: boolean;
}

// API client functions
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function checkHealth(): Promise<boolean> {
  try {
    const response = await fetch(`${API_BASE_URL}/api/health`, {
      method: 'GET',
    });
    return response.ok;
  } catch {
    return false;
  }
}

export async function submitJobDescription(
  jobDescription: string,
  maxCandidates: number = 10
): Promise<RecruitmentResponse> {
  const response = await fetch(`${API_BASE_URL}/api/recruit`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      job_description: jobDescription,
      max_candidates: maxCandidates,
    }),
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || 'Failed to submit job description');
  }

  return response.json();
}