import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def train_model() -> None:
    data_path = "data/auto-mpg.csv"
    model_path = "models/mpg_model.pkl"

    df = pd.read_csv(data_path)

    features = ["cylinders", "horsepower", "weight"]
    target = "mpg"
    X = df[features]
    y = df[target]

    rf = RandomForestRegressor(n_estimators=150, max_depth=5)
    rf.fit(X, y)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(rf, f)


if __name__ == "__main__":
    train_model()
