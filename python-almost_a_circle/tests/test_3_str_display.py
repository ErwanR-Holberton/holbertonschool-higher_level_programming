#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestStrDisplay(unittest.TestCase):
    def test_str(self):
        r1 = Rectangle(2, 2, 0, 0, 20)
        s1 = Square(2, 0, 0, 20)
        self.assertEqual(str(r1), "[Rectangle] (20) 0/0 - 2/2")
        self.assertEqual(str(s1), "[Square] (20) 0/0 - 2")

    def test_Display(self):
        r1 = Rectangle(2, 2, 0, 0, 21)
        s1 = Square(2, 0, 0, 21)
        self.assertEqual(r1.display(), print("##\n##\n"))
        self.assertEqual(s1.display(), print("##\n##\n"))
        r1.__x = 1
        r1.__y = 2
        s1.__x = 1
        s1.__y = 2
        self.assertEqual(r1.display(), print("\n\n ##\n ##\n"))
        self.assertEqual(s1.display(), print("\n\n ##\n ##\n"))


if __name__ == '__main__':
    unittest.main()
