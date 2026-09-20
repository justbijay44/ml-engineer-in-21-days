# A/B Testing — Rolling Out a New Fraud Model

How I'd validate a new/retrained fraud model against the current one before fully replacing it.

## Types of error

- **Type I error**: concluding "B is better" when it actually isn't — a false positive on the comparison, caused by chance/randomness in the sample.
- **Type II error**: the opposite — B actually is better, but the test fails to detect it. Often caused by too small a sample size.

## Setup

- Randomly assign each incoming transaction to group A (current model) or group B (candidate model) — not split by time of day, since fraud patterns vary by time of day.
- Log a `model_version` field alongside each prediction, per group.
- Run both simultaneously for a fixed period, then compare metrics between the two groups.

## Sample size

Sample size is how much test data each group needs before a comparison is trustworthy. Too little data means too little signal to detect a real (but modest) difference between groups — the comparison ends up dominated by noise.

## Sequential vs. fixed horizon

- **Sequential**: check results as data comes in, stop early if a clear winner emerges — similar to early stopping during training. The tradeoff: every extra "peek" at the results is another chance at a false positive, so sequential testing needs statistical corrections to stay valid.
- **Fixed horizon**: decide the total sample size upfront, don't look at results until that number is reached, then analyze once.