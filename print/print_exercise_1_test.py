import pytest
import print_exercise_1 as ex1

def test_print_greeting() -> None:
    assert ex1.print_greeting() == 'Learn Python'