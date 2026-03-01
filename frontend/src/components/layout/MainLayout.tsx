/**
 * Main Layout Component
 * Shared layout with header, navigation, and footer
 */

import React, { useState } from 'react';
import { Link, Outlet, useLocation } from 'react-router-dom';
import { Moon, Sun } from 'lucide-react';

export const MainLayout: React.FC = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const location = useLocation();

  const toggleMode = () => {
    setDarkMode(!darkMode);
  };

  const isActive = (path: string) => {
    return location.pathname === path || location.pathname.startsWith(path + '/');
  };

  return (
    <div className={`app ${darkMode ? 'dark-mode' : ''}`}>
      <header className="app-header">
        <div className="header-content">
          <Link to="/" className="header-title">
            <h1>Trust-Aware AI Learning</h1>
          </Link>
          
          <button 
            className="mobile-menu-toggle"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle menu"
          >
            ☰
          </button>

          <nav className={`main-nav ${mobileMenuOpen ? 'mobile-open' : ''}`}>
            <Link 
              to="/" 
              className={`nav-link ${isActive('/') && location.pathname === '/' ? 'active' : ''}`}
            >
              Home
            </Link>
            
            <div className="nav-dropdown">
              <span className="nav-link dropdown-trigger">Student</span>
              <div className="dropdown-menu">
                <Link to="/student/login" className="dropdown-item">Login</Link>
                <Link to="/student/dashboard" className="dropdown-item">Dashboard</Link>
                <Link to="/student/literacy" className="dropdown-item">AI Literacy</Link>
              </div>
            </div>

            <div className="nav-dropdown">
              <span className="nav-link dropdown-trigger">Educator</span>
              <div className="dropdown-menu">
                <Link to="/educator/login" className="dropdown-item">Login</Link>
                <Link to="/educator/dashboard" className="dropdown-item">Dashboard</Link>
              </div>
            </div>

            <div className="nav-dropdown">
              <span className="nav-link dropdown-trigger">Admin</span>
              <div className="dropdown-menu">
                <Link to="/admin/login" className="dropdown-item">Login</Link>
                <Link to="/admin/dashboard" className="dropdown-item">Dashboard</Link>
              </div>
            </div>

            <div className="nav-dropdown">
              <span className="nav-link dropdown-trigger">More</span>
              <div className="dropdown-menu">
                <Link to="/challenge" className="dropdown-item">Challenge Mode</Link>
                <Link to="/voice" className="dropdown-item">Voice Mode</Link>
                <Link to="/settings/accessibility" className="dropdown-item">Accessibility</Link>
              </div>
            </div>
          </nav>

          <button 
            className="theme-toggle" 
            onClick={toggleMode}
            aria-label="Toggle dark mode"
          >
            {darkMode ? <Sun size={20} /> : <Moon size={20} />}
          </button>
        </div>
      </header>

      <main className="app-main">
        <Outlet />
      </main>

      <footer className="app-footer">
        <p>Trust-Aware AI Learning Platform • Academic Design</p>
      </footer>
    </div>
  );
};
