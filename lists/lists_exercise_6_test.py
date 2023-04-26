import pytest
import lists.lists_exercise_6 as ex6

def test_sort_tuple() -> None:
    techs = ('python', 'java', 'sql', 'aws')
    expected = ('aws', 'java', 'python', 'sql')
    assert ex6.sort_tuple(techs) == expected