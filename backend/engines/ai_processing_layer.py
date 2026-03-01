"""
AI Processing Layer for Trust-Aware AI Learning Platform MVP.

This module orchestrates LLM queries with enhanced prompting to generate
responses with uncertainty tagging and confidence scoring.
"""

import os
import json
import uuid
from datetime import datetime
from typing import Dict, Any
from groq import Groq
from dotenv import load_dotenv

from backend.models.schemas import AIResponse, ConfidenceScore, ConfidenceBreakdown


# Load environment variables
load_dotenv()


class AIProcessingLayer:
    """
    Orchestrates LLM queries with structured prompting for uncertainty tagging.
    
    The AIProcessingLayer generates AI responses with embedded uncertainty markers
    and confidence assessments, enabling transparent trust calibration in the
    learning platform.
    """
    
    def __init__(self, api_key: str | None = None):
        """
        Initialize the AIProcessingLayer with GROQ client.
        
        Args:
            api_key: GROQ API key. If None, reads from GROQ_API_KEY env var.
        
        Raises:
            ValueError: If no API key is provided or found in environment.
        """
        self.api_key = api_key or os.getenv("GROQ_API_KEY")

        if not self.api_key:
            raise ValueError("Groq API key is required")

        self.client = Groq(api_key=self.api_key)

        self.model = "llama-3.1-8b-instant"
    
    def query_llm(self, query_text: str) -> AIResponse:
        """
        Query the LLM with enhanced prompting for uncertainty tagging.
        
        Generates a structured response with uncertainty markers, confidence
        scoring, and detailed breakdown of confidence factors.
        
        Args:
            query_text: The user's query text
        
        Returns:
            AIResponse object with tagged response and confidence assessment
        
        Raises:
            ValueError: If query text is empty
            RuntimeError: If LLM query fails or returns invalid data
        """
        if not query_text or not query_text.strip():
            raise ValueError("Query text cannot be empty")
        
        # Construct the enhanced prompt
        prompt = self._build_enhanced_prompt(query_text)
        
        try:
            # Call GROQ API
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an educational AI assistant that promotes "
                            "trust calibration by being transparent about uncertainty."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,  # Balanced temperature for educational responses
                response_format={"type": "json_object"}
            )
            
            # Extract and parse response
            response_content = completion.choices[0].message.content
            if not response_content:
                raise RuntimeError("Empty response from LLM")
            
            llm_data = self._parse_llm_response(response_content)
            
            # Build AIResponse object
            return self._build_ai_response(llm_data)
            
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse LLM response as JSON: {e}")
        except Exception as e:
            raise RuntimeError(f"LLM query failed: {e}")

    def _build_enhanced_prompt(self, query_text: str) -> str:
        """
        Build the enhanced prompt with uncertainty tagging instructions.
        
        Args:
            query_text: The user's query
        
        Returns:
            Formatted prompt string with structured output requirements
        """
        return f"""You are an educational AI assistant that promotes trust calibration.

Answer the following question, and tag any uncertain statements with [UNCERTAIN]...[/UNCERTAIN].

Question: {query_text}

Provide your response in JSON format:
{{
  "response_text": "<answer with [UNCERTAIN] tags>",
  "confidence_score": <0-100>,
  "confidence_justification": "<explanation>",
  "question_clarity": "<High/Medium/Low>",
  "topic_complexity": "<Low/Medium/High>",
  "missing_information": "<Yes/No>"
}}

Guidelines:
- Tag sentences where you're uncertain with [UNCERTAIN]...[/UNCERTAIN]
- Be honest about limitations
- Provide clear, educational responses
- Include confidence assessment
- confidence_score: 0-100 integer based on your certainty
- confidence_justification: Explain why you assigned this confidence level
- question_clarity: How well-formulated the question is
- topic_complexity: Inherent difficulty of the topic
- missing_information: Whether you lack critical information to answer fully

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
        llm_data = json.loads(response_content)
        
        # Validate required fields
        required_fields = [
            "response_text",
            "confidence_score",
            "confidence_justification",
            "question_clarity",
            "topic_complexity",
            "missing_information"
        ]
        
        for field in required_fields:
            if field not in llm_data:
                raise RuntimeError(f"Missing required field: {field}")
        
        # Validate field values
        if not llm_data["response_text"] or not llm_data["response_text"].strip():
            raise RuntimeError("response_text cannot be empty")
        
        score = llm_data["confidence_score"]
        if not isinstance(score, (int, float)) or not (0 <= score <= 100):
            raise RuntimeError(
                f"Invalid confidence_score: {score}. Must be 0-100."
            )
        
        if not llm_data["confidence_justification"] or not llm_data["confidence_justification"].strip():
            raise RuntimeError("confidence_justification cannot be empty")
        
        if llm_data["question_clarity"] not in ["High", "Medium", "Low"]:
            raise RuntimeError(
                f"Invalid question_clarity: {llm_data['question_clarity']}"
            )
        
        if llm_data["topic_complexity"] not in ["Low", "Medium", "High"]:
            raise RuntimeError(
                f"Invalid topic_complexity: {llm_data['topic_complexity']}"
            )
        
        if llm_data["missing_information"] not in ["Yes", "No"]:
            raise RuntimeError(
                f"Invalid missing_information: {llm_data['missing_information']}"
            )
        
        return llm_data
    
    def _build_ai_response(self, llm_data: Dict[str, Any]) -> AIResponse:
        """
        Build an AIResponse object from parsed LLM data.
        
        Args:
            llm_data: Validated data dictionary from LLM
        
        Returns:
            AIResponse object with unique ID and timestamp
        """
        # Build confidence breakdown
        breakdown = ConfidenceBreakdown(
            question_clarity=llm_data["question_clarity"],
            topic_complexity=llm_data["topic_complexity"],
            missing_information=llm_data["missing_information"]
        )
        
        # Build confidence score
        score = float(llm_data["confidence_score"])
        should_warn = score < 70.0
        
        confidence = ConfidenceScore(
            score=score,
            justification=llm_data["confidence_justification"].strip(),
            breakdown=breakdown,
            should_warn=should_warn
        )
        
        # Generate unique response ID
        response_id = str(uuid.uuid4())
        
        # Create AIResponse
        return AIResponse(
            response_text=llm_data["response_text"].strip(),
            confidence=confidence,
            response_id=response_id,
            timestamp=datetime.now()
        )
