import { EvaluatedCandidate } from '@/lib/api';
import CandidateCard from './CandidateCard';

interface ResultsListProps {
  candidates: EvaluatedCandidate[];
}

export default function ResultsList({ candidates }: ResultsListProps) {
  if (!candidates || candidates.length === 0) {
    return null;
  }

  return (
    <div className="mt-4">
      <h3 className="text-lg font-semibold text-gray-900 mb-3">
        Top Candidates
      </h3>
      <div className="space-y-4">
        {candidates.map((candidate, index) => (
          <CandidateCard
            key={`${candidate.profile.email}-${index}`}
            candidate={candidate}
            rank={index + 1}
          />
        ))}
      </div>
    </div>
  );
}