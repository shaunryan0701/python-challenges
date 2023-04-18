import pytest
import calculation.calculation_exercise_5 as ex5

def test_geometric_sequence() -> None:
    assert ex5.geometric_sequence(10) == 4096

def test_sum_geometric_sequence() -> None:
    assert ex5.sum_geometric_sequence(6) == 504