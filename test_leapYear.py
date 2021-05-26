import io
import sys
import pytest
import leapYear
import unittest
from unittest.mock import patch
from io import StringIO

class TestLeapYear(unittest.TestCase):
        @patch('builtins.input', side_effect=['0'])
    def test_year_zero(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear(0)                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['0 is a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

    # @patch('builtins.input', side_effect=['2020'])
    # def testValidLeapYear(self,mock_input):
    #     # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
    #     capturedOutput = io.StringIO()                  # Create StringIO object
    #     sys.stdout = capturedOutput                     #  and redirect stdout.
    #     leapYear.calcLeapYear(2020)                                    # Call function.
    #     sys.stdout = sys.__stdout__                     # Reset redirect.
    #     expected = ['2020 is a leap year', '']
    #     actual = capturedOutput.getvalue().split('\n')
    #     self.assertEqual(actual, expected)
    
    # @patch('builtins.input', side_effect=['2019'])
    # def testNonValidLeapYear(self,mock_input):
    #     # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
    #     capturedOutput = io.StringIO()                  # Create StringIO object
    #     sys.stdout = capturedOutput                     #  and redirect stdout.
    #     leapYear.calcLeapYear(2019)                                  # Call function.
    #     sys.stdout = sys.__stdout__                     # Reset redirect.
    #     expected = ['2019 is not a leap year', '']
    #     actual = capturedOutput.getvalue().split('\n')
    #     self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

