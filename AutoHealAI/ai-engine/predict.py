import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.ensemble import RandomForestClassifier


class AutoHealPredictor:
    def __init__(self):
        self.anomaly_model = IsolationForest(contamination=0.1, random_state=42)
        self.risk_model = RandomForestClassifier(n_estimators=100, random_state=42)

    def fit(self, df: pd.DataFrame):
        features = df[["cpu", "memory", "latency", "error_rate", "restarts"]]
        labels = df["failure_label"]
        self.anomaly_model.fit(features)
        self.risk_model.fit(features, labels)

    def infer(self, row: dict):
        x = [[row["cpu"], row["memory"], row["latency"], row["error_rate"], row["restarts"]]]
        anomaly_score = float(self.anomaly_model.decision_function(x)[0])
        failure_prob = float(self.risk_model.predict_proba(x)[0][1])
        severity = "critical" if failure_prob > 0.8 else "high" if failure_prob > 0.6 else "medium" if failure_prob > 0.35 else "low"
        return {
            "failure_probability": round(failure_prob, 3),
            "anomaly_score": round(anomaly_score, 3),
            "severity": severity,
            "confidence": round(min(0.99, 0.55 + abs(failure_prob - 0.5)), 3),
        }
