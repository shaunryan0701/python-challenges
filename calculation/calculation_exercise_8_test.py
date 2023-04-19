import pytest
import calculation.calculation_exercise_8 as ex8

def test_geometric_mean() -> None:
    assert ex8.geometric_mean([4, 3, 4.5, 5]) == 4.05