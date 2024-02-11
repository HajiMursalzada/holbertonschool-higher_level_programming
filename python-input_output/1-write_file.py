#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """Write data to filename"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
