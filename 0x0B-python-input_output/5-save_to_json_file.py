#!/usr/bin/python3
"""saves an object to a text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """saves an object to a text file using json"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
