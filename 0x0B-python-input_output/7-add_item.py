#!/usr/bin/python3
"""
a script that adds all arguments to
a Python list, and then save them to a file
"""
import sys
from os import path

if __name__ == "__main__":
    """the main driver of the file"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    if path.exists('add_item.json'):
        json_list = load_from_json_file('add_item.json')
    else:
        json_list = []

    with open("add_item.json", 'w', encoding="utf-8") as f:
        pass

    for i in range(1, len(sys.argv)):
        json_list.append(sys.argv[i])

    save_to_json_file(json_list, "add_item.json")
