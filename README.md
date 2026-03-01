# Trust-Aware AI Learning Platform (MVP)

An explainable AI learning system designed to calibrate student trust in AI responses through confidence scoring, uncertainty tagging, and reflective verification challenges.

This prototype demonstrates how responsible AI interaction can reduce blind trust, improve comprehension, and support inclusive learning environments.

---

## Problem

Students increasingly rely on AI tools, but:
- AI responses can be over-trusted without verification
- Uncertainty is rarely surfaced clearly
- Feedback lacks explainability
- Low-confidence learners need guided reflection, not just answers

This system introduces trust-aware learning — where AI not only answers, but communicates confidence and encourages validation.

---

## What Makes This Different

Unlike generic AI tutors, this platform:

- Surfaces model confidence with structured breakdown
- Tags uncertain segments explicitly in responses
- Generates reflective challenge questions
- Includes simplification mode for accessibility
- Uses a Reflective Achievement Model instead of gamified points
- Supports inclusive UI design (light/dark modes, large readable layout)

The goal is calibrated trust, not engagement gamification.

---

## Core MVP Features

- AI query endpoint with structured JSON output
- Confidence score with clarity and complexity breakdown
- Uncertainty tagging using inline markers
- Challenge Mode for verification-based learning
- Simplification Engine for low-literacy accessibility
- Reflective Achievement tracking (non-gamified)

---

## Tech Stack

Backend:
- FastAPI
- Pydantic
- LLM integration (Groq API)
- Uvicorn

Frontend:
- React
- TypeScript
- Vite
- Axios

Architecture:
- Modular engine-based backend (TrustEngine, ChallengeEngine, SimplificationEngine)
- Clean API separation
- Single-column accessible UI layout

---

## Project Structure

```
├── backend/
│   ├── api/          # API endpoints
│   ├── engines/      # Trust Engine, Challenge Engine, Simplification Engine
│   └── models/       # Pydantic data models
├── frontend/
│   └── src/
│       ├── components/  # React components
│       ├── services/    # API service layer
│       └── types/       # TypeScript type definitions
```
## Setup Instructions

### 1. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```
Run the server:
```bash
uvicorn backend.api.main:app --reload
```
API documentation will be available at:
http://localhost:8000/docs

---
### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at:
http://localhost:5173
---
## Environment Variables

Create a `backend/.env` file based on `.env.example`:
- `GROQ_API_KEY`: Your GROQ API key
