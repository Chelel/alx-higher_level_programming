#!/usr/bin/python3
"""a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class)"""


def is_same_class(obj, a_class):
    """function that returns True if the object is
    exactly an instance of the specified class"""
    return type(obj) == a_class
