import pytest
import strings.strings_exercise_4 as ex4

def test_check_string_returns_true() -> None:
    path1 = 'youtube.com/watch?v=5EhRztVxums'
    assert ex4.check_string(path1, check_string='youtube') == True

def test_check_string_returns_true() -> None:
    path2 = 'google.com/search?q=car'
    assert ex4.check_string(path2, check_string='youtube') == False