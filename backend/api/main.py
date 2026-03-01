"""
FastAPI backend API layer for Trust-Aware AI Learning Platform MVP.

This module provides REST endpoints that integrate all engines:
- AIProcessingLayer for LLM queries with uncertainty tagging
- ChallengeEngine for generating verification questions
- SimplificationEngine for text simplification

Endpoints:
- POST /api/query: Query LLM with confidence scoring
- POST /api/challenge: Generate verification challenge
- POST /api/simplify: Simplify complex text
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from backend.engines.ai_processing_layer import AIProcessingLayer
from backend.engines.challenge_engine import ChallengeEngine
from backend.engines.simplification_engine import SimplificationEngine
from backend.models.schemas import AIResponse, Challenge, SimplifiedResponse
from groq import Groq


# Load environment variables
load_dotenv()


# Global engine instances
ai_processing_layer: AIProcessingLayer | None = None
challenge_engine: ChallengeEngine | None = None
simplification_engine: SimplificationEngine | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initialize engines at startup and cleanup at shutdown.
    
    Engines are initialized once at startup to avoid per-request overhead.
    """
    global ai_processing_layer, challenge_engine, simplification_engine
    
    # Startup: Initialize engines
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("WARNING: GROQ_API_KEY not found in environment")
        print("API endpoints will fail until API key is configured")
    else:
        try:
            ai_processing_layer = AIProcessingLayer(api_key=api_key)
            challenge_engine = ChallengeEngine(api_key=api_key)
            simplification_engine = SimplificationEngine(api_key=api_key)
            print("✓ All engines initialized successfully")
        except Exception as e:
            print(f"ERROR: Failed to initialize engines: {e}")
    
    yield
    
    # Shutdown: Cleanup (if needed)
    ai_processing_layer = None
    challenge_engine = None
    simplification_engine = None


# Create FastAPI application
app = FastAPI(
    title="Trust-Aware AI Learning Platform API",
    description="REST API for trust calibration and AI learning",
    version="1.0.0",
    lifespan=lifespan
)


# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:5173",  # Alternative localhost
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods for MVP
    allow_headers=["*"],  # Allow all headers for MVP
)


# Request/Response models for API endpoints
class QueryRequest(BaseModel):
    """Request model for /api/query endpoint."""
    query_text: str = Field(
        ...,
        min_length=1,
        description="The user's query text"
    )


class ChallengeRequest(BaseModel):
    """Request model for /api/challenge endpoint."""
    response_id: str = Field(
        ...,
        min_length=1,
        description="ID of the AI response to challenge"
    )
    response_text: str = Field(
        ...,
        min_length=1,
        description="The AI response text"
    )
    query_text: str = Field(
        default="",
        description="Original query text (optional for MVP)"
    )


class SimplifyRequest(BaseModel):
    """Request model for /api/simplify endpoint."""
    text: str = Field(
        ...,
        min_length=1,
        description="Text to simplify"
    )
    response_id: str = Field(
        ...,
        min_length=1,
        description="ID of the response being simplified"
    )


# API Endpoints
@app.post("/api/query", response_model=AIResponse)
async def query_endpoint(request: QueryRequest) -> AIResponse:
    """
    Query the LLM with uncertainty tagging and confidence scoring.
    
    Args:
        request: QueryRequest with query_text
    
    Returns:
        AIResponse with tagged text, confidence score, and breakdown
    
    Raises:
        HTTPException: 400 for invalid input, 500 for processing errors
    """
    if not ai_processing_layer:
        raise HTTPException(
            status_code=500,
            detail="AI Processing Layer not initialized. Check API key configuration."
        )
    
    try:
        response = ai_processing_layer.query_llm(request.query_text)
        return response
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except Exception as e:
        print("FULL ERROR:", repr(e))   # 👈 ADD THIS LINE
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/api/challenge", response_model=Challenge)
async def challenge_endpoint(request: ChallengeRequest) -> Challenge:
    """
    Generate a verification challenge for an AI response.
    
    Args:
        request: ChallengeRequest with response_id and response_text
    
    Returns:
        Challenge with verification question
   oi 
    Raises:
        HTTPException: 400 for invalid input, 500 for processing errors
    """
    if not challenge_engine:
        raise HTTPException(
            status_code=500,
            detail="Challenge Engine not initialized. Check API key configuration."
        )
    
    try:
        # Use query_text if provided, otherwise use a default
        query_text = request.query_text or "User query"
        
        challenge = challenge_engine.generate_challenge(
            response_text=request.response_text,
            query_text=query_text,
            response_id=request.response_id
        )
        return challenge
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )


@app.post("/api/simplify", response_model=SimplifiedResponse)
async def simplify_endpoint(request: SimplifyRequest) -> SimplifiedResponse:
    """
    Simplify complex text for easier comprehension.
    
    Args:
        request: SimplifyRequest with text and response_id
    
    Returns:
        SimplifiedResponse with original and simplified text
    
    Raises:
        HTTPException: 400 for invalid input, 500 for processing errors
    """
    if not simplification_engine:
        raise HTTPException(
            status_code=500,
            detail="Simplification Engine not initialized. Check API key configuration."
        )
    
    try:
        simplified = simplification_engine.simplify(
            text=request.text,
            response_id=request.response_id
        )
        return simplified
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )


# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        Status information including engine initialization state
    """
    return {
        "status": "healthy",
        "engines": {
            "ai_processing_layer": ai_processing_layer is not None,
            "challenge_engine": challenge_engine is not None,
            "simplification_engine": simplification_engine is not None
        }
    }
