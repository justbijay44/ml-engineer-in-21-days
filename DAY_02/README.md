# Day 2 — Terminal Data Explorer

## What I built
- Continued the same `explore.py` from Day 1. Added `sort_rows` (sort by any column) and `bar_chart` (a groupby-style bar chart, similar to pandas' `groupby().value_counts()`), plus a simple CLI so the tool can be run as `py explore.py <command> <args>` instead of editing the script each time.

## How to run
```
py explore.py <command> <args...>
# e.g.
py explore.py describe
py explore.py filter Age ">" 30
py explore.py sort Age
py explore.py bar_chart Pclass Survived
```

## Dataset
Titanic dataset — download from:
https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
Save as `data/titanic.csv`.

## Interesting bug / decision
- To make the bar chart ordered by count (largest first), I used `sorted()` on the dict's `.items()`. That returns a list of tuples, not a dict — so I couldn't index it like a dict anymore, only unpack each tuple as `key, val`. Small thing, but it clarified the difference between a dict and a list of tuples for me. Also never thought it but we cannt slice a dict, for such case also we can do the same thing convert to list.

</content>
