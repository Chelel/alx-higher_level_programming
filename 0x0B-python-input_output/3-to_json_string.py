#!/usr/bin/python3
"""3-to_json_string.py
returns the JSON representation of an object (string"""


import json


def to_json_string(my_obj):
    """the function returns the JSON
    representation of an object (string)"""

    return json.dumps(my_obj)
