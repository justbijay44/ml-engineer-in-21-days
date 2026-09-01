text = "WrIte a function count_vowels(s)"

def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    if not text:
        return 0
    
    for char in text.lower():
        if char in vowels:
            count += 1

    return count

print(count_vowels(text))