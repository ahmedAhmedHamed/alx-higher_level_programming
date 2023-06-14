#!/usr/bin/python3
"""makes a class into a json"""


def class_to_json(obj):
    """makes a class into a json
        using its variables
    """
    return vars(obj)
