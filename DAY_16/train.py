import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

def build_features(df):
    df["Datetime"]= pd.to_datetime(df["Datetime"])
    df = df.set_index("Datetime")
    df = df.sort_index()

    df["hour"] = df.index.hour
    df["dayofweek"] = df.index.dayofweek
    df["month"] = df.index.month
    df["year"] = df.index.year

    df["lag_day"] = df["PJME_MW"].shift(24)
    df["lag_week"] = df["PJME_MW"].shift(168)        

    df["rolling_day"] = df["PJME_MW"].rolling(24).mean()

    df = df.dropna()

    return df

def train_test(df):
    train = df[df.index < "2017-01-01"]
    test = df[df.index >= "2017-01-01"]

    X_train = train.drop(columns=['PJME_MW'])
    y_train = train['PJME_MW']
    X_test = test.drop(columns=['PJME_MW'])
    y_test = test['PJME_MW']

    return X_train, X_test, y_train, y_test

def train_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5

    print(f"MAE: {mae}")
    print(f"RMSE: {rmse}")

    return mae, rmse


if __name__ == "__main__":
    import os
    import kagglehub

    path = kagglehub.dataset_download("robikscube/hourly-energy-consumption")

    df = pd.read_csv(os.path.join(path, "PJME_hourly.csv"))

    df = build_features(df)

    X_train, X_test, y_train, y_test = train_test(df)

    mae, rmse = train_model(
        RandomForestRegressor(n_estimators=100, random_state=42),
        X_train, X_test, y_train, y_test
    )