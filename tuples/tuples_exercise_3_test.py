import pytest
import tuples.tuples_exercise_3 as ex3

def test_insert_tuple() -> None:
    members = (('Kate', 23), ('Tom', 19))
    jono = ('John', 26)
    assert ex3.insert_tuple(members, jono) == (('Kate', 23), ('John', 26), ('Tom', 19))