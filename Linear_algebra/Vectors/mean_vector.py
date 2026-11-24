# Componentwise means of a list

from typing import List
from scaling_vector import scalar_multiply
from componentwise_sum import vector_sum

Vector = List[float]
def vector_mean(vectors: Vector):
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

print(vector_mean([[81, 2, 38], [3, 56, 78], [9, 10, 3]]))