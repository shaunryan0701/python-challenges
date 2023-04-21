import pytest
import strings.strings_exercise_1 as ex1

def test_capitalise() -> None:
    input_string = 'welcome to the world!'
    assert ex1.capitalise(input_string) == 'Welcome to the world!'