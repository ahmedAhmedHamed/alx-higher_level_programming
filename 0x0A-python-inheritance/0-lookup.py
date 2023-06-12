#!/usr/bin/python3

""" this is a module for the 0-lookup question."""


def lookup(obj):
    """ this is the lookup function
        it lists all the attributes of the obj object
    """
    return list(dir(obj))
