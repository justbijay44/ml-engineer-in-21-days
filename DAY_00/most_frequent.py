def most_frequent(lst):
    freq = {}

    for item in lst:
        freq[item] = freq.get(item, 0) + 1

    return max(freq.items(), key=lambda x: x[1])[0]

print(most_frequent([1, 10, 2, 4, 2, 6, 4, 4]))