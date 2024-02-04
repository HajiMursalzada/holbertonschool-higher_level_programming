#!/usr/bin/python3
"""4-print_square.py and tests/4-print_square.txt"""


def print_square(size):
    """Print a square with '#' followed by a newline.
    size (int): the dimensions of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
