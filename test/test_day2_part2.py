import pytest
from src.day2.part2 import safe_reports
from unittest.mock import patch

@patch("src.day2.part2.create_reports")
def test_returns_int(mock_create_reports):

    mock_create_reports.return_value = [[7, 6, 4, 2, 1]]

    result = safe_reports()

    assert type(result) == int

@patch("src.day2.part2.create_reports")
def test_for_single_level_removal(mock_create_reports):

    mock_create_reports.return_value = [[1, 3, 6, 7, 16]]

    result = safe_reports()

    expected = 1

    assert result == expected


@patch("src.day2.part2.create_reports")
def test_for_double_level_removal(mock_create_reports):

    mock_create_reports.return_value = [[1, 3, 6, 7, 16, 32]]

    result = safe_reports()

    expected = 0

    assert result == expected

@patch("src.day2.part2.create_reports")
def test_with_full_test_input(mock_create_reports):

    mock_create_reports.return_value = [[7, 6, 4, 2, 1],
                                        [1, 2, 7, 8, 9],
                                        [9, 7, 6, 2, 1],
                                        [1, 3, 2, 4, 5],
                                        [8, 6, 4, 4, 1],
                                        [1, 3, 6, 7, 9]]

    result = safe_reports()

    expected = 4

    assert result == expected