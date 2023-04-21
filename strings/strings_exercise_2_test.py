import pytest
import strings.strings_exercise_2 as ex2

def test_count_occurrences() -> None:
    search_string = 'python is a popular programming language.'
    assert ex2.count_occurrences(search_string, 'p') ==  4