import os
import pandas as pd


def load_dataset() -> None:
    save_path = "data/auto-mpg.csv"
    url = "https://huggingface.co/datasets/scikit-learn/auto-mpg/resolve/main/auto-mpg.csv"

    df = pd.read_csv(url, na_values="?")
    df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path)


if __name__ == "__main__":
    load_dataset()
