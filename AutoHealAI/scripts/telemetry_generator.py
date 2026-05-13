import random
import time
import requests

SERVICES = ["api-gateway", "billing", "auth", "recommendation"]


def generate_metric(service: str):
    return {
        "service": service,
        "cpu": round(random.uniform(20, 98), 2),
        "memory": round(random.uniform(25, 99), 2),
        "latency": round(random.uniform(20, 1200), 2),
        "error_rate": round(random.uniform(0.0, 0.2), 4),
        "restarts": random.randint(0, 8),
    }


if __name__ == "__main__":
    while True:
        for service in SERVICES:
            payload = generate_metric(service)
            try:
                requests.post("http://localhost:8000/api/v1/telemetry/ingest", json=payload, timeout=3)
            except Exception:
                pass
        time.sleep(3)
