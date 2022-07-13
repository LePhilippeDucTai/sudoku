import numpy as np
import itertools as it

SUDOKU_NUMS = set(range(1, 10))
INDICES_SUDOKU = list(range(9))


def get_block(mat, i, j):
    row = (i // 3) * 3
    col = (j // 3) * 3
    return mat[row : row + 3, col : col + 3].flatten()


def get_col(mat, j):
    return mat[:, j]


def get_row(mat, i):
    return mat[i, :]


def choices(grid, row, col):
    return (
        SUDOKU_NUMS
        - set(get_row(grid, row))
        - set(get_col(grid, col))
        - set(get_block(grid, row, col))
    )


def sudoku_fill_one(_grid):
    """Pour tout élément de grid : remplir par le nombre
    manquant si c'est l'unique élément qu'on puisse mettre."""
    grid = _grid.copy()
    cartesian = it.product(range(9), repeat=2)
    indices = filter(lambda i: grid[i] == 0, cartesian)
    for row, col in indices:
        available_choices = choices(grid, row, col)
        if len(available_choices) == 1:
            grid[row, col] = available_choices.pop()
            return sudoku_fill_one(grid)
    return grid


class SudokuSolver:
    def __init__(self, sudoku_grid: np.array):
        self.sudoku_grid = sudoku_grid

    def solve(self, sudoku):
        pass


def main():
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    grid = np.array(puzzle).reshape(9, 9)
    res = sudoku_fill_one(grid)
    print(res)


if __name__ == "__main__":
    main()
