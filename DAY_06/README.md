# Day 6 — Numpy + Pandas + Titanic EDA

## What I built
- Finished vectorizing Game of Life with `np.where`. Learned pandas basics and saw how Week 1's manual functions (filter, sort, groupby) collapse into one-liners. Did a full EDA on the Titanic dataset in a notebook.

## How to run
```
py game_of_life.py
py pandas_intro.py
# titanic_eda.ipynb - open in VSCode/Jupyter and run cells
```

## Interesting bug / decision
- `fillna`/`dropna` return a new object, they don't change `df` in place — forgot to reassign at first.
- Switched from `.py` to `.ipynb` for the EDA, since this was exploratory rather than building a reusable tool.
- Pclass correlates negatively with survival, but that's not a contradiction — lower Pclass numbers mean better class, so it actually agrees with the Fare finding.
</content>
