import pytest
import calculation.calculation_exercise_2 as ex2

def test_calculate_compound_interest() -> None:
    assert ex2.calculate_compound_interest(1000, 3, 5) == 1159.27