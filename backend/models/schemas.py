"""
Pydantic data models for Trust-Aware AI Learning Platform MVP.

These models support core trust calibration features with confidence breakdown,
enabling transparent AI responses with uncertainty indicators.
"""

from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field, field_validator


class ConfidenceBreakdown(BaseModel):
    """
    Breakdown of confidence factors for AI responses.
    
    Provides transparency into why the AI has a certain confidence level
    by analyzing question clarity, topic complexity, and information gaps.
    """
    question_clarity: Literal["High", "Medium", "Low"] = Field(
        ...,
        description="How clearly the question is formulated"
    )
    topic_complexity: Literal["Low", "Medium", "High"] = Field(
        ...,
        description="Complexity level of the topic being addressed"
    )
    missing_information: Literal["Yes", "No"] = Field(
        ...,
        description="Whether critical information is missing for a complete answer"
    )


class ConfidenceScore(BaseModel):
    """
    Confidence score for AI responses with justification and breakdown.
    
    Includes automatic warning flag for low confidence responses (< 70).
    """
    score: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Confidence score between 0 and 100"
    )
    justification: str = Field(
        ...,
        min_length=1,
        description="Human-readable explanation of the confidence score"
    )
    breakdown: ConfidenceBreakdown = Field(
        ...,
        description="Detailed breakdown of confidence factors"
    )
    should_warn: bool = Field(
        ...,
        description="True if confidence score is below 70 (warning threshold)"
    )
    
    @field_validator('justification')
    @classmethod
    def justification_not_empty(cls, v: str) -> str:
        """Ensure justification is not just whitespace."""
        if not v.strip():
            raise ValueError("Justification cannot be empty or whitespace only")
        return v


class QueryContext(BaseModel):
    """
    Context information for a user query.
    
    Captures the query text, timing, and optional session tracking.
    """
    query_text: str = Field(
        ...,
        min_length=1,
        description="The user's query text"
    )
    timestamp: datetime = Field(
        ...,
        description="When the query was submitted"
    )
    session_id: Optional[str] = Field(
        default=None,
        description="Optional session identifier for tracking related queries"
    )
    
    @field_validator('query_text')
    @classmethod
    def query_text_not_empty(cls, v: str) -> str:
        """Ensure query text is not just whitespace."""
        if not v.strip():
            raise ValueError("Query text cannot be empty or whitespace only")
        return v


class AIResponse(BaseModel):
    """
    AI-generated response with confidence scoring and uncertainty markers.
    
    Response text may contain [UNCERTAIN]...[/UNCERTAIN] tags to highlight
    uncertain portions of the response.
    """
    response_text: str = Field(
        ...,
        min_length=1,
        description="AI response text with optional [UNCERTAIN] tags"
    )
    confidence: ConfidenceScore = Field(
        ...,
        description="Confidence score with breakdown and justification"
    )
    response_id: str = Field(
        ...,
        min_length=1,
        description="Unique identifier for this response"
    )
    timestamp: datetime = Field(
        ...,
        description="When the response was generated"
    )
    
    @field_validator('response_text', 'response_id')
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        """Ensure text fields are not just whitespace."""
        if not v.strip():
            raise ValueError("Text field cannot be empty or whitespace only")
        return v


class Challenge(BaseModel):
    """
    User challenge to an AI response.
    
    Allows users to question or request clarification on specific responses,
    supporting the trust calibration learning process.
    """
    challenge_id: str = Field(
        ...,
        min_length=1,
        description="Unique identifier for this challenge"
    )
    question_text: str = Field(
        ...,
        min_length=1,
        description="The user's challenge or question"
    )
    related_response_id: str = Field(
        ...,
        min_length=1,
        description="ID of the AI response being challenged"
    )
    
    @field_validator('challenge_id', 'question_text', 'related_response_id')
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        """Ensure text fields are not just whitespace."""
        if not v.strip():
            raise ValueError("Text field cannot be empty or whitespace only")
        return v


class SimplifiedResponse(BaseModel):
    """
    Simplified version of an AI response for improved comprehension.
    
    Provides an easier-to-understand version of complex responses while
    maintaining the original for reference.
    """
    original_text: str = Field(
        ...,
        min_length=1,
        description="Original AI response text"
    )
    simplified_text: str = Field(
        ...,
        min_length=1,
        description="Simplified version of the response"
    )
    response_id: str = Field(
        ...,
        min_length=1,
        description="ID of the response being simplified"
    )
    
    @field_validator('original_text', 'simplified_text', 'response_id')
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        """Ensure text fields are not just whitespace."""
        if not v.strip():
            raise ValueError("Text field cannot be empty or whitespace only")
        return v
