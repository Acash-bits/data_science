# Creating an identity matrix
# Where 1s are on the diagonal and 0s elsewhere

from typing import Callable
from typing import List

Matrix = List[List[float]]

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int],float]) -> Matrix:
    """
    Returns a num_rows * num_cols matrix
    whose (i,j)-th entry is entry_fn(i,j)
    """

    return[[entry_fn(i,j) # given i, create a list
            for j in range(num_cols)] # [entry_fn (i,0),......]
            for i in range(num_rows)] # create one list for each i

def identity_matrix(n:int) -> Matrix:
    """Returns the n*n identity matrix"""
    return make_matrix(n,n, lambda i, j: 1 if i == j else 0)

print(identity_matrix(5))