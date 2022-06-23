import io
import sys
import unittest
from unittest.mock import patch

from welcome_text import welcome_text
from cashier import cashier
from convert_gel_usd import gel_usd, USD
from find_maximum import get_maximum
from equality_str_repr import equality_repr
from even_odd import even_or_odd
from overflow import overflow
from check_sorting import is_sorted
from add_square import add_square
from driver_speed_test import driver_speed_test


class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=["Raphael", "Kalandadze"])
    def test_welcome_text_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        welcome_text()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "Hello Raphael Kalandadze nice to meet you!\n"

    @patch('builtins.input', side_effect=["", ""])
    def test_welcome_text_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        welcome_text()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "Hello   nice to meet you!\n"

    @patch('builtins.input', side_effect=["20", "7"])
    def test_cashier_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        cashier()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "13\n"

    @patch('builtins.input', side_effect=["100", "100"])
    def test_cashier_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        cashier()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "0\n"

    @patch('builtins.input', side_effect=["13", "gel"])
    def test_gel_usd_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        gel_usd()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == f"{13 * USD}\n"

    @patch('builtins.input', side_effect=["15", "usd"])
    def test_gel_usd_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        gel_usd()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == f"{15 / USD}\n"

    @patch('builtins.input', side_effect=["12.123123123", "usd"])
    def test_gel_usd_3(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        gel_usd()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == f"{12.123123123 / USD}\n"

    @patch('builtins.input', side_effect=["13", "7", "-3"])
    def test_find_maximum_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        get_maximum()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "13\n"

    @patch('builtins.input', side_effect=["1", "2", "3"])
    def test_find_maximum_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        get_maximum()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "3\n"

    @patch('builtins.input', side_effect=["1", "5", "0"])
    def test_find_maximum_3(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        get_maximum()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "5\n"

    @patch('builtins.input', side_effect=["1", "5"])
    def test_equality_repr_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        equality_repr()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "1 + 5 = 6\n"

    @patch('builtins.input', side_effect=["1", "1"])
    def test_equality_repr_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        equality_repr()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "1 + 1 = 2\n"

    @patch('builtins.input', side_effect=["1"])
    def test_even_or_odd_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        even_or_odd()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "odd\n"

    @patch('builtins.input', side_effect=["0"])
    def test_even_or_odd_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        even_or_odd()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "even\n"

    @patch('builtins.input', side_effect=["-4"])
    def test_even_or_odd_3(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        even_or_odd()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "even\n"

    @patch('builtins.input', side_effect=["0", "10"])
    def test_overflow_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        overflow()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "10\n"

    @patch('builtins.input', side_effect=["50", "60"])
    def test_overflow_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        overflow()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "overflow\n"

    @patch('builtins.input', side_effect=["-1", "-1", "2"])
    def test_is_sorted_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        is_sorted()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "sorted\n"

    @patch('builtins.input', side_effect=["5", "6", "1"])
    def test_is_sorted_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        is_sorted()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "not sorted\n"

    @patch('builtins.input', side_effect=["5", "2", "4"])
    def test_is_sorted_3(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        is_sorted()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "not sorted\n"

    @patch('builtins.input', side_effect=["1"])
    def test_add_square_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        add_square()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "2\n"

    @patch('builtins.input', side_effect=["-2"])
    def test_add_square_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        add_square()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "2\n"

    @patch('builtins.input', side_effect=["62", "True"])
    def test_driver_speed_1(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        driver_speed_test()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "0\n"

    @patch('builtins.input', side_effect=["62", "False"])
    def test_driver_speed_2(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        driver_speed_test()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "100\n"

    @patch('builtins.input', side_effect=["82", "False"])
    def test_driver_speed_3(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        driver_speed_test()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "200\n"

    @patch('builtins.input', side_effect=["82", "True"])
    def test_driver_speed_4(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        driver_speed_test()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "100\n"

    @patch('builtins.input', side_effect=["102", "False"])
    def test_driver_speed_5(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        driver_speed_test()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "arrested\n"

    @patch('builtins.input', side_effect=["102", "True"])
    def test_driver_speed_6(self, mock_inputs):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        driver_speed_test()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert captured_output.getvalue() == "200\n"


if __name__ == '__main__':
    unittest.main()
