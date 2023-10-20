#!/usr/bin/python3
"""a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
