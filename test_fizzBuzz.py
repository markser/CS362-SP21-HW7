import io
from io import StringIO
import sys
import unittest
from unittest.mock import patch
import pytest
import fizzBuzz

# pytest test_fizzBuzz.py

class TestCalculator(unittest.TestCase):
    # @patch('builtins.input', side_effect=['1'])
    def test_number_one(self):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        fizzBuzz.fizzBuzz()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['1', '']
        actual = capturedOutput.getvalue().split('\n')
        # self.assertEqual(actual, expected
        # if (actual.find(expected[0])):
        self.assertTrue(expected[0] in actual)
    
    def test_number_fizz(self):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        fizzBuzz.fizzBuzz()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        actual = capturedOutput.getvalue().split('\n')
        actualNumOfFizz = actual.count('Fizz')
        # self.assertEqual(actual, expected
        # if (actual.find(expected[0])):
        self.assertTrue(33 == actualNumOfFizz)

