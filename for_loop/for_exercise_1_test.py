import pytest
import for_loop.for_exercise_1 as ex1

def test_all_2_digit_numbers_divisable_by_11() -> None:
    expected_result = '11,22,33,44,55,66,77,88,99'
    assert ex1.all_2_digit_numbers_divisable_by_11() == expected_result