# pyright: strict

Grid = list[list[int]]

def simulate2048(grid: Grid, moves: str) -> Grid:
    state: Grid = []

    for move in moves:
        state = change(grid, move)

        end_turn: bool = False

        for r, row in enumerate(state):
            for c, col in enumerate(row):
                if col == 0 and not end_turn:
                    state[r][c] = 1
                    end_turn = True
                    break
                else:
                    pass

        if end_turn:
            grid = state
        else:
            if grid == state:
                pass
            else:
                break

    return grid

def change(grid: Grid, move: str) -> Grid:
    state: Grid = []
    n: int = len(grid)

    if move == "W" or move == "E":
        for row in grid:
            shifted_row: list[int] = shift(row)
            merged_row: list[int] = merge(shifted_row, move)
            final_row: list[int] = fill(merged_row, n, move)

            state.append(final_row)
    else:
        for col in zip(*grid):
            shifted_col: list[int] = shift(list(col))
            merged_col: list[int] = merge(shifted_col, "W" if move == "N" else "E")
            final_col: list[int] = fill(merged_col, n, "W" if move == "N" else "E")

            state.append(final_col)

        state = [list(row) for row in zip(*state)]

    return state

def shift(row: list[int]) -> list[int]:
    return [num for num in row if num != 0]

def merge(row: list[int], move: str) -> list[int]:
    merged_row: list[int] = []
    n: int = len(row)

    if move == "E":
        row = row[::-1]
    else:
        pass

    i: int = 0

    while i < n:
        if i == n-1:
            merged_row.append(row[i])
        elif row[i] == row[i+1]:
            merged_row.append(row[i]*2)
            i += 1
        else:
            merged_row.append(row[i])

        i += 1

    if move == "E":
        merged_row = merged_row[::-1]
    else:
        pass

    return merged_row

def fill(row: list[int], n: int, move: str) -> list[int]:
    filled_row: list[int] = []

    if move == "W":
        filled_row = row + [0 for _ in range(n-len(row))]
    else:
        filled_row = [0 for _ in range(n-len(row))] + row

    return filled_row