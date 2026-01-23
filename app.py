from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="ML Inference API")

# Load model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Model API is running"}

@app.post("/predict")
def predict(features: list):
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)[0]

    return {
        "name": "Hubert",
        "roll_no": "YOUR_ROLL_NO",
        "wine_quality": int(round(prediction))
    }
