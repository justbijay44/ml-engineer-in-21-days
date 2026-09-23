# Capstone — Credit Card Fraud Detection

## What I built
An end-to-end fraud detection system on the credit card fraud dataset (284k transactions, ~0.17% fraud):
- RandomForest model (beat LightGBM), 91% precision / 78% recall on the fraud class
- MongoDB logging for predictions — compound index, a drift check, and an aggregation pipeline for deduplication
- FastAPI `/predict` endpoint
- Dockerized (API + MongoDB via Compose), with CI on GitHub Actions
- [A/B-testing writeup](api/AB_TESTING.md) for rolling out future model versions

## How to run
```
docker compose up --build
```
Then open `localhost:8000/docs` to try `/predict`.

To just retrain the model:
```
py src/train.py
```

## Interesting bug / decision
- A threshold tuned for one model doesn't transfer to another — reusing RandomForest's threshold on LightGBM gave 1071 false positives.
- Tuning for cross-validated recall found a model that looked better in CV but performed worse on the real test set than the simple untuned baseline — kept the baseline.
- `joblib.load` deserializes arbitrary code, so the model/scaler files should only ever come from a trusted source, never user-uploaded.

