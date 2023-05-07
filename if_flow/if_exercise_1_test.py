import pytest
import if_flow.if_exercise_1 as ex1

def test_check_file_extension() -> None:
    filename = '01012020_sales.xlsx'
    file_extension = 'xlsx'

    assert ex1.check_file_extension(file_name=filename, file_extension=file_extension) == True