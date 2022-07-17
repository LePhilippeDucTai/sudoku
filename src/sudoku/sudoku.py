import functools as ft
from collections import Counter
from itertools import chain

import numpy as np

from sudoku.utils.timing import time_it

SUDOKU_NUMS = set(range(1, 10))


def flatten(list_of_lists):
    "Flatten one level of nesting"
    return chain.from_iterable(list_of_lists)


def fill_block(mat, i, j, num):
    row = (i // 3) * 3
    col = (j // 3) * 3
    mat[row : row + 3, col : col + 3] = num


def separate_dims(index):
    left, right = index
    return (left, slice(None)), (slice(None), right)


def fill_x(grid, indices_where_num):
    indices_to_fill = [separate_dims(index) for index in indices_where_num]
    for ind in flatten(indices_to_fill):
        grid[ind] = -1


def fill_impossibles(original_grid, num):
    cgrid = original_grid.copy()
    indices_where_num = np.argwhere(cgrid == num)
    fill_x(cgrid, indices_where_num)
    for index in indices_where_num:
        fill_block(cgrid, *index, -1)
    return cgrid


def fill_numbers(grid):
    cgrid = grid.copy()
    change = 0
    for num in SUDOKU_NUMS:
        mask_grid = fill_impossibles(cgrid, num)
        zeros_cgrid = np.argwhere(mask_grid == 0)
        blocks = (zeros_cgrid // 3) * 3
        n_blocks = 3 * blocks[:, 0] + blocks[:, 1]
        unique_val = [n for n, c in Counter(n_blocks).items() if c == 1]
        filtres_ = ft.reduce(lambda acc, x: acc | (n_blocks == x), unique_val, False)
        ind_to_fill = zeros_cgrid[filtres_]
        for ind in list(map(tuple, ind_to_fill)):
            cgrid[ind] = num

        if np.any(ind_to_fill):
            change = 1

    if change:
        return fill_numbers(cgrid)
    return cgrid


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


def sudoku_basic_fill(_grid: np.ndarray) -> np.ndarray:
    """Pour tout élément de grid : remplir par le nombre
    manquant si c'est l'unique élément qu'on puisse mettre."""
    grid = _grid.copy()
    grid_enum = np.ndenumerate(grid)
    null_cells = (index for index, value in grid_enum if value == 0)
    coords_valid_values = (
        (*index, valid_choices.pop())
        for index in null_cells
        if len(valid_choices := choices(grid, *index)) == 1
    )
    x_y_val = tuple(zip(*coords_valid_values))
    if x_y_val:
        row, col, values = x_y_val
        grid[row, col] = values
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
    grid = fill_numbers(_grid)
    grid = sudoku_basic_fill(grid)
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


@time_it
def sudoku_solve(grid):
    return sudoku_solver(grid)
