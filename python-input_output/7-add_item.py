#!/usr/bin/python3
"""Add item"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file")\
        .save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file")\
        .load_from_json_file

    file_name = "add_item.json"
    json_data = []

    with open(file_name, "a+") as file:
        file.seek(0)
        data = file.read()

        if len(data) == 0 and len(sys.argv) > 1:
            json_data.extend(sys.argv[1:])
            save_to_json_file(json_data, file_name)
        else:
            json_data = load_from_json_file("add_item.json")
            if len(sys.argv) > 1:
                json_data.extend(sys.argv[1:])
                save_to_json_file(json_data, "add_item.json")
