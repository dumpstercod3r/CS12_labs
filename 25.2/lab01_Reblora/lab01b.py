# pyright: strict

from collections.abc import Sequence

Grid = Sequence[str]
Coord = tuple[int, int]

class Model:
    def __init__(self, grid: Grid, moves: str) -> None:
        self._grid: Grid = grid
        self._lenr: int = len(grid)
        self._lenc: int = len(grid[0])
        self._piece_coords: list[Coord] = [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if "#" in col]
        self._obstacle_coords: list[Coord] = [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if "x" in col]
        self._moves: str= moves

    def move_around(self) -> list[str]:
        for move in self._moves:
            if move == "L" or move == "R":
                self.x_move(move)
            elif move == "U" or move == "D":
                self.y_move(move)
            else:
                raise ValueError(f"{move} is not a valid moveset.")

        return self.finalize_grid()

    def x_move(self, move: str):
        new_piece_coords: list[Coord] = []
        valid: bool = True

        if move == "L":
            for piece_coord in self._piece_coords:
                new_position: Coord = (piece_coord[0], piece_coord[1]-1)

                if new_position[1] <= -1 or new_position in self._obstacle_coords:
                    valid = False
                    break
                else:
                    new_piece_coords.append(new_position)

        elif move == "R":
            for piece_coord in self._piece_coords:
                new_position: Coord = (piece_coord[0], piece_coord[1]+1)

                if new_position[1] >= self._lenc or new_position in self._obstacle_coords:
                    valid = False
                    break
                else:
                    new_piece_coords.append(new_position)

        else:
            raise ValueError(f"{move} is neither 'L' or 'R'.")

        if valid:
            self._piece_coords = new_piece_coords
        else:
            pass

    def y_move(self, move: str):
        new_piece_coords: list[Coord] = []
        valid: bool = True

        if move == "U":
            for piece_coord in self._piece_coords:
                new_position: Coord = (piece_coord[0]-1, piece_coord[1])

                if new_position[0] <= -1 or new_position in self._obstacle_coords:
                    valid = False
                    break
                else:
                    new_piece_coords.append(new_position)

        elif move == "D":
            for piece_coord in self._piece_coords:
                new_position: Coord = (piece_coord[0]+1, piece_coord[1])

                if new_position[0] >= self._lenr or new_position in self._obstacle_coords:
                    valid = False
                    break
                else:
                    new_piece_coords.append(new_position)

        else:
            raise ValueError(f"{move} is neither 'L' or 'R'.")

        if valid:
            self._piece_coords = new_piece_coords
        else:
            pass

    def finalize_grid(self) -> list[str]:
        grid: list[list[str]] = [list(".")*self._lenc for _ in range(self._lenr)]

        for r, c in self._piece_coords:
            grid[r][c] = "#"

        for r, c in self._obstacle_coords:
            grid[r][c] = "x"

        return ["".join(row) for row in grid]

def move_around(grid: Grid, moves: str) -> list[str]:
    return Model(grid, moves).move_around()