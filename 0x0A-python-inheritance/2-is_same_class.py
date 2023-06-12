#!/usr/bin/python3
"""this is the module for 2-is_same_class """


def is_same_class(obj, a_class):
    """function that checks if two classes are the same
        (class type)
    """
    if type(obj) == a_class:
        return True
    return False
