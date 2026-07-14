"""Backend application entrypoint for the Local Autonomous Coding Platform."""
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import uvicorn
from . import orchestrator

app = FastAPI(title="Local Autonomous Coding Platform - Backend")

@app.get("/health")
async def health():
    return JSONResponse({"status": "ok"})

@app.get("/agents")
async def list_agents():
    return ["planner", "coder", "reviewer"]

@app.websocket("/ws/logs")
async def websocket_logs(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_text()
            # Echo for now
            await ws.send_text(f"received: {data}")
    except Exception:
        await ws.close()

# Simple startup hook
@app.on_event("startup")
async def startup_event():
    orchestrator.setup()

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
