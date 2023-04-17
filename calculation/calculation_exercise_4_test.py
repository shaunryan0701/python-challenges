import pytest
import calculation.calculation_exercise_4 as ex4

def test_arithmetic_sequence() -> None:
    assert ex4.arithmetic_sequence(10) == 50

def test_sum_arithmetic_sequence_with_one_element() -> None:
    assert ex4.sum_arithmetic_sequence(1) == 14 

def test_sum_arithmetic_sequence_with_many_elements() -> None:
    assert ex4.sum_arithmetic_sequence(10) == 320