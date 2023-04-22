import pytest
import sets.sets_exercise_1 as ex1

def test_add_item_to_set() -> None:
    subjects = {'mathematics', 'biology'}

    assert ex1.add_item_to_set(subjects, 'english') == {'english', 'biology', 'mathematics'}