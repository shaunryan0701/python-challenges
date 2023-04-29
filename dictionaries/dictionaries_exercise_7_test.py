import pytest
import dictionaries.dictionaries_exercise_7 as ex7

def test_add_dictionary_item() -> None:
    stocks = {
      'MSFT.US': {'Microsoft Corp': 184},
      'AAPL.US': {'Apple Inc': 310},
      'MMM.US': {'3M Co': 148}
    }

    expected_stocks = {
      'MSFT.US': {'Microsoft Corp': 184},
      'AAPL.US': {'Apple Inc': 310},
      'MMM.US': {'3M Co': 148},
      'V.US': {'Visa Inc': 185}
    }

    assert ex7.add_dictionary_item(stocks, 'V.US', 'Visa Inc', 185) == expected_stocks