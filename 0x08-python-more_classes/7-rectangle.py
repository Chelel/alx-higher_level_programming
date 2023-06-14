#!/usr/bin/python3
""" String representation"""


class Rectangle:
    """a class rectangle with Private
    instance attribute: width and
    Private instance attribute: height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """rectangle width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height retriever"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ''
        else:
            rectangle = ""
            for i in range(self.height):
                rectangle += "#" * self.width + "\n"
            return rectangle[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __del__(self):
        """when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
