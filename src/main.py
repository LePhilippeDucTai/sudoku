import numpy as np

from sudoku.sudoku import sudoku_solve
from sudoku.utils.timing import time_it


@time_it
def main():
    # 623 ms
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

    # 365 ms
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

    grid = np.array(puzzle).reshape(9, 9)
    res = sudoku_solve(grid)
    print(res)


if __name__ == "__main__":
    main()
