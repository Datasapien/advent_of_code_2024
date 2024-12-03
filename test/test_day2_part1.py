import pytest
from src.day2.day2_part1 import safe_reports
from unittest.mock import patch

@patch("src.day1.day1_create_lists.create_lists")
def test_returns_int(mock_create_lists):

    mock_create_lists.return_value = [[3,4,2,1,3,3],[4,3,5,3,9,3]]

    result = safe_reports()

    assert type(result) == int