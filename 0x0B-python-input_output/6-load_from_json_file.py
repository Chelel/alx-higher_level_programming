#!/usr/bin/python3
"""6-load_from_json_file.py
Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """this function creates an Object from a “JSON file”"""

    with open(filename, encoding='utf-8') as file:
        return json.load(file)
