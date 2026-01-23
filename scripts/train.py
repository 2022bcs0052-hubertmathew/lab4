import json
import joblib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
X, y = load_wine(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Save model
joblib.dump(model, "model.pkl")

# Save metrics
metrics = {
    "r2": round(float(r2), 4),
    "mse": round(float(mse), 4)
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)

print("Training completed")
print(metrics)

