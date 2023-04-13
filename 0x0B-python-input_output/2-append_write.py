#!/usr/bin/python3
"""2-append_write.py
appends a string at the end of a text fil
"""


def append_write(filename="", text=""):
    """This function that appends a string at the end
    of a text file (UTF8) and returns the
    number of characters added"""

    with open(filename, 'a', encoding='utf-8') as file:
        text_written = file.write(text)
        return text_written
