import pytest
import strings.strings_exercise_5 as ex5

def test_search_tuple_for_string() -> None:
    path1 = (
      'https://e-smartdata.teachable.com/p/'
      'sciezka-data-scientist-machine-learning-engineer'
    )

    path2 = (
    'https://e-smartdata.teachable.com/p/'
    'sciezka-bi-analyst-data-analyst'
)

    assert ex5.search_tuple_for_string(path1, 'scientist') == 49
    assert ex5.search_tuple_for_string(path2, 'scientist') == -1
