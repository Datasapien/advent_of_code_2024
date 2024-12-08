import pytest
from src.day2.part1 import safe_reports
from unittest.mock import patch

@patch("src.day2.part1.create_reports")
def test_returns_int(mock_create_reports):

    mock_create_reports.return_value = [[7, 6, 4, 2, 1]]

    result = safe_reports()

    assert type(result) == int

@patch("src.day2.part1.create_reports")
def test_for_single_ascending_safe_report(mock_create_reports):

    mock_create_reports.return_value = [[1, 3, 6, 7, 9]]

    result = safe_reports()

    expected = 1

    assert result == expected

@patch("src.day2.part1.create_reports")
def test_for_two_ascending_safe_reports(mock_create_reports):

    mock_create_reports.return_value = [[1, 3, 6, 7, 9],[1, 3, 6, 7, 9]]

    result = safe_reports()

    expected = 2

    assert result == expected

@patch("src.day2.part1.create_reports")
def test_for_one_ascending_safe_report(mock_create_reports):

    mock_create_reports.return_value = [[1, 3, 6, 7, 9],[1, 2, 7, 8, 9]]

    result = safe_reports()

    expected = 1

    assert result == expected

@patch("src.day2.part1.create_reports")
def test_for_single_descending_safe_report(mock_create_reports):

    mock_create_reports.return_value = [[7, 6, 4, 2, 1]]

    result = safe_reports()

    expected = 1

    assert result == expected

@patch("src.day2.part1.create_reports")
def test_for_two_descending_safe_reports(mock_create_reports):

    mock_create_reports.return_value = [[7, 6, 4, 2, 1],[7, 6, 4, 2, 1]]

    result = safe_reports()

    expected = 2

    assert result == expected

@patch("src.day2.part1.create_reports")
def test_for_one_descending_safe_report(mock_create_reports):

    mock_create_reports.return_value = [[7, 6, 4, 2, 1],[10, 6, 4, 2, 1]]

    result = safe_reports()

    expected = 1

    assert result == expected

@patch("src.day2.part1.create_reports")
def test_with_full_test_input(mock_create_reports):

    mock_create_reports.return_value = [[7, 6, 4, 2, 1],
                                        [1, 2, 7, 8, 9],
                                        [9, 7, 6, 2, 1],
                                        [1, 3, 2, 4, 5],
                                        [8, 6, 4, 4, 1],
                                        [1, 3, 6, 7, 9]]

    result = safe_reports()

    expected = 2

    assert result == expected