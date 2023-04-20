import pytest
import slicing.slicing_exercise_1 as ex1

def test_retrieve_file_extension() -> None:
    file_name = 'Bollox_to_this.jpg'
    assert ex1.retrieve_file_extension(file_name) == 'jpg'