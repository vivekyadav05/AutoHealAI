import numpy as np


def predict_failure(cpu: float, memory: float, latency: float, error_rate: float, restarts: int):
    signal = (0.25 * cpu) + (0.25 * memory) + (0.2 * latency / 1000.0) + (0.2 * error_rate * 100) + (0.1 * restarts * 10)
    prob = float(1 / (1 + np.exp(-0.04 * (signal - 40))))

    if prob >= 0.8:
        severity = "critical"
        recommendation = "Immediate pod restart and deployment rollback check."
    elif prob >= 0.6:
        severity = "high"
        recommendation = "Scale replicas and inspect recent deployment diff."
    elif prob >= 0.4:
        severity = "medium"
        recommendation = "Enable traffic rerouting and increase monitoring frequency."
    else:
        severity = "low"
        recommendation = "No immediate action required; continue baseline monitoring."

    confidence = round(min(0.99, 0.6 + (abs(prob - 0.5))), 3)
    return round(prob, 3), severity, confidence, recommendation
