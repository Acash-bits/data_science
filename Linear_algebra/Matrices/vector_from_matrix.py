# Creating a vector from matrix

from typing import Tuple
from typing import List

Vector = List[float]
Matrix = List[List[float]]

def get_row (A: Matrix, i: int) -> Vector:
    """Return the i-th row of A (as a vector)"""
    return A[i]

def get_column(A: Matrix, j:int) -> Vector:
    """Return the j-th column of A (as a vector)"""
    return [A_i[j]          # jth element of the row A_i
            for A_i in A]   # for each row A_i

# Creating a matrix
x = [[1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ]

print("Matrix")
for x_i in x:
    print(x_i)

print("\nCreating vector from the rows of Matrix")
print(get_row(x, 3))

print("\nCreating Vector from the columns of Matrix")
print(get_column(x, 2))