
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# Simulate realistic metrics dataset
np.random.seed(42)
n_samples = 10000

# Simulated features: CPU usage, Memory usage, Response time, Error rate
cpu = np.random.beta(2, 5, size=n_samples)
memory = np.random.beta(2, 5, size=n_samples)
latency = np.random.exponential(scale=0.3, size=n_samples)
error_rate = np.random.binomial(1, 0.1, size=n_samples) + np.random.normal(0, 0.05, size=n_samples)

X = np.vstack((cpu, memory, latency, error_rate)).T

# Label: 0 if any metric is beyond threshold
y = ((cpu < 0.7) & (memory < 0.7) & (latency < 0.5) & (error_rate < 0.3)).astype(int)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/health_model.pkl")
