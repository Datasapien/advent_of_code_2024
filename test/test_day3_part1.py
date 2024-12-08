import pytest
from src.day3.part1 import multiplier_adder
from unittest.mock import patch

@patch("src.day3.part1.create_memory")
def test_returns_int(mock_create_memory):

    mock_create_memory.return_value = ["mul(4,5)"]

    result = multiplier_adder()

    assert type(result) == int

@patch("src.day3.part1.create_memory")
def test_returns_correct_value_for_single_mul(mock_create_memory):

    mock_create_memory.return_value = ["mul(4,5)"]

    result = multiplier_adder()

    expected = 20

    assert result == expected

@patch("src.day3.part1.create_memory")
def test_returns_correct_value_for_multiple_mul(mock_create_memory):

    mock_create_memory.return_value = ["mul(4,5)","mul(3,6)"]

    result = multiplier_adder()

    expected = 38

    assert result == expected

@patch("src.day3.part1.create_memory")
def test_returns_correct_value_for_single_corrupt_str(mock_create_memory):

    mock_create_memory.return_value = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]

    result = multiplier_adder()

    expected = 161

    assert result == expected

@patch("src.day3.part1.create_memory")
def test_returns_correct_value_for_two_corrupt_strs(mock_create_memory):

    mock_create_memory.return_value = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]

    result = multiplier_adder()

    expected = 322

    assert result == expected