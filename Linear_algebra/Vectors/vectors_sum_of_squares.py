# Summing the squares of coordinates
from typing import List

Vector = List[float]

def sum_of_squares(v: Vector):
    """"Returns v_i * v_i + ....... v_n * v_n"""
    return sum(v_i * v_i for v_i in v)

print(sum_of_squares([4,8,3]))