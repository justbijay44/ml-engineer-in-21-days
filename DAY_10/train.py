import joblib
import pandas as pd
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def load_dataset(file_path: str):
    df = pd.read_csv(file_path, sep='\t', header=None, 
                        names=['label', 'message'])

    df = df.drop_duplicates() 
    return df

def build_pipeline(model):
    return Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('model', model)
    ])

if __name__ == "__main__":
    FILE_PATH = 'data/sms.tsv'
    MODEL_PATH = Path('models')
    MODEL_PATH.mkdir(exist_ok=True)

    df = load_dataset(FILE_PATH)
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'], df['label'], test_size=0.2, random_state=42,
        stratify=df['label']
    )

    pipe = build_pipeline(LogisticRegression(class_weight='balanced'))
    pipe.fit(X_train, y_train)

    y_pred = pipe.predict(X_test)
    print(accuracy_score(y_test, y_pred), '\n')
    print(classification_report(y_test, y_pred), '\n')

    joblib.dump(pipe, MODEL_PATH / 'models.pkl')