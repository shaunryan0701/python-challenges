import pytest
import if_flow.if_exercise_5 as ex5

def test_check_and_udpate_dict_value() -> None:
    project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
    }

    expected_project_ids = {'01': 'open', '02': 'open', '03': 'in progress', '04': 'completed'}
    assert ex5.check_and_udpate_dict_value(project_ids, '02') == expected_project_ids  