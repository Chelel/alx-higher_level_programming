#!/usr/bin/python3
"""10-student.py
Student to JSON with filter"""


class Student:
    """class Student that defines a student by
    Public instance attributes:
    first_name
    last_name
    age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of class instance. If attrs is a list of strings,
        only attribute names contained in this list must be retrieved"""

        if attrs is None:
            return self.__dict__

        dict1 = {}
        for key in attrs:
            if hasattr(self, key):
                dict1[key] = getattr(self, key)
        return dict1

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for key in json:
            self.__dict__.update({key: json[key]})

