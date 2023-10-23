#!/usr/bin/python3
"""defines a square class that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=0, y=0, id=None)
