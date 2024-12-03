import pytest
from src.day_1.day_1 import find_distance

def test_returns_int():
    #arrange
    test_a = [3,4,2,1,3,3]
    test_b = [4,3,5,3,9,3]

    #act
    result = find_distance(test_a, test_b)

    #assert
    assert type(result) == int

def test_returns_correct_value_for_single_item_list():
    #arrange
    test_a = [3]
    test_b = [4]

    #act
    result = find_distance(test_a, test_b)
    expected = 1

    #assert
    assert result == expected

def test_returns_correct_value_for_sorted_two_item_list():
    #arrange
    test_a = [3,5]
    test_b = [4,9]

    #act
    result = find_distance(test_a, test_b)
    expected = 5
    
    #assert
    assert result == expected

def test_returns_correct_value_for_unsorted_two_item_list():
    #arrange
    test_a = [3,5]
    test_b = [9,4]

    #act
    result = find_distance(test_a, test_b)
    expected = 5
    
    #assert
    assert result == expected

def test_returns_correct_value_for_long_unsorted_lists():
    #arrange
    test_a = [3,4,2,1,3,3]
    test_b = [4,3,5,3,9,3]

    #act
    result = find_distance(test_a, test_b)
    expected = 11
    
    #assert
    assert result == expected