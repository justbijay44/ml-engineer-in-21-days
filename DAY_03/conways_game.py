import random
import time
import subprocess

def create_grid(row, col):
    two_d = [
        [random.choice([0, 1]) for _ in range(col)]
        for _ in range(row)
    ]
    return two_d

def print_grid(two_d):
    for r in two_d:
        display_row = ['■' if cell else '·' for cell in r]
        print(' '.join(display_row))

def count_neighbors(grid, row, col):
    pos = [-1, 0, 1]
    live_counts = 0
    for dr in pos:
        for dc in pos:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc]:
                    live_counts += 1

    return live_counts

def next_state(cell, live_count):
    if cell and 2 <= live_count <= 3:
        return 1
    else:
        if live_count == 3:
            return 1
    return 0

def next_generation(grid):
    row_length = len(grid)
    col_length = len(grid[0])
    new_grid = []
    for r in range(row_length):
        new_row = []
        for c in range(col_length):
            live_counts = count_neighbors(grid, r, c)
            new_state = next_state(grid[r][c], live_counts)
            new_row.append(new_state)
        new_grid.append(new_row)

    return new_grid

def generations(original_gen, num_generations=5):
    gen = original_gen
    result = []
    for _ in range(1, num_generations):
        new_gen = next_generation(gen)
        result.append(new_gen)
        gen = new_gen

    return result

if __name__ == "__main__":

    original_gen = create_grid(15, 15)
    print("Original ('■': Alive | '·': Dead )")
    print_grid(original_gen)

    gens = generations(original_gen, num_generations=20)

    for idx, gen in enumerate(gens):
        subprocess.run("cls", shell=True)
        print(f"\nGeneration {idx + 1}\n")
        print_grid(gen)
        time.sleep(1)