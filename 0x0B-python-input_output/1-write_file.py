#!/usr/bin/python3
""" Write to a file"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, 'w', encoding="UTF-8") as f:
        n = f.write(text)
        return n
