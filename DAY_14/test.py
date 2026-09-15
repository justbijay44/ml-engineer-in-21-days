from transformers import pipeline

ner = pipeline("ner")

print(ner("Elon Musk founded SpaceX in California."))