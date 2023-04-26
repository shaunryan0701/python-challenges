import pytest
import lists.lists_exercise_5 as ex5

def test_extend_list_with_list() -> None:
    day1 = ['3984', '9042', '4829', '2380']
    day2 = ['4231', '5234', '1345', '2455']
    expected = ['3984', '9042', '4829', '2380', '4231', '5234', '1345', '2455']

    assert ex5.extend_list(day1, day2) == expected

def test_extend_list_with_tuple() -> None:
    day1 = ['3984', '9042', '4829', '2380']
    day2 = ('4231', '5234', '1345', '2455')
    expected = ['3984', '9042', '4829', '2380', '4231', '5234', '1345', '2455']

    assert ex5.extend_list(day1, day2) == expected

def test_extend_list_with_string() -> None:
    day1 = ['3984', '9042', '4829', '2380']
    day2 = 'day2'
    expected = ['3984', '9042', '4829', '2380', 'd', 'a', 'y', '2']

    assert ex5.extend_list(day1, day2) == expected

# a set is unordered so there is no guarantee that this would work
# def test_extend_list_with_set() -> None:
#     day1 = ['3984', '9042', '4829', '2380']
#     day2 = {'4231', '5234', '1345', '2455'}
#     expected = ['3984', '9042', '4829', '2380', '4231', '5234', '1345', '2455']

#     assert ex5.extend_list(day1, day2) == expected