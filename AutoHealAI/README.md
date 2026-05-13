# AutoHealAI

AI-Driven Predictive Self-Healing Cloud Infrastructure Platform.

AutoHealAI is a production-oriented reference project that combines DevOps, cloud-native operations, AI/ML prediction, and autonomous remediation into one platform.

## Key Capabilities

- Real-time infrastructure telemetry ingestion and visualization
- AI-based failure prediction with confidence and severity scores
- Autonomous remediation playbooks via Kubernetes API
- Root-cause analysis based on metrics, logs, and deployment history
- Explainable AI decision timeline and recommendations
- Multi-agent orchestration for monitoring, diagnosis, recovery, and validation

## Tech Stack

- Frontend: React, Tailwind CSS, Recharts, Axios
- Backend: FastAPI, WebSockets, JWT auth, SQLAlchemy
- AI/ML: Scikit-learn, XGBoost, Pandas, NumPy
- Data/Streaming: PostgreSQL, Kafka, Spark job scaffold
- Observability: Prometheus, Grafana, ELK stack
- Infra: Docker, Kubernetes, Terraform

## Project Structure

- `frontend/` React dashboard and pages
- `backend/` FastAPI services and APIs
- `ai-engine/` prediction, simulation, explainability modules
- `k8s/` Kubernetes manifests
- `terraform/` IaC for cloud bootstrap
- `docker/` Dockerfiles and compose helpers
- `monitoring/` Prometheus and Grafana config
- `scripts/` telemetry generators and seed scripts
- `docs/` setup, architecture, API and research documentation

## Quick Start

1. Install Docker + Docker Compose, Python 3.11+, Node 20+.
2. Copy env file:
   - `cp .env.example .env`
3. Start local platform:
   - `docker compose up --build`
4. Open **on your machine** while the stack is running (these are not public URLs and will not load from the GitHub website alone):
   - [Frontend dashboard](http://localhost:5173)
   - [Backend API docs (Swagger)](http://localhost:8000/docs)
   - [Grafana](http://localhost:3000) (login `admin` / `admin` unless you changed it)
   - [Kibana](http://localhost:5601)

The frontend talks to the API through a **relative** `/api/v1` path and the Vite dev proxy, so sidebar navigation and data loading work the same in Docker and local dev.

## Push to GitHub

See [docs/github-setup.md](docs/github-setup.md) for creating the remote repository and pushing this project.

## Demo Login

- Email: `admin@autohealai.local`
- Password: `admin123`

## Research Contribution Highlights

- Hybrid prediction using anomaly + supervised risk scoring
- Explainable decision cards for each remediation
- Deployment risk guardrail with automatic rollback trigger
- Reproducible outage simulation for comparative experiments

See `docs/` for full architecture, setup, and publication-ready notes.
