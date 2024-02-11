#!/usr/bin/python3
"""Load from json file"""


import json


def load_from_json_file(filename):
    """Load form json file"""
    with open(filename) as file:
        data = file.read()
    return json.loads(data)
