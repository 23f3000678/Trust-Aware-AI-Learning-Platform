/**
 * Admin Dashboard Page
 */

import React, { useState } from 'react';

export const AdminDashboard: React.FC = () => {
  const [llmEnabled, setLlmEnabled] = useState(true);
  const [analyticsEnabled, setAnalyticsEnabled] = useState(true);

  return (
    <div className="page-container">
      <div className="dashboard-header">
        <h2>Admin Dashboard</h2>
      </div>

      <div className="dashboard-grid">
        <div className="dashboard-card">
          <h3>LLM Provider Status</h3>
          <div className="status-item">
            <span className="status-label">Provider:</span>
            <span className="status-value">Groq (Llama 3.1)</span>
          </div>
          <div className="status-item">
            <span className="status-label">Status:</span>
            <span className="status-badge success">Active</span>
          </div>
          <div className="status-item">
            <span className="status-label">API Calls Today:</span>
            <span className="status-value">1,247</span>
          </div>
        </div>

        <div className="dashboard-card">
          <h3>System Health</h3>
          <div className="health-item">
            <span className="health-label">API Response Time</span>
            <span className="health-value success">245ms</span>
          </div>
          <div className="health-item">
            <span className="health-label">Uptime</span>
            <span className="health-value success">99.8%</span>
          </div>
          <div className="health-item">
            <span className="health-label">Error Rate</span>
            <span className="health-value success">0.2%</span>
          </div>
        </div>

        <div className="dashboard-card">
          <h3>Usage Summary</h3>
          <div className="stat-row">
            <span className="stat-label">Total Users:</span>
            <span className="stat-value">156</span>
          </div>
          <div className="stat-row">
            <span className="stat-label">Queries Today:</span>
            <span className="stat-value">892</span>
          </div>
          <div className="stat-row">
            <span className="stat-label">Challenges Generated:</span>
            <span className="stat-value">445</span>
          </div>
        </div>

        <div className="dashboard-card">
          <h3>System Controls</h3>
          <div className="toggle-item">
            <label className="toggle-label">
              <input
                type="checkbox"
                checked={llmEnabled}
                onChange={(e) => setLlmEnabled(e.target.checked)}
              />
              <span>LLM Provider Enabled</span>
            </label>
          </div>
          <div className="toggle-item">
            <label className="toggle-label">
              <input
                type="checkbox"
                checked={analyticsEnabled}
                onChange={(e) => setAnalyticsEnabled(e.target.checked)}
              />
              <span>Analytics Collection</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  );
};
