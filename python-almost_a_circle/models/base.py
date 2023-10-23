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

    def to_json_string(list_dictionaries):
        """return json string from list"""
        return json.dumps(list_dictionaries)
