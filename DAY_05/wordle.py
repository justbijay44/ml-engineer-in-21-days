import random
from collections import Counter

list_of_word = ["apple", "grape", "chair", "brave", "stone"]

def check_guess(secret, guess):
    match = [None] * len(secret) 

    secret_count = Counter(secret)
    
    for idx, (s, g) in enumerate(zip(secret, guess)):
        if s == g:
            secret_count[s] -= 1
            match[idx] = g.upper()

    for idx, (s, g) in enumerate(zip(secret, guess)):
        if match[idx] is None:
            if g in secret and secret_count[g] > 0:
                secret_count[g] -= 1
                match[idx] = '🟡'
            else:    
                match[idx] = '🔴'

    return match

if __name__ == "__main__":
    secret = random.choice(list_of_word)
    count = 6
    while True:
        if count == 0:
            print(f"The word was: {secret}")
            break

        print(f"Guesses remaining: {count}")
        user_inp = input("Guess('q' to exit): \n")

        if user_inp == 'q':
            break

        if len(user_inp) != 5:
            print("Please enter a 5 letter word")
            continue

        if user_inp == secret:
            print(f"You Win!. Word was {user_inp.upper()}")
            break

        match = check_guess(secret, user_inp)
        print(' '.join(m for m in match))
        count -= 1

