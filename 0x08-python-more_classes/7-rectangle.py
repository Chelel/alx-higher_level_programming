#!/usr/bin/python3

""" class Rectangle that defines a rectangle"""


class Rectangle:
    """A class Rectangle.
    Takes in args for width and height of a rectangle, and contains methods
    for calculation of the area or perimeter. __str__, __repr__, and __del__
    fuctionality defined below.
    Attributes:
        number_of_instances (int): counter incrementing for every
            instantiation, and decrementing for every instance deletion.
        print_symbol (str): single character to be used in assembling string
            representation of rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    """represents a class Rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the instance attributes
        width and height with the value 0"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rectangle = []
            for i in range(self.height):
                rectangle.append(str(self.print_symbol) * self.width)
        return "\n".join(rectangle)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
