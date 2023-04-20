import pytest
import slicing.slicing_exercise_2 as ex2

def test_retrieve_3_parts() -> None:
    test_string = 'PKV-89415-PLN'
    assert ex2.retrieve_3_parts(test_string) == 'PKVPLN'