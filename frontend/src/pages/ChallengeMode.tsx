/**
 * Challenge Mode Page
 */

import React, { useState } from 'react';

export const ChallengeMode: React.FC = () => {
  const [answer, setAnswer] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="page-container">
      <div className="challenge-header">
        <h2>Challenge Mode</h2>
        <p className="challenge-subtitle">Test your understanding</p>
      </div>

      <div className="challenge-container">
        <div className="challenge-card">
          <h3>Challenge Question</h3>
          <p className="challenge-question-text">
            What is the primary difference between supervised and unsupervised learning 
            in machine learning? Provide an example of each.
          </p>
        </div>

        <form onSubmit={handleSubmit} className="challenge-form">
          <div className="form-group">
            <label htmlFor="answer">Your Answer</label>
            <textarea
              id="answer"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              placeholder="Type your answer here..."
              rows={8}
              disabled={submitted}
            />
          </div>
          <button 
            type="submit" 
            className="submit-button"
            disabled={submitted || !answer.trim()}
          >
            {submitted ? 'Submitted' : 'Submit Answer'}
          </button>
        </form>

        {submitted && (
          <div className="feedback-area">
            <h3>Feedback</h3>
            <p className="feedback-text">
              Thank you for your response! In the full version, this would provide 
              detailed feedback on your answer and suggest areas for improvement.
            </p>
            <div className="feedback-actions">
              <button 
                className="action-button"
                onClick={() => {
                  setAnswer('');
                  setSubmitted(false);
                }}
              >
                Try Another Challenge
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
