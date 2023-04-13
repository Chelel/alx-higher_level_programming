#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string"""

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        strn = ""
        for line in text:
            strn += line
            if search_string in line:
                strn += new_string
        fo.write(strn)
