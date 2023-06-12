#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """ a class BaseGeometry"""
    def area(self):
        """Public instance method that raises an Exception
        area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "Public instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError(f'{name}  must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
