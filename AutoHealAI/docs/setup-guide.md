# Setup Guide

## Prerequisites

- Docker Desktop
- Python 3.10+
- Node 20+ (for running frontend outside Docker)

## Steps

1. Copy environment file:
   - `cp .env.example .env`
2. Start the platform:
   - `docker compose up --build`
3. Generate synthetic telemetry:
   - `python scripts/telemetry_generator.py`
4. Open dashboard at `http://localhost:5173`.
