import pytest
import lists.lists_exercise_7 as ex7

def test_join_list_elements() -> None:
    hashtags = ['summer', 'time', 'vibes']
    assert ex7.join_list_elements(hashtags) == '#summer#time#vibes'