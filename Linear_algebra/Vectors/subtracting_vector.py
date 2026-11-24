# Subtracting vector

from typing import List

Vector = List[float]

def subtract(v: Vector, w: Vector):
    """Subtracting Corresponding Elements"""
    if len(v) == len(w): #vectors must be of same length
        return[v_i - w_i for v_i, w_i in zip(v,w)]
    else:
        raise ValueError("Vectors must be of same length")

print(subtract([3,5,-1], [4,6,-10]))