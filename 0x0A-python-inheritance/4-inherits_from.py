#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """function that returns True if the object
    is an instance of a class that inherited
    from the specified class"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
