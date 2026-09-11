# Day 10 — SMS Spam Classifier (NLP)

## What I built
- An SMS spam/ham classifier using TF-IDF + Logistic Regression, tuned for class imbalance, packaged as one sklearn Pipeline, containerized with Docker, and checked by CI.

## How to run
```
py train.py
py predict.py

# or containerized
docker build -t sms-classifier .
docker run sms-classifier
```

## CI
`.github/workflows/ci-day10.yml` (repo root) installs dependencies, downloads the dataset, and runs `train.py` on every push.

## Interesting bug / decision
- Learned NLP isn't one specific tool — it's the broad field of getting machines to understand and respond to language, covering translation, semantic analysis, generation, and more. TF-IDF is just one way to represent text as numbers.
- Adding message length as an extra feature didn't actually improve the model — the text content alone already captured that signal.
</content>
