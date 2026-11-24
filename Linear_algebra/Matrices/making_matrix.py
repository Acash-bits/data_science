# Creating a matrix by giving the shape
# And Letting the function generate it's element

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

print(make_matrix(4,3,lambda i, j: i*j))