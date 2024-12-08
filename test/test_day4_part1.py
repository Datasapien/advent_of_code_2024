import pytest
from src.day4.part1 import create_word_search
from unittest.mock import mock_open, patch

test_input = "XY"

class TestCreateWordSearch():
    @patch('builtins.open', new_callable=mock_open, read_data=test_input)
    def test_returns_list_of_lists(self, mock_data):

        result = create_word_search()

        expected = [["X","Y"]]

        assert result == expected
        assert type(result) == list
        assert type(result[0]) == list