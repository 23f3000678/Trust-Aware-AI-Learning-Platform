"""
Basic validation tests for Pydantic schemas.

Run with: pytest backend/models/test_schemas.py
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from .schemas import (
    ConfidenceBreakdown,
    ConfidenceScore,
    QueryContext,
    AIResponse,
    Challenge,
    SimplifiedResponse,
)


def test_confidence_breakdown_valid():
    """Test valid ConfidenceBreakdown creation."""
    breakdown = ConfidenceBreakdown(
        question_clarity="High",
        topic_complexity="Low",
        missing_information="No"
    )
    assert breakdown.question_clarity == "High"
    assert breakdown.topic_complexity == "Low"
    assert breakdown.missing_information == "No"


def test_confidence_score_valid():
    """Test valid ConfidenceScore with proper range."""
    breakdown = ConfidenceBreakdown(
        question_clarity="Medium",
        topic_complexity="Medium",
        missing_isnformation="No"
    )
    score = ConfidenceScore(
        score=85.5,
        justification="High confidence due to clear question and available data",
        breakdown=breakdown,
        should_warn=False
    )
    assert score.score == 85.5
    assert score.should_warn is False


def test_confidence_score_invalid_range():
    """Test ConfidenceScore rejects out-of-range values."""
    breakdown = ConfidenceBreakdown(
        question_clarity="High",
        topic_complexity="Low",
        missing_information="No"
    )
    
    with pytest.raises(ValidationError):
        ConfidenceScore(
            score=150.0,  # Invalid: > 100
            justification="Test",
            breakdown=breakdown,
            should_warn=False
        )
    
    with pytest.raises(ValidationError):
        ConfidenceScore(
            score=-10.0,  # Invalid: < 0
            justification="Test",
            breakdown=breakdown,
            should_warn=False
        )


def test_confidence_score_empty_justification():
    """Test ConfidenceScore rejects empty justification."""
    breakdown = ConfidenceBreakdown(
        question_clarity="High",
        topic_complexity="Low",
        missing_information="No"
    )
    
    with pytest.raises(ValidationError):
        ConfidenceScore(
            score=80.0,
            justification="   ",  # Whitespace only
            breakdown=breakdown,
            should_warn=False
        )


def test_query_context_valid():
    """Test valid QueryContext creation."""
    context = QueryContext(
        query_text="What is machine learning?",
        timestamp=datetime.now(),
        session_id="session-123"
    )
    assert context.query_text == "What is machine learning?"
    assert context.session_id == "session-123"


def test_query_context_optional_session():
    """Test QueryContext with optional session_id."""
    context = QueryContext(
        query_text="What is AI?",
        timestamp=datetime.now()
    )
    assert context.session_id is None


def test_ai_response_valid():
    """Test valid AIResponse creation."""
    breakdown = ConfidenceBreakdown(
        question_clarity="High",
        topic_complexity="Medium",
        missing_information="No"
    )
    confidence = ConfidenceScore(
        score=90.0,
        justification="Clear question with comprehensive answer",
        breakdown=breakdown,
        should_warn=False
    )
    response = AIResponse(
        response_text="Machine learning is [UNCERTAIN]a subset of AI[/UNCERTAIN].",
        confidence=confidence,
        response_id="resp-001",
        timestamp=datetime.now()
    )
    assert "UNCERTAIN" in response.response_text
    assert response.response_id == "resp-001"


def test_challenge_valid():
    """Test valid Challenge creation."""
    challenge = Challenge(
        challenge_id="chal-001",
        question_text="Can you explain this further?",
        related_response_id="resp-001"
    )
    assert challenge.challenge_id == "chal-001"
    assert challenge.related_response_id == "resp-001"


def test_simplified_response_valid():
    """Test valid SimplifiedResponse creation."""
    simplified = SimplifiedResponse(
        original_text="Complex technical explanation with jargon.",
        simplified_text="Simple explanation in plain language.",
        response_id="resp-001"
    )
    assert simplified.response_id == "resp-001"
    assert len(simplified.simplified_text) > 0


def test_empty_text_validation():
    """Test that empty text fields are rejected across models."""
    with pytest.raises(ValidationError):
        QueryContext(
            query_text="   ",  # Whitespace only
            timestamp=datetime.now()
        )
    
    with pytest.raises(ValidationError):
        Challenge(
            challenge_id="",  # Empty
            question_text="Test",
            related_response_id="resp-001"
        )
