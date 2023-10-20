#!/usr/bin/python3
"""class my int with inversed operators"""


class MyInt(int):
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value != other.value
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        return True
