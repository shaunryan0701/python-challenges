'''
Find the roots of a quadratic equation given a, b and c
equation = ax**2 + bc + c = 0
quadratic formula = x = -b +- sqrt(b**2 - 4ac) / 2a
'''
import math

def roots_of_quadratic(a: int, b: int, c: int) -> tuple:
    root1 = (-b - math.sqrt(b ** 2 - (4*a*c))) / 2*a
    root2 = (-b + math.sqrt(b ** 2 - (4*a*c))) / 2*a

    return (root1, root2)