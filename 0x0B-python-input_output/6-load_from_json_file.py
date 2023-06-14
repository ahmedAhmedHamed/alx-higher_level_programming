#!/usr/bin/python3
"""loads a python file from a json"""
import json


def load_from_json_file(filename):
    """returns the json object in filename"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.loads(file.readline().rstrip())
