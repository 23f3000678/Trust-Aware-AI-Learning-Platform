/**
 * Voice Mode Page - Placeholder
 */

import React from 'react';

export const VoiceMode: React.FC = () => {
  return (
    <div className="page-container">
      <div className="placeholder-container">
        <div className="placeholder-card">
          <div className="placeholder-icon">
            <svg 
              width="120" 
              height="120" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              strokeWidth="2"
            >
              <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" />
              <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
              <line x1="12" y1="19" x2="12" y2="23" />
              <line x1="8" y1="23" x2="16" y2="23" />
            </svg>
          </div>
          <h2>Voice Interaction</h2>
          <p className="placeholder-text">
            Voice interaction coming soon
          </p>
          <p className="placeholder-description">
            This feature will allow you to interact with the AI learning platform 
            using voice commands and receive audio responses.
          </p>
        </div>
      </div>
    </div>
  );
};
