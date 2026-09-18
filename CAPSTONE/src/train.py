import os
import joblib
import pandas as pd
from pathlib import Path

from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

def load_data(path):
    df = pd.read_csv(os.path.join(path, 'creditcard.csv'))
    return df

def build_features(df):
    df = df.drop_duplicates()
    df["hours"] = (df["Time"] % 86400) / 3600
    return df

def split_and_scale(df, scale):
    X = df.drop(columns=['Time', 'Class'])
    y = df['Class']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42)

    X_train["Amount"] = scale.fit_transform(X_train[["Amount"]])
    X_test["Amount"] = scale.transform(X_test[["Amount"]])

    return X_train, X_test, y_train, y_test

def train_model(model, X_train, X_test, y_train, y_test, probability=0.3):
    model.fit(X_train, y_train)
    proba = model.predict_proba(X_test)[:, 1]
    pred = (proba > probability).astype(int)

    print(f"Confusion report:\n {confusion_matrix(y_test, pred)}\n")
    print(f"Classification report:\n {classification_report(y_test, pred)}")

    return model

if __name__ == "__main__":

    import kagglehub
    path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

    df = load_data(path)

    df = build_features(df)

    scale = RobustScaler()

    X_train, X_test, y_train, y_test = split_and_scale(df, scale)

    model = train_model(
        RandomForestClassifier(
            n_estimators=100, random_state=42, class_weight="balanced"
        ),
        X_train, X_test, y_train, y_test
    )

    model_dir = Path(__file__).parent.parent / "models"
    model_dir.mkdir(exist_ok=True)

    joblib.dump(model, model_dir / "model.joblib")
    joblib.dump(scale, model_dir / "scale.joblib")