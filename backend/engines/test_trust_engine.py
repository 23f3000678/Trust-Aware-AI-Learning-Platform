"""
Basic tests for TrustEngine class.

These tests demonstrate the TrustEngine API and validate basic functionality.
Note: Tests that call the GROQ API require a valid API key and will incur costs.
"""

import pytest
from backend.engines.trust_engine import TrustEngine
from backend.models.schemas import ConfidenceScore


class TestTrustEngineInit:
    """Tests for TrustEngine initialization."""
    
    def test_init_without_api_key_raises_error(self, monkeypatch):
        """Test that TrustEngine raises error when no API key is available."""
        monkeypatch.delenv("GROQ_API_KEY", raising=False)
        
        with pytest.raises(ValueError, match="Groq API key is required"):
            TrustEngine()
    
    def test_init_with_api_key_parameter(self):
        """Test that TrustEngine accepts API key as parameter."""
        engine = TrustEngine(api_key="test-key-123")
        assert engine.api_key == "test-key-123"
    
    def test_init_with_env_var(self, monkeypatch):
        """Test that TrustEngine reads API key from environment."""
        monkeypatch.setenv("GROQ_API_KEY", "env-key-456")
        engine = TrustEngine()
        assert engine.api_key == "env-key-456"


class TestComputeConfidence:
    """Tests for compute_confidence method."""
    
    def test_empty_response_text_raises_error(self):
        """Test that empty response text raises ValueError."""
        engine = TrustEngine(api_key="test-key")
        
        with pytest.raises(ValueError, match="Response text cannot be empty"):
            engine.compute_confidence("", "What is Python?")
    
    def test_empty_query_text_raises_error(self):
        """Test that empty query text raises ValueError."""
        engine = TrustEngine(api_key="test-key")
        
        with pytest.raises(ValueError, match="Query text cannot be empty"):
            engine.compute_confidence("Python is a programming language", "")
    
    def test_whitespace_only_texts_raise_error(self):
        """Test that whitespace-only texts raise ValueError."""
        engine = TrustEngine(api_key="test-key")
        
        with pytest.raises(ValueError, match="Response text cannot be empty"):
            engine.compute_confidence("   ", "What is Python?")
        
        with pytest.raises(ValueError, match="Query text cannot be empty"):
            engine.compute_confidence("Python is a language", "   ")


class TestPromptBuilding:
    """Tests for internal prompt building."""
    
    def test_build_analysis_prompt_format(self):
        """Test that analysis prompt is properly formatted."""
        engine = TrustEngine(api_key="test-key")
        
        query = "What is machine learning?"
        response = "Machine learning is a subset of AI."
        
        prompt = engine._build_analysis_prompt(query, response)
        
        assert "Question: What is machine learning?" in prompt
        assert "Answer: Machine learning is a subset of AI." in prompt
        assert "confidence_score" in prompt
        assert "justification" in prompt
        assert "question_clarity" in prompt
        assert "topic_complexity" in prompt
        assert "missing_information" in prompt


class TestResponseParsing:
    """Tests for LLM response parsing."""
    
    def test_parse_valid_response(self):
        """Test parsing of valid LLM response."""
        engine = TrustEngine(api_key="test-key")
        
        valid_response = """{
            "confidence_score": 85,
            "justification": "Clear question with comprehensive answer",
            "question_clarity": "High",
            "topic_complexity": "Medium",
            "missing_information": "No"
        }"""
        
        result = engine._parse_llm_response(valid_response)
        
        assert result["confidence_score"] == 85
        assert result["justification"] == "Clear question with comprehensive answer"
        assert result["question_clarity"] == "High"
        assert result["topic_complexity"] == "Medium"
        assert result["missing_information"] == "No"
    
    def test_parse_missing_field_raises_error(self):
        """Test that missing required field raises RuntimeError."""
        engine = TrustEngine(api_key="test-key")
        
        invalid_response = """{
            "confidence_score": 85,
            "justification": "Test"
        }"""
        
        with pytest.raises(RuntimeError, match="Missing required field"):
            engine._parse_llm_response(invalid_response)
    
    def test_parse_invalid_score_raises_error(self):
        """Test that invalid confidence score raises RuntimeError."""
        engine = TrustEngine(api_key="test-key")
        
        invalid_response = """{
            "confidence_score": 150,
            "justification": "Test",
            "question_clarity": "High",
            "topic_complexity": "Medium",
            "missing_information": "No"
        }"""
        
        with pytest.raises(RuntimeError, match="Invalid confidence_score"):
            engine._parse_llm_response(invalid_response)
    
    def test_parse_invalid_clarity_raises_error(self):
        """Test that invalid question_clarity raises RuntimeError."""
        engine = TrustEngine(api_key="test-key")
        
        invalid_response = """{
            "confidence_score": 85,
            "justification": "Test",
            "question_clarity": "VeryHigh",
            "topic_complexity": "Medium",
            "missing_information": "No"
        }"""
        
        with pytest.raises(RuntimeError, match="Invalid question_clarity"):
            engine._parse_llm_response(invalid_response)


class TestConfidenceScoreBuilding:
    """Tests for building ConfidenceScore objects."""
    
    def test_build_confidence_score_with_high_confidence(self):
        """Test building ConfidenceScore with high confidence (no warning)."""
        engine = TrustEngine(api_key="test-key")
        
        analysis = {
            "confidence_score": 85,
            "justification": "Clear and complete answer",
            "question_clarity": "High",
            "topic_complexity": "Low",
            "missing_information": "No"
        }
        
        result = engine._build_confidence_score(analysis)
        
        assert isinstance(result, ConfidenceScore)
        assert result.score == 85.0
        assert result.justification == "Clear and complete answer"
        assert result.should_warn is False
        assert result.breakdown.question_clarity == "High"
        assert result.breakdown.topic_complexity == "Low"
        assert result.breakdown.missing_information == "No"
    
    def test_build_confidence_score_with_low_confidence(self):
        """Test building ConfidenceScore with low confidence (warning)."""
        engine = TrustEngine(api_key="test-key")
        
        analysis = {
            "confidence_score": 45,
            "justification": "Unclear question with incomplete answer",
            "question_clarity": "Low",
            "topic_complexity": "High",
            "missing_information": "Yes"
        }
        
        result = engine._build_confidence_score(analysis)
        
        assert result.score == 45.0
        assert result.should_warn is True
        assert result.breakdown.question_clarity == "Low"
        assert result.breakdown.topic_complexity == "High"
        assert result.breakdown.missing_information == "Yes"
    
    def test_build_confidence_score_at_threshold(self):
        """Test building ConfidenceScore at warning threshold (70)."""
        engine = TrustEngine(api_key="test-key")
        
        analysis = {
            "confidence_score": 70,
            "justification": "Adequate answer",
            "question_clarity": "Medium",
            "topic_complexity": "Medium",
            "missing_information": "No"
        }
        
        result = engine._build_confidence_score(analysis)
        
        assert result.score == 70.0
        assert result.should_warn is False  # 70 is not below threshold
        
        # Test just below threshold
        analysis["confidence_score"] = 69
        result = engine._build_confidence_score(analysis)
        assert result.should_warn is True


# Integration test (requires valid API key and will incur costs)
@pytest.mark.integration
@pytest.mark.skip(reason="Requires valid GROQ API key and incurs costs")
class TestTrustEngineIntegration:
    """Integration tests that call the actual GROQ API."""
    
    def test_compute_confidence_real_api(self):
        """Test compute_confidence with real GROQ API call."""
        engine = TrustEngine()  # Uses GROQ_API_KEY from environment
        
        query = "What is the capital of France?"
        response = "The capital of France is Paris."
        
        result = engine.compute_confidence(response, query)
        
        assert isinstance(result, ConfidenceScore)
        assert 0 <= result.score <= 100
        assert len(result.justification) > 0
        assert result.breakdown.question_clarity in ["High", "Medium", "Low"]
        assert result.breakdown.topic_complexity in ["Low", "Medium", "High"]
        assert result.breakdown.missing_information in ["Yes", "No"]
