import pytest
import strings.strings_exercise_8 as ex8

def test_pad_with_zeroes() -> None:
    assert ex8.pad_with_zeroes(34) == '000034'
