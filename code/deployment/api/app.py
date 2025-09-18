import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

with open("/app/models/mpg_model.pkl", "rb") as f:
    model = pickle.load(f)


class CarFeatures(BaseModel):
    cylinders: int = Field(..., ge=1, le=16, examples=[4, 6, 8])
    horsepower: int = Field(..., ge=50, le=1800, examples=[160, 250, 525])
    weight: int = Field(..., ge=1000, le=5000, examples=[1500, 2700, 3140])


@app.post("/predict")
def predict(data: CarFeatures):
    df = pd.DataFrame([{
        "cylinders": data.cylinders,
        "horsepower": data.horsepower,
        "weight": data.weight
    }])

    prediction = model.predict(df)
    
    return {"mpg": round(prediction[0], 2)}
