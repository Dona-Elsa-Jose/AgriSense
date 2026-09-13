import os
import pickle
import pandas as pd
from backend.schemas import SoilInput, CropOutput, CropCandidate

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# Load model safely
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
else:
    model = None

PROFITABILITY_SCORES = {
    "rice": 0.82, "maize": 0.74, "chickpea": 0.78, "kidneybeans": 0.80,
    "pigeonpeas": 0.71, "mothbeans": 0.65, "mungbean": 0.68, "blackgram": 0.70,
    "lentil": 0.73, "pomegranate": 0.89, "banana": 0.85, "mango": 0.88,
    "grapes": 0.92, "watermelon": 0.76, "muskmelon": 0.77, "apple": 0.90,
    "orange": 0.84, "papaya": 0.83, "coconut": 0.81, "cotton": 0.79,
    "jute": 0.72, "coffee": 0.87
}

def predict_crop(soil: SoilInput) -> CropOutput:
    if model is None:
        raise FileNotFoundError(f"model.pkl not found at {MODEL_PATH}. Run train.py first.")

    # Wrap in DataFrame to match trained feature names and remove warnings
    features_df = pd.DataFrame([{
        'n': soil.N,
        'p': soil.P,
        'k': soil.K,
        'temperature': soil.temperature,
        'humidity': soil.humidity,
        'ph': soil.ph,
        'rainfall': soil.rainfall
    }])

    probabilities = model.predict_proba(features_df)[0]
    classes = model.classes_

    top_indices = probabilities.argsort()[::-1][:3]

    top_crops = []
    for idx in top_indices:
        crop_name = str(classes[idx])
        conf = float(probabilities[idx])
        prof_score = PROFITABILITY_SCORES.get(crop_name.lower(), 0.70)

        candidate = CropCandidate(
            crop=crop_name,
            confidence=round(conf, 4),
            profitability_score=prof_score
        )
        top_crops.append(candidate)

    return CropOutput(
        top_crops=top_crops,
        recommended_crop=top_crops[0].crop
    )