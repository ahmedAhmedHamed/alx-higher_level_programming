#!/usr/bin/python3
"""is kind of class"""


def is_kind_of_class(obj, a_class):
    """checks if obj inherits from or is a_class"""
    if type(obj) == a_class:
        return True
    elif issubclass(type(obj), a_class):
        return True
    return False
