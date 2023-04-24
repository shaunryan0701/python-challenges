import pytest
import tuples.tuples_exercise_2 as ex2

def test_add_tuples() -> None:
    dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
    dji2 = ('HD.US', 'GS.US', 'NKE.US')
    assert ex2.add_tuples(dji1, dji2) == (('AAPL.US', 'IBM.US', 'MSFT.US'), ('HD.US', 'GS.US', 'NKE.US'))