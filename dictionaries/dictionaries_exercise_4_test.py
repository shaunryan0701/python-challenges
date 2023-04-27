import pytest
import dictionaries.dictionaries_exercise_4 as ex4

def test_extract_dict_items_by_key() -> None: 
  capitals = {
      'USA': 'Washington',
      'Germany': 'Berlin',
      'Austria': 'Vienna'
  }
  assert ex4.extract_dict_items_by_key(capitals, 'Austria') == 'Vienna'