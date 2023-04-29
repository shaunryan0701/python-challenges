import pytest
import dictionaries.dictionaries_exercise_6 as ex6

def test_update_dictionary() -> None:
    stocks = {
      'MSFT.US': {'Microsoft Corp': 184},
      'AAPL.US': {'Apple Inc': 310},
      'MMM.US': {'3M Co': 148}
    }

    expected_stocks = {
      'MSFT.US': {'Microsoft Corp': 199},
      'AAPL.US': {'Apple Inc': 310},
      'MMM.US': {'3M Co': 148}
    }
    assert ex6.update_dictionary(stocks, 'MSFT.US', 199) == expected_stocks