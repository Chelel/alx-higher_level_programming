#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """ The class reps a Rectangle"""
    def __init__(self, height=0, width=0):
        """ The rectangle is initialized with the height and width as given
        Args:
        The height and width are of type int initialized to a default value 0
        """
        self.height = height
        self.width = width

     @property
    def width(self):
        """Ges the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
