#!/usr/bin/python3
"""
101-add_attribute.py
"""


def add_attribute(obj, attribute, value):
    """
    Attempts to set or update `attribute` with `value`.
    Raises:
    - TypeError: if the object can't have new attribute,
    with the message "can't add new attribute"

    Returns:
    None
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
