# 🧠 AI Tourism Zone Recommender

This is a demo project showcasing how **Artificial Intelligence can assist in urban planning**, specifically in identifying optimal zones for tourism development based on real-world geospatial data.

The prototype is a simplified version of a much larger vision: **AI-driven urbanization**, where entire cities can be planned using intelligent algorithms.

---

## 📌 What Does It Do?

- Takes region data in **GeoJSON** format
- Analyzes features like:
  - **Elevation**
  - **Water proximity**
  - **Road accessibility**
- Uses a trained **RandomForestRegressor** model to predict tourism potential
- Visualizes **Top 3 recommended zones** on an interactive map using **Leaflet.js**

---

## 🛠️ Tech Stack

| Layer         | Technology           |
|--------------|----------------------|
| Backend       | Python, FastAPI       |
| Machine Learning | scikit-learn (RandomForest) |
| Data Format   | GeoJSON (custom / simulated) |
| Frontend      | HTML, CSS, Leaflet.js |
| Deployment    | Localhost (demo mode) |

---

## 🧠 Model Logic

The AI model scores each region based on:
```plaintext
Tourism Score = 
  (Elevation × 0.3) + 
  (Road Access × 10) + 
  (Water Proximity > 0.7 ? +100 : 0)