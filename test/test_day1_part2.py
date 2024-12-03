import pytest
from src.day1.day1_part2 import similarity_score
from unittest.mock import patch

@patch("src.day1.day1_part2.create_lists")
def test_returns_int(mock_create_lists):

    mock_create_lists.return_value = [[3,4,2,1,3,3],[4,3,5,3,9,3]]

    result = similarity_score()

    assert type(result) == int

@patch("src.day1.day1_part2.create_lists")
def test_returns_correct_value_for_single_value_list(mock_create_lists):

    mock_create_lists.return_value = [[3],[3]]

    result = similarity_score()
    expected = 3

    assert result == expected

@patch("src.day1.day1_part2.create_lists")
def test_returns_correct_value_for_two_value_list(mock_create_lists):

    mock_create_lists.return_value = [[3,4],[3,3]]

    result = similarity_score()
    expected = 6

    assert result == expected

@patch("src.day1.day1_part2.create_lists")
def test_returns_correct_value_for_full_test_list(mock_create_lists):

    mock_create_lists.return_value = [[3,4,2,1,3,3],[4,3,5,3,9,3]]

    result = similarity_score()
    expected = 31

    assert result == expected