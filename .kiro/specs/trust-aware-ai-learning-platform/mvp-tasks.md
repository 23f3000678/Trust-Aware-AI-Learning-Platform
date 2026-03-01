# MVP Implementation Plan: Trust-Aware AI Learning Platform (Hackathon Demo)

## Overview

This is a **reduced scope MVP** for Phase 1 prototype demonstration. Focus is on core trust calibration functionality with minimal infrastructure. This is NOT the full production roadmap.

**MVP Goal**: User submits question → Receives structured explanation → Sees confidence score + breakdown → Uncertain sentences highlighted → Can generate challenge question → Can simplify explanation

## MVP Tasks

- [x] 1. Set up project structure and development environment
  - Create backend directory structure (api, engines, models)
  - Create frontend directory structure (src/components, src/services, src/types)
  - Set up Python virtual environment and install dependencies (FastAPI, GROQ, pydantic)
  - Set up Node.js project and install dependencies (React, TypeScript, axios)
  - Create .env.example for configuration
  - _MVP Scope: Minimal setup only_

- [ ] 2. Implement core data models
  - [x] 2.1 Create Python data models using Pydantic
    - Define ConfidenceScore with breakdown fields
    - Define QueryContext, Challenge, Response models
    - Add validation rules for all fields
    - _MVP Scope: Core models only_
  
  - [x] 2.2 Create TypeScript type definitions
    - Define interfaces matching Python models
    - Export types for use across frontend
    - _MVP Scope: Core types only_

- [ ] 3. Implement Trust Engine with confidence breakdown
  - [x] 3.1 Create TrustEngine class with enhanced confidence scoring
    - Implement compute_confidence() method using LLM-based analysis
    - Return structured response with:
      - confidence_score (0-100)
      - confidence_justification (string explanation)
      - breakdown object with:
        - question_clarity: "High" | "Medium" | "Low"
        - topic_complexity: "Low" | "Medium" | "High"
        - missing_information: "Yes" | "No"
    - Use structured LLM prompting (NOT statistical token analysis)
    - _MVP Scope: LLM-based confidence breakdown only_
  
  - [x] 3.2 Implement uncertainty warning logic
    - Create should_display_warning() method with 70% threshold
    - Return boolean for frontend warning banner
    - _MVP Scope: Simple threshold check only_

- [ ] 4. Implement AI Processing Layer with structured responses
  - [x] 4.1 Create AIProcessingLayer class with enhanced prompting
    - Implement query_llm() method with GROQ API integration
    - Engineer prompts to return structured JSON with:
      - response_text (with [UNCERTAIN] tags for uncertain sentences)
      - confidence_score
      - confidence_justification
      - breakdown (question_clarity, topic_complexity, missing_information)
    - Parse structured JSON responses from LLM
    - Tag uncertain sentences with [UNCERTAIN]...[/UNCERTAIN] markers
    - _MVP Scope: Structured JSON + uncertainty tagging only_
  
  - [x] 4.2 Implement basic error handling
    - Handle API timeouts with simple retry (3 attempts)
    - Provide user-friendly error messages
    - _MVP Scope: Basic retry + friendly errors only, NO cost tracking_

- [ ] 5. Implement Challenge Engine (minimal)
  - [x] 5.1 Create ChallengeEngine class with single verification challenge
    - Implement generate_challenge() method
    - Generate ONE verification-style follow-up question based on response
    - Return challenge with question text only
    - _MVP Scope: Single verification question only, NO evaluation, NO hints, NO difficulty adaptation_

- [ ] 6. Implement Simplification Engine (minimal)
  - [x] 6.1 Create SimplificationEngine class with LLM-based simplification
    - Implement simplify() method using LLM prompting
    - Request simpler language from LLM
    - Return simplified text
    - _MVP Scope: LLM simplification only, NO reading level calculation, NO accuracy validation_

- [ ] 7. Implement FastAPI backend API layer
  - [x] 7.1 Create API endpoints
    - POST /api/query - Submit learner query, return structured response with confidence
    - POST /api/challenge - Generate verification challenge for given response
    - POST /api/simplify - Simplify given text
    - _MVP Scope: Three endpoints only, NO authentication, NO rate limiting_
  
  - [x] 7.2 Integrate engines into API endpoints
    - Wire TrustEngine, ChallengeEngine, SimplificationEngine, AIProcessingLayer
    - Implement request flow: query → LLM → trust scoring → response
    - _MVP Scope: Basic integration only, NO tests_

- [ ] 8. Implement React frontend UI
  - [x] 8.1 Create main query interface component
    - Build input form for learner queries
    - Display AI responses with [UNCERTAIN] text highlighted in yellow
    - Display confidence score prominently
    - Display confidence breakdown (3 indicators: clarity, complexity, missing info)
    - Show warning banner when confidence < 70
    - _MVP Scope: Core UI with uncertainty highlighting + breakdown display_
  
  - [x] 8.2 Create challenge interaction components
    - Display single verification challenge question
    - Provide answer input interface
    - _MVP Scope: Display challenge only, NO evaluation, NO feedback_
  
  - [x] 8.3 Create simplification toggle
    - Add "Simplify" button
    - Display simplified response when clicked
    - _MVP Scope: Simple toggle only_

- [ ] 9. Implement in-memory data storage
  - [x] 9.1 Create simple in-memory store
    - Store recent interactions in memory (list/dict)
    - Implement basic get/set methods
    - _MVP Scope: In-memory only, NO encryption, NO persistence_

- [ ] 10. Create basic documentation
  - [x] 10.1 Write README with setup instructions
    - Document installation steps
    - Provide configuration guide (GROQ API key)
    - Include usage examples
    - _MVP Scope: Basic setup guide only_
  
  - [x] 10.2 Document API endpoints
    - Document request/response formats for 3 endpoints
    - Include example requests
    - _MVP Scope: API docs only_

## Explicitly Excluded from MVP

- ❌ Task 12: AI Literacy Tracking Module
- ❌ Task 14: Analytics collection
- ❌ Task 16: Docker, TLS, encryption
- ❌ All property tests (2.3, 3.4, 4.4, 6.5, 7.3, etc.)
- ❌ All unit test suites beyond minimal sanity checks
- ❌ Task 8: Governance Module (content safety scanning)
- ❌ Cost tracking (4.3)
- ❌ Adaptive hints (6.3)
- ❌ Challenge evaluation (6.2)
- ❌ Gamification tracking (6.4)
- ❌ Reading level calculation (7.2)
- ❌ Accuracy validation (7.2)
- ❌ Role-based access control
- ❌ Database integration
- ❌ Session management
- ❌ User accounts
- ❌ Educator/Admin dashboards
- ❌ Multilingual support
- ❌ Voice interaction
- ❌ Edge deployment

## MVP Success Criteria

✅ User can submit a question
✅ System returns structured explanation with [UNCERTAIN] tags
✅ Confidence score (0-100) displayed prominently
✅ Confidence breakdown (3 indicators) displayed
✅ Uncertain sentences highlighted in yellow
✅ Warning banner appears when confidence < 70
✅ User can generate ONE verification challenge question
✅ User can simplify the explanation

**Stop once this flow is stable and functional.**

## Notes

- This is a hackathon demo build
- Focus on core trust calibration features only
- Minimal infrastructure and testing
- No production-grade security or scalability
- Single-user, in-memory operation
- GROQ API key required for LLM integration
