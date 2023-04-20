import pytest
import slicing.slicing_exercise_3 as ex3

def test_convert_to_binary() -> None:
    input_string = '1 0 0 1 0 1'
    assert ex3.convert_to_binary(input_string) == 37