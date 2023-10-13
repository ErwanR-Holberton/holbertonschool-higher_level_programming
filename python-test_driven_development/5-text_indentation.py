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
    flag = 0
    for letter in text:
        if flag == 1:
            flag = 0
            continue
        print(letter, end="")
        if letter in ".?:":
            print("\n")
            flag = 1
