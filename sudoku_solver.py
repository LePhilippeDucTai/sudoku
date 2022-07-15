import functools as ft
from typing import List, Tuple

import numpy as np

SUDOKU_NUMS = set(range(1, 10))


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


def coords_to_fill(grid_enum, grid):
    (row, col), value = grid_enum
    if value == 0:
        valid_choices = choices(grid, row, col)
        if len(valid_choices) == 1:
            return row, col, valid_choices.pop()


def cells_to_fill(acc: list, free_cell: List[Tuple[int, int, int]], grid):
    """free_cell : (row, col), x (ndenumerate)
    Accumule 'acc' des tuples (row, col, value) valides
    """
    if valid := coords_to_fill(free_cell, grid):
        return acc + [valid]
    return acc


def grid_cells_to_fill(grid):
    return ft.partial(cells_to_fill, grid=grid)


def sudoku_basic_fill(_grid: np.ndarray) -> np.ndarray:
    """Pour tout élément de grid : remplir par le nombre
    manquant si c'est l'unique élément qu'on puisse mettre."""
    grid = _grid.copy()
    grid_enum = np.ndenumerate(grid)
    coords_valid_values = ft.reduce(grid_cells_to_fill(grid), grid_enum, [])
    x_y_val = tuple(zip(*coords_valid_values))
    if x_y_val:
        x, y, values = x_y_val
        grid[x, y] = values
        return sudoku_basic_fill(grid)
    return grid


def is_valid(grid):
    for indice, _ in np.ndenumerate(grid):
        row, col = indice
        cols = set(get_col(grid, col))
        rows = set(get_row(grid, row))
        blocks = set(get_block(grid, row, col))
        if any(x != SUDOKU_NUMS for x in (cols, rows, blocks)):
            return False
    return True


def coalesce(*args):
    for arg in args:
        if arg is not None:
            return arg


def mutate_grid_solve(grid, indices, value):
    _grid = grid.copy()
    _grid[indices] = value
    return sudoku_solver(_grid)


def sudoku_solver(_grid):
    grid = sudoku_basic_fill(_grid)
    if is_valid(grid):
        return grid
    cells_enum = np.ndenumerate(grid)
    null_cells = (index for index, value in cells_enum if value == 0)
    cells_choices = ((index, choices(grid, *index)) for index in null_cells)
    filter_has_two_choices = ((i, x) for i, x in cells_choices if len(x) == 2)
    try:
        indices, set_to_pop = next(filter_has_two_choices)
        return coalesce(
            mutate_grid_solve(grid, indices, set_to_pop.pop()),
            mutate_grid_solve(grid, indices, set_to_pop.pop()),
        )
    except StopIteration:
        return None


def main():
    puzzle = [
        [6, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 9, 0, 6],
        [0, 9, 0, 7, 4, 0, 8, 0, 0],
        [0, 1, 0, 6, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 1, 0, 8, 0],
        [0, 0, 4, 0, 7, 5, 0, 1, 0],
        [7, 0, 5, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 5],
    ]
    grid = np.array(puzzle).reshape(9, 9)
    res = sudoku_solver(grid)
    print(res)


if __name__ == "__main__":
    main()
