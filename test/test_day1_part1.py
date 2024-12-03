import pytest
from src.day1.day1_part1 import find_distance
from unittest.mock import patch

@patch("src.day1.day1_part1.create_lists")
def test_returns_int(mock_create_lists):
    #arrange
    mock_create_lists.return_value = [[3,4,2,1,3,3],[4,3,5,3,9,3]]

    #act
    result = find_distance()

    #assert
    assert type(result) == int

@patch("src.day1.day1_part1.create_lists")
def test_returns_correct_value_for_single_item_list(mock_create_lists):
    #arrange
    mock_create_lists.return_value = [[3],[4]]

    #act
    result = find_distance()
    expected = 1

    #assert
    assert result == expected

@patch("src.day1.day1_part1.create_lists")
def test_returns_correct_value_for_sorted_two_item_list(mock_create_lists):
    #arrange
    mock_create_lists.return_value = [[3,5],[4,9]]

    #act
    result = find_distance()
    expected = 5
    
    #assert
    assert result == expected

@patch("src.day1.day1_part1.create_lists")
def test_returns_correct_value_for_unsorted_two_item_list(mock_create_lists):
    #arrange
    mock_create_lists.return_value = [[3,5],[9,4]]

    #act
    result = find_distance()
    expected = 5
    
    #assert
    assert result == expected

@patch("src.day1.day1_part1.create_lists")
def test_returns_correct_value_for_long_unsorted_lists(mock_create_lists):
    #arrange
    mock_create_lists.return_value = [[3,4,2,1,3,3],[4,3,5,3,9,3]]


    #act
    result = find_distance()
    expected = 11
    
    #assert
    assert result == expected