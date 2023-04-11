#!/usr/bin/python3
"""100-my_int.py
"""


class MyInt(int):
    """subclass of type int that has the ==
    and != operators inverted.
    """

    def __eq__(self, other):
        """Reverses the  == operator.
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """Reverses the != operator.
        """
        return int(self) == int(other)
