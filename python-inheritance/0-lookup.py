#!/usr/bin/python3
"""print all attributes from an object"""


def lookup(obj):
    """commentaire pour dire plus de choses"""
    attributes = []
    for i in dir(obj):
        attributes.append(i)
    return attributes
