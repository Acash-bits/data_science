# Scaling vector using scalar
# In layman terms multiplying vector using scalar

from typing import List

Vector = List[float]

def scalar_multiply(s: float, v: Vector):
    """Multiplies every element by c"""
    return[s * v_i for v_i in v]

print(scalar_multiply(3, [5,3,9]))