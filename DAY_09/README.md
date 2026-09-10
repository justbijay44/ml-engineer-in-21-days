# Day 9 — Titanic sklearn Pipeline, Docker, and CI

## What I built
- A full sklearn pipeline for the Titanic dataset: preprocessing, feature engineering, a tuned RandomForest model, saved and served through a standalone script, containerized with Docker, and checked by a CI workflow on every push.

## How to run
```
# train the model
py train.py

# run a sample prediction
py predict.py

# or run it containerized
docker build -t titanic-model .
docker run titanic-model
```

## CI
`.github/workflows/ci.yml` (repo root) installs dependencies, downloads the dataset, and runs `train.py` on every push.

## Interesting bug / decision
- Used `ColumnTransformer` + `Pipeline` so any model can be swapped in without rewriting preprocessing — keeps things modular and DRY.
- CI caught a real bug that worked fine locally: `Path("models").mkdir(exist_ok=True)` returns `None`, not the path — crashed the moment it ran in a clean environment.
</content>
