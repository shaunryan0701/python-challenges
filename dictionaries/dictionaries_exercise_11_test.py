import pytest
import dictionaries.dictionaries_exercise_11 as ex11

def test_delete_from_dict() -> None:  
    stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
    expected_stats = {'site': 'e-smartdata.org', 'type': 'organic'}

    assert ex11.delete_from_dict(stats, 'traffic') == expected_stats 