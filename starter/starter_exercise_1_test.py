import pytest 
import starter_exercise_1 as ex1

def test_print_version() -> None:
    assert(ex1.get_version() == '3.11.2')


