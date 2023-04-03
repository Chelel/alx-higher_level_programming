#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """ The class reps a Rectangle"""
    def __init__(self, length=0, width=0):
        """ 
The rectangle is initialized with the length and width as given

Args:
The length and width are of type int initialized to a default value 0
 """
        self.length = length
        self.width = width

    @property
    def width(self):
        """ 
Gets the width of the rectangle and returns the same
 """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width has to be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        
    @property
    def length(self):
        """ Gets the length of the rectangle and returns the same"""
        return self.__length
    
    @length.setter
    def length(self, value):
        """ Initialize the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("length has to be an interger")
        elif value < 0:
            raise ValueError("length must be >= 0")
        self.__length = value
