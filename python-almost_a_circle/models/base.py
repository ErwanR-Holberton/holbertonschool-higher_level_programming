#!/usr/bin/python3
""" def of a class"""
import json


class Base:
    """ def of a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string from list"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objects to json"""
        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string(
                    [o.to_dictionary() for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """return the json representation of json string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance with attributes from a dictionnary"""
        if cls.__name__ == "Square":
            rectangle = cls(1)
        if cls.__name__ == "Rectangle":
            rectangle = cls(1, 1)
        rectangle.update(**dictionary)
        return rectangle

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                return [cls.create(**a)
                        for a in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
