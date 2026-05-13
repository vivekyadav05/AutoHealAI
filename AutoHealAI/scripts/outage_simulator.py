import random
import json
from datetime import datetime, timedelta


def simulate(minutes=60):
    timeline = []
    now = datetime.utcnow()
    for i in range(minutes):
        spike = random.random() < 0.15
        leak = random.random() < 0.1
        overload = random.random() < 0.12
        stress = min(1.0, 0.2 + (0.4 if spike else 0) + (0.3 if leak else 0) + (0.35 if overload else 0))
        downtime = round(stress * random.uniform(2, 12), 2)
        timeline.append(
            {
                "timestamp": (now + timedelta(minutes=i)).isoformat() + "Z",
                "traffic_spike": spike,
                "memory_leak": leak,
                "service_overload": overload,
                "stress_score": round(stress, 3),
                "expected_downtime_min": downtime,
                "recommended_replicas": max(2, int(2 + stress * 8)),
            }
        )
    return timeline


if __name__ == "__main__":
    data = simulate()
    with open("simulated_outages.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Generated simulated_outages.json")
