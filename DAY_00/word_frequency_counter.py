# text = 'It makes sense they felt smoother than expected. It is worth testing with something less "interview-question-shaped" before I can fully calibrate.'

text = """

Build a word-frequency counter. Give it any block of text and it should print the top 5 most-used words, ignoring case and punctuation ("The" and "the." should count as the same word).

No function signature from me — decide the structure yourself (function? class? script?). Take your time.

"""

def word_frequency_counter(text):
    dict_ = {}
    for word in text.split():
        for char in word:
            if not char.isalpha():
                word = word.replace(char, ' ')
        word = word.lower().strip()

        if word:
            dict_[word] = dict_.get(word, 0) + 1

    top_5 = sorted(dict_.items(), key=lambda x: x[1], reverse=True)[:5]

    print("Top 5 words: \n")
    
    return '\n'.join(f"{item[0].title()}: {item[1]}"for item in top_5)

print(word_frequency_counter(text))