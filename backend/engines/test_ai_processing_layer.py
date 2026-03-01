"""
Tests for AIProcessingLayer class.

Tests the core functionality of LLM query orchestration with uncertainty tagging.
"""

import pytest
from unittest.mock import Mock, patch
from datetime import datetime

from backend.engines.ai_processing_layer import AIProcessingLayer
from backend.models.schemas import AIResponse


class TestAIProcessingLayer:
    """Test suite for AIProcessingLayer."""
    
    def test_initialization_with_api_key(self):
        """Test initialization with explicit API key."""
        layer = AIProcessingLayer(api_key="test-key")
        assert layer.api_key == "test-key"
        assert layer.model == "llama-3.1-8b-instant"
    
    def test_initialization_without_api_key_raises_error(self):
        """Test initialization fails without API key."""
        with patch.dict('os.environ', {}, clear=True):
            with pytest.raises(ValueError, match="Groq API key is required"):
                AIProcessingLayer()
    
    def test_query_llm_with_empty_text_raises_error(self):
        """Test query_llm raises error for empty query text."""
        layer = AIProcessingLayer(api_key="test-key")
        
        with pytest.raises(ValueError, match="Query text cannot be empty"):
            layer.query_llm("")
        
        with pytest.raises(ValueError, match="Query text cannot be empty"):
            layer.query_llm("   ")
    
    @patch('backend.engines.ai_processing_layer.Groq')
    def test_query_llm_success(self, mock_Groq_class):
        """Test successful LLM query with structured response."""
        # Mock Groq client
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        # Mock completion response
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = """{
            "response_text": "Python is a high-level programming language. [UNCERTAIN]It was created around 1991.[/UNCERTAIN]",
            "confidence_score": 85,
            "confidence_justification": "I'm confident about Python being high-level but uncertain about the exact year.",
            "question_clarity": "High",
            "topic_complexity": "Low",
            "missing_information": "No"
        }"""
        
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Create layer and query
        layer = AIProcessingLayer(api_key="test-key")
        response = layer.query_llm("What is Python?")
        
        # Verify response structure
        assert isinstance(response, AIResponse)
        assert "Python is a high-level programming language" in response.response_text
        assert "[UNCERTAIN]" in response.response_text
        assert response.confidence.score == 85.0
        assert response.confidence.should_warn is False
        assert response.confidence.breakdown.question_clarity == "High"
        assert response.confidence.breakdown.topic_complexity == "Low"
        assert response.confidence.breakdown.missing_information == "No"
        assert response.response_id is not None
        assert isinstance(response.timestamp, datetime)
    
    @patch('backend.engines.ai_processing_layer.Groq')
    def test_query_llm_with_low_confidence(self, mock_Groq_class):
        """Test LLM query with low confidence triggers warning."""
        # Mock Groq client
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        # Mock completion response with low confidence
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = """{
            "response_text": "[UNCERTAIN]I'm not sure about this topic.[/UNCERTAIN]",
            "confidence_score": 45,
            "confidence_justification": "The question is unclear and I lack domain knowledge.",
            "question_clarity": "Low",
            "topic_complexity": "High",
            "missing_information": "Yes"
        }"""
        
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Create layer and query
        layer = AIProcessingLayer(api_key="test-key")
        response = layer.query_llm("Unclear question?")
        
        # Verify warning flag is set
        assert response.confidence.score == 45.0
        assert response.confidence.should_warn is True
        assert response.confidence.breakdown.question_clarity == "Low"
        assert response.confidence.breakdown.topic_complexity == "High"
        assert response.confidence.breakdown.missing_information == "Yes"
    
    @patch('backend.engines.ai_processing_layer.Groq')
    def test_query_llm_with_invalid_json_raises_error(self, mock_Groq_class):
        """Test query_llm handles invalid JSON gracefully."""
        # Mock Groq client
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        # Mock completion with invalid JSON
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = "Not valid JSON"
        
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Create layer and query
        layer = AIProcessingLayer(api_key="test-key")
        
        with pytest.raises(RuntimeError, match="Failed to parse LLM response as JSON"):
            layer.query_llm("Test question")
    
    @patch('backend.engines.ai_processing_layer.Groq')
    def test_query_llm_with_missing_fields_raises_error(self, mock_Groq_class):
        """Test query_llm validates required fields."""
        # Mock Groq client
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        # Mock completion with missing fields
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = """{
            "response_text": "Some response",
            "confidence_score": 80
        }"""
        
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Create layer and query
        layer = AIProcessingLayer(api_key="test-key")
        
        with pytest.raises(RuntimeError, match="Missing required field"):
            layer.query_llm("Test question")
    
    def test_build_enhanced_prompt(self):
        """Test enhanced prompt construction."""
        layer = AIProcessingLayer(api_key="test-key")
        prompt = layer._build_enhanced_prompt("What is AI?")
        
        assert "What is AI?" in prompt
        assert "[UNCERTAIN]" in prompt
        assert "JSON format" in prompt
        assert "confidence_score" in prompt
        assert "question_clarity" in prompt
        assert "topic_complexity" in prompt
        assert "missing_information" in prompt
