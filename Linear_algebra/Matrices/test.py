
from typing import Callable, List

Matrix = List[List[float]]

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:

    return [
        [entry_fn(i, j) for j in range(num_cols)]
        for i in range(num_rows)
    ]

def entry_fn(i, j):
    return float(i + j)

print(make_matrix(3, 4, entry_fn))
