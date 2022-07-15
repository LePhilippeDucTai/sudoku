import functools as ft
import itertools as it
from typing import List, Tuple

import numpy as np

from timing import time_it

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


def sudoku_solver(_grid: np.ndarray) -> np.ndarray:
    """Pour tout élément de grid : remplir par le nombre
    manquant si c'est l'unique élément qu'on puisse mettre."""
    if is_valid(_grid):
        return _grid
    
    grid = _grid.copy()
    grid_enum = np.ndenumerate(grid)
    null_cells = (index for index, value in grid_enum if value == 0)
    t1, t2 = it.tee(((index, available) for index in null_cells if len(available := choices(grid, *index)) in {1,2}))
    uniques = ((index, available) for index, available in t1 if len(available) == 1)
    couples = ((index, available) for index, available in t2 if len(available) == 2)
    try:
        index, valid = next(uniques)
        grid[index] = valid.pop()
        return sudoku_solver(grid)
    except StopIteration:
        try:
            index, valid_vals = next(couples)
            return coalesce(
                mutate_grid_solve(grid, index, valid_vals.pop()),
                mutate_grid_solve(grid, index, valid_vals.pop()),
            )
        except StopIteration:
            return None


def mutate_grid_solve(grid, indices, value):
    _grid = grid.copy()
    _grid[indices] = value
    return sudoku_solver(_grid)


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


# def sudoku_solver(_grid):
#     grid = sudoku_basic_fill(_grid)
#     if is_valid(grid):
#         return grid
#     cells_enum = np.ndenumerate(grid)
#     null_cells = (index for index, value in cells_enum if value == 0)
#     cells_choices = ((index, choices(grid, *index)) for index in null_cells)
#     filter_has_two_choices = ((i, x) for i, x in cells_choices if len(x) == 2)
#     try:
#         indices, set_to_pop = next(filter_has_two_choices)
#         return coalesce(
#             mutate_grid_solve(grid, indices, set_to_pop.pop()),
#             mutate_grid_solve(grid, indices, set_to_pop.pop()),
#         )
#     except StopIteration:
#         return None


@time_it
def sudoku_solve(grid):
    return sudoku_solver(grid)


def main():
    puzzle = [
        [0, 8, 4, 0, 1, 0, 6, 0, 0],
        [2, 5, 0, 0, 0, 4, 0, 0, 0],
        [6, 1, 3, 8, 0, 0, 5, 4, 0],
        [8, 0, 2, 0, 6, 0, 0, 0, 7],
        [0, 4, 5, 2, 0, 0, 0, 9, 6],
        [0, 0, 6, 0, 3, 5, 2, 0, 0],
        [0, 7, 8, 0, 2, 0, 4, 1, 5],
        [0, 2, 9, 0, 5, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 7, 0, 0, 0]
    ]

    # puzzle = [
    #     [6, 0, 0, 3, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 9, 0, 6],
    #     [0, 9, 0, 7, 4, 0, 8, 0, 0],
    #     [0, 1, 0, 6, 0, 0, 7, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 9, 0, 0, 1, 0, 8, 0],
    #     [0, 0, 4, 0, 7, 5, 0, 1, 0],
    #     [7, 0, 5, 0, 0, 2, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 3, 0, 0, 5],
    # ]

    # puzzle = [
    #     [0, 0, 0, 8, 0, 0, 0, 7, 0],
    #     [0, 9, 0, 0, 0, 0, 0, 3, 0],
    #     [1, 0, 0, 0, 0, 4, 9, 0, 8],
    #     [0, 0, 0, 0, 0, 0, 0, 9, 0],
    #     [4, 0, 0, 0, 5, 0, 0, 0, 0],
    #     [0, 1, 0, 3, 0, 0, 6, 0, 2],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 7],
    #     [0, 6, 0, 2, 0, 0, 8, 0, 1],
    #     [0, 0, 2, 0, 0, 3, 0, 0, 0],
    # ]

    # puzzle = [
    #     [0, 0, 5, 3, 0, 0, 0, 0, 0],
    #     [8, 0, 0, 0, 0, 0, 0, 2, 0],
    #     [0, 7, 0, 0, 1, 0, 5, 0, 0],
    #     [4, 0, 0, 0, 0, 5, 3, 0, 0],
    #     [0, 1, 0, 0, 7, 0, 0, 0, 6],
    #     [0, 0, 3, 2, 0, 0, 0, 8, 0],
    #     [0, 6, 0, 5, 0, 0, 0, 0, 9],
    #     [0, 0, 4, 0, 0, 0, 0, 3, 0],
    #     [0, 0, 0, 0, 0, 9, 7, 0, 0],
    # ]

    # # AI Escargot (600 ms)
    # puzzle = [
    #     [1, 0, 0, 0, 0, 7, 0, 9, 0],
    #     [0, 3, 0, 0, 2, 0, 0, 0, 8],
    #     [0, 0, 9, 6, 0, 0, 5, 0, 0],
    #     [0, 0, 5, 3, 0, 0, 9, 0, 0],
    #     [0, 1, 0, 0, 8, 0, 0, 0, 2],
    #     [6, 0, 0, 0, 0, 4, 0, 0, 0],
    #     [3, 0, 0, 0, 0, 0, 0, 1, 0],
    #     [0, 4, 0, 0, 0, 0, 0, 0, 7],
    #     [0, 0, 7, 0, 0, 0, 3, 0, 0]
    # ]

    # # World's Hardest (10 secs computing time)
    # # https://www.conceptispuzzles.com/index.aspx?uri=info/article/424
    puzzle = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
    ]

    grid = np.array(puzzle).reshape(9, 9)
    res = sudoku_solve(grid)
    print(res)


if __name__ == "__main__":
    main()
