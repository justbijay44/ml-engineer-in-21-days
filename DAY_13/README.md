# Day 13 — CIFAR-10 Capstone: CNN + FastAPI

## What I built
CIFAR-10 pipeline: EDA -> CNN train/predict -> inference function -> FastAPI endpoint.

## How to run
```
py train.py
py predict.py

# serve predictions via API
uvicorn app:app --reload
# then open http://127.0.0.1:8000/docs to upload an image
```

## Interesting bug / decision
A conv layer's input channels must match the image's channels (or the previous layer's output channels) — only the output channel count is a free choice.
