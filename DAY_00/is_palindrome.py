def is_palindrome(text):
    if not text:
        return False

    clean_text = ''.join(char for char in text if char.isalnum())
    reversed_text = clean_text[::-1]
    return clean_text.lower() == reversed_text.lower()

print(is_palindrome("race caR"))