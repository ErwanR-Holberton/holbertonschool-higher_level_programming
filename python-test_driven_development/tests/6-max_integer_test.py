#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_negative(self):
        self.assertEqual(max_integer([-5, -700]), -5)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
