# Day 14 — News Entity Analyzer (NER)

## What I built
Finished Day 13's Docker/CI, then started a news entity analyzer using NER on a HuggingFace dataset.

## How to run
```
py analyze.py
```

## Interesting bug / decision
NER only tags a fixed set of entity types, so it can split a word into subword pieces (marked with `##`) when it doesn't match a known one. It also prefixes tags with `I-` to mark "inside an entity."
