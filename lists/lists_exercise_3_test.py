import pytest
import lists.lists_exercise_3 as ex3

def test_unique_chars() -> None:
    text = 'Python programming'
    assert ex3.unique_chars(text) == ['a', 'g', 'h', 'i', 'm', 'n', 'o', 'p', 'r', 't', 'y'] 