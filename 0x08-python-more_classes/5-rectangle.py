#!/usr/bin/python3

""" class Rectangle that defines a rectangle"""


class Rectangle:
    """represents a class Rectangle"""
    def __init__(self, width=0, height=0):
        """set the instance attributes width and height with the value 0"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return ('#' * self.__width + '\n') * self.__height

    def __repr__(self):
        return "Rectangle(%i, %i)" % (self.__width, self.__height)

    def __del__(self):
        print('Bye rectangle...')
