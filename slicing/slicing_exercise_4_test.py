import pytest
import slicing.slicing_exercise_4 as ex4

def test_reverse_string() -> None:
    assert ex4.reverse_string('This is Bollox!') == '!xolloB si sihT'