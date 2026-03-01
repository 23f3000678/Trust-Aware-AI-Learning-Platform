"""
Tests for ChallengeEngine class.

Run with: python -m pytest backend/engines/test_challenge_engine.py -v
"""

import pytest
from unittest.mock import Mock, patch
from backend.engines.challenge_engine import ChallengeEngine
from backend.models.schemas import Challenge


class TestChallengeEngineInit:
    """Test ChallengeEngine initialization."""
    
    def test_init_with_api_key(self):
        """Test initialization with explicit API key."""
        engine = ChallengeEngine(api_key="test-key-123")
        assert engine.api_key == "test-key-123"
        assert engine.model == "llama-3.1-8b-instant"
    
    def test_init_without_api_key_raises_error(self):
        """Test initialization without API key raises ValueError."""
        with patch.dict('os.environ', {}, clear=True):
            with pytest.raises(ValueError, match="Groq API key is required"):
                ChallengeEngine()
    
    def test_init_with_env_var(self):
        """Test initialization with API key from environment."""
        with patch.dict('os.environ', {'GROQ_API_KEY': 'env-key-456'}):
            engine = ChallengeEngine()
            assert engine.api_key == "env-key-456"


class TestGenerateChallenge:
    """Test challenge generation."""
    
    @pytest.fixture
    def engine(self):
        """Create a ChallengeEngine instance for testing."""
        return ChallengeEngine(api_key="test-key")
    
    def test_generate_challenge_empty_response_text(self, engine):
        """Test that empty response text raises ValueError."""
        with pytest.raises(ValueError, match="Response text cannot be empty"):
            engine.generate_challenge("", "What is Python?", "resp-123")
    
    def test_generate_challenge_empty_query_text(self, engine):
        """Test that empty query text raises ValueError."""
        with pytest.raises(ValueError, match="Query text cannot be empty"):
            engine.generate_challenge("Python is a language", "", "resp-123")
    
    def test_generate_challenge_empty_response_id(self, engine):
        """Test that empty response ID raises ValueError."""
        with pytest.raises(ValueError, match="Response ID cannot be empty"):
            engine.generate_challenge("Python is a language", "What is Python?", "")
    
    def test_generate_challenge_success(self, engine):
        """Test successful challenge generation."""
        # Mock GROQ API response
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = '''
        {
            "question_text": "Is Python a compiled or interpreted language?"
        }
        '''
        
        with patch.object(engine.client.chat.completions, 'create', return_value=mock_completion):
            challenge = engine.generate_challenge(
                response_text="Python is an interpreted programming language.",
                query_text="What is Python?",
                response_id="resp-123"
            )
        
        assert isinstance(challenge, Challenge)
        assert challenge.question_text == "Is Python a compiled or interpreted language?"
        assert challenge.related_response_id == "resp-123"
        assert len(challenge.challenge_id) > 0
    
    def test_generate_challenge_empty_llm_response(self, engine):
        """Test that empty LLM response raises RuntimeError."""
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = None
        
        with patch.object(engine.client.chat.completions, 'create', return_value=mock_completion):
            with pytest.raises(RuntimeError, match="Empty response from LLM"):
                engine.generate_challenge(
                    "Python is a language",
                    "What is Python?",
                    "resp-123"
                )
    
    def test_generate_challenge_invalid_json(self, engine):
        """Test that invalid JSON raises RuntimeError."""
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = "Not valid JSON"
        
        with patch.object(engine.client.chat.completions, 'create', return_value=mock_completion):
            with pytest.raises(RuntimeError, match="Failed to parse LLM response as JSON"):
                engine.generate_challenge(
                    "Python is a language",
                    "What is Python?",
                    "resp-123"
                )
    
    def test_generate_challenge_missing_question_text(self, engine):
        """Test that missing question_text raises RuntimeError."""
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = '{"wrong_field": "value"}'
        
        with patch.object(engine.client.chat.completions, 'create', return_value=mock_completion):
            with pytest.raises(RuntimeError, match="Missing required field: question_text"):
                engine.generate_challenge(
                    "Python is a language",
                    "What is Python?",
                    "resp-123"
                )
    
    def test_generate_challenge_empty_question_text(self, engine):
        """Test that empty question_text raises RuntimeError."""
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = '{"question_text": "   "}'
        
        with patch.object(engine.client.chat.completions, 'create', return_value=mock_completion):
            with pytest.raises(RuntimeError, match="question_text cannot be empty"):
                engine.generate_challenge(
                    "Python is a language",
                    "What is Python?",
                    "resp-123"
                )
    
    def test_generate_challenge_api_exception(self, engine):
        """Test that API exceptions are wrapped in RuntimeError."""
        with patch.object(engine.client.chat.completions, 'create', side_effect=Exception("API Error")):
            with pytest.raises(RuntimeError, match="Challenge generation failed"):
                engine.generate_challenge(
                    "Python is a language",
                    "What is Python?",
                    "resp-123"
                )


class TestBuildChallengePrompt:
    """Test prompt building."""
    
    @pytest.fixture
    def engine(self):
        """Create a ChallengeEngine instance for testing."""
        return ChallengeEngine(api_key="test-key")
    
    def test_build_challenge_prompt_contains_qa_pair(self, engine):
        """Test that prompt contains the Q&A pair."""
        prompt = engine._build_challenge_prompt(
            "What is Python?",
            "Python is a programming language."
        )
        
        assert "What is Python?" in prompt
        assert "Python is a programming language." in prompt
        assert "verification question" in prompt.lower()
        assert "JSON format" in prompt
    
    def test_build_challenge_prompt_contains_guidelines(self, engine):
        """Test that prompt contains generation guidelines."""
        prompt = engine._build_challenge_prompt(
            "What is Python?",
            "Python is a programming language."
        )
        
        assert "Guidelines:" in prompt
        assert "educational" in prompt.lower()
        assert "understanding" in prompt.lower()


class TestParseLLMResponse:
    """Test LLM response parsing."""
    
    @pytest.fixture
    def engine(self):
        """Create a ChallengeEngine instance for testing."""
        return ChallengeEngine(api_key="test-key")
    
    def test_parse_valid_response(self, engine):
        """Test parsing valid LLM response."""
        response = '{"question_text": "Is this correct?"}'
        result = engine._parse_llm_response(response)
        
        assert result["question_text"] == "Is this correct?"
    
    def test_parse_missing_question_text(self, engine):
        """Test parsing response without question_text."""
        response = '{"wrong_field": "value"}'
        
        with pytest.raises(RuntimeError, match="Missing required field: question_text"):
            engine._parse_llm_response(response)
    
    def test_parse_empty_question_text(self, engine):
        """Test parsing response with empty question_text."""
        response = '{"question_text": ""}'
        
        with pytest.raises(RuntimeError, match="question_text cannot be empty"):
            engine._parse_llm_response(response)
    
    def test_parse_whitespace_question_text(self, engine):
        """Test parsing response with whitespace-only question_text."""
        response = '{"question_text": "   "}'
        
        with pytest.raises(RuntimeError, match="question_text cannot be empty"):
            engine._parse_llm_response(response)


class TestBuildChallenge:
    """Test Challenge object building."""
    
    @pytest.fixture
    def engine(self):
        """Create a ChallengeEngine instance for testing."""
        return ChallengeEngine(api_key="test-key")
    
    def test_build_challenge_creates_valid_object(self, engine):
        """Test building a valid Challenge object."""
        llm_data = {"question_text": "Is this correct?"}
        challenge = engine._build_challenge(llm_data, "resp-123")
        
        assert isinstance(challenge, Challenge)
        assert challenge.question_text == "Is this correct?"
        assert challenge.related_response_id == "resp-123"
        assert len(challenge.challenge_id) > 0
    
    def test_build_challenge_strips_whitespace(self, engine):
        """Test that question text is stripped of whitespace."""
        llm_data = {"question_text": "  Is this correct?  "}
        challenge = engine._build_challenge(llm_data, "resp-123")
        
        assert challenge.question_text == "Is this correct?"
    
    def test_build_challenge_unique_ids(self, engine):
        """Test that each challenge gets a unique ID."""
        llm_data = {"question_text": "Is this correct?"}
        challenge1 = engine._build_challenge(llm_data, "resp-123")
        challenge2 = engine._build_challenge(llm_data, "resp-123")
        
        assert challenge1.challenge_id != challenge2.challenge_id
