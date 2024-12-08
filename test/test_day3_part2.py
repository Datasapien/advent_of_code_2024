import pytest
from src.day3.part2 import create_memory,extract_valid_memory_string, extract_valid_muls, calculate_total
from unittest.mock import mock_open, patch
import csv
import unittest

test_string = "mul(1,1)mul[1,1]don't()mul(2,2)mul[2,2]do()mul(3,3)mul[3,3]don't()mul(4,4)mul[4,4]do()mul(5,5)mul[5,5]don't()mul(6,6)mul[6,6]do()mul(7,7)mul[7,7]expect168"

class TestCreateMemory():
    @patch('builtins.open', new_callable=mock_open, read_data=test_string)
    def test_create_memory_returns_string(self, mock_file):
        # Call the function
        result = create_memory()

        # Expected result based on mocked file data
        expected = test_string

        # Check that the result matches the expected outcome
        assert result == expected

class TestExtractValidMemoryStrings():
    @patch("src.day3.part2.create_memory")
    def test_extracts_valid_string(self, mock_create_memory):
        mock_create_memory.return_value = test_string

        result = extract_valid_memory_string()

        expected = 'mul(1,1)mul[1,1]do()mul(3,3)mul[3,3]do()mul(5,5)mul[5,5]do()mul(7,7)mul[7,7]expect168'
        
        assert result == expected

class TestExtractValidMuls():
    @patch("src.day3.part2.extract_valid_memory_string")
    def test_extracts_valid_mul(self, mock_extract_valid_memory_string):

        mock_extract_valid_memory_string.return_value = "mul(1,1)mul[1,1]mul(3,3)mul[3,3]mul(5,5)mul[5,5]mul(7,7)mul[7,7]expect168"

        result = extract_valid_muls()

        expected = "mul(1,1)mul(3,3)mul(5,5)mul(7,7)"
        
        assert result == expected

class TestCalculateMuls():

    @patch("src.day3.part2.extract_valid_muls")
    def test_returns_int(self,mock_create_memory):

        mock_create_memory.return_value = "mul(1,1)mul(3,3)mul(5,5)mul(7,7)"

        result = calculate_total()

        assert type(result) == int

    @patch("src.day3.part2.extract_valid_muls")
    def test_returns_correct_value(self,mock_create_memory):

        mock_create_memory.return_value = "mul(1,1)mul(3,3)mul(5,5)mul(7,7)"

        result = calculate_total()

        expected = 84

        assert result == expected