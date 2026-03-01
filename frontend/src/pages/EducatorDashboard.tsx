/**
 * Educator Dashboard Page
 */

import React from 'react';

export const EducatorDashboard: React.FC = () => {
  return (
    <div className="page-container">
      <div className="dashboard-header">
        <h2>Educator Dashboard</h2>
      </div>

      <div className="dashboard-grid">
        <div className="dashboard-card">
          <h3>Class Analytics</h3>
          <div className="stat-row">
            <span className="stat-label">Total Students:</span>
            <span className="stat-value">32</span>
          </div>
          <div className="stat-row">
            <span className="stat-label">Active This Week:</span>
            <span className="stat-value">28</span>
          </div>
          <div className="stat-row">
            <span className="stat-label">Challenges Completed:</span>
            <span className="stat-value">156</span>
          </div>
        </div>

        <div className="dashboard-card score-card">
          <h3>Average AI Literacy Score</h3>
          <div className="big-score">72</div>
          <p className="score-subtitle">Class Average</p>
        </div>

        <div className="dashboard-card">
          <h3>Confidence Trends</h3>
          <div className="trend-item">
            <span className="trend-label">High Confidence Responses</span>
            <span className="trend-value success">65%</span>
          </div>
          <div className="trend-item">
            <span className="trend-label">Medium Confidence</span>
            <span className="trend-value warning">25%</span>
          </div>
          <div className="trend-item">
            <span className="trend-label">Low Confidence</span>
            <span className="trend-value error">10%</span>
          </div>
        </div>

        <div className="dashboard-actions">
          <button className="action-button primary-action">
            Export Report
          </button>
          <button className="action-button">
            View Student Progress
          </button>
        </div>
      </div>
    </div>
  );
};
