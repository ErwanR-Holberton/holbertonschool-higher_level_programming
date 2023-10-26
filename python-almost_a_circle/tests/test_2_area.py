#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestAreaGetterSetter(unittest.TestCase):
    def test_rectangle_area_and_setter_getter(self):
        r1 = Rectangle(5, 5, 1, 1)
        self.assertEqual(r1.area(), 25)
        r1.height = 2
        r1.width = 2
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.area(), 4)
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(ValueError):
            r1.height = -5
        with self.assertRaises(ValueError):
            r1.width = -5
        with self.assertRaises(TypeError):
            r1.height = "-5"
        with self.assertRaises(TypeError):
            r1.width = "-5"
        with self.assertRaises(TypeError):
            r1.height = (1, 2)
        with self.assertRaises(TypeError):
            r1.width = (1, 2)
        with self.assertRaises(TypeError):
            r1.height = [(1)]
        with self.assertRaises(TypeError):
            r1.width = [(1)]
        with self.assertRaises(TypeError):
            r1.height = {1}
        with self.assertRaises(TypeError):
            r1.width = {5}
        with self.assertRaises(TypeError):
            r1.height = True
        with self.assertRaises(TypeError):
            r1.width = True
        with self.assertRaises(TypeError):
            r1.height = 5.2
        with self.assertRaises(TypeError):
            r1.width = 3.1
        r1.x = 0
        r1.y = 0
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        with self.assertRaises(ValueError):
            r1.x = -5
        with self.assertRaises(ValueError):
            r1.y = -5
        with self.assertRaises(TypeError):
            r1.x = "-5"
        with self.assertRaises(TypeError):
            r1.y = "-5"
        with self.assertRaises(TypeError):
            r1.x = (1, 2)
        with self.assertRaises(TypeError):
            r1.y = (1, 2)
        with self.assertRaises(TypeError):
            r1.x = [(1)]
        with self.assertRaises(TypeError):
            r1.y = [(1)]
        with self.assertRaises(TypeError):
            r1.x = {1}
        with self.assertRaises(TypeError):
            r1.y = {5}
        with self.assertRaises(TypeError):
            r1.x = True
        with self.assertRaises(TypeError):
            r1.y = True
        with self.assertRaises(TypeError):
            r1.x = 5.2
        with self.assertRaises(TypeError):
            r1.y = 3.1

    def test_square_area_and_setter_getter(self):
        s1 = Square(5, 1, 1)
        self.assertEqual(s1.area(), 25)
        s1.size = 2
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.area(), 4)
        with self.assertRaises(ValueError):
            s1.height = 0
        with self.assertRaises(ValueError):
            s1.width = 0
        with self.assertRaises(ValueError):
            s1.height = -5
        with self.assertRaises(ValueError):
            s1.width = -5
        with self.assertRaises(TypeError):
            s1.height = "-5"
        with self.assertRaises(TypeError):
            s1.width = "-5"
        with self.assertRaises(TypeError):
            s1.height = (1, 2)
        with self.assertRaises(TypeError):
            s1.width = (1, 2)
        with self.assertRaises(TypeError):
            s1.height = [(1)]
        with self.assertRaises(TypeError):
            s1.width = [(1)]
        with self.assertRaises(TypeError):
            s1.height = {1}
        with self.assertRaises(TypeError):
            s1.width = {5}
        with self.assertRaises(TypeError):
            s1.height = True
        with self.assertRaises(TypeError):
            s1.width = True
        with self.assertRaises(TypeError):
            s1.height = 5.2
        with self.assertRaises(TypeError):
            s1.width = 3.1
        s1.x = 0
        s1.y = 0
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        with self.assertRaises(ValueError):
            s1.x = -5
        with self.assertRaises(ValueError):
            s1.y = -5
        with self.assertRaises(TypeError):
            s1.x = "-5"
        with self.assertRaises(TypeError):
            s1.y = "-5"
        with self.assertRaises(TypeError):
            s1.x = (1, 2)
        with self.assertRaises(TypeError):
            s1.y = (1, 2)
        with self.assertRaises(TypeError):
            s1.x = [(1)]
        with self.assertRaises(TypeError):
            s1.y = [(1)]
        with self.assertRaises(TypeError):
            s1.x = {1}
        with self.assertRaises(TypeError):
            s1.y = {5}
        with self.assertRaises(TypeError):
            s1.x = True
        with self.assertRaises(TypeError):
            s1.y = True
        with self.assertRaises(TypeError):
            s1.x = 5.2
        with self.assertRaises(TypeError):
            s1.y = 3.1



if __name__ == '__main__':
    unittest.main()
