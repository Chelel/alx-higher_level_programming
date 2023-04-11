#!/usr/bin/python3
"""python-inheritance task 2."""


def is_same_class(obj, a_class):
    """is_same_class(obj, a_class) function tests if the object
    is exactly an instance of the specified class.

    Args-
    obj object of any type
    a_class (class): class to test against
    returns True if the obj is an instance of the specified class;
    otherwise False."""

    return type(obj) == a_class
