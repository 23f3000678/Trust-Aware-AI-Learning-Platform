# Trust-Aware AI Learning Platform MVP

A hackathon demo for an AI-powered learning platform that adapts to student trust levels.

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

## Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

Create a `backend/.env` file based on `.env.example`:
- `GROQ_API_KEY`: Your GROQ API key
