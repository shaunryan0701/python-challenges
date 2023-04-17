import pytest
import calculation.calculation_exercise_3 as ex3

def test_delta_of_quadratic_equation() -> None:
    assert ex3.delta_of_quadratic_equation(3, -4, 1) == 4