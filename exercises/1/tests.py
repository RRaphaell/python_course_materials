import unittest
import sys
import io

from list_max import find_max_price_in_list
from list_sum import list_sum
from power import power
from filter_list import filter_list
from print_persons_info import get_smart_people
from smallest_numbers import smallest_numbers


class Test(unittest.TestCase):

    def setUp(self):
        self.test_lst1 = [1, 2, 3]
        self.test_lst2 = [1, 100, 7, 12, 3, 10, 5]
        self.test_lst3 = [2]
        self.test_lst4 = [1, -1, 2]

    def test_list_sum_1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        list_sum(self.test_lst1)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(str(sum(self.test_lst1))+"\n", captured_output.getvalue())

    def test_list_sum_2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        list_sum(self.test_lst2)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(str(sum(self.test_lst2))+"\n", captured_output.getvalue())

    def test_list_sum_3(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        list_sum(self.test_lst3)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(str(sum(self.test_lst3))+"\n", captured_output.getvalue())

    def test_list_max_1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        find_max_price_in_list(self.test_lst1)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(str(max(self.test_lst1))+"\n", captured_output.getvalue())

    def test_list_max_2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        find_max_price_in_list(self.test_lst2)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(str(max(self.test_lst2))+"\n", captured_output.getvalue())

    def test_list_max_3(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        find_max_price_in_list(self.test_lst3)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(str(max(self.test_lst3))+"\n", captured_output.getvalue())

    def test_power_1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        power(2, 4)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(f"{2**4}\n", captured_output.getvalue())

    def test_power_2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        power(1, 4)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(f"{1**4}\n", captured_output.getvalue())

    def test_power_3(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        power(0, 4)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(f"{0**4}\n", captured_output.getvalue())

    def test_list_filtering_1(self):
        _from, _to = 1, 10
        filtered_list = list(filter(lambda x: x in range(_from+1, _to), self.test_lst2))

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        filter_list(self.test_lst2, _from, _to)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(str, filtered_list))+"\n", captured_output.getvalue())

    def test_list_filtering_2(self):
        _from, _to = 90, 110
        filtered_list = list(filter(lambda x: x in range(_from+1, _to), self.test_lst2))

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        filter_list(self.test_lst2, _from, _to)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(str, filtered_list))+"\n", captured_output.getvalue())

    def test_list_filtering_3(self):
        _from, _to = 200, 300
        filtered_list = list(filter(lambda x: x in range(_from+1, _to), self.test_lst2))

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        filter_list(self.test_lst2, _from, _to)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(str, filtered_list)), captured_output.getvalue())

    def test_persons_info_1(self):
        names = ["Oliver", "Charlotte", "William", "Sophia", "Benjamin", "Isabella", "Lucas", "Henry", "Evelyn", "Alex"]
        knows_java = [False, True, False, False, True, False, True, False, False, True]
        knows_python = [False, False, True, False, True, False, False, False, True, True]
        filtered_list = filter(lambda x: x[1] or x[2], zip(names, knows_java, knows_python))

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        get_smart_people(names, knows_java, knows_python)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(lambda x: str(x[0]), filtered_list))+"\n", captured_output.getvalue())

    def test_persons_info_2(self):
        names = ["Oliver"]
        knows_java = [True]
        knows_python = [False]
        filtered_list = filter(lambda x: x[1] or x[2], zip(names, knows_java, knows_python))

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        get_smart_people(names, knows_java, knows_python)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(lambda x: str(x[0]), filtered_list))+"\n", captured_output.getvalue())

    def test_persons_info_3(self):
        names = ["Oliver"]
        knows_java = [False]
        knows_python = [True]
        filtered_list = filter(lambda x: x[1] or x[2], zip(names, knows_java, knows_python))

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        get_smart_people(names, knows_java, knows_python)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(lambda x: str(x[0]), filtered_list))+"\n", captured_output.getvalue())

    def test_persons_info_4(self):
        names = ["Oliver", "Charlotte"]
        knows_java = [False, False]
        knows_python = [False, False]
        filtered_list = filter(lambda x: x[1] or x[2], zip(names, knows_java, knows_python))

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        get_smart_people(names, knows_java, knows_python)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(lambda x: str(x[0]), filtered_list)), captured_output.getvalue())

    def test_smalles_number_1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        smallest_numbers(self.test_lst1)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(str, sorted(self.test_lst1[:3])))+"\n", captured_output.getvalue())

    def test_smalles_number_2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        smallest_numbers(self.test_lst2)
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(str, sorted(self.test_lst2[:3])))+"\n", captured_output.getvalue())

    def test_smalles_number_3(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        smallest_numbers([10, 10, 10, 10, 10, 0, 0, 0])
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("\n".join(map(str, sorted([10, 10, 10, 10, 10, 0, 0, 0])[:3]))+"\n", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
