import pytest
import dictionaries.dictionaries_exercise_12 as ex12

def test_find_dict_item_by_key() -> None:
    users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}

    assert ex12.find_dict_item_by_key(users, '004') == 'indefinite'