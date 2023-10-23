#!/usr/bin/python3
"""defines a square class that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id=None)

    def __str__(self):
        """returns description of square"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
