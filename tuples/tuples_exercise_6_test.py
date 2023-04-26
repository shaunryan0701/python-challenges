import pytest
import tuples.tuples_exercise_6 as ex6

def test_sort_tuple_within_tuple_asc() -> None:
    info = (('Monica', 19), ('Tom', 21), ('John', 18))
    assert ex6.sort_tuple_within_tuple(info) == (('John', 18), ('Monica', 19), ('Tom', 21))

def test_sort_tuple_within_tuple_desc() -> None:
    info = (('Monica', 19), ('Tom', 21), ('John', 18))
    assert ex6.sort_tuple_within_tuple(info, 'D') == (('Tom', 21), ('Monica', 19), ('John', 18))