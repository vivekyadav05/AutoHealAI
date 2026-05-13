# Deployment Guide

## Docker Deployment

- `docker compose up --build -d`

## Kubernetes Deployment

1. Build and push images.
2. Apply manifests:
   - `kubectl apply -f k8s/namespace.yaml`
   - `kubectl apply -f k8s/backend.yaml`
   - `kubectl apply -f k8s/frontend.yaml`
   - `kubectl apply -f k8s/hpa.yaml`

## Terraform Bootstrap

- `cd terraform`
- `terraform init`
- `terraform plan`
- `terraform apply`
