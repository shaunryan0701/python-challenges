import pytest
import strings.strings_exercise_7 as ex7

def test_split_string_by_lines() -> None:
    text = """Python is a general-purpose language.
Python is popular."""
    assert ex7.split_string_by_lines(text) == [
        'Python is a general-purpose language.',
        'Python is popular.'
        ]