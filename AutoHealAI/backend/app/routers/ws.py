import asyncio
import random
from datetime import datetime
from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/live")
async def live_feed(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_json(
                {
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "cpu": round(random.uniform(30, 95), 2),
                    "memory": round(random.uniform(35, 97), 2),
                    "latency": round(random.uniform(40, 800), 2),
                    "error_rate": round(random.uniform(0.0, 0.15), 4),
                }
            )
            await asyncio.sleep(2)
    except Exception:
        await websocket.close()
