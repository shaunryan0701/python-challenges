import pytest
import print.print_exercise_2 as ex2

def test_return_name():
    assert ex2.print_age(25) == 'I am 25 years old'