# Day 11 — PyTorch Basics (Autograd, nn.Module, Optimizers)

## What I built
- Day 7's linear regression, redone in PyTorch: first with raw tensors + autograd, then again the standard way with `nn.Module` + `optim.SGD`.
- Day 8's XOR net, redone in PyTorch using `nn.Linear` layers instead of hand-written weight matrices.

## How to run
```
py test.py                     # linear regression, manual autograd
py linear_regression_nn.py     # linear regression, nn.Module + optim.SGD
py xor_nn.py                   # XOR net, nn.Module + optim.Adam
```

## Interesting bug / decision
- `.backward()` adds to `.grad` instead of replacing it — forgetting to zero it each step made gradients pile up and the loss explode.
- `m = m - lr*grad` inside `no_grad()` quietly breaks `requires_grad` on `m`. Fixed with in-place `m -= lr*grad`.
- Plain `optim.SGD` got stuck on XOR at ~0.693 loss, same as Day 8. Switching to `optim.Adam` fixed it (loss ~0.01) — it uses past gradients to move smarter, not just a fixed step every time.
