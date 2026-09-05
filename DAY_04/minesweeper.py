import random
import subprocess


def build_grid(row, col, fill):
    """
    To create a 2D grid
    """

    return [
        [fill() for _ in range(col)]
        for _ in range(row)
    ]

def display_grid(grid):
    """
    To display the 2D grid visually
    """

    print('   ' + ' '.join(f"{c:>2}" for c in range(len(grid[0]))))
    print()
    for idx, r in enumerate(grid):
        print(f"{idx:>2}",' '.join(f"{row:>2}" for row in r))

def neighbor_mine_count(grid, row, col):
    """
    To count the 'M' present around the cell formed with row and col
    """

    pos = [-1, 0, 1]
    mine_count = 0

    for r in pos:
        for c in pos:
            if r == 0 and c == 0:
                continue
            nr, nc = row + r, col + c
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc]:
                    mine_count += 1

    return mine_count

def build_display_grid(grid):
    """
    To build the grid which consist of the answers
    Returns: the new_grid and the total mines
    """

    new_grid = []
    mine_count = 0
    for row in range(len(grid)):
        rows = []
        for col in range(len(grid[0])):
            if grid[row][col]:
                mine_count += 1
                rows.append('M')
            else:
                count = neighbor_mine_count(grid, row, col)
                rows.append('*' if not count else count)
        new_grid.append(rows)
    return new_grid, mine_count

def display_board(display_grid_values, track_grid):
    """
    The board user see and play on
    """

    board = []
    for row in range(len(track_grid)):
        rows = []
        for col in range(len(track_grid[0])):
            rows.append('?' if not track_grid[row][col] 
                        else display_grid_values[row][col])
        board.append(rows)
    return board

def reveal_cell(track_grid, new_grid, row, col):
    """
    It toggles to reveal the cell and 
    if cell is '*' it can reveal the neigbor cells if they are '*' too
    """

    track_grid[row][col] = True
    pos = [-1, 0, 1]

    if new_grid[row][col] == '*':
        for r in pos:
            for c in pos:
                if r == 0 and c == 0:
                    continue

                nr, nc = row + r, col + c
                if 0 <= nr < len(new_grid) and 0 <= nc < len(new_grid[0]):
                    if not track_grid[nr][nc]:
                        reveal_cell(track_grid, new_grid, nr, nc)

if __name__ == "__main__":
    row, col = 15, 15
    grid = build_grid(row, col, lambda: int(random.random() < 0.15))
    track_grid = build_grid(row, col, lambda: False)

    new_grid, mine_count = build_display_grid(grid)

    total_cells = len(grid) * len(grid[0])
    safe_cells = total_cells - mine_count

    board = display_board(new_grid, track_grid)
    print("If You hit '*' it can reveal neighbor cells too.")

    while True:
        # subprocess.run("cls", shell=True)
        print(f"Total Mines: {mine_count}")
        display_grid(board)

        try:
            user_inp = input("\nEnter row and col with a space('q' to exit): ")
            if user_inp == 'q':
                break

            row, col = user_inp.split(' ')
            row, col = int(row), int(col)

            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                print("Out of the board range. Please enter within range value")
                continue

            if track_grid[row][col] == True:
                print("This cell is already revealed")
                continue

            reveal_cell(track_grid, new_grid, row, col)
            board = display_board(new_grid, track_grid)

            score = 0
            score = sum(sum(r) for r in track_grid)

            print(f"Score: {score}")
            if new_grid[row][col] == 'M':
                print("Game Over. You hit the mine.")
                break

            if score == safe_cells:
                print("You Win!")
                break

        except Exception as e:
            print("You can only enter row and col with space or 'q' to quit")
            continue