#!/usr/bin/python3
"""function that add attribute if possible"""


def add_attribute(obj, attr, value):
    """function that add attribute if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
