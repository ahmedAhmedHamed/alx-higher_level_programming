#!/usr/bin/python3
"""from json string to python object"""
import json


def from_json_string(my_str):
    """makes a python object from my_str"""
    return json.loads(my_str)
