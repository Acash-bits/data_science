# Creating a matrix and counting rows and column in it

from typing import Tuple
from typing import List

Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns ## of rows of A, # columns of A"""
    num_rows = len(A)
    num_columns = len(A[0]) if A else 0 # Number of elemetns in first row
    return num_rows, num_columns

print(shape([[1,2,3], # First Row
            [4,5,6]])) # Second Row