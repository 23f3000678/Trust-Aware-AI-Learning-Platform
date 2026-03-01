# Testing the Frontend

## Prerequisites

1. **Backend must be running** on http://localhost:8000
2. **GROQ API key** must be configured in backend/.env

## Starting the Backend

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn api.main:app --reload
```

Verify backend is running by visiting: http://localhost:8000/docs

## Starting the Frontend

```bash
cd frontend
npm run dev
```

The frontend will be available at: http://localhost:5173

## Testing the Features

### 1. Query Interface
- Enter a question in the text area
- Click "Submit Query"
- Verify you see:
  - AI response text
  - Yellow highlighting on [UNCERTAIN] text
  - Confidence score (0-100)
  - Confidence breakdown with 3 indicators
  - Warning banner if confidence < 70

### 2. Challenge Feature
- After receiving a response, click "🎯 Challenge Me"
- Verify you see:
  - A challenge question displayed
  - Note about MVP limitations
  - Close button (×) to dismiss

### 3. Simplification Feature
- After receiving a response, click "📖 Simplify"
- Verify you see:
  - Simplified version of the text
  - Toggle buttons to switch between Simplified/Original
  - Close button (×) to dismiss

## Example Test Queries

### High Confidence Query
```
What is 2 + 2?
```
Expected: High confidence score, no warning banner

### Low Confidence Query
```
What will the stock market do tomorrow?
```
Expected: Low confidence score, warning banner, uncertain text highlighted

### Complex Topic Query
```
Explain quantum entanglement
```
Expected: Medium-high complexity, possible uncertain sections

## Troubleshooting

### Backend Connection Error
- Error: "Network Error" or "Failed to get response"
- Solution: Ensure backend is running on http://localhost:8000
- Check: Visit http://localhost:8000/docs to verify

### CORS Error
- Error: "CORS policy" in browser console
- Solution: Backend should have CORS middleware configured
- Check: backend/api/main.py should have CORSMiddleware

### TypeScript Errors
- Run: `npm run build` to check for compilation errors
- All files should compile without errors

### Styling Issues
- Verify: frontend/src/index.css is imported in App.tsx
- Check: Browser developer tools for CSS loading

## API Endpoints Being Called

1. **POST /api/query**
   - Request: `{ "query_text": "your question" }`
   - Response: AIResponse with confidence and breakdown

2. **POST /api/challenge**
   - Request: `{ "response_id": "...", "response_text": "..." }`
   - Response: Challenge with question_text

3. **POST /api/simplify**
   - Request: `{ "text": "...", "response_id": "..." }`
   - Response: SimplifiedResponse with original and simplified text

## Browser Console

Open browser developer tools (F12) to see:
- Network requests to backend
- Any JavaScript errors
- API response data

## Success Criteria

✅ Can submit queries and receive responses
✅ Uncertain text is highlighted in yellow
✅ Confidence score displays with correct color
✅ Breakdown shows 3 indicators
✅ Warning banner appears for low confidence
✅ Challenge button generates questions
✅ Simplify button creates simplified versions
✅ Toggle works between original/simplified
✅ No console errors
✅ Responsive design works on mobile
