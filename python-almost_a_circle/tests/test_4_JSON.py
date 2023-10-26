#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestJSON(unittest.TestCase):
    def test_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(r1.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(s1.to_dictionary(), {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_JSON_string(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(r1.to_json_string(r1.to_dictionary()), "{\"id\": 5, \"width\": 1, \"height\": 2, \"x\": 3, \"y\": 4}")
        self.assertEqual(s1.to_json_string(s1.to_dictionary()), "{\"id\": 4, \"size\": 1, \"x\": 2, \"y\": 3}")


if __name__ == '__main__':
    unittest.main()
