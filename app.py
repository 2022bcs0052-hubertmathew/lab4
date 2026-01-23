from fastapi import FastAPI, Form
import joblib
import numpy as np

app = FastAPI(title="ML Inference API")

# Load trained model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Model API is running"}

@app.post("/predict")
def predict(features: str = Form(...)):
    """
    features should be comma-separated numbers:
    Example: "13.2,2.77,2.51,18.5,..."
    """

    # Convert string → list of floats
    try:
        values = [float(x) for x in features.split(",")]
    except:
        return {"error": "Invalid input format"}

    data = np.array(values).reshape(1, -1)
    prediction = model.predict(data)[0]

    return {
        "name": "Hubert",
        "roll_no": "2022bcs0052",
        "wine_quality": int(round(prediction))
    }
