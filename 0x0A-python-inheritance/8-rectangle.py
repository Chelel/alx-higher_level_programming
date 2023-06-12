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


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)


