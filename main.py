# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import subprocess
import uvicorn

app = FastAPI(title="Health Orchestrator")

# Load trained ML model
model = joblib.load("health_model.pkl")

class HealthResponse(BaseModel):
    service: str
    status: str
    action_taken: str

@app.get("/healthcheck", response_model=HealthResponse)
def healthcheck():
    # Simulated real-time metrics (replace with Prometheus or GCP API later)
    cpu = 0.65
    memory = 0.7
    latency = 0.45
    error_rate = 0.2
    X = np.array([[cpu, memory, latency, error_rate]])

    prediction = model.predict(X)[0]
    service_name = "health-orchestrator"

    if prediction == 1:
        status = "healthy"
        action = "none"
    else:
        status = "unhealthy"
        action = "restarted"
        # Auto-restart Kubernetes deployment
        subprocess.run([
            "kubectl", "rollout", "restart", f"deployment/{service_name}"
        ])

    return HealthResponse(service=service_name, status=status, action_taken=action)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
