import pytest
import lists.lists_exercise_4 as ex4

def test_add_to_list() -> None:
    filenames = ['view.jpg', 'bear.jpg', 'ball.png']
    expected_filenames = ['phone.jpg', 'view.jpg', 'bear.jpg', 'ball.png']
    assert ex4.add_to_list(filenames, 'phone.jpg') == expected_filenames

def test_remove_from_list() -> None:
    filenames = ['view.jpg', 'bear.jpg', 'ball.png']
    expected_filenames = ['view.jpg', 'bear.jpg']
    assert ex4.remove_from_list(filenames, 'ball.png') == expected_filenames