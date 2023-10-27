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

    def test_save_JSON(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(1, 2, 3, 4)
        Rectangle.save_to_file([r1])
        Square.save_to_file([s1])
        self.assertEqual(Rectangle.load_from_file()[0].x, r1.x)
        self.assertEqual(Rectangle.load_from_file()[0].y, r1.y)
        self.assertEqual(Rectangle.load_from_file()[0].width, r1.width)
        self.assertEqual(Rectangle.load_from_file()[0].height, r1.height)
        self.assertEqual(Rectangle.load_from_file()[0].id, r1.id)
        self.assertEqual(Square.load_from_file()[0].x, s1.x)
        self.assertEqual(Square.load_from_file()[0].y, s1.y)
        self.assertEqual(Square.load_from_file()[0].size, s1.size)
        self.assertEqual(Square.load_from_file()[0].id, s1.id)

    def test_create(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(1, 2, 3, 4)
        dict_r = r1.to_dictionary()
        dict_s = s1.to_dictionary()
        r2 = Rectangle.create(**dict_r)
        s2 = Square.create(**dict_s)
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r2.id, r2.id)
        self.assertEqual(r2.height, r2.height)
        self.assertEqual(r2.width, r2.width)
        self.assertEqual(r2.x, r2.x)
        self.assertEqual(r2.y, r2.y)

    def test_fromJSON(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        expected = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertEqual(json_list_input, expected)



if __name__ == '__main__':
    unittest.main()
