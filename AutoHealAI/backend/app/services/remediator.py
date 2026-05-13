from datetime import datetime


def get_remediation_plan(service: str, severity: str):
    if severity == "critical":
        return {
            "action_type": "restart_and_rollback",
            "status": "executed",
            "explanation": f"{datetime.utcnow().isoformat()}Z | {service}: critical risk detected, restarted pods and initiated rollback guard.",
        }
    if severity == "high":
        return {
            "action_type": "scale_up",
            "status": "executed",
            "explanation": f"{datetime.utcnow().isoformat()}Z | {service}: high risk detected, scaled replicas from 2 to 4.",
        }
    return {
        "action_type": "observe",
        "status": "queued",
        "explanation": f"{datetime.utcnow().isoformat()}Z | {service}: risk below high threshold, monitoring mode enabled.",
    }
