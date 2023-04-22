import pytest
import sets.sets_exercise_3 as ex3

def test_symmetric_difference() -> None:
    A = {2, 4, 6, 8}
    B = {4, 10} 
    assert ex3.symmetric_difference(A, B) == {2, 6, 8, 10}