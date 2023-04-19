import pytest
import calculation.calculation_exercise_7 as ex7

def test_roots_of_quadratic() -> None:
    a = 1
    b = 5
    c = 4
    assert ex7.roots_of_quadratic(a, b, c) == (-4.0, -1.0)