import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")

def train_model():
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(f"Could not find {DATASET_PATH}. Please ensure dataset.csv exists in the crop directory.")

    print(f"Loading Kaggle dataset from {DATASET_PATH}...")
    df = pd.read_csv(DATASET_PATH)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()
    df.rename(columns={'ph': 'ph', 'crop': 'label'}, inplace=True)

    X = df[['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"\nModel trained successfully! Test Accuracy: {acc * 100:.2f}%")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
