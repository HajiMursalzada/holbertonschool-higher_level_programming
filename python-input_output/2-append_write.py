#!/usr/bin/python3
"""Append file"""


def append_write(filename="", text=""):
    """Append data to filename"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
