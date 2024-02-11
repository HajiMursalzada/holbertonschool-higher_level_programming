#!/usr/bin/python3
"""Check type"""


def is_same_class(obj, a_class):
    """Check if the object is an instance of the specified class."""
    if type(obj) is a_class:
        return True
    return False
