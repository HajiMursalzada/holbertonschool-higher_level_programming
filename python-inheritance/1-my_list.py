#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """Create class inherits list"""
    def print_sorted(self):
        print(sorted(self))
