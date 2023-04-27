import pytest
import dictionaries.dictionaries_exercise_3 as ex3

def test_extract_dict_items() -> None: 
  capitals = {
      'USA': 'Washington',
      'Germany': 'Berlin',
      'Austria': 'Vienna'
  }
  assert ex3.extract_dict_items(capitals) == [('USA', 'Washington'), ('Germany', 'Berlin'), ('Austria', 'Vienna')]