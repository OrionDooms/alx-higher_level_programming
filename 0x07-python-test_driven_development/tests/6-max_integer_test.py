#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_number(self):
        result = [3]
        self.assertEqual(max_integer(result), 3)

    def test_positive_list(self):
        result = [4, 8, 3, 2, 5, 6]
        self.assertEqual(max_integer(result), 8)

    def test_negative_list(self):
        result = [-4, -8, -3, -2, -5, -6]
        self.assertEqual(max_integer(result), -2)

    def test_float_list(self):
        result = [4.6, 2.8, 3, -2, 6.5, 6]
        self.assertEqual(max_integer(result), 6.5)

    def test_string_list(self):
        result = ["Hello", "Alx", "School"]
        self.assertEqual(max_integer(result), "School")

    def test_string(self):
        result = "Hello"
        self.assertEqual(max_integer(result), "o")


if __name__ == '__main__':
    unittest.main()
