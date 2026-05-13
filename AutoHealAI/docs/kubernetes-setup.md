# Kubernetes Setup

## Prerequisites

- Minikube or managed Kubernetes cluster
- Metrics server installed (required for HPA)

## Deploy

- `kubectl apply -f k8s/`

## Verify

- `kubectl get pods -n autohealai`
- `kubectl get svc -n autohealai`
- `kubectl get hpa -n autohealai`
