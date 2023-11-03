#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests is used for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defination of unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Testing an_ordered list_of_integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Testing an_unordered list_of_integers."""
        unordered = [1, 4, 2, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Testing a_list with a beginning max_value."""
        max_at_beginning = [6, 5, 4, 2]
        self.assertEqual(max_integer(max_at_beginning), 6)

    def test_empty_list(self):
        """Testing an empty_list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Testing a list with a single_element."""
        one_element = [8]
        self.assertEqual(max_integer(one_element), 8)

    def test_floats(self):
        """Testing a_list of_floats."""
        floats = [1.54, 6.34, -9.124, 15.3, 6.1]
        self.assertEqual(max_integer(floats), 15.3)

    def test_ints_and_floats(self):
        """Testing a list_of inegers and_floats."""
        ints_and_floats = [1.54, 15.6, -10, 16, 7]
        self.assertEqual(max_integer(ints_and_floats), 16)

    def test_string(self):
        """Testing a_string."""
        string = "Mahmud"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_strings(self):
        """Testing list_of_strings."""
        strings = ["Mahmud", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Testing an_empty_string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
