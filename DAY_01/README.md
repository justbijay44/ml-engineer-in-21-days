# Day 1 — Terminal Data Explorer

## What I built
- We explored the titanic dataset to replicate the describe, filter manually instead of using pandas

## How to run
```
py explore.py
```

## Dataset
Titanic dataset — download from:
https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
Save as `data/titanic.csv`.

## Interesting bug / decision
- instead of a regular if/else we have used a try/except block for filtering, so the same function can handle both numeric and string columns without knowing the type ahead of time.
</content>
