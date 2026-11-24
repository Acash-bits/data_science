# Adding two vectors

from typing import List

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    """Add corresponding elements"""
    assert len(v) == len(w), "vectors must be of same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]

print(add([1,2,3], [4,5,6]))