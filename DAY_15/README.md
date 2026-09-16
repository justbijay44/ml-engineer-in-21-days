# Day 15 — CIFAR-10 Improved (Augmentation, BatchNorm, Dropout)

## What I built
Rewrote the CIFAR-10 CNN from scratch and iteratively improved it: data augmentation, per-epoch test evaluation, batch norm, dropout, and a third conv layer. Took accuracy from Day 13's 66.49% baseline to 79.83%, with a save-best-checkpoint so the strongest epoch is always kept. Added a standalone inference function and FastAPI endpoint here too, separate from Day 13's baseline.

## How to run
```
py train.py
py predict.py

# serve predictions via API
uvicorn app:app --reload
```

## Interesting bug / decision
- Forgetting `model.eval()` before inference left dropout active at prediction time, silently degrading and destabilizing results (75.98% instead of the real 79.83%).
- Kept Day 13's original model untouched as a baseline rather than overwriting it — Day 15 is the improved, separate version.
- A conv layer's output-channel count (e.g. 64) and the image's spatial size (32x32) are unrelated numbers that just happen to overlap — mixed these up more than once while recomputing the flatten size after adding a third conv layer.
