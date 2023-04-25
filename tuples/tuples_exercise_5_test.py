import pytest
import tuples.tuples_exercise_5 as ex5

def test_sort_tuple_asc() -> None:
    names = ('Monica', 'Tom', 'John', 'Michael')
    assert ex5.sort_tuple(names, 'A') == ('John', 'Michael', 'Monica', 'Tom')

def test_sort_tuple_desc() -> None:
    names = ('Monica', 'Tom', 'John', 'Michael')
    assert ex5.sort_tuple(names, 'D') == ('Tom', 'Monica', 'Michael', 'John')