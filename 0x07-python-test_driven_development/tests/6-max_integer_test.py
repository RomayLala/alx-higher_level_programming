#!/usr/bin/python3
"""Unittest for max_integer([..]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer function."""

    def test_max_at_end(self):
        """Test when the max integer is at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test when the max integer is in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Test when the list contains only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test when the list contains negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test when the list contains both positive and negative numbers."""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_all_equal(self):
        """Test when all elements in the list are equal."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

if __name__ == "__main__":
    unittest.main()
