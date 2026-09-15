import difflib

from datasets import load_dataset
from transformers import pipeline

def raw_entities(ner, text, threshold=0.8):
    results = ner(text)
    word_list = []
    for item in results:
        if item['score'] >= threshold and len(item['word']) > 2 and not item['word'].startswith("#"):
            word_list.append((item['word'], item['entity_group']))
    return word_list

def extract_entities(words, similarity_score = 0.7):
    canonical_counts = {}
    for word, entity in words:
        matched = False

        for in_word in canonical_counts:
            similarity = difflib.SequenceMatcher(None, in_word, word).ratio()

            if similarity > similarity_score or in_word in word or word in in_word:
                canonical_counts[in_word]["count"] += 1
                matched = True
                break

        if not matched:
            canonical_counts[word] = {
                "count": 1,
                "entity": entity,
            }

    return canonical_counts

if __name__ == "__main__":
    news_data = load_dataset("fancyzhx/ag_news")

    ner = pipeline("ner", aggregation_strategy="simple")

    texts = news_data["train"][:50]["text"]

    all_words = []
    for text in texts:
        all_words.extend(raw_entities(ner, text))

    canonical_counts = extract_entities(all_words)
    top10_key_words = sorted(canonical_counts.items(), key=lambda x: x[1]["count"], reverse=True)[:10]
    print(top10_key_words)