/**
 * Student Dashboard Page
 */

import React from 'react';
import { useNavigate } from 'react-router-dom';

export const StudentDashboard: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="page-container">
      <div className="dashboard-header">
        <h2>Your AI Literacy Growth</h2>
        <p className="dashboard-subtitle">Track your cognitive development and understanding of AI</p>
      </div>

      <div className="dashboard-grid">
        <div className="dashboard-card score-card">
          <h3>AI Literacy Score</h3>
          <div className="big-score">78</div>
          <p className="score-subtitle">Out of 100</p>
          <p className="score-explanation">
            This score reflects your understanding of AI capabilities and limitations
          </p>
        </div>

        <div className="dashboard-card">
          <h3>Cognitive Growth Metrics</h3>
          <div className="progress-item">
            <span className="progress-label">Calibration Accuracy</span>
            <div className="progress-bar">
              <div className="progress-fill" style={{ width: '75%' }}></div>
            </div>
            <span className="progress-value">75%</span>
            <p className="metric-description">Alignment between your trust and AI confidence</p>
          </div>
          <div className="progress-item">
            <span className="progress-label">Error Detection Rate</span>
            <div className="progress-bar">
              <div className="progress-fill" style={{ width: '60%' }}></div>
            </div>
            <span className="progress-value">60%</span>
            <p className="metric-description">Ability to identify uncertain AI outputs</p>
          </div>
          <div className="progress-item">
            <span className="progress-label">Verification Behavior</span>
            <div className="progress-bar">
              <div className="progress-fill" style={{ width: '85%' }}></div>
            </div>
            <span className="progress-value">85%</span>
            <p className="metric-description">Consistency in checking AI responses</p>
          </div>
        </div>

        <div className="dashboard-card">
          <h3>Recent Milestones</h3>
          <ul className="milestone-list">
            <li>Verified 5 low-confidence responses</li>
            <li>Identified 3 uncertain AI outputs</li>
            <li>Completed 20 AI interactions</li>
          </ul>
          <p className="milestone-note">
            Milestones reflect your learning behavior patterns
          </p>
        </div>

        <div className="dashboard-card">
          <h3>Improvement Since Last Week</h3>
          <div className="improvement-metric">
            <span className="metric-label">Calibration Accuracy:</span>
            <span className="metric-value improvement">+12%</span>
          </div>
          <div className="improvement-metric">
            <span className="metric-label">Error Detection:</span>
            <span className="metric-value improvement">+8%</span>
          </div>
          <div className="improvement-metric">
            <span className="metric-label">Verification Frequency:</span>
            <span className="metric-value improvement">+15%</span>
          </div>
        </div>

        <div className="dashboard-card reflection-card">
          <h3>Recent Reflection Prompt</h3>
          <p className="reflection-prompt">
            "You accepted a low-confidence answer without verification. What signals could you check next time?"
          </p>
          <p className="reflection-note">
            Reflection prompts help you think critically about AI interactions
          </p>
        </div>

        <div className="dashboard-actions">
          <button 
            className="action-button primary-action"
            onClick={() => navigate('/')}
          >
            Continue Learning
          </button>
          <button 
            className="action-button"
            onClick={() => navigate('/student/literacy')}
          >
            View Detailed Growth Timeline
          </button>
        </div>
      </div>
    </div>
  );
};
