#!/usr/bin/python3
# function that adds two intergers


def add_integer(a, b=98):
    """Function takes two arguments a and b
     Args:
     a(type(int,float))
     b(int,float) initialized to a default value 98
     """

    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    """Checks whether the args provided are of type int or float
    They have to be casted to integers if they are float
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a+b
