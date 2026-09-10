import joblib
import pandas as pd
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def prepare_data(df):
    df = df.copy()

    df['title'] = df['Name'].str.extract(r'([A-Za-z]+)\.', expand=False)
    df['title'] = df['title'].apply(
        lambda title: title 
        if title in ['Mr', 'Miss', 'Mrs', 'Master'] else 'Other'
    )

    nominal_cols = ['Sex', 'Embarked', 'title']
    numerical_cols = ['Age', 'SibSp', 'Parch', 'Fare']
    cols_to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'Survived']

    preprocessor = ColumnTransformer(transformers=[
        ('Nom', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')), 
            ('ohe', OneHotEncoder(drop='first'))]), nominal_cols),

        ('Standard', Pipeline([
            ('imputer', SimpleImputer(strategy='median')), 
            ('scaler', StandardScaler())]), numerical_cols),
    ], remainder='passthrough')

    X = df.drop(columns=cols_to_drop)
    y = df['Survived']

    return train_test_split(X, y, test_size=0.2, random_state=42), preprocessor

def run_pipeline(model, preprocessor):
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('model', model),
    ])
    return pipe

def run_model(model, preprocessor, X_train, X_val, y_train, y_val):
    pipe = run_pipeline(model, preprocessor)
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Classification Matrix: \n{classification_report(y_val, y_pred)}\n")
    print(f"Confusion Matrix: \n{confusion_matrix(y_val, y_pred)}")

    return pipe

if __name__ == "__main__":
    titantic_df = pd.read_csv("data/titanic.csv")
    (X_train, X_val, y_train, y_val), preprocessor = prepare_data(titantic_df)

    model = run_model(
        RandomForestClassifier(
            max_depth = 10, min_samples_split = 5, n_estimators = 200, random_state=42
        ), 
        preprocessor,
        X_train, X_val, y_train, y_val
    )

    model_dir = Path("models").mkdir(exist_ok=True)
    joblib.dump(model, model_dir / "model.pkl")