#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new_dictionary = a_dictionary
    for key in a_new_dictionary:
        a_new_dictionary[key] = a_new_dictionary[key] * 2
    return a_new_dictionary
