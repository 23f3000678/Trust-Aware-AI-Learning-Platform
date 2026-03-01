/**
 * Main App component for Trust-Aware AI Learning Platform
 * Clean Academic Minimal - Soft Notebook Theme with Routing
 */

import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { MainLayout } from './components/layout/MainLayout';
import { Home } from './pages/Home';
import { StudentLogin } from './pages/StudentLogin';
import { EducatorLogin } from './pages/EducatorLogin';
import { AdminLogin } from './pages/AdminLogin';
import { StudentDashboard } from './pages/StudentDashboard';
import { EducatorDashboard } from './pages/EducatorDashboard';
import { AdminDashboard } from './pages/AdminDashboard';
import { AILiteracyDashboard } from './pages/AILiteracyDashboard';
import { AccessibilitySettings } from './pages/AccessibilitySettings';
import { ChallengeMode } from './pages/ChallengeMode';
import { VoiceMode } from './pages/VoiceMode';
import './index.css';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route index element={<Home />} />
          <Route path="student/login" element={<StudentLogin />} />
          <Route path="educator/login" element={<EducatorLogin />} />
          <Route path="admin/login" element={<AdminLogin />} />
          <Route path="student/dashboard" element={<StudentDashboard />} />
          <Route path="educator/dashboard" element={<EducatorDashboard />} />
          <Route path="admin/dashboard" element={<AdminDashboard />} />
          <Route path="student/literacy" element={<AILiteracyDashboard />} />
          <Route path="settings/accessibility" element={<AccessibilitySettings />} />
          <Route path="challenge" element={<ChallengeMode />} />
          <Route path="voice" element={<VoiceMode />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
