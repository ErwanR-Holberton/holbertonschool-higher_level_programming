#!/usr/bin/python3
"""return dictionary description of object"""
import json


def class_to_json(obj):
    """return dictionary description of object"""
    return obj.__dict__
