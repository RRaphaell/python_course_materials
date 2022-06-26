import unittest
import math
from functools import reduce

from accumulate import accumulate
from join_tuples import join_tuples
from multiply import multiply
from subset import is_subset
from subtraction import subtraction
from transactions import get_balance
from uniques import flatten_only_unique


class Test(unittest.TestCase):

    def test_accumulate_1(self):
        arg = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
        self.assertEqual([sum(t) for t in arg], accumulate(arg))

    def test_accumulate_2(self):
        arg = [(1, 2), (2, 3), (3, 4)]
        self.assertEqual([sum(t) for t in arg], accumulate(arg))

    def test_accumulate_3(self):
        arg = [(1,), (2,), (3,), (2,)]
        self.assertEqual([sum(t) for t in arg], accumulate(arg))

    def test_join_tuples_1(self):
        args = [(5, 6), (5, 7), (5, 8), (6, 10), (6, 20), (7, 13)]
        output = [(5, 6, 7, 8), (6, 10, 20), (7, 13)]
        self.assertEqual(output, join_tuples(args))

    def test_join_tuples_2(self):
        args = [(1, 2), (3, 4), (5, 6), (7, 8)]
        self.assertEqual(args, join_tuples(args))

    def test_multiply_1(self):
        arg = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
        self.assertEqual([math.prod(t) for t in arg], multiply(arg))

    def test_multiply_2(self):
        arg = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
        self.assertEqual([math.prod(t) for t in arg], multiply(arg))

    def test_multiply_3(self):
        arg = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
        self.assertEqual([math.prod(t) for t in arg], multiply(arg))

    def test_is_subset_1(self):
        set1 = {1, 2, 3, 4, 5}
        set2 = {5, 4, 3}
        self.assertEqual(set2.issubset(set1), is_subset(set1, set2))

    def test_is_subset_2(self):
        set1 = {1}
        set2 = {1}
        self.assertEqual(set2.issubset(set1), is_subset(set1, set2))

    def test_is_subset_3(self):
        set1 = {1, 2, 3}
        set2 = {5, 4, 3}
        self.assertEqual(set2.issubset(set1), is_subset(set1, set2))

    def test_subtraction_1(self):
        set1 = {1, 2, 3}
        set2 = {5, 4, 3}
        self.assertEqual(set1-set2, subtraction(set1, set2))

    def test_subtraction_2(self):
        set1 = {1, 2, 3}
        set2 = {5, 4, 3}
        self.assertEqual(set1-set2, subtraction(set1, set2))

    def test_subtraction_3(self):
        set1 = {1, 2, 3}
        set2 = {5, 4, 3}
        self.assertEqual(set1-set2, subtraction(set1, set2))

    def test_uniques_1(self):
        arg = [(1, 3, 4), (1, 1, 1), (4, 5, 5)]
        self.assertEqual(reduce(lambda x, y: set(x) | set(y), arg), flatten_only_unique(arg))

    def test_uniques_2(self):
        arg = [(1, 3, 4), (1, 1, 1), (4, 5, 5)]
        self.assertEqual(reduce(lambda x, y: set(x) | set(y), arg), flatten_only_unique(arg))

    def test_uniques_3(self):
        arg = [(1, 3, 4), (1, 1, 1), (4, 5, 5)]
        self.assertEqual(reduce(lambda x, y: set(x) | set(y), arg), flatten_only_unique(arg))

    def test_transactions_1(self):
        arg = [("25-Nov-2021", "01001021877", "01003577801", 10),
               ("25-Nov-2021", "01001021877", "01003577801", 20),
               ("03-Dec-2021", "01003577801", "02007783199", 30),
               ("04-Dec-2021", "40057831990", "46001233211", 50)]
        output = [("01001021877", 70),
                  ("01003577801", 100),
                  ("02007783199", 130),
                  ("40057831990", 50),
                  ("46001233211", 150)]
        self.assertEqual(output, get_balance(arg))


if __name__ == '__main__':
    unittest.main()
