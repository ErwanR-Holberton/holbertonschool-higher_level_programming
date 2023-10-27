#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestJSON(unittest.TestCase):
    def test_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(r1.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(s1.to_dictionary(), {'id': 4, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(dict, type(r1.to_dictionary()))
        self.assertEqual(dict, type(s1.to_dictionary()))

    def test_JSON_string(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(1, 2, 3, 4)
        str_r = "{\"id\": 5, \"width\": 1, \"height\": 2, \"x\": 3, \"y\": 4}"
        str_s = "{\"id\": 4, \"size\": 1, \"x\": 2, \"y\": 3}"
        self.assertEqual(r1.to_json_string(r1.to_dictionary()), str_r)
        self.assertEqual(s1.to_json_string(s1.to_dictionary()), str_s)
        self.assertEqual(type(r1.to_json_string(r1.to_dictionary())), str)
        self.assertEqual(type(s1.to_json_string(s1.to_dictionary())), str)
        self.assertEqual(r1.to_json_string(None), "[]")
        self.assertEqual(s1.to_json_string(None), "[]")
        self.assertEqual(r1.to_json_string([]), "[]")
        self.assertEqual(s1.to_json_string([]), "[]")



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

        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
        self.assertEqual(type(Rectangle.load_from_file()), list)
        self.assertEqual(type(Square.load_from_file()), list)

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("a")
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(5)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())
            self.assertEqual(str, type(f.read()))
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
            self.assertEqual(str, type(f.read()))

        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])


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
        list_r = [{'id': 125, 'width': 5, 'height': 4}, {'id': 126, 'width': 3, 'height': 20}]
        list_s = [{'id': 128, 'size': 5}, {'id': 129, 'size': 3}]
        expected_r = '[{"id": 125, "width": 5, "height": 4}, {"id": 126, "width": 3, "height": 20}]'
        expected_s = '[{"id": 128, "size": 5}, {"id": 129, "size": 3}]'
        j_string_r = Rectangle.to_json_string(list_r)
        j_string_s = Square.to_json_string(list_s)
        self.assertEqual(j_string_r, expected_r)
        self.assertEqual(j_string_s, expected_s)
        self.assertEqual(type(j_string_r), str)
        self.assertEqual(type(j_string_s), str)

    def test_JSON2(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(5, 4, 3, 202)
        dict_r = r1.to_dictionary()
        dict_s = s1.to_dictionary()
        j_string_r = Base.to_json_string([dict_r])
        j_string_s = Base.to_json_string([dict_s])
        self.assertEqual(type(j_string_r), str)
        self.assertEqual(type(j_string_s), str)
        self.assertEqual(json.loads(j_string_r), [{"id": 5, "width": 1, "height": 2, "y": 4, "x": 3}])
        self.assertEqual(json.loads(j_string_s), [{"id": 202, "size": 5, "y": 3, "x": 4}])
        j_string_r = Base.to_json_string(None)
        self.assertEqual(j_string_r, "[]")
        j_string_r = Base.to_json_string([])
        self.assertEqual(j_string_r, "[]")
        j_string_r = Rectangle.to_json_string(None)
        self.assertEqual(j_string_r, "[]")
        j_string_r = Rectangle.to_json_string([])
        self.assertEqual(j_string_r, "[]")
        j_string_r = Square.to_json_string(None)
        self.assertEqual(j_string_r, "[]")
        j_string_r = Square.to_json_string([])
        self.assertEqual(j_string_r, "[]")




if __name__ == '__main__':
    unittest.main()
