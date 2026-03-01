# Data Models - Trust-Aware AI Learning Platform

This directory contains Pydantic data models for the MVP implementation.

## Models Overview

### ConfidenceBreakdown
Provides transparency into confidence factors:
- `question_clarity`: "High" | "Medium" | "Low"
- `topic_complexity`: "Low" | "Medium" | "High"
- `missing_information`: "Yes" | "No"

### ConfidenceScore
Complete confidence assessment:
- `score`: 0-100 (validated range)
- `justification`: Non-empty explanation
- `breakdown`: ConfidenceBreakdown instance
- `should_warn`: Auto-flag for scores < 70

### QueryContext
User query information:
- `query_text`: Non-empty query string
- `timestamp`: Query submission time
- `session_id`: Optional session tracking

### AIResponse
AI-generated response with confidence:
- `response_text`: May contain `[UNCERTAIN]...[/UNCERTAIN]` tags
- `confidence`: ConfidenceScore instance
- `response_id`: Unique identifier
- `timestamp`: Response generation time

### Challenge
User challenge to AI response:
- `challenge_id`: Unique identifier
- `question_text`: Challenge question
- `related_response_id`: ID of challenged response

### SimplifiedResponse
Simplified version of complex responses:
- `original_text`: Original response
- `simplified_text`: Simplified version
- `response_id`: Response identifier

## Validation Rules

All models include:
- Range validation for numeric fields (0-100 for confidence scores)
- Non-empty validation for text fields (no whitespace-only strings)
- Type validation via Pydantic
- Field descriptions for API documentation

## Usage Example

```python
from backend.models import ConfidenceBreakdown, ConfidenceScore, AIResponse
from datetime import datetime

# Create confidence breakdown
breakdown = ConfidenceBreakdown(
    question_clarity="High",
    topic_complexity="Medium",
    missing_information="No"
)

# Create confidence score
confidence = ConfidenceScore(
    score=85.0,
    justification="Clear question with comprehensive data available",
    breakdown=breakdown,
    should_warn=False
)

# Create AI response
response = AIResponse(
    response_text="Machine learning is a subset of AI that [UNCERTAIN]enables systems to learn[/UNCERTAIN].",
    confidence=confidence,
    response_id="resp-12345",
    timestamp=datetime.now()
)
```

## Testing

Run tests with:
```bash
pytest backend/models/test_schemas.py -v
```

## MVP Scope

These models focus on core trust calibration features:
- ✅ Confidence scoring with breakdown
- ✅ Uncertainty markers in responses
- ✅ Challenge mechanism
- ✅ Response simplification
- ❌ Database relationships (future)
- ❌ Complex validation logic (future)
