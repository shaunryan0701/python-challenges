import pytest
import if_flow.if_exercise_3 as ex3

def test_check_is_int_float() -> None:
    number = 1.0
    assert ex3.check_is_int(number) == 'NO'

def test_check_is_int() -> None:
    number = 1
    assert ex3.check_is_int(number) == 'YES'