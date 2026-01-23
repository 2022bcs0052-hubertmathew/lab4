from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

app = FastAPI(title="ML Inference API")

# Load trained model
model = joblib.load("model.pkl")

# Request schema
class Features(BaseModel):
    features: List[float]

@app.get("/")
def home():
    return {"message": "Model API is running"}

@app.post("/predict")
def predict(data: Features):
    values = data.features
    arr = np.array(values).reshape(1, -1)
    prediction = model.predict(arr)[0]

    return {
        "name": "Hubert",
        "roll_no": "2022bcs0052",
        "wine_quality": int(round(prediction))
    }
