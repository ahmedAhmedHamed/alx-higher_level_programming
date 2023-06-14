#!/usr/bin/python3
"""module for append after"""


def append_after(filename="", search_string="", new_string=""):
    """appends a new string after every line
    containing search_string"""
    with open(filename, "r") as f:
        contents = f.readlines()

    for counter, value in enumerate(contents):
        if value.find(search_string) != -1:
            contents.insert(counter + 1, new_string)
            counter += 1

    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)
