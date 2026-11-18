# Adding Vectors Componentwise

from typing import List

Vector = List[float]

def vector_sum(vectors: List[Vector]):
    """Sum all corresponding elements"""
    # Check that vector is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are of all same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements
               for v in vectors), "vector sizes different"

    # the i-th element of the result is the sum of every vector[i]
    return[sum(vector[i] for vector in vectors)
           for i in range(num_elements)]

# print(vector_sum([[1,3,5], [1,5,7], [3,5,6]]))