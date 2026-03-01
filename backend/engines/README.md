# Backend Engines

This directory contains the core processing engines for the Trust-Aware AI Learning Platform.

## Components

### AI Processing Layer

The `AIProcessingLayer` orchestrates LLM queries with enhanced prompting to generate responses with uncertainty tagging and confidence scoring.

### Trust Engine

The `TrustEngine` uses LLM-based analysis to compute confidence scores with detailed breakdowns for AI responses.

### Challenge Engine

The `ChallengeEngine` generates interactive verification challenges to help learners test their understanding of AI responses.

### Simplification Engine

The `SimplificationEngine` uses LLM-based processing to simplify complex AI responses, making them easier to understand while preserving accuracy.

---

## AI Processing Layer

The AI Processing Layer is the primary interface for generating AI responses with uncertainty awareness. It uses structured prompting to produce responses with embedded uncertainty markers and confidence assessments.

### Overview

The `AIProcessingLayer` class generates AI responses using GROQ's API with:
- Response text with `[UNCERTAIN]...[/UNCERTAIN]` tags around uncertain statements
- Overall confidence score (0-100)
- Detailed justification explaining the confidence level
- Breakdown of contributing factors:
  - Question clarity (High/Medium/Low)
  - Topic complexity (Low/Medium/High)
  - Missing information (Yes/No)
- Unique response ID and timestamp
- Automatic warning flag for low confidence responses (< 70)

### Usage

#### Basic Example

```python
from backend.engines import AIProcessingLayer

# Initialize with API key from environment
layer = AIProcessingLayer()

# Or provide API key explicitly
layer = AIProcessingLayer(api_key="your-api-key")

# Query the LLM
query = "What is machine learning?"
response = layer.query_llm(query)

print(f"Response: {response.response_text}")
print(f"Confidence: {response.confidence.score}")
print(f"Should warn: {response.confidence.should_warn}")
print(f"Response ID: {response.response_id}")
```

#### Working with Uncertainty Tags

```python
response = layer.query_llm("When was Python created?")

# Response text contains uncertainty markers
# Example: "Python is a high-level language. [UNCERTAIN]It was created around 1991.[/UNCERTAIN]"

# Extract uncertain portions
import re
uncertain_parts = re.findall(r'\[UNCERTAIN\](.*?)\[/UNCERTAIN\]', response.response_text)
print(f"Uncertain statements: {uncertain_parts}")
```

### Enhanced Prompting Strategy

The AIProcessingLayer uses a carefully crafted prompt that:

1. **Sets the educational context**: Positions the AI as an educational assistant focused on trust calibration
2. **Instructs uncertainty tagging**: Explicitly asks the AI to mark uncertain statements
3. **Requests structured output**: Requires JSON format with all necessary fields
4. **Provides clear guidelines**: Explains how to assess confidence and use tags

Example prompt structure:
```
You are an educational AI assistant that promotes trust calibration.

Answer the following question, and tag any uncertain statements with [UNCERTAIN]...[/UNCERTAIN].

Question: {query_text}

Provide your response in JSON format:
{
  "response_text": "<answer with [UNCERTAIN] tags>",
  "confidence_score": <0-100>,
  "confidence_justification": "<explanation>",
  "question_clarity": "<High/Medium/Low>",
  "topic_complexity": "<Low/Medium/High>",
  "missing_information": "<Yes/No>"
}
```

### Configuration

The AIProcessingLayer requires an GROQ API key. You can provide it in two ways:

1. **Environment variable** (recommended):
   ```bash
   export GROQ_API_KEY="your-api-key"
   ```

2. **Constructor parameter**:
   ```python
   layer = AIProcessingLayer(api_key="your-api-key")
   ```

### Error Handling

```python
try:
    response = layer.query_llm(query_text)
except ValueError as e:
    # Empty or whitespace-only query
    print(f"Invalid input: {e}")
except RuntimeError as e:
    # LLM API failure or invalid response
    print(f"Query failed: {e}")
```

### API Reference

#### `AIProcessingLayer`

##### `__init__(api_key: str | None = None)`

Initialize the AIProcessingLayer.

**Parameters:**
- `api_key` (str, optional): GROQ API key. If None, reads from `GROQ_API_KEY` environment variable.

**Raises:**
- `ValueError`: If no API key is provided or found in environment.

##### `query_llm(query_text: str) -> AIResponse`

Query the LLM with enhanced prompting for uncertainty tagging.

**Parameters:**
- `query_text` (str): The user's query text

**Returns:**
- `AIResponse`: Object containing response text with uncertainty tags, confidence score with breakdown, unique ID, and timestamp

**Raises:**
- `ValueError`: If query text is empty or whitespace-only
- `RuntimeError`: If LLM query fails or returns invalid data

---

## Trust Engine

The Trust Engine provides LLM-based confidence analysis for existing Q&A pairs.

### Overview

The `TrustEngine` class analyzes Q&A pairs using GROQ's API to provide:
- Overall confidence score (0-100)
- Detailed justification explaining the score
- Breakdown of contributing factors:
  - Question clarity (High/Medium/Low)
  - Topic complexity (Low/Medium/High)
  - Missing information (Yes/No)
- Automatic warning flag for low confidence responses (< 70)

## Usage

### Basic Example

```python
from backend.engines import TrustEngine

# Initialize with API key from environment
engine = TrustEngine()

# Or provide API key explicitly
engine = TrustEngine(api_key="your-api-key")

# Compute confidence for a Q&A pair
query = "What is machine learning?"
response = "Machine learning is a subset of artificial intelligence..."

confidence = engine.compute_confidence(
    response_text=response,
    query_text=query
)

print(f"Score: {confidence.score}")
print(f"Justification: {confidence.justification}")
print(f"Should warn: {confidence.should_warn}")
print(f"Question clarity: {confidence.breakdown.question_clarity}")
print(f"Topic complexity: {confidence.breakdown.topic_complexity}")
print(f"Missing info: {confidence.breakdown.missing_information}")
```

### Configuration

The TrustEngine requires an GROQ API key. You can provide it in two ways:

1. **Environment variable** (recommended):
   ```bash
   export GROQ_API_KEY="your-api-key"
   ```

2. **Constructor parameter**:
   ```python
   engine = TrustEngine(api_key="your-api-key")
   ```

### Error Handling

The TrustEngine raises exceptions for various error conditions:

```python
try:
    confidence = engine.compute_confidence(response_text, query_text)
except ValueError as e:
    # Empty or whitespace-only text
    print(f"Invalid input: {e}")
except RuntimeError as e:
    # LLM API failure or invalid response
    print(f"Analysis failed: {e}")
```

## Implementation Details

### LLM-Based Analysis

The TrustEngine uses structured prompting to ask the LLM to analyze Q&A pairs:

```
Analyze this Q&A pair and provide confidence assessment:

Question: {query_text}
Answer: {response_text}

Provide your analysis in JSON format:
{
  "confidence_score": <0-100>,
  "justification": "<explanation>",
  "question_clarity": "<High/Medium/Low>",
  "topic_complexity": "<Low/Medium/High>",
  "missing_information": "<Yes/No>"
}
```

### Model Selection

The MVP uses `gpt-4o-mini` for cost-effective analysis. This can be configured by modifying the `self.model` attribute in the `TrustEngine.__init__` method.

### Warning Threshold

Responses with confidence scores below 70 automatically set `should_warn=True`. This threshold is hardcoded in the `_build_confidence_score` method.

## Testing

Run the test suite:

```bash
# Run unit tests (no API calls)
pytest backend/engines/test_trust_engine.py

# Run integration tests (requires API key, incurs costs)
pytest backend/engines/test_trust_engine.py -m integration
```

## MVP Scope

The current implementation focuses on:
- ✅ LLM-based confidence analysis
- ✅ Structured JSON response parsing
- ✅ Basic error handling
- ✅ Pydantic model integration

Future enhancements (post-MVP):
- ❌ Response caching
- ❌ Batch processing
- ❌ Token probability analysis
- ❌ Performance optimization
- ❌ Alternative LLM providers

## Dependencies

- `GROQ`: GROQ API client
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation (via backend.models)

## API Reference

### TrustEngine

#### `__init__(api_key: str | None = None)`

Initialize the TrustEngine.

**Parameters:**
- `api_key` (str, optional): GROQ API key. If None, reads from `GROQ_API_KEY` environment variable.

**Raises:**
- `ValueError`: If no API key is provided or found in environment.

#### `compute_confidence(response_text: str, query_text: str) -> ConfidenceScore`

Compute confidence score for an AI response.

**Parameters:**
- `response_text` (str): The AI-generated response to analyze
- `query_text` (str): The original user query

**Returns:**
- `ConfidenceScore`: Object containing score, justification, breakdown, and warning flag

**Raises:**
- `ValueError`: If response or query text is empty or whitespace-only
- `RuntimeError`: If LLM analysis fails or returns invalid data


---

## Challenge Engine

The Challenge Engine generates interactive learning challenges to help users test their understanding of AI responses through verification questions.

### Overview

The `ChallengeEngine` class generates verification challenges using GROQ's API to provide:
- One verification-style follow-up question per Q&A pair
- Educational questions that test understanding
- Simple "Is this correct?" or "Which statement is accurate?" formats
- Unique challenge IDs for tracking
- Reference to the original response being challenged

### Usage

#### Basic Example

```python
from backend.engines import ChallengeEngine

# Initialize with API key from environment
engine = ChallengeEngine()

# Or provide API key explicitly
engine = ChallengeEngine(api_key="your-api-key")

# Generate a challenge for a Q&A pair
query = "What is Python?"
response = "Python is a high-level, interpreted programming language..."
response_id = "resp-123"

challenge = engine.generate_challenge(
    response_text=response,
    query_text=query,
    response_id=response_id
)

print(f"Challenge ID: {challenge.challenge_id}")
print(f"Question: {challenge.question_text}")
print(f"Related Response: {challenge.related_response_id}")
```

#### Working with Uncertain Responses

```python
# Generate challenge for response with uncertainty tags
response = "Python is a language. [UNCERTAIN]It was created around 1991.[/UNCERTAIN]"
query = "When was Python created?"

challenge = engine.generate_challenge(
    response_text=response,
    query_text=query,
    response_id="resp-456"
)

# The challenge will test understanding of the response
print(f"Verification question: {challenge.question_text}")
```

### Challenge Generation Strategy

The ChallengeEngine uses structured prompting to generate educational verification questions:

1. **Analyzes the Q&A pair**: Understands the key concepts in the response
2. **Creates verification question**: Generates a question that tests understanding
3. **Keeps it simple**: Uses straightforward formats like "Is this correct?"
4. **Makes it educational**: Focuses on reinforcing key concepts, not tricking the learner

Example prompt structure:
```
Based on this Q&A pair, generate ONE verification question to help the learner test their understanding.

Question: {query_text}
Answer: {response_text}

Generate a verification question in JSON format:
{
  "question_text": "<verification question>"
}

Guidelines:
- Create a question that tests understanding of the answer
- Use "Is this correct?" or "Which statement is accurate?" format
- Keep it simple and focused
- Make it educational, not tricky
```

### Configuration

The ChallengeEngine requires an GROQ API key. You can provide it in two ways:

1. **Environment variable** (recommended):
   ```bash
   export GROQ_API_KEY="your-api-key"
   ```

2. **Constructor parameter**:
   ```python
   engine = ChallengeEngine(api_key="your-api-key")
   ```

### Error Handling

```python
try:
    challenge = engine.generate_challenge(response_text, query_text, response_id)
except ValueError as e:
    # Empty or whitespace-only text
    print(f"Invalid input: {e}")
except RuntimeError as e:
    # LLM API failure or invalid response
    print(f"Challenge generation failed: {e}")
```

### API Reference

#### `ChallengeEngine`

##### `__init__(api_key: str | None = None)`

Initialize the ChallengeEngine.

**Parameters:**
- `api_key` (str, optional): GROQ API key. If None, reads from `GROQ_API_KEY` environment variable.

**Raises:**
- `ValueError`: If no API key is provided or found in environment.

##### `generate_challenge(response_text: str, query_text: str, response_id: str) -> Challenge`

Generate a verification challenge based on a Q&A pair.

**Parameters:**
- `response_text` (str): The AI's response text (may contain [UNCERTAIN] tags)
- `query_text` (str): The original user query
- `response_id` (str): ID of the response being challenged

**Returns:**
- `Challenge`: Object containing challenge ID, verification question, and related response ID

**Raises:**
- `ValueError`: If response_text, query_text, or response_id is empty or whitespace-only
- `RuntimeError`: If LLM query fails or returns invalid data

### Implementation Details

#### LLM-Based Generation

The ChallengeEngine uses structured prompting to ask the LLM to generate verification questions that:
- Test understanding of the key concepts in the response
- Use simple, clear language
- Focus on educational value rather than difficulty
- Help reinforce learning through active recall

#### Model Selection

The MVP uses `gpt-4o-mini` for cost-effective challenge generation. This can be configured by modifying the `self.model` attribute in the `ChallengeEngine.__init__` method.

#### Unique Challenge IDs

Each challenge receives a unique UUID to enable tracking and reference. The ID is generated using Python's `uuid.uuid4()` function.

### Testing

Run the test suite:

```bash
# Run unit tests (no API calls)
pytest backend/engines/test_challenge_engine.py -v

# Run specific test class
pytest backend/engines/test_challenge_engine.py::TestGenerateChallenge -v
```

### MVP Scope

The current implementation focuses on:
- ✅ Single verification question generation
- ✅ LLM-based question creation
- ✅ Structured JSON response parsing
- ✅ Basic error handling
- ✅ Pydantic model integration
- ✅ Unique challenge ID generation

Future enhancements (post-MVP):
- ❌ Multiple challenge types (verification, application, analysis)
- ❌ Challenge evaluation and scoring
- ❌ Adaptive hints based on user performance
- ❌ Difficulty level adjustment
- ❌ Challenge tracking and analytics
- ❌ Response caching

### Dependencies

- `GROQ`: GROQ API client
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation (via backend.models)
- `uuid`: Unique ID generation

### Example Usage

See `example_challenge_engine.py` for complete examples demonstrating:
- Basic challenge generation
- Working with uncertain responses
- Handling different subject areas (programming, science, history)
- Error handling patterns


---

## Simplification Engine

The Simplification Engine provides LLM-based text simplification to make complex AI responses more accessible to a general audience.

### Overview

The `SimplificationEngine` class simplifies text using GROQ's API to provide:
- Simplified version of complex text
- Preservation of factual accuracy
- Maintenance of core meaning
- Improved accessibility through simpler words and shorter sentences
- Reference to the original text and response ID

### Usage

#### Basic Example

```python
from backend.engines import SimplificationEngine

# Initialize with API key from environment
engine = SimplificationEngine()

# Or provide API key explicitly
engine = SimplificationEngine(api_key="your-api-key")

# Simplify complex text
complex_text = """
Quantum entanglement is a physical phenomenon that occurs when a group of 
particles are generated, interact, or share spatial proximity in a way such 
that the quantum state of each particle of the group cannot be described 
independently of the state of the others.
"""

simplified = engine.simplify(
    text=complex_text,
    response_id="resp-123"
)

print(f"Original: {simplified.original_text}")
print(f"Simplified: {simplified.simplified_text}")
print(f"Response ID: {simplified.response_id}")
```

#### Working with AI Responses

```python
# Simplify an AI response with uncertainty tags
response_text = """
The exact date of the invention of the printing press is [UNCERTAIN]believed 
to be around 1440[/UNCERTAIN], when Johannes Gutenberg developed movable type 
printing in Europe.
"""

simplified = engine.simplify(
    text=response_text,
    response_id="resp-456"
)

# The simplified version will be easier to understand
print(f"Simplified: {simplified.simplified_text}")
```

### Simplification Strategy

The SimplificationEngine uses structured prompting to generate accessible text:

1. **Analyzes the original text**: Identifies complex concepts and terminology
2. **Simplifies language**: Uses simpler words and shorter sentences
3. **Breaks down concepts**: Makes complex ideas more digestible
4. **Preserves accuracy**: Maintains factual correctness
5. **Keeps core meaning**: Ensures the essential message remains intact

Example prompt structure:
```
Simplify the following text to make it easier to understand while preserving accuracy.

Original text: {text}

Provide your simplified version in JSON format:
{
  "simplified_text": "<simplified version>"
}

Guidelines:
- Use simpler words and shorter sentences
- Break down complex concepts
- Maintain factual accuracy
- Keep the core meaning intact
- Make it accessible to a general audience
```

### Configuration

The SimplificationEngine requires an GROQ API key. You can provide it in two ways:

1. **Environment variable** (recommended):
   ```bash
   export GROQ_API_KEY="your-api-key"
   ```

2. **Constructor parameter**:
   ```python
   engine = SimplificationEngine(api_key="your-api-key")
   ```

### Error Handling

```python
try:
    simplified = engine.simplify(text, response_id)
except ValueError as e:
    # Empty or whitespace-only text or response_id
    print(f"Invalid input: {e}")
except RuntimeError as e:
    # LLM API failure or invalid response
    print(f"Simplification failed: {e}")
```

### API Reference

#### `SimplificationEngine`

##### `__init__(api_key: str | None = None)`

Initialize the SimplificationEngine.

**Parameters:**
- `api_key` (str, optional): GROQ API key. If None, reads from `GROQ_API_KEY` environment variable.

**Raises:**
- `ValueError`: If no API key is provided or found in environment.

##### `simplify(text: str, response_id: str) -> SimplifiedResponse`

Simplify text using LLM-based processing.

**Parameters:**
- `text` (str): The text to simplify
- `response_id` (str): Unique identifier for the response being simplified

**Returns:**
- `SimplifiedResponse`: Object containing original text, simplified text, and response ID

**Raises:**
- `ValueError`: If text or response_id is empty or whitespace-only
- `RuntimeError`: If LLM query fails or returns invalid data

### Implementation Details

#### LLM-Based Simplification

The SimplificationEngine uses structured prompting to ask the LLM to simplify text while:
- Using simpler vocabulary
- Creating shorter, clearer sentences
- Breaking down complex concepts into digestible parts
- Maintaining factual accuracy
- Preserving the core meaning and message

#### Model Selection

The MVP uses `gpt-4o-mini` for cost-effective simplification. This can be configured by modifying the `self.model` attribute in the `SimplificationEngine.__init__` method.

#### Temperature Setting

The engine uses a lower temperature (0.3) for consistent, reliable simplification that maintains accuracy while improving clarity.

### Testing

Run the test suite:

```bash
# Run unit tests (no API calls)
pytest backend/engines/test_simplification_engine.py -v

# Run specific test class
pytest backend/engines/test_simplification_engine.py::TestSimplificationEngine -v
```

### MVP Scope

The current implementation focuses on:
- ✅ LLM-based text simplification
- ✅ Structured JSON response parsing
- ✅ Basic error handling
- ✅ Pydantic model integration
- ✅ Whitespace trimming

Future enhancements (post-MVP):
- ❌ Reading level calculation
- ❌ Semantic similarity validation
- ❌ Complexity scoring
- ❌ Multiple simplification levels
- ❌ Response caching
- ❌ Batch processing

### Dependencies

- `GROQ`: GROQ API client
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation (via backend.models)

### Example Usage

See `example_simplification_engine.py` for complete examples demonstrating:
- Simplifying technical content
- Working with responses containing uncertainty markers
- Simplifying medical/scientific explanations
- Error handling patterns
