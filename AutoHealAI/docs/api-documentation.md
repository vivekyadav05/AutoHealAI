# API Documentation

Base URL: `http://localhost:8000/api/v1`

## Endpoints

- `GET /health` service health
- `POST /auth/login` JWT token issue
- `POST /telemetry/ingest` ingest live telemetry and trigger prediction
- `GET /telemetry/latest` fetch latest metrics
- `GET /predictions/` list AI predictions
- `GET /incidents/` list incidents
- `GET /decisions/` list remediation decisions
- `WS /ws/live` websocket live stream
