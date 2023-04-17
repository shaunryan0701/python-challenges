import pytest
import print.print_exercise_5 as ex5

def test_return_format() -> None:
    pi = 3.1415926535
    assert ex5.return_format(pi) == 'Pi: 3.14'