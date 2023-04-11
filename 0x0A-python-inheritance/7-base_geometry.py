#!/usr/bin/python3
"""7-base_geometry.py: Integer validator"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """Public instance method
        that raises an Exception with the
        message area() is not implemented"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that a value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
