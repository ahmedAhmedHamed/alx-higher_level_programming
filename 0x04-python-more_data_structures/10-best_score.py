#!/usr/bin/python3
def best_score(a_dictionary):
    temp = None
    tempkey = None
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        if temp is None or a_dictionary[key] > temp:
            temp = a_dictionary[key]
            tempkey = key
    return tempkey
