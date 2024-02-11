#!/usr/bin/python3
"""Save to json file"""


import json


def save_to_json_file(my_obj, filename):
    """Save json object to new file"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
