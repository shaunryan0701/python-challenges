import pytest
import dictionaries.dictionaries_Exercise_5 as ex5

def test_get_dictionary_values_by_key() -> None:
    stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
  }
    assert ex5.get_dictionary_values_by_key(stocks, 'MSFT.US' ) == 184