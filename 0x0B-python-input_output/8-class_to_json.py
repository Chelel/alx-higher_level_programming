#!/usr/bin/python3
"""8-class_to_json.py
Class to JSON"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""

    j_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            j_dict[key] = value

    return j_dict
