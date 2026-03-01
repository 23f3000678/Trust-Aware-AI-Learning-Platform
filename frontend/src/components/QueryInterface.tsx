/**
 * Main query interface component
 * Handles user input, displays AI responses with uncertainty highlighting
 */

import React, { useState } from 'react';
import type { AIResponse, Challenge, SimplifiedResponse } from '../types';
import { submitQuery, generateChallenge, simplifyText } from '../services/api';
import { ConfidenceDisplay } from './ConfidenceDisplay';
import { ChallengeDisplay } from './ChallengeDisplay';
import { SimplificationToggle } from './SimplificationToggle';

export const QueryInterface: React.FC = () => {
  const [queryText, setQueryText] = useState('');
  const [response, setResponse] = useState<AIResponse | null>(null);
  const [challenge, setChallenge] = useState<Challenge | null>(null);
  const [simplification, setSimplification] = useState<SimplifiedResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [challengeLoading, setChallengeLoading] = useState(false);
  const [simplifyLoading, setSimplifyLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!queryText.trim()) {
      setError('Please enter a question');
      return;
    }

    setLoading(true);
    setError(null);
    setResponse(null);
    setChallenge(null);
    setSimplification(null);

    try {
      const aiResponse = await submitQuery(queryText);
      setResponse(aiResponse);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to get response');
    } finally {
      setLoading(false);
    }
  };

  const handleChallenge = async () => {
    if (!response) return;

    setChallengeLoading(true);
    try {
      const challengeResponse = await generateChallenge(
        response.response_id,
        response.response_text
      );
      setChallenge(challengeResponse);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to generate challenge');
    } finally {
      setChallengeLoading(false);
    }
  };

  const handleSimplify = async () => {
    if (!response) return;

    setSimplifyLoading(true);
    try {
      const simplifiedResponse = await simplifyText(
        response.response_text,
        response.response_id
      );
      setSimplification(simplifiedResponse);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to simplify text');
    } finally {
      setSimplifyLoading(false);
    }
  };

  /**
   * Parse response text and highlight [UNCERTAIN]...[/UNCERTAIN] tags
   */
  const renderResponseText = (text: string) => {
    const parts: React.ReactNode[] = [];
    let lastIndex = 0;
    const uncertainRegex = /\[UNCERTAIN\](.*?)\[\/UNCERTAIN\]/gs;
    let match;

    while ((match = uncertainRegex.exec(text)) !== null) {
      // Add text before the uncertain tag
      if (match.index > lastIndex) {
        parts.push(text.substring(lastIndex, match.index));
      }
      
      // Add highlighted uncertain text
      parts.push(
        <span key={match.index} className="uncertain-text">
          {match[1]}
        </span>
      );
      
      lastIndex = match.index + match[0].length;
    }

    // Add remaining text
    if (lastIndex < text.length) {
      parts.push(text.substring(lastIndex));
    }

    return parts.length > 0 ? parts : text;
  };

  return (
    <div className="query-interface">
      <form onSubmit={handleSubmit} className="query-form">
        <div className="form-group">
          <label htmlFor="query-input">Ask a question:</label>
          <textarea
            id="query-input"
            value={queryText}
            onChange={(e) => setQueryText(e.target.value)}
            placeholder="Enter your question here..."
            rows={4}
            disabled={loading}
          />
        </div>
        <button type="submit" disabled={loading} className="submit-button">
          {loading ? 'Processing...' : 'Submit Query'}
        </button>
      </form>

      {error && (
        <div className="error-message">
          Error: {error}
        </div>
      )}

      {response && (
        <div className="response-container">
          <div className="response-header">
            <h3>AI Response</h3>
            <div className="response-actions">
              <button
                onClick={handleChallenge}
                disabled={challengeLoading}
                className="action-button challenge-button"
              >
                {challengeLoading ? 'Loading...' : 'Challenge Me'}
              </button>
              <button
                onClick={handleSimplify}
                disabled={simplifyLoading}
                className="action-button simplify-button"
              >
                {simplifyLoading ? 'Loading...' : 'Simplify'}
              </button>
            </div>
          </div>

          <div className="response-text">
            {renderResponseText(response.response_text)}
          </div>

          <ConfidenceDisplay confidence={response.confidence} />

          {challenge && (
            <ChallengeDisplay
              challenge={challenge}
              onClose={() => setChallenge(null)}
            />
          )}

          {simplification && (
            <SimplificationToggle
              simplification={simplification}
              onClose={() => setSimplification(null)}
            />
          )}
        </div>
      )}
    </div>
  );
};
