import numpy as np

def build_grid(row, col):
    return np.random.randint(0, 2, size=(row, col))

def live_neigbors_count(grid, padded_grid):
    count = np.zeros_like(grid)
    pos = [-1, 0, 1]
    rows, cols = grid.shape

    for dr in pos:
        for dc in pos:
            if dr == 0 and dc == 0:
                continue
            count += padded_grid[1 + dr : 1 + dr + rows, 1 + dc : 1 + dc + cols]
    return count

def next_generation(grid, live_count):
    survives = (grid == 1) & ((live_count == 2) | (live_count == 3))
    born = (grid == 0) & (live_count == 3)
    new_grid = np.where(survives | born, 1, 0)
    return new_grid

grid = build_grid(3, 3)
padded_grid = np.pad(grid, 1)

live_count = live_neigbors_count(grid, padded_grid)

print(grid)
print(live_count)
print(next_generation(grid, live_count))