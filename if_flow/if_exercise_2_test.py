import pytest
import if_flow.if_exercise_2 as ex2

def test_check_if_string_is_upper() -> None:
    test_string = 'UTFYRDJLVHFD'

    assert ex2.check_if_string_is_upper(test_string) == 'YES'

def test_check_if_string_is_upper_with_lower() -> None:
    test_string = 'nbvuytTRRUYDYT'

    assert ex2.check_if_string_is_upper(test_string) == 'NO'