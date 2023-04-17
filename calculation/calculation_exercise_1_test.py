import pytest

import calculation.calculation_exercise_1 as ex1

def test_calculate_area_of_circle():
    assert ex1.calculate_area_of_circle(5) == 78.5 