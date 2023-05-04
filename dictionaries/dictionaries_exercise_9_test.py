import pytest
import dictionaries.dictionaries_exercise_9 as ex9

def test_extract_from_list_to_dict() -> None:
  tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]
  expected_tickers = {
    0: 'AAPL.US', 
    1: 'AXP.US', 
    2: 'BA.US', 
    3: 'CAT.US', 
    4: 'CSCO.US', 
    5: 'CVX.US', 
    6: 'DIS.US', 
    7: 'DOW.US', 
    8: 'GS.US', 
    9: 'HD.US', 
    10: 'IBM.US', 
    11: 'INTC.US'
  }

  assert ex9.extract_from_list_to_dict(tickers) == expected_tickers