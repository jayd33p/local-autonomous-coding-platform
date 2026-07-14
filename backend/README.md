# Backend README

This backend provides a FastAPI-based scaffold for the autonomous coding platform.

Run locally:

1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. uvicorn app.main:app --reload --port 8000

Endpoints:
- GET /health
- GET /agents
- WebSocket /ws/logs

