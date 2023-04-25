import pytest
import tuples.tuples_exercise_4 as ex4

def test_count_tuple_elements() -> None:
    
    default = ('YES', 'NO', 'NO', 'YES', 'NO')
    assert ex4.count_tuple_elements(default, 'YES') == 2