# Day 16 — Time Series Forecasting (Hourly Energy Demand)

## What I built
An hourly energy demand forecaster (PJM Interconnection data) — EDA with seasonal decomposition, lag/rolling-window feature engineering, and a RandomForestRegressor evaluated with MAE/RMSE on a chronological train/test split.

## How to run
```
py train.py
```

## Interesting bug / decision
- Adding very short lags (1-3 hours) dropped error massively, but it turned out the model was just learning "predict about the same as last hour" — which only works for 1-hour-ahead forecasting. Reverted to longer-horizon features (lag_day, lag_week, rolling_day) since that's the actually useful version of the problem.
- Time series indexes need to be sorted before date-string slicing works (`df["2012-10":"2012-11"]` fails on an unsorted DatetimeIndex).

