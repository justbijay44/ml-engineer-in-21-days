# Day 7 — Linear & Logistic Regression from Scratch

## What I built
- Two of the most fundamental ML models from scratch: linear regression (continuous values) and logistic regression (binary classification), both using the same core pattern: predict -> calculate loss -> compute gradient -> update.

## How to run
```
py linear_regression.py
py logistic_regression.py
```

## Interesting bug / decision
- Logistic regression adds one extra step: the sigmoid function. We need a confidence score for "is this 0 or 1," which only makes sense as a 0-1 probability, not any raw number. Sigmoid squashes the linear output into that range — negative values push toward 0, positive toward 1.
</content>
