/**
 * Component to display confidence score and breakdown
 */

import React from 'react';
import type { ConfidenceScore } from '../types';

interface ConfidenceDisplayProps {
  confidence: ConfidenceScore;
}

export const ConfidenceDisplay: React.FC<ConfidenceDisplayProps> = ({ confidence }) => {
  const { score, justification, breakdown, should_warn } = confidence;
  
  // Use CSS classes for color coding based on confidence score
  const scoreClass = score >= 70 ? 'score-high' : 'score-low';
  
  return (
    <div className="confidence-display">
      {should_warn && (
        <div className="warning-banner">
          Low Confidence Warning: This response may be incomplete or uncertain.
        </div>
      )}
      
      <div className={`confidence-score ${scoreClass}`}>
        <div className="score-value">
          {score}%
        </div>
        <div className="score-label">Confidence</div>
      </div>
      
      <div className="confidence-breakdown">
        <h4>Confidence Breakdown</h4>
        <div className="breakdown-item">
          <span className="breakdown-label">Question Clarity:</span>
          <span className={`breakdown-value clarity-${breakdown.question_clarity.toLowerCase()}`}>
            {breakdown.question_clarity}
          </span>
        </div>
        <div className="breakdown-item">
          <span className="breakdown-label">Topic Complexity:</span>
          <span className={`breakdown-value complexity-${breakdown.topic_complexity.toLowerCase()}`}>
            {breakdown.topic_complexity}
          </span>
        </div>
        <div className="breakdown-item">
          <span className="breakdown-label">Missing Information:</span>
          <span className={`breakdown-value missing-${breakdown.missing_information.toLowerCase()}`}>
            {breakdown.missing_information}
          </span>
        </div>
      </div>
      
      <div className="confidence-justification">
        <h4>Why this confidence score?</h4>
        <p>{justification}</p>
      </div>
    </div>
  );
};
