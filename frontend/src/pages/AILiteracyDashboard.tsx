/**
 * AI Literacy Dashboard Page
 */

import React from 'react';

export const AILiteracyDashboard: React.FC = () => {
  return (
    <div className="page-container">
      <div className="dashboard-header">
        <h2>AI Literacy Growth Timeline</h2>
        <p className="dashboard-subtitle">Your cognitive development in understanding AI</p>
      </div>

      <div className="dashboard-grid">
        <div className="dashboard-card score-card">
          <h3>Overall AI Literacy Score</h3>
          <div className="big-score">78</div>
          <p className="score-subtitle">Out of 100</p>
          <p className="score-explanation">
            Reflects your understanding of AI capabilities, limitations, and appropriate use
          </p>
        </div>

        <div className="dashboard-card">
          <h3>Score Breakdown</h3>
          <div className="breakdown-row">
            <span className="breakdown-label">Calibration Accuracy</span>
            <span className="breakdown-score">82/100</span>
          </div>
          <div className="breakdown-row">
            <span className="breakdown-label">Error Detection Rate</span>
            <span className="breakdown-score">75/100</span>
          </div>
          <div className="breakdown-row">
            <span className="breakdown-label">Verification Behavior</span>
            <span className="breakdown-score">80/100</span>
          </div>
          <div className="breakdown-row">
            <span className="breakdown-label">Challenge Reasoning Quality</span>
            <span className="breakdown-score">72/100</span>
          </div>
        </div>

        <div className="dashboard-card">
          <h3>Calibration Accuracy Metrics</h3>
          <div className="calibration-metric">
            <span className="metric-label">Trust-Confidence Alignment:</span>
            <span className="metric-value">85%</span>
          </div>
          <div className="calibration-metric">
            <span className="metric-label">Overconfidence Rate:</span>
            <span className="metric-value">12%</span>
          </div>
          <div className="calibration-metric">
            <span className="metric-label">Underconfidence Rate:</span>
            <span className="metric-value">8%</span>
          </div>
          <p className="metric-description">
            Calibration measures how well your trust aligns with AI confidence levels
          </p>
        </div>

        <div className="dashboard-card">
          <h3>Verification Behavior</h3>
          <div className="stat-row">
            <span className="stat-label">Total Verifications:</span>
            <span className="stat-value">45</span>
          </div>
          <div className="stat-row">
            <span className="stat-label">Successful Identifications:</span>
            <span className="stat-value success">38</span>
          </div>
          <div className="stat-row">
            <span className="stat-label">Success Rate:</span>
            <span className="stat-value">84%</span>
          </div>
          <p className="metric-description">
            Tracks your ability to identify uncertain or incorrect AI outputs
          </p>
        </div>

        <div className="dashboard-card growth-timeline">
          <h3>Growth Timeline</h3>
          <div className="timeline-item">
            <span className="timeline-date">This Week</span>
            <span className="timeline-metric">Literacy Score: 78 (+5)</span>
          </div>
          <div className="timeline-item">
            <span className="timeline-date">Last Week</span>
            <span className="timeline-metric">Literacy Score: 73 (+3)</span>
          </div>
          <div className="timeline-item">
            <span className="timeline-date">2 Weeks Ago</span>
            <span className="timeline-metric">Literacy Score: 70 (+2)</span>
          </div>
          <p className="timeline-note">
            Simple line graph visualization would appear here in full implementation
          </p>
        </div>

        <div className="dashboard-card reflective-section">
          <h3>Reflective Prompts</h3>
          <div className="prompt-item">
            <p className="prompt-question">
              How confident were you in your last response?
            </p>
            <textarea 
              className="prompt-input" 
              placeholder="Reflect on your confidence level..."
              rows={3}
            />
          </div>
          <div className="prompt-item">
            <p className="prompt-question">
              What strategies did you use to verify the information?
            </p>
            <textarea 
              className="prompt-input" 
              placeholder="Describe your verification approach..."
              rows={3}
            />
          </div>
          <button className="action-button">Save Reflection</button>
        </div>
      </div>
    </div>
  );
};
