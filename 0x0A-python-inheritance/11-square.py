#!/usr/bin/python3
"""Full rectangle"""


class BaseGeometry:
    """a class BaseGeometry"""
    def area(self):
        """Public instance method  that raises an
        Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        return self.__height * self.__width


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size: def __init__(self, size)::
            size must be private. No getter or setter
            size must be a positive integer, validated by integer_validator"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)


    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
