# Day 12 — MNIST: MLP vs CNN (PyTorch)

## What I built
MLP and CNN classifiers for MNIST, in PyTorch.

## How to run
```
# MLP
py mlp/train.py
py mlp/predict.py

# CNN
py cnn/train.py
py cnn/predict.py
```

## Interesting bug / decision
Both the conv kernel and max-pool slide a window over the image, but the kernel learns weights while max-pool just takes the max — no learning involved.
