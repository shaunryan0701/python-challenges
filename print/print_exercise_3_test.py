import pytest
import print.print_exercise_3 as ex3

def test_return_learning_info() -> None:
    assert ex3.return_learning_info('Python', 3.8) == 'I am learning Python version 3.8'