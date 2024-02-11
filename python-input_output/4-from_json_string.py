#!/usr/bin/python3
"""From JSON"""


import json


def from_json_string(my_str):
    """From JSON to object"""
    return json.loads(my_str)
