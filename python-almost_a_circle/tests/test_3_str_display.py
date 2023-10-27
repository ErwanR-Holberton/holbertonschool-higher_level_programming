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

    def test_update(self):
        r2 = Rectangle(2, 2, 0, 0, 22)
        s2 = Square(2, 0, 0, 23)
        r2.update(24, 2, 3, 4, 5)
        s2.update(25, 8, 9, 10)
        self.assertEqual(r2.id, 24)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
        self.assertEqual(s2.id, 25)
        self.assertEqual(s2.size, 8)
        self.assertEqual(s2.x, 9)
        self.assertEqual(s2.y, 10)

        r2.update(x=1, id=52, height=3, width=3, y=2)
        s2.update(x=1, id=53, size=2, y=2)
        self.assertEqual(r2.id, 52)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(s2.id, 53)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)

        r3 = Rectangle(2, 2, 0, 0, "22")
        self.assertEqual(r3.id, "22")
        r3.update(x=1, id="52", height=3, width=3, y=2)
        self.assertEqual(r3.id, "52")

        with self.assertRaises(TypeError):
            r3.update(x=1, id="52", height="3", width=3, y=2)
        with self.assertRaises(TypeError):
            r3.update(x="1", id="52", height=3, width=3, y=2)
        with self.assertRaises(TypeError):
            r3.update(x=1, id="52", height=3, width="3", y=2)
        with self.assertRaises(TypeError):
            r3.update(x=1, id="52", height=3, width=3, y="2")
        with self.assertRaises(ValueError):
            r3.update(x=1, id="52", height=3, width=3, y=-1)
        with self.assertRaises(ValueError):
            r3.update(x=-1, id="52", height=3, width=3, y=2)
        with self.assertRaises(ValueError):
            r3.update(x=1, id="52", height=-3, width=3, y=0)
        with self.assertRaises(ValueError):
            r3.update(x=1, id="52", height=3, width=-3, y=0)

        #s3 = Square("2", "0", "0", "23")



if __name__ == '__main__':
    unittest.main()
