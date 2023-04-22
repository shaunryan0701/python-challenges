import pytest
import sets.sets_exercise_4 as ex4

def test_symmetric_difference() -> None:

    ad1_id = {'001', '002', '003'}
    ad2_id = {'002', '003', '007'}  

    assert ex4.symmetric_difference(ad1_id, ad2_id) == {'001', '007'}