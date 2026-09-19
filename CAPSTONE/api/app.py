import os
import joblib
from pathlib import Path
from pydantic import BaseModel

from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from db.mongo import make_connection, create_indexes, insert_prediction

model = joblib.load(Path(__file__).parent.parent / "models" / "model.joblib")
scale = joblib.load(Path(__file__).parent.parent / "models" / "scale.joblib")

uri = os.environ.get("MONGO_URL", "mongodb://localhost:27017")

@asynccontextmanager
async def lifespan(app: FastAPI):
    db, collection = make_connection("fraud_db", "predictions", uri)
    create_indexes(collection)
    app.state.collection = collection
    yield

app = FastAPI(lifespan=lifespan, title="Fraud Detection")

class TransactionInput(BaseModel):
    V1              : float
    V2              : float
    V3              : float
    V4              : float
    V5              : float
    V6              : float
    V7              : float
    V8              : float
    V9              : float
    V10             : float
    V11             : float
    V12             : float
    V13             : float
    V14             : float
    V15             : float
    V16             : float
    V17             : float
    V18             : float
    V19             : float
    V20             : float
    V21             : float
    V22             : float
    V23             : float
    V24             : float
    V25             : float
    V26             : float
    V27             : float
    V28             : float
    amount          : float
    hours           : float
    transaction_id  : int

@app.post("/predict")
def predict(inp: TransactionInput, request: Request):
    data = inp.model_dump()
    scaled_amount = scale.transform([[data["amount"]]])[0][0]
    features = [data[f"V{i}"] for i in range(1, 29)] + [scaled_amount] + [data["hours"]]
    prediction = model.predict_proba([features])[:, 1]

    prob = float(prediction[0])
    label = "fraud" if prob > 0.3 else "not fraud"

    insert_prediction(
        collection=request.app.state.collection,
        transaction_id=inp.transaction_id,
        amount=inp.amount,
        hours=inp.hours,
        prediction=label,
        probability=prob
    )

    return f"Model Prediction: {label} | Probability: {prob}"