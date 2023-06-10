import pytest
import functions.functions_exercise_6 as ex6

def test_any_item_is_truthy() -> None:
  items = ('', 0.0, 0, False)
  assert ex6.any_item_is_truthy(items=items) == False