#!/usr/bin/python3
"""a class MyList that inherits from list:"""


class MyList(list):
    """All the elements of the list will be of type int"""

    def print_sorted(self):
        """Public instance method: def print_sorted(self):
        that prints the list, but sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
