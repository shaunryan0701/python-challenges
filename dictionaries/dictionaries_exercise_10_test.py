import pytest
import dictionaries.dictionaries_exercise_10 as ex10

def test_extract_unique_items() -> None:
    project_ids = {
      '01': 'open', 
      '03': 'in progress',
      '05': 'in progress',
      '04': 'completed'
    }

    expected_project_ids = ['completed', 'in progress', 'open']

    assert ex10.extract_unique_items(project_ids) == expected_project_ids