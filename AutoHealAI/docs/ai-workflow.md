# AI Workflow

1. Monitoring Agent ingests infrastructure telemetry.
2. Prediction Agent computes failure probability.
3. Diagnosis Agent correlates restart spikes with latency and deployment events.
4. Recovery Agent selects playbook (restart, scale, rollback, isolate).
5. Validation Agent checks whether metrics normalize after remediation.
6. Explainability Agent produces human-readable decision narrative and confidence score.
