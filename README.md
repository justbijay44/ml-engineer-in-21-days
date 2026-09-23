# ML Engineer in 21 Days

A self-directed 21-day plan (2026-09-02 to 2026-09-23) to build ML engineering skills through daily projects, going from Python fundamentals to a full production-shaped capstone.

## Highlight: Fraud Detection Capstone

**[CAPSTONE/](CAPSTONE/)** — the flagship project, built over the final days. An end-to-end fraud detection system:
- EDA and feature engineering on a real, heavily imbalanced dataset (284k transactions, 0.17% fraud)
- RandomForest model, compared against LightGBM, with precision/recall threshold tuning
- MongoDB for logging predictions (compound index, aggregation pipeline for deduplication, a basic drift-monitoring check)
- FastAPI serving endpoint, containerized with Docker Compose (API + MongoDB), CI via GitHub Actions
- A written A/B-testing methodology doc for safely rolling out future model versions

## Day-by-day

Early days build fundamentals (from-scratch data structures, algorithms, small games) before moving into numpy/pandas, classical ML from scratch (linear/logistic regression, k-NN, a tiny neural net), PyTorch, computer vision (MNIST, CIFAR-10), NLP (NER), time series forecasting, and finally the capstone above.

| Day | Topic |
|---|---|
| [DAY_00](DAY_00/) | Python fundamentals diagnostic |
| [DAY_01](DAY_01/)–[DAY_02](DAY_02/) | Terminal data explorer (CSV tool from scratch) |
| [DAY_03](DAY_03/)–[DAY_05](DAY_05/) | Standalone projects (Conway's Game of Life, Minesweeper, Wordle), numpy intro |
| [DAY_06](DAY_06/) | Pandas, Titanic EDA |
| [DAY_07](DAY_07/)–[DAY_08](DAY_08/) | ML from scratch: linear/logistic regression, k-NN, tiny neural net |
| [DAY_09](DAY_09/) | Full sklearn pipeline (Titanic) — tuning, feature engineering, Docker, CI |
| [DAY_10](DAY_10/) | Classical NLP — SMS spam classifier (TF-IDF), Docker, CI |
| [DAY_11](DAY_11/) | PyTorch fundamentals (autograd, nn.Module, optimizers) |
| [DAY_12](DAY_12/) | MNIST classifier (MLP + CNN) |
| [DAY_13](DAY_13/)–[DAY_15](DAY_15/) | CIFAR-10 image classifier — CNN, FastAPI, Docker, CI, accuracy improvements (66% → 80%) |
| [DAY_14](DAY_14/) | Named Entity Recognition (HuggingFace transformers) |
| [DAY_16](DAY_16/) | Time series forecasting (hourly energy demand) |
| [CAPSTONE](CAPSTONE/) | Fraud detection — see above |
