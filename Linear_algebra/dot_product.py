# Using dot product

from typing import List

Vector = List[float]

def dot_product(v: Vector, w: Vector) -> float:
    """Computes v_i * w_i + ..... v_n * w_n"""
    assert len(v) == len(w), "vectors must be of same length"
    
    return(sum(v_i * w_i for v_i, w_i in zip(v, w)))

print(dot_product([4,2], [6,7]))
