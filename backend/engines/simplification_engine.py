"""
Simplification Engine for Trust-Aware AI Learning Platform MVP.

This module provides LLM-based text simplification to make complex AI responses
easier to understand while preserving accuracy.
"""

import os
import json
from groq import Groq
from dotenv import load_dotenv

from backend.models.schemas import SimplifiedResponse


# Load environment variables
load_dotenv()


class SimplificationEngine:
    """
    LLM-based text simplification engine.
    
    The SimplificationEngine uses GROQ's API to simplify complex text,
    making it more accessible to a general audience while maintaining
    factual accuracy and core meaning.
    """
    
    def __init__(self, api_key: str | None = None):
        """
        Initialize the SimplificationEngine with GROQ client.
        
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
    
    def simplify(self, text: str, response_id: str) -> SimplifiedResponse:
        """
        Simplify text using LLM-based processing.
        
        Takes complex text and generates a simplified version that is easier
        to understand while preserving accuracy and core meaning.
        
        Args:
            text: The text to simplify
            response_id: Unique identifier for the response being simplified
        
        Returns:
            SimplifiedResponse object with original and simplified text
        
        Raises:
            ValueError: If text or response_id is empty
            RuntimeError: If LLM query fails or returns invalid data
        """
        if not text or not text.strip():
            raise ValueError("Text to simplify cannot be empty")
        
        if not response_id or not response_id.strip():
            raise ValueError("Response ID cannot be empty")
        
        # Construct the simplification prompt
        prompt = self._build_simplification_prompt(text)
        
        try:
            # Call GROQ API
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert at simplifying complex text "
                            "while maintaining accuracy and core meaning."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,  # Lower temperature for consistent simplification
                response_format={"type": "json_object"}
            )
            
            # Extract and parse response
            response_content = completion.choices[0].message.content
            if not response_content:
                raise RuntimeError("Empty response from LLM")
            
            simplified_text = self._parse_simplification_response(response_content)
            
            # Build SimplifiedResponse object
            return SimplifiedResponse(
                original_text=text.strip(),
                simplified_text=simplified_text,
                response_id=response_id.strip()
            )
            
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse LLM response as JSON: {e}")
        except Exception as e:
            raise RuntimeError(f"LLM simplification failed: {e}")
    
    def _build_simplification_prompt(self, text: str) -> str:
        """
        Build the simplification prompt with clear guidelines.
        
        Args:
            text: The text to simplify
        
        Returns:
            Formatted prompt string with structured output requirements
        """
        return f"""Simplify the following text to make it easier to understand while preserving accuracy.

Original text: {text}

Provide your simplified version in JSON format:
{{
  "simplified_text": "<simplified version>"
}}

Guidelines:
- Use simpler words and shorter sentences
- Break down complex concepts
- Maintain factual accuracy
- Keep the core meaning intact
- Make it accessible to a general audience

Respond with ONLY the JSON object, no additional text."""
    
    def _parse_simplification_response(self, response_content: str) -> str:
        """
        Parse and validate the LLM's simplification response.
        
        Args:
            response_content: Raw JSON string from LLM
        
        Returns:
            Simplified text string
        
        Raises:
            RuntimeError: If response is missing required field or has invalid value
        """
        llm_data = json.loads(response_content)
        
        # Validate required field
        if "simplified_text" not in llm_data:
            raise RuntimeError("Missing required field: simplified_text")
        
        simplified_text = llm_data["simplified_text"]
        
        # Validate field value
        if not simplified_text or not simplified_text.strip():
            raise RuntimeError("simplified_text cannot be empty")
        
        return simplified_text.strip()
