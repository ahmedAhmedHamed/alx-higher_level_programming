#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dictionary = a_dictionary
    if key in new_dictionary:
        del new_dictionary[key]
    return new_dictionary
