#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """a function that adds a new attribute to an object"""
    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
