#!/usr/bin/python3
"""Type"""


def inherits_from(obj, a_class):
    """Check type"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
