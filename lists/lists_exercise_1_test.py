import pytest
import lists.lists_exercise_1 as ex1

def test_append_to_a_list() -> None:
    cities = ['Los Angeles', 'New York', 'Chicago']
    assert ex1.append_to_a_list(cities, 'Houston') == ['Los Angeles', 'New York', 'Chicago', 'Houston']