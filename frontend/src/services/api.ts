/**
 * API client for Trust-Aware AI Learning Platform
 * Handles all communication with the FastAPI backend
 */

import axios from 'axios';
import type {
  QueryRequest,
  AIResponse,
  ChallengeRequest,
  Challenge,
  SimplifyRequest,
  SimplifiedResponse,
} from '../types';

const API_BASE_URL = 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Submit a query to the AI and get a response with confidence scores
 */
export const submitQuery = async (queryText: string): Promise<AIResponse> => {
  const request: QueryRequest = { query_text: queryText };
  const response = await apiClient.post<AIResponse>('/api/query', request);
  return response.data;
};

/**
 * Generate a challenge question for a given response
 */
export const generateChallenge = async (
  responseId: string,
  responseText: string
): Promise<Challenge> => {
  const request: ChallengeRequest = {
    response_id: responseId,
    response_text: responseText,
  };
  const response = await apiClient.post<Challenge>('/api/challenge', request);
  return response.data;
};

/**
 * Simplify a response text for easier understanding
 */
export const simplifyText = async (
  text: string,
  responseId: string
): Promise<SimplifiedResponse> => {
  const request: SimplifyRequest = {
    text,
    response_id: responseId,
  };
  const response = await apiClient.post<SimplifiedResponse>('/api/simplify', request);
  return response.data;
};
