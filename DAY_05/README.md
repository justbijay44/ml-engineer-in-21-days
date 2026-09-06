# Day 5 — Wordle + Numpy Intro

## What I built
- A Wordle clone from scratch — guess a 5-letter word in 6 tries. Then started numpy, comparing it to a week of manual grid code: rebuilt Game of Life's neighbor counting with array slicing instead of nested loops.

## How to run
```
py wordle.py
py numpy_intro.py
py game_of_life.py
```

## Rules (Wordle, for reference)
- Guess the secret 5-letter word in 6 tries
- Each letter is marked: correct spot, wrong spot (in the word, different position), or not in the word
- Handles duplicate letters correctly (e.g. guessing two Es when the secret only has one)

## Interesting bug / decision
- Duplicate letters in a guess (e.g. two Es when the secret only has one) needed two passes: mark all exact matches first, then only credit "wrong spot" up to how many of that letter are actually left over. A single left-to-right pass over-credits.
- Numpy's neighbor counting was the hardest mental shift so far,no loop over cells at all. Pad the grid with zeros, then shift-and-add 8 sliced copies of it. Took a while to stop thinking cell-by-cell.
</content>
