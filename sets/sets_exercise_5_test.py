import pytest
import sets.sets_exercise_5 as ex5

def test_intersection_of_two_sets() -> None:
    is_clicked = {'9001', '9002', '9005'}
    is_bought = {'9002', '9004', '9005'}
    assert ex5.intersection_of_two_sets(is_clicked, is_bought) == {'9002', '9005'}