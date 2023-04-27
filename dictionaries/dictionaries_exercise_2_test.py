import pytest
import dictionaries.dictionaries_exercise_2 as ex2

def test_extract_dict_values() -> None: 
  capitals = {
      'USA': 'Washington',
      'Germany': 'Berlin',
      'Austria': 'Vienna'
  }
  assert ex2.extract_dict_values(capitals) == ['Washington', 'Berlin', 'Vienna']