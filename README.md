# Microservice Health Orchestrator

This system monitors microservice health using Prometheus metrics and performs intelligent healing actions (like restart, reroute, scale) based on a trained ML model.

## Key Components

- Real-time health monitoring via Prometheus
- ML-based failure prediction
- Kubernetes orchestrator for self-healing
- Grafana dashboard integration
- Dockerized deployment with Kubernetes support

## How to Run

1. Train the health model: `python models/train_health_model.py`
2. Deploy Prometheus and Grafana.
3. Deploy orchestrator using Kubernetes manifests in `k8s/`.

## License

MIT
