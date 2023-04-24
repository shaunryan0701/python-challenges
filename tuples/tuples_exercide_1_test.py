import pytest
import tuples.tuples_exercise_1 as ex1

def test_join_tuples() -> None:
    dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
    dji2 = ('HD.US', 'GS.US', 'NKE.US')
    assert ex1.join_tuples(dji1, dji2) == ('AAPL.US', 'IBM.US', 'MSFT.US', 'HD.US', 'GS.US', 'NKE.US')