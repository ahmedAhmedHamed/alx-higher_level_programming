#!/usr/bin/python3
"""makes a class into a json"""
import json


def class_to_json(obj):
    """makes a class into a json"""
    return json.dumps(vars(obj))
