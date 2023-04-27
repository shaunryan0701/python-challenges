import pytest
import dictionaries.dictionaries_exercise_1 as ex1

def test_extract_dict_keys() -> None: 
  capitals = {
      'USA': 'Washington',
      'Germany': 'Berlin',
      'Austria': 'Vienna'
  }
  assert ex1.extract_dict_keys(capitals) == ['USA', 'Germany', 'Austria']