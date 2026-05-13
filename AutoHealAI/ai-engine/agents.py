from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class AgentResult:
    agent: str
    output: Dict[str, Any]


def monitoring_agent(metric: Dict[str, Any]) -> AgentResult:
    return AgentResult("MonitoringAgent", {"status": "collected", "metric": metric})


def prediction_agent(prediction: Dict[str, Any]) -> AgentResult:
    return AgentResult("PredictionAgent", {"status": "predicted", "prediction": prediction})


def diagnosis_agent(context: Dict[str, Any]) -> AgentResult:
    reason = "Deployment instability suspected" if context.get("restarts", 0) > 3 else "Resource pressure"
    return AgentResult("DiagnosisAgent", {"root_cause": reason})


def recovery_agent(severity: str) -> AgentResult:
    action = "rollback" if severity == "critical" else "scale_up" if severity == "high" else "observe"
    return AgentResult("RecoveryAgent", {"action": action})


def validation_agent() -> AgentResult:
    return AgentResult("ValidationAgent", {"status": "verified"})


def explainability_agent(decision: Dict[str, Any]) -> AgentResult:
    narrative = (
        f"Action '{decision.get('action')}' selected because predicted failure risk was "
        f"{decision.get('failure_probability', 'N/A')}."
    )
    return AgentResult("ExplainabilityAgent", {"narrative": narrative})
