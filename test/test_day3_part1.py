import pytest
from src.day3.day3_part1 import multiplier_adder
from unittest.mock import patch

@patch("src.day3.day3_part1.create_memory")
def xtest_returns_int(mock_create_memory):

    mock_create_memory.return_value = ["mul(4,5)"]

    result = multiplier_adder()

    assert type(result) == int

@patch("src.day3.day3_part1.create_memory")
def xtest_returns_correct_value_for_single_mul(mock_create_memory):

    mock_create_memory.return_value = ["mul(4,5)"]

    result = multiplier_adder()

    expected = 20

    assert result == expected

@patch("src.day3.day3_part1.create_memory")
def test_returns_correct_value_for_multiple_mul(mock_create_memory):

    mock_create_memory.return_value = ["mul(4,5)","mul(3,6)"]

    result = multiplier_adder()

    expected = 38

    assert result == expected