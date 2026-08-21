from functools import cache

vector = tuple[int, int]

def poutine_path(r: int, c: int, grid: tuple[tuple[int, ...]]) -> int:
    move_up = (-1, 0)
    move_right = (0, 1)

    moves = (move_up, move_right)

    def get_rubes(pos: vector) -> int:
        return grid[pos[0]][pos[1]]

    @cache
    def _poutine_path(cur_pos: vector) -> int:
        if cur_pos == (0, c - 1):
            return get_rubes(cur_pos)

        elif is_out_bounds(cur_pos):
            return 0

        else:
            return get_rubes(cur_pos) + max(_poutine_path(vector_addition(cur_pos, move)) for move in moves)

    def is_out_bounds(pos: vector) -> bool:
        return pos[0] < 0 or pos[1] > c - 1

    return _poutine_path((r - 1, 0))

def vector_addition(v1: vector, v2: vector) -> vector:
    return (v1[0] + v2[0], v1[1] + v2[1])

assert poutine_path(1, 1, ((1,),)) == 1