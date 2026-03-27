from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import pandas as pd
import numpy as np
from model import prepare_X, w0, w

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Car Price Prediction API is running"}

@app.post("/predict")
def predict(car: dict):
    df = pd.DataFrame([car])

    X = prepare_X(df)
    y_pred = w0 + X.dot(w)

    price = np.expm1(y_pred[0])

    return {"predicted_price": float(price)}