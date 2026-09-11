import joblib

model = joblib.load('models/models.pkl')

sample_text = ["You just won $100,000!!! Click the link to claim it.", "Hey, How are you?"]

prediction = model.predict(sample_text)

print('\n'.join(prediction))