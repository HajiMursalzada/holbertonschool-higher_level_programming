#!/usr/bin/python3
"""Type"""


def is_kind_of_class(obj, a_class):
    """Check type"""
    if isinstance(obj, a_class):
        return True
    return False
