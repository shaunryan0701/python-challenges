import pytest
import if_flow.if_exercise_4 as ex4

def test_check_if_item_in_list() -> None:
    project_ids = ['02134', '24253']
    project_id = '01234'    

    expected_project_ids = ['02134', '24253', '01234']

    assert ex4.check_if_item_in_list(project_ids, project_id) == expected_project_ids

def test_check_if_item_in_list_already_exists() -> None:
    project_ids = ['02134', '24253']
    project_id = '24253'    

    expected_project_ids = ['02134', '24253']

    assert ex4.check_if_item_in_list(project_ids, project_id) == expected_project_ids