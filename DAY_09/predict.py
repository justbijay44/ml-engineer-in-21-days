import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

sample = pd.DataFrame([{
    "Pclass": 3,
    "Sex": "male",
    "Age": 22,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked": "S",
    "title": "Mr",
}])

prediction = model.predict(sample)
print("Survived" if prediction[0] == 1 else "Did not survive.")