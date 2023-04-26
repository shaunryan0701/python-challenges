import pytest
import lists.lists_exercise_2 as ex2

def test_count_occurences() -> None:
    idx = ['001', '002', '001', '003', '001']
    assert ex2.count_occurences(idx, '001') == 3