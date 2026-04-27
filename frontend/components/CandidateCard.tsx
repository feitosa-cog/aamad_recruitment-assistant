import { EvaluatedCandidate } from '@/lib/api';

interface CandidateCardProps {
  candidate: EvaluatedCandidate;
  rank: number;
}

export default function CandidateCard({ candidate, rank }: CandidateCardProps) {
  const { profile, match_score, match_reasoning, strengths, gaps } = candidate;

  // Determine score color
  const getScoreColor = (score: number) => {
    if (score >= 80) return 'bg-green-100 text-green-800';
    if (score >= 60) return 'bg-yellow-100 text-yellow-800';
    return 'bg-red-100 text-red-800';
  };

  return (
    <div className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
      {/* Header with rank and score */}
      <div className="flex items-start justify-between mb-3">
        <div>
          <span className="text-sm font-medium text-gray-500">#{rank}</span>
          <h3 className="text-lg font-semibold text-gray-900">
            {profile.name}
          </h3>
          <p className="text-sm text-gray-600">{profile.education}</p>
        </div>
        <div className={`px-3 py-1 rounded-full text-sm font-medium ${getScoreColor(match_score)}`}>
          {match_score}%
        </div>
      </div>

      {/* Contact info */}
      <div className="mb-3 text-sm text-gray-600">
        <p>📧 {profile.email}</p>
        <p>💼 {profile.experience_years} years experience</p>
        <p>📂 Source: {profile.source}</p>
      </div>

      {/* Skills */}
      <div className="mb-3">
        <p className="text-sm font-medium text-gray-700 mb-1">Skills:</p>
        <div className="flex flex-wrap gap-1">
          {profile.skills.map((skill, index) => (
            <span
              key={index}
              className="px-2 py-0.5 bg-gray-100 text-gray-700 text-xs rounded"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* Match reasoning */}
      <div className="mb-3">
        <p className="text-sm font-medium text-gray-700 mb-1">Match Reasoning:</p>
        <p className="text-sm text-gray-600">{match_reasoning}</p>
      </div>

      {/* Strengths */}
      {strengths.length > 0 && (
        <div className="mb-2">
          <p className="text-sm font-medium text-gray-700 mb-1">✅ Strengths:</p>
          <ul className="text-sm text-gray-600 space-y-1">
            {strengths.slice(0, 3).map((strength, index) => (
              <li key={index} className="flex items-start gap-1">
                <span className="text-green-500">•</span>
                {strength}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Gaps */}
      {gaps.length > 0 && (
        <div>
          <p className="text-sm font-medium text-gray-700 mb-1">⚠️ Gaps:</p>
          <ul className="text-sm text-gray-600 space-y-1">
            {gaps.slice(0, 3).map((gap, index) => (
              <li key={index} className="flex items-start gap-1">
                <span className="text-yellow-500">•</span>
                {gap}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}