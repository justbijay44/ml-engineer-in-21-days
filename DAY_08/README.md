# Day 8 — k-NN and a Tiny Neural Net from Scratch

## What I built
- k-NN from scratch (distance + majority vote). A tiny 2-layer neural net from scratch on the XOR problem.

## How to run
```
py knn.py
py neural_net.py
```

## Interesting bug / decision
- Forward/backward pass logic was correct, but loss never went below ~0.69 no matter the learning rate or seed tried. A known quirk of small sigmoid networks on XOR — didn't chase it further.
</content>
