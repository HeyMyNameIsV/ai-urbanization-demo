from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import joblib
import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("tourism_model.pkl")

@app.get("/recommendations")
def get_recommendations():
    with open("geo_data.json", "r") as f:
        geojson = json.load(f)

    results = []
    for feature in geojson["features"]:
        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]

        input_features = np.array([
            props["elevation"],
            props["water_proximity"],
            props["road_access_score"]
        ]).reshape(1, -1)

        score = model.predict(input_features)[0]

        results.append({
            "name": props["name"],
            "score": round(score, 2),
            "lat": coords[1],
            "lon": coords[0]
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return {"recommendations": results[:3]}