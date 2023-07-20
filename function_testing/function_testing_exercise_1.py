import unittest
import math
import os

def area(radius):
    """The function returns the area of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return math.pi * radius ** 2

