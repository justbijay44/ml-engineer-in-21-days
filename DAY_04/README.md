# Day 4 — Minesweeper

## What I built
- Playable terminal Minesweeper from scratch. Random mines, neighbor counting, reveal with flood-fill, win/lose detection.

## How to run
```
py minesweeper.py
```

## Rules (for reference)
- Mines are placed randomly (~15% of cells)
- Each safe cell shows how many of its 8 neighbors are mines
- Revealing a blank cell (0 neighboring mines) auto-reveals its connected neighbors
- Hit a mine -> game over. Reveal every safe cell -> win.

## Interesting bug / decision
- Picked Minesweeper to get more reps with 2D grids after Day 3's Game of Life.
- First time using recursion — the flood-fill reveal calls itself on each blank neighbor.
- Merged two near-identical grid-builder functions into one, `build_grid(row, col, fill)`, passing in a function to decide each cell's value. Bug: forgot to call it (`fill` vs `fill()`), so cells held the function itself instead of its result.
</content>
