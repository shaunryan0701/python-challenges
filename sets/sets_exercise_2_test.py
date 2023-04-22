import pytest
import sets.sets_exercise_2 as ex2

def test_count_items_in_set() -> None:
    text = 'Programming in python.'
    assert ex2.count_items_in_set(text) == 8