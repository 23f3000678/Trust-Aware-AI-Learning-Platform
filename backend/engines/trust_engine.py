"""
Trust Engine for LLM-based confidence scoring.

This module provides the core TrustEngine class that analyzes AI responses
using LLM-based analysis to compute confidence scores with detailed breakdowns.
"""

import os
import json
from typing import Dict, Any
from groq import Groq
from dotenv import load_dotenv

from backend.models.schemas import ConfidenceScore, ConfidenceBreakdown


# Load environment variables
load_dotenv()


class TrustEngine:
    """
    Core engine for computing confidence scores using LLM-based analysis.
    
    The TrustEngine uses GROQ's API to analyze Q&A pairs and provide
    structured confidence assessments with detailed breakdowns of factors
    affecting confidence levels.
    """
    
    def __init__(self, api_key: str | None = None):
        """
        Initialize the TrustEngine with GROQ client.
        
        Args:
            api_key: GROQ API key. If None, reads from GROQ_API_KEY env var.
        
        Raises:
            ValueError: If no API key is provided or found in environment.
        """
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Groq API key is required. Provide via api_key parameter "
                "or GROQ_API_KEY environment variable."
            )
        
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.1-8b-instant"
    
    def compute_confidence(
        self,
        response_text: str,
        query_text: str
    ) -> ConfidenceScore:
        """
        Compute confidence score for an AI response using LLM analysis.
        
        Analyzes the Q&A pair to determine overall confidence, provide
        justification, and break down contributing factors.
        
        Args:
            response_text: The AI-generated response to analyze
            query_text: The original user query
        
        Returns:
            ConfidenceScore object with score, justification, and breakdown
        
        Raises:
            ValueError: If response or query text is empty
            RuntimeError: If LLM analysis fails or returns invalid data
        """
        if not response_text or not response_text.strip():
            raise ValueError("Response text cannot be empty")
        if not query_text or not query_text.strip():
            raise ValueError("Query text cannot be empty")
        
        # Construct the analysis prompt
        prompt = self._build_analysis_prompt(query_text, response_text)
        
        try:
            # Call GROQ API
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert at analyzing AI responses and "
                            "assessing confidence levels. Provide structured "
                            "JSON analysis of Q&A pairs."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,  # Lower temperature for more consistent analysis
                response_format={"type": "json_object"}
            )
            
            # Extract and parse response
            response_content = completion.choices[0].message.content
            if not response_content:
                raise RuntimeError("Empty response from LLM")
            
            analysis = self._parse_llm_response(response_content)
            
            # Build ConfidenceScore object
            return self._build_confidence_score(analysis)
            
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse LLM response as JSON: {e}")
        except Exception as e:
            raise RuntimeError(f"LLM analysis failed: {e}")
    
    def _build_analysis_prompt(self, query_text: str, response_text: str) -> str:
        """
        Build the structured prompt for LLM analysis.
        
        Args:
            query_text: The user's query
            response_text: The AI's response
        
        Returns:
            Formatted prompt string
        """
        return f"""Analyze this Q&A pair and provide confidence assessment:

Question: {query_text}

Answer: {response_text}

Provide your analysis in JSON format:
{{
  "confidence_score": <0-100>,
  "justification": "<explanation>",
  "question_clarity": "<High/Medium/Low>",
  "topic_complexity": "<Low/Medium/High>",
  "missing_information": "<Yes/No>"
}}

Guidelines:
- confidence_score: 0-100 integer based on answer quality and completeness
- justification: Clear explanation of why this confidence level was assigned
- question_clarity: How well-formulated and specific the question is
- topic_complexity: Inherent difficulty of the topic
- missing_information: Whether critical information is absent from the answer

Respond with ONLY the JSON object, no additional text."""
    
    def _parse_llm_response(self, response_content: str) -> Dict[str, Any]:
        """
        Parse and validate the LLM's JSON response.
        
        Args:
            response_content: Raw JSON string from LLM
        
        Returns:
            Parsed dictionary with validated fields
        
        Raises:
            RuntimeError: If response is missing required fields or has invalid values
        """
        analysis = json.loads(response_content)
        
        # Validate required fields
        required_fields = [
            "confidence_score",
            "justification",
            "question_clarity",
            "topic_complexity",
            "missing_information"
        ]
        
        for field in required_fields:
            if field not in analysis:
                raise RuntimeError(f"Missing required field: {field}")
        
        # Validate field values
        score = analysis["confidence_score"]
        if not isinstance(score, (int, float)) or not (0 <= score <= 100):
            raise RuntimeError(
                f"Invalid confidence_score: {score}. Must be 0-100."
            )
        
        if analysis["question_clarity"] not in ["High", "Medium", "Low"]:
            raise RuntimeError(
                f"Invalid question_clarity: {analysis['question_clarity']}"
            )
        
        if analysis["topic_complexity"] not in ["Low", "Medium", "High"]:
            raise RuntimeError(
                f"Invalid topic_complexity: {analysis['topic_complexity']}"
            )
        
        if analysis["missing_information"] not in ["Yes", "No"]:
            raise RuntimeError(
                f"Invalid missing_information: {analysis['missing_information']}"
            )
        
        if not analysis["justification"] or not analysis["justification"].strip():
            raise RuntimeError("Justification cannot be empty")
        
        return analysis
    
    def _build_confidence_score(self, analysis: Dict[str, Any]) -> ConfidenceScore:
        """
        Build a ConfidenceScore object from parsed analysis.
        
        Args:
            analysis: Validated analysis dictionary from LLM
        
        Returns:
            ConfidenceScore object
        """
        breakdown = ConfidenceBreakdown(
            question_clarity=analysis["question_clarity"],
            topic_complexity=analysis["topic_complexity"],
            missing_information=analysis["missing_information"]
        )
        
        score = float(analysis["confidence_score"])
        should_warn = score < 70.0
        
        return ConfidenceScore(
            score=score,
            justification=analysis["justification"].strip(),
            breakdown=breakdown,
            should_warn=should_warn
        )
