#!/usr/bin/python3
"""0-read_file.py
a function that reads a text file (UTF8)
and prints it to stdout:"""


def read_file(filename=""):
    """This a function reads a text file and
    prints it to stdout"""

    with open(filename, encoding='utf:8') as file:
        print(file.read(), end='')
