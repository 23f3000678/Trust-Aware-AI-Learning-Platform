"""
Unit tests for SimplificationEngine.

Tests LLM-based text simplification with proper error handling.
"""

import pytest
from unittest.mock import Mock, patch
from backend.engines.simplification_engine import SimplificationEngine
from backend.models.schemas import SimplifiedResponse


class TestSimplificationEngine:
    """Test suite for SimplificationEngine."""
    
    def test_init_with_api_key(self):
        """Test initialization with explicit API key."""
        engine = SimplificationEngine(api_key="test-key-123")
        assert engine.api_key == "test-key-123"
        assert engine.model == "llama-3.1-8b-instant"
    
    def test_init_without_api_key_raises_error(self):
        """Test initialization fails without API key."""
        with patch.dict('os.environ', {}, clear=True):
            with pytest.raises(ValueError, match="Groq API key is required"):
                SimplificationEngine()
    
    def test_init_with_env_var(self):
        """Test initialization with API key from environment."""
        with patch.dict('os.environ', {'GROQ_API_KEY': 'env-key-456'}):
            engine = SimplificationEngine()
            assert engine.api_key == "env-key-456"
    
    def test_simplify_empty_text_raises_error(self):
        """Test simplify raises error for empty text."""
        engine = SimplificationEngine(api_key="test-key")
        
        with pytest.raises(ValueError, match="Text to simplify cannot be empty"):
            engine.simplify("", "response-123")
        
        with pytest.raises(ValueError, match="Text to simplify cannot be empty"):
            engine.simplify("   ", "response-123")
    
    def test_simplify_empty_response_id_raises_error(self):
        """Test simplify raises error for empty response_id."""
        engine = SimplificationEngine(api_key="test-key")
        
        with pytest.raises(ValueError, match="Response ID cannot be empty"):
            engine.simplify("Some text", "")
        
        with pytest.raises(ValueError, match="Response ID cannot be empty"):
            engine.simplify("Some text", "   ")
    
    @patch('backend.engines.simplification_engine.Groq')
    def test_simplify_success(self, mock_Groq_class):
        """Test successful text simplification."""
        # Setup mock
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = '''
        {
            "simplified_text": "This is a simple version of the text."
        }
        '''
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Test
        engine = SimplificationEngine(api_key="test-key")
        result = engine.simplify(
            "This is an extraordinarily complex and convoluted text.",
            "response-123"
        )
        
        # Verify
        assert isinstance(result, SimplifiedResponse)
        assert result.original_text == "This is an extraordinarily complex and convoluted text."
        assert result.simplified_text == "This is a simple version of the text."
        assert result.response_id == "response-123"
        
        # Verify API call
        mock_client.chat.completions.create.assert_called_once()
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        assert call_kwargs['model'] == "llama-3.1-8b-instant"
        assert call_kwargs['temperature'] == 0.3
        assert call_kwargs['response_format'] == {"type": "json_object"}
    
    @patch('backend.engines.simplification_engine.Groq')
    def test_simplify_empty_llm_response_raises_error(self, mock_Groq_class):
        """Test simplify raises error when LLM returns empty response."""
        # Setup mock
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = None
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Test
        engine = SimplificationEngine(api_key="test-key")
        
        with pytest.raises(RuntimeError, match="Empty response from LLM"):
            engine.simplify("Some text", "response-123")
    
    @patch('backend.engines.simplification_engine.Groq')
    def test_simplify_invalid_json_raises_error(self, mock_Groq_class):
        """Test simplify raises error for invalid JSON response."""
        # Setup mock
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = "Not valid JSON"
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Test
        engine = SimplificationEngine(api_key="test-key")
        
        with pytest.raises(RuntimeError, match="Failed to parse LLM response as JSON"):
            engine.simplify("Some text", "response-123")
    
    @patch('backend.engines.simplification_engine.Groq')
    def test_simplify_missing_field_raises_error(self, mock_Groq_class):
        """Test simplify raises error when simplified_text field is missing."""
        # Setup mock
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = '{"wrong_field": "value"}'
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Test
        engine = SimplificationEngine(api_key="test-key")
        
        with pytest.raises(RuntimeError, match="Missing required field: simplified_text"):
            engine.simplify("Some text", "response-123")
    
    @patch('backend.engines.simplification_engine.Groq')
    def test_simplify_empty_simplified_text_raises_error(self, mock_Groq_class):
        """Test simplify raises error when simplified_text is empty."""
        # Setup mock
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        
        mock_completion = Mock()
        mock_completion.choices = [Mock()]
        mock_completion.choices[0].message.content = '{"simplified_text": ""}'
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Test
        engine = SimplificationEngine(api_key="test-key")
        
        with pytest.raises(RuntimeError, match="simplified_text cannot be empty"):
            engine.simplify("Some text", "response-123")
    
    @patch('backend.engines.simplification_engine.Groq')
    def test_simplify_api_error_raises_runtime_error(self, mock_Groq_class):
        """Test simplify raises RuntimeError when API call fails."""
        # Setup mock
        mock_client = Mock()
        mock_Groq_class.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        # Test
        engine = SimplificationEngine(api_key="test-key")
        
        with pytest.raises(RuntimeError, match="LLM simplification failed: API Error"):
            engine.simplify("Some text", "response-123")
    
    def test_build_simplification_prompt(self):
        """Test prompt construction includes all required elements."""
        engine = SimplificationEngine(api_key="test-key")
        prompt = engine._build_simplification_prompt("Complex text here")
        
        # Verify prompt contains key elements
        assert "Complex text here" in prompt
        assert "simplified_text" in prompt
        assert "simpler words" in prompt
        assert "shorter sentences" in prompt
        assert "factual accuracy" in prompt
        assert "JSON format" in prompt
    
    def test_parse_simplification_response_success(self):
        """Test successful parsing of simplification response."""
        engine = SimplificationEngine(api_key="test-key")
        
        json_response = '{"simplified_text": "Simple version"}'
        result = engine._parse_simplification_response(json_response)
        
        assert result == "Simple version"
    
    def test_parse_simplification_response_strips_whitespace(self):
        """Test parsing strips whitespace from simplified text."""
        engine = SimplificationEngine(api_key="test-key")
        
        json_response = '{"simplified_text": "  Simple version  "}'
        result = engine._parse_simplification_response(json_response)
        
        assert result == "Simple version"
