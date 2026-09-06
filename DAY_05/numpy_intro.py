import numpy as np

grid = np.random.randint(0, 2, size=(5, 5))

print(grid)
# print(grid.shape)
# print(grid[0])
# print(grid[0, 2])
# print(grid.sum())

print(grid[:, 0])
print(grid[1:3, 1:3])
print(grid * 2)
print(grid > 0)