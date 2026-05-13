import time
from collections import defaultdict, deque
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, health, telemetry, incidents, predictions, ai_decisions, ws, deployments
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutoHealAI API", version="1.0.0")
_hits = defaultdict(deque)


@app.middleware("http")
async def simple_rate_limit(request: Request, call_next):
    client_ip = request.client.host if request.client else "unknown"
    now = time.time()
    window = 60
    limit = 120
    q = _hits[client_ip]
    while q and q[0] < now - window:
        q.popleft()
    if len(q) >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    q.append(now)
    return await call_next(request)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(telemetry.router, prefix="/api/v1/telemetry", tags=["telemetry"])
app.include_router(incidents.router, prefix="/api/v1/incidents", tags=["incidents"])
app.include_router(predictions.router, prefix="/api/v1/predictions", tags=["predictions"])
app.include_router(ai_decisions.router, prefix="/api/v1/decisions", tags=["ai-decisions"])
app.include_router(deployments.router, prefix="/api/v1/deployments", tags=["deployments"])
app.include_router(ws.router, prefix="/api/v1/ws", tags=["ws"])
