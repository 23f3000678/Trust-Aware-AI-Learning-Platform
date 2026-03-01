/**
 * Component to toggle between original and simplified text
 */

import React, { useState } from 'react';
import type { SimplifiedResponse } from '../types';

interface SimplificationToggleProps {
  simplification: SimplifiedResponse;
  onClose: () => void;
}

export const SimplificationToggle: React.FC<SimplificationToggleProps> = ({
  simplification,
  onClose,
}) => {
  const [showSimplified, setShowSimplified] = useState(true);
  
  return (
    <div className="simplification-toggle">
      <div className="simplification-header">
        <h4>Simplified Version</h4>
        <button className="close-button" onClick={onClose}>×</button>
      </div>
      
      <div className="toggle-buttons">
        <button
          className={`toggle-button ${showSimplified ? 'active' : ''}`}
          onClick={() => setShowSimplified(true)}
        >
          Simplified
        </button>
        <button
          className={`toggle-button ${!showSimplified ? 'active' : ''}`}
          onClick={() => setShowSimplified(false)}
        >
          Original
        </button>
      </div>
      
      <div className="simplification-content">
        {showSimplified ? (
          <p className="simplified-text">{simplification.simplified_text}</p>
        ) : (
          <p className="original-text">{simplification.original_text}</p>
        )}
      </div>
    </div>
  );
};
