import pytest
import data_types.data_types_exercise_1 as ex1

def test_data_type() -> None:
    input_string = "Bollox"
    assert ex1.data_type(input_string) == type('')