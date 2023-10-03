#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """
        Test for an empty list. Should return None.
        """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """
        Test for a list with a single element. Should return the element itself.
        """
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """
        Test for a list of positive numbers. Should return the maximum.
        """
        self.assertEqual(max_integer([3, 5, 2, 8, 1]), 8)

    def test_negative_numbers(self):
        """
        Test for a list of negative numbers. Should return the maximum (the least negative).
        """
        self.assertEqual(max_integer([-3, -5, -2, -8, -1]), -1)

    def test_mixed_numbers(self):
        """
        Test for a list of mixed positive and negative numbers. Should return the maximum positive.
        """
        self.assertEqual(max_integer([3, -5, 2, -8, 1]), 3)

    def test_duplicate_maximum(self):
        """
        Test for a list with duplicate maximum values. Should return the maximum.
        """
        self.assertEqual(max_integer([3, 5, 2, 8, 8]), 8)

    def test_float_numbers(self):
        """
        Test for a list of floating-point numbers. Should return the maximum.
        """
        self.assertAlmostEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

if __name__ == '__main__':
    unittest.main()

