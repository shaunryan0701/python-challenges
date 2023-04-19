import pytest
import calculation.calculation_exercise_9 as ex9

def test_standard_deviation() -> None:
    assert ex9.standard_deviation([10, 11, 9]) == 0.82