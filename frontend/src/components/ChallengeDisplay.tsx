/**
 * Component to display challenge questions
 */

import React from 'react';
import type { Challenge } from '../types';

interface ChallengeDisplayProps {
  challenge: Challenge;
  onClose: () => void;
}

export const ChallengeDisplay: React.FC<ChallengeDisplayProps> = ({ challenge, onClose }) => {
  return (
    <div className="challenge-display">
      <div className="challenge-header">
        <h4>Challenge Question</h4>
        <button className="close-button" onClick={onClose}>×</button>
      </div>
      <div className="challenge-content">
        <p className="challenge-question">{challenge.question_text}</p>
        <p className="challenge-note">
          Think about this question to verify your understanding. 
          (Answer evaluation not available in MVP)
        </p>
      </div>
    </div>
  );
};
