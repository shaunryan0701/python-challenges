import pytest
import print.print_exercise_4 as ex4

def test_return_price():
    assert ex4.return_price(1.99) == 'This costs 1.99'