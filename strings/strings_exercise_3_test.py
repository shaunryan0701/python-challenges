import pytest
import strings.strings_exercise_3 as ex3

def test_check_string_end() -> None:
    code1 = 'FVNISJND-XX-2020'
    code2 = 'FVNISJND-XY-2019'
    assert ex3.check_string_end(code1) == '2020'
    assert ex3.check_string_end(code2) == '2019'