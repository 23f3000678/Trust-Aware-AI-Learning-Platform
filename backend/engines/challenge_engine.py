"""
Challenge Engine for Trust-Aware AI Learning Platform MVP.

This module generates interactive learning challenges to help users test
their understanding of AI responses through verification questions.
"""

import os
import json
import uuid
from typing import Dict, Any
from groq import Groq
from dotenv import load_dotenv

from backend.models.schemas import Challenge


# Load environment variables
load_dotenv()


class ChallengeEngine:
    """
    Generates verification challenges based on Q&A pairs.
    
    The ChallengeEngine creates educational follow-up questions that help
    learners test their understanding of AI responses, supporting active
    learning and trust calibration.
    """
    
    def __init__(self, api_key: str | None = None):
        """
        Initialize the ChallengeEngine with GROQ client.
        
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
    
    def generate_challenge(
        self,
        response_text: str,
        query_text: str,
        response_id: str
    ) -> Challenge:
        """
        Generate a verification challenge based on a Q&A pair.
        
        Creates one verification-style follow-up question to help the learner
        test their understanding of the AI response.
        
        Args:
            response_text: The AI's response text
            query_text: The original user query
            response_id: ID of the response being challenged
        
        Returns:
            Challenge object with verification question
        
        Raises:
            ValueError: If response_text or query_text is empty
            RuntimeError: If LLM query fails or returns invalid data
        """
        if not response_text or not response_text.strip():
            raise ValueError("Response text cannot be empty")
        
        if not query_text or not query_text.strip():
            raise ValueError("Query text cannot be empty")
        
        if not response_id or not response_id.strip():
            raise ValueError("Response ID cannot be empty")
        
        # Construct the challenge generation prompt
        prompt = self._build_challenge_prompt(query_text, response_text)
        
        try:
            # Call GROQ API
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an educational AI that creates verification "
                            "questions to help learners test their understanding."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,  # Balanced temperature for educational content
                response_format={"type": "json_object"}
            )
            
            # Extract and parse response
            response_content = completion.choices[0].message.content
            if not response_content:
                raise RuntimeError("Empty response from LLM")
            
            llm_data = self._parse_llm_response(response_content)
            
            # Build Challenge object
            return self._build_challenge(llm_data, response_id)
            
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse LLM response as JSON: {e}")
        except Exception as e:
            raise RuntimeError(f"Challenge generation failed: {e}")
    
    def _build_challenge_prompt(
        self,
        query_text: str,
        response_text: str
    ) -> str:
        """
        Build the prompt for challenge generation.
        
        Args:
            query_text: The original user query
            response_text: The AI's response
        
        Returns:
            Formatted prompt string with structured output requirements
        """
        return f"""Based on this Q&A pair, generate ONE verification question to help the learner test their understanding.

Question: {query_text}
Answer: {response_text}

Generate a verification question in JSON format:
{{
  "question_text": "<verification question>"
}}

Guidelines:
- Create a question that tests understanding of the answer
- Use "Is this correct?" or "Which statement is accurate?" format
- Keep it simple and focused
- Make it educational, not tricky
- The question should help reinforce key concepts from the answer
- Avoid questions that are too easy or too difficult

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
        
        # Validate required field
        if "question_text" not in llm_data:
            raise RuntimeError("Missing required field: question_text")
        
        # Validate field value
        if not llm_data["question_text"] or not llm_data["question_text"].strip():
            raise RuntimeError("question_text cannot be empty")
        
        return llm_data
    
    def _build_challenge(
        self,
        llm_data: Dict[str, Any],
        response_id: str
    ) -> Challenge:
        """
        Build a Challenge object from parsed LLM data.
        
        Args:
            llm_data: Validated data dictionary from LLM
            response_id: ID of the response being challenged
        
        Returns:
            Challenge object with unique ID
        """
        # Generate unique challenge ID
        challenge_id = str(uuid.uuid4())
        
        # Create Challenge
        return Challenge(
            challenge_id=challenge_id,
            question_text=llm_data["question_text"].strip(),
            related_response_id=response_id
        )
