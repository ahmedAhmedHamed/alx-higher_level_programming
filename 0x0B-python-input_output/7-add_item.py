#!/usr/bin/python3
"""
a script that adds all arguments to
a Python list, and then save them to a file
"""
import json
import sys

if __name__ == "__main__":
    """the main driver of the file"""
    argv_split = sys.argv[1:]
    json_list = []
    for count, value in argv_split:
        json_list.append(argv_split)
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    save_to_json_file(json_list, "add_item.json")
