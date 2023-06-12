#!/usr/bin/python3

"""eturns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object"""


def lookup(obj):
    """a function that returns the list of available
    attributes and methods of an object"""

    return dir(obj)
