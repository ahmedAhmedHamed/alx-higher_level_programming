#!/usr/bin/python3
"""module that has inherits from func"""


def inherits_from(obj, a_class):
    """ checks if obj inherits from a_class directly or indirectly"""
    if type(obj) == a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    return False
