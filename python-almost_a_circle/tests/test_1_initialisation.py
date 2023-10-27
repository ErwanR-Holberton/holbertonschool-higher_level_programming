#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestInit(unittest.TestCase):
    def test_classes(self):
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(issubclass(Rectangle, Square))
        self.assertFalse(issubclass(Base, Rectangle))
        self.assertFalse(issubclass(Base, Square))

    def test_base_initialization_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(1.2)
        self.assertEqual(b3.id, 1.2)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 3)
        b6 = Base(-5)
        self.assertEqual(b6.id, -5)
        b7 = Base("-5")
        self.assertEqual(b7.id, "-5")

    def test_rectangle_initialization_id(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)
        r3 = Rectangle(2, 5)
        self.assertEqual(r3.id, 4)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        r4 = Rectangle(3, 6, 1)
        self.assertEqual(r4.id, 5)
        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 6)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 0)
        r5 = Rectangle(1, 2, 3, 4, 20)
        self.assertEqual(r5.id, 20)
        self.assertEqual(r5.width, 1)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 3)
        self.assertEqual(r5.y, 4)

        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, -5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, "-5")
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, [-5])
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, {-5})
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, (5, ))
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, -5)
        with self.assertRaises(TypeError):
            r5 = Rectangle("5", 1)
        with self.assertRaises(TypeError):
            r5 = Rectangle([-5], 1)
        with self.assertRaises(TypeError):
            r5 = Rectangle({-5}, 1)
        with self.assertRaises(TypeError):
            r5 = Rectangle((5, ), 1)
        with self.assertRaises(TypeError):
            r5 = Rectangle(0.2, 1)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 0.2)
        with self.assertRaises(TypeError):
            r5 = Rectangle(True, 5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, True)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, "1")
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, {1})
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, [1])
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, (1, 1))
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, 0.1)
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, 1, -5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, True)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, 1, "1")
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, 1, {1})
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, 1, [1])
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, 1, (1, 1))
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, 1, 0.1)
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, 1, 1, -5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 1, 1, True)

    def test_square_initialization_id(self):
        with self.assertRaises(TypeError):
            s1 = Square()
        s1 = Square(3)
        self.assertEqual(s1.id, 37)
        self.assertEqual(s1.size, 3)
        s2 = Square(3, 1, 5, 50)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 5)
        self.assertEqual(s2.id, 50)
        with self.assertRaises(TypeError):
            s5 = Square((5, ))
        with self.assertRaises(TypeError):
            s5 = Square("esdf")
        with self.assertRaises(TypeError):
            s5 = Square([5])
        with self.assertRaises(TypeError):
            s5 = Square({1})
        with self.assertRaises(ValueError):
            s5 = Square(0)
        with self.assertRaises(ValueError):
            s5 = Square(-5)
        with self.assertRaises(TypeError):
            s5 = Square(0.2)
        with self.assertRaises(TypeError):
            s5 = Square(True)
        with self.assertRaises(TypeError):
            s5 = Square(1, "1")
        with self.assertRaises(ValueError):
            s5 = Square(1, -5)
        with self.assertRaises(TypeError):
            s5 = Square(1, [1])
        with self.assertRaises(TypeError):
            s5 = Square(1, {1})
        with self.assertRaises(TypeError):
            s5 = Square(1, (1, 1))
        with self.assertRaises(TypeError):
            s5 = Square(1, 0.2)
        with self.assertRaises(TypeError):
            s5 = Square(1, True)
        with self.assertRaises(TypeError):
            s5 = Square(1, 1, "1")
        with self.assertRaises(ValueError):
            s5 = Square(1, 1, -5)
        with self.assertRaises(TypeError):
            s5 = Square(1, 1, [1])
        with self.assertRaises(TypeError):
            s5 = Square(1, 1, {1})
        with self.assertRaises(TypeError):
            s5 = Square(1, 1, (1, 1))
        with self.assertRaises(TypeError):
            s5 = Square(1, 1, 0.2)
        with self.assertRaises(TypeError):
            s5 = Square(1, 1, True)


if __name__ == '__main__':
    unittest.main()
