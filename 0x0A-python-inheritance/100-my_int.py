#!/usr/bin/python3
"""My integer"""



class MyInt(int):
    """a class MyInt that inherits from int"""
    def __eq__(self, other):
        """takes two args  self and other, and returns a
        Boolean value indicating whether they are equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """takes two args  self and other, and returns a
        Boolean value indicating whether they are not  equal"""
        return super().__eq__(other)

