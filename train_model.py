import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Simulated training data
data = {
    "elevation": [200, 900, 300, 1100, 700, 500],
    "water_proximity": [0.1, 0.9, 0.2, 0.8, 0.5, 0.6],
    "road_access_score": [9, 6, 8, 4, 5, 7],
    "tourism_score": [180, 430, 210, 470, 350, 300]
}

df = pd.DataFrame(data)

X = df.drop(columns=["tourism_score"])
y = df["tourism_score"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "tourism_model.pkl")
print("✅ Model trained and saved.")