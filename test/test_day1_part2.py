import pytest
from src.day1.day1_part1 import similarity_score
from unittest.mock import patch

@patch("src.day1.day1_create_lists.create_lists")
def test_returns_int(mock_create_lists):
    #arrange
    mock_create_lists.return_value = [[3,4,2,1,3,3],[4,3,5,3,9,3]]

    #act
    result = similarity_score()

    #assert
    assert type(result) == int