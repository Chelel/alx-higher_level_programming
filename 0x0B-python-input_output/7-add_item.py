#!/usr/bin/python3
"""7-add_item.py
Load, add, save"""


import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv_n = argv[1:]

try:
    txt_list = son_file("add_item.json")
except:
    txt_list = []
finally:
    for arg in argv_n:
        txt_list.append(arg)
    save_to_json_file(txt_list, "add_item.json")
