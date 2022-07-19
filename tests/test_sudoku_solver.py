from numpy import array
from numpy.testing import assert_array_equal

from sudoku.sudoku import sudoku_solve


def test_worlds_hardest():
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
    expected = [
        [8, 1, 2, 7, 5, 3, 6, 4, 9],
        [9, 4, 3, 6, 8, 2, 1, 7, 5],
        [6, 7, 5, 4, 9, 1, 2, 8, 3],
        [1, 5, 4, 2, 3, 7, 8, 9, 6],
        [3, 6, 9, 8, 4, 5, 7, 2, 1],
        [2, 8, 7, 1, 6, 9, 5, 3, 4],
        [5, 2, 1, 9, 7, 4, 3, 6, 8],
        [4, 3, 8, 5, 2, 6, 9, 1, 7],
        [7, 9, 6, 3, 1, 8, 4, 5, 2],
    ]
    grid = array(puzzle).reshape((9, 9))
    assert_array_equal(sudoku_solve(grid), expected)


def test_evil_sudoku():
    puzzle = [
        [0, 0, 0, 8, 0, 0, 0, 7, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 0],
        [1, 0, 0, 0, 0, 4, 9, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [4, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 1, 0, 3, 0, 0, 6, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 6, 0, 2, 0, 0, 8, 0, 1],
        [0, 0, 2, 0, 0, 3, 0, 0, 0],
    ]
    expected = [
        [2, 5, 4, 8, 3, 9, 1, 7, 6],
        [8, 9, 7, 5, 6, 1, 2, 3, 4],
        [1, 3, 6, 7, 2, 4, 9, 5, 8],
        [6, 7, 3, 1, 8, 2, 4, 9, 5],
        [4, 2, 8, 9, 5, 6, 7, 1, 3],
        [9, 1, 5, 3, 4, 7, 6, 8, 2],
        [5, 4, 1, 6, 9, 8, 3, 2, 7],
        [3, 6, 9, 2, 7, 5, 8, 4, 1],
        [7, 8, 2, 4, 1, 3, 5, 6, 9],
    ]
    grid = array(puzzle).reshape((9, 9))
    assert_array_equal(sudoku_solve(grid), expected)


def test_easy_sudoku():
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
    expected = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    grid = array(puzzle).reshape((9, 9))
    assert_array_equal(sudoku_solve(grid), expected)


def test_hard_sudoku():
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
    expected = [
        [6, 5, 8, 3, 2, 9, 1, 4, 7],
        [4, 3, 7, 1, 5, 8, 9, 2, 6],
        [1, 9, 2, 7, 4, 6, 8, 5, 3],
        [5, 1, 3, 6, 8, 4, 7, 9, 2],
        [8, 4, 6, 2, 9, 7, 5, 3, 1],
        [2, 7, 9, 5, 3, 1, 6, 8, 4],
        [3, 6, 4, 9, 7, 5, 2, 1, 8],
        [7, 8, 5, 4, 1, 2, 3, 6, 9],
        [9, 2, 1, 8, 6, 3, 4, 7, 5],
    ]
    grid = array(puzzle).reshape((9, 9))
    assert_array_equal(sudoku_solve(grid), expected)


def test_hard_sudoku_2():
    puzzle = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 9, 0, 7, 0, 5],
        [0, 7, 4, 0, 0, 0, 0, 6, 0],
        [0, 8, 0, 0, 0, 3, 0, 0, 9],
        [9, 0, 2, 0, 1, 0, 3, 7, 0],
        [0, 3, 1, 6, 0, 0, 9, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 4, 0, 6, 0, 0],
    ]
    expected = [
        [7, 5, 3, 2, 8, 4, 1, 9, 6],
        [4, 9, 6, 1, 5, 7, 8, 3, 2],
        [2, 1, 8, 3, 9, 6, 7, 4, 5],
        [3, 7, 4, 9, 2, 8, 5, 6, 1],
        [1, 8, 5, 7, 6, 3, 4, 2, 9],
        [9, 6, 2, 4, 1, 5, 3, 7, 8],
        [5, 3, 1, 6, 7, 2, 9, 8, 4],
        [6, 4, 9, 8, 3, 1, 2, 5, 7],
        [8, 2, 7, 5, 4, 9, 6, 1, 3],
    ]
    grid = array(puzzle).reshape((9, 9))
    assert_array_equal(sudoku_solve(grid), expected)


def test_ai_escargot():
    puzzle = [
        [1, 0, 0, 0, 0, 7, 0, 9, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 9, 6, 0, 0, 5, 0, 0],
        [0, 0, 5, 3, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 2],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 3, 0, 0],
    ]
    expected = [
        [1, 6, 2, 8, 5, 7, 4, 9, 3],
        [5, 3, 4, 1, 2, 9, 6, 7, 8],
        [7, 8, 9, 6, 4, 3, 5, 2, 1],
        [4, 7, 5, 3, 1, 2, 9, 8, 6],
        [9, 1, 3, 5, 8, 6, 7, 4, 2],
        [6, 2, 8, 7, 9, 4, 1, 3, 5],
        [3, 5, 6, 4, 7, 8, 2, 1, 9],
        [2, 4, 1, 9, 3, 5, 8, 6, 7],
        [8, 9, 7, 2, 6, 1, 3, 5, 4],
    ]
    grid = array(puzzle).reshape((9, 9))
    assert_array_equal(sudoku_solve(grid), expected)


def test_hard_3_sudoku():
    puzzle = [
        [0, 0, 5, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 7, 0, 0, 1, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 5, 3, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 3, 2, 0, 0, 0, 8, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 9],
        [0, 0, 4, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0],
    ]
    expected = [
        [1, 4, 5, 3, 2, 7, 6, 9, 8],
        [8, 3, 9, 6, 5, 4, 1, 2, 7],
        [6, 7, 2, 9, 1, 8, 5, 4, 3],
        [4, 9, 6, 1, 8, 5, 3, 7, 2],
        [2, 1, 8, 4, 7, 3, 9, 5, 6],
        [7, 5, 3, 2, 9, 6, 4, 8, 1],
        [3, 6, 7, 5, 4, 2, 8, 1, 9],
        [9, 8, 4, 7, 6, 1, 2, 3, 5],
        [5, 2, 1, 8, 3, 9, 7, 6, 4],
    ]
    grid = array(puzzle).reshape((9, 9))
    assert_array_equal(sudoku_solve(grid), expected)