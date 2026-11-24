import math
from typing import List
from vectors_sum_of_squares import sum_of_squares
from subtracting_vector import subtract

Vector = List[float]

def squared_distance(v:Vector, w: Vector):
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector):
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v,w))