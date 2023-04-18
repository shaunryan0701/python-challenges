import pytest
import calculation.calculation_exercise_6 as ex6

def test_calc_midpoint() -> None:
    pointA = (2, 4)
    pointB = (-4, 6)
    assert ex6.calc_midpoint(pointA, pointB) == (-1.0, 5.0)