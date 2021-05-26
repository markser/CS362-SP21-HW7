import io
import sys
import pytest
import leapYear
import unittest
from unittest.mock import patch
from io import StringIO

class TestLeapYear(unittest.TestCase):
    @patch('builtins.input', side_effect=['400'])
    def test_year_divisible_by_400_true(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear(400)                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['400 is a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['0'])
    def test_year_divisible_by_400_false(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear(1100)                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['1100 is not a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['200'])
    def test_year_divisible_by_100_true(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear(200)                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['200 is not a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['100'])
    def test_year_divisible_by_100_false(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear(100)                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['100 is not a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['4'])
    def test_year_divisible_by_4_true(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear(4)                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['4 is a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['5'])
    def test_year_divisible_by_4_false(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear(5)                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['5 is not a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

