# Architecture

```text
Telemetry Sources -> Kafka -> Stream Processor -> AI Prediction Engine
                                      |               |
                                      v               v
                              FastAPI Ingestion   Remediation Engine
                                      |               |
                                      v               v
                                 PostgreSQL <-> Explainability Service
                                      |
                                      v
                           React Dashboard + Grafana + Kibana
```

## Components

- Monitoring Agent: collects service and infra metrics
- Prediction Agent: forecasts outage probability and severity
- Diagnosis Agent: determines probable root cause
- Recovery Agent: triggers remediation actions
- Validation Agent: confirms post-fix stability
- Explainability Agent: narrates why a decision was taken
