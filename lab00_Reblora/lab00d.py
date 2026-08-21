# pyright: strict

def poutine_path(row: int, col: int, grid: tuple[tuple[int, ...], ...]) -> int:
    memory: dict[tuple[int, int], int] = {}

    def _poutine_path(r: int, c: int) -> int:
        if (r, c) in memory:
            return memory[(r, c)]
        else:
            if r < 0 or c == col:
                return 0
            elif r == 0 and c == col-1:
                return grid[r][c]
            else:
                rubles: int = grid[r][c] + max(_poutine_path(r-1, c), _poutine_path(r, c+1))

                memory[(r, c)] = rubles

                return rubles

    return _poutine_path(row-1, 0)