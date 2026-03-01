/**
 * TypeScript type definitions for Trust-Aware AI Learning Platform MVP
 * These types match the Python Pydantic models in backend/models/schemas.py
 */

/**
 * Breakdown of confidence factors for an AI response
 */
export interface ConfidenceBreakdown {
  /** Clarity of the user's question */
  question_clarity: "High" | "Medium" | "Low";
  /** Complexity of the topic being discussed */
  topic_complexity: "Low" | "Medium" | "High";
  /** Whether critical information is missing */
  missing_information: "Yes" | "No";
}

/**
 * Confidence score for an AI response with justification
 */
export interface ConfidenceScore {
  /** Confidence score from 0-100 */
  score: number;
  /** Human-readable explanation of the confidence score */
  justification: string;
  /** Detailed breakdown of confidence factors */
  breakdown: ConfidenceBreakdown;
  /** Whether to display a warning to the user */
  should_warn: boolean;
}

/**
 * Context information for a user query
 */
export interface QueryContext {
  /** The user's question or query text */
  query_text: string;
  /** ISO 8601 datetime string when the query was made */
  timestamp: string;
  /** Optional session identifier for tracking */
  session_id?: string | null;
}

/**
 * AI-generated response with confidence metadata
 */
export interface AIResponse {
  /** Response text, may contain [UNCERTAIN]...[/UNCERTAIN] tags */
  response_text: string;
  /** Confidence score and breakdown */
  confidence: ConfidenceScore;
  /** Unique identifier for this response */
  response_id: string;
  /** ISO 8601 datetime string when the response was generated */
  timestamp: string;
}

/**
 * Challenge question generated to help verify understanding
 */
export interface Challenge {
  /** Unique identifier for this challenge */
  challenge_id: string;
  /** The challenge question text */
  question_text: string;
  /** ID of the response this challenge relates to */
  related_response_id: string;
}

/**
 * Simplified version of a response for easier understanding
 */
export interface SimplifiedResponse {
  /** Original complex text */
  original_text: string;
  /** Simplified version of the text */
  simplified_text: string;
  /** ID of the response this simplification relates to */
  response_id: string;
}

// API Request Types

/**
 * Request payload for querying the AI
 */
export interface QueryRequest {
  /** The user's question or query text */
  query_text: string;
}

/**
 * Request payload for generating a challenge question
 */
export interface ChallengeRequest {
  /** ID of the response to challenge */
  response_id: string;
  /** Text of the response to challenge */
  response_text: string;
}

/**
 * Request payload for simplifying text
 */
export interface SimplifyRequest {
  /** Text to simplify */
  text: string;
  /** ID of the response being simplified */
  response_id: string;
}
