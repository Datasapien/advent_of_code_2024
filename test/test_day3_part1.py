import pytest
from src.day3.day3_part1 import func
from unittest.mock import patch

@patch("")
def test(mock):

    mock.return_value = [[7, 6, 4, 2, 1]]

    result = func()

    assert type(result) == int