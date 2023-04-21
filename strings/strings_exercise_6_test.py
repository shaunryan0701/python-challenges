import pytest
import strings.strings_exercise_6 as ex6

def test_check_for_alpha_numeric_false() -> None:
    code1 = 'FVNISJND-20'
    assert ex6.check_for_alpha_numeric(code1) == False


def test_check_for_alpha_numeric_false() -> None:
    code2 = 'FVNISJND20'
    assert ex6.check_for_alpha_numeric(code2) == True