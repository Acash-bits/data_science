# Computing magnitude of a vector

import math
from typing import List

Vector = List[float]

def magnitude(v: Vector):
    """"Returns the magnitude (or length) of v"""
    vector_sum = sum(v_i * v_i for v_i in v)
    return math.sqrt(vector_sum)

print(magnitude([4,3]))