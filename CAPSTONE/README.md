# Capstone — Credit Card Fraud Detection

## What I built
A fraud detection model on the credit card fraud dataset (284k transactions, ~0.17% fraud). Cleaned duplicates, engineered an `hours` feature from `Time`, scaled `Amount` with a RobustScaler, and compared RandomForest against LightGBM. RandomForest with `class_weight="balanced"` won. Final result: 91% precision / 78% recall on the fraud class.

## How to run
```
py src/train.py
```

## Interesting bug / decision
- A threshold tuned for one model doesn't transfer to another — reusing RandomForest's threshold on LightGBM gave 1071 false positives.
- Tuning for cross-validated recall found a model that looked better in CV but performed worse on the real test set than the simple untuned baseline — kept the baseline.

