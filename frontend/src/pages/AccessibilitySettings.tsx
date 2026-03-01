/**
 * Accessibility Settings Page
 */

import React, { useState } from 'react';

export const AccessibilitySettings: React.FC = () => {
  const [fontSize, setFontSize] = useState('medium');
  const [simplificationDefault, setSimplificationDefault] = useState(false);
  const [keyboardNav, setKeyboardNav] = useState(true);

  return (
    <div className="page-container">
      <div className="settings-header">
        <h2>Accessibility Settings</h2>
      </div>

      <div className="settings-grid">
        <div className="settings-card">
          <h3>Display Settings</h3>
          
          <div className="setting-item">
            <label className="setting-label">Font Size</label>
            <select 
              value={fontSize} 
              onChange={(e) => setFontSize(e.target.value)}
              className="setting-select"
            >
              <option value="small">Small (16px)</option>
              <option value="medium">Medium (17px)</option>
              <option value="large">Large (19px)</option>
              <option value="xlarge">Extra Large (22px)</option>
            </select>
          </div>
        </div>

        <div className="settings-card">
          <h3>Content Preferences</h3>
          
          <div className="setting-item">
            <label className="toggle-label">
              <input
                type="checkbox"
                checked={simplificationDefault}
                onChange={(e) => setSimplificationDefault(e.target.checked)}
              />
              <span>Enable Simplification by Default</span>
            </label>
            <p className="setting-description">
              Automatically simplify complex explanations
            </p>
          </div>
        </div>

        <div className="settings-card">
          <h3>Navigation</h3>
          
          <div className="setting-item">
            <label className="toggle-label">
              <input
                type="checkbox"
                checked={keyboardNav}
                onChange={(e) => setKeyboardNav(e.target.checked)}
              />
              <span>Enhanced Keyboard Navigation</span>
            </label>
            <p className="setting-description">
              Enable additional keyboard shortcuts and focus indicators
            </p>
          </div>
        </div>

        <div className="settings-actions">
          <button className="action-button primary-action">
            Save Settings
          </button>
          <button className="action-button">
            Reset to Defaults
          </button>
        </div>
      </div>
    </div>
  );
};
