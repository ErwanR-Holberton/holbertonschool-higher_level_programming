#!/usr/bin/python3
"""
this
is a
5 line comment
"""


def text_indentation(text):
    """
    indenting a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for letter in text:
        print(letter, end="")
        if letter in ".?:":
            print("\n")
