#!/usr/bin/python3
""" same as write file but with append"""


def append_write(filename="", text=""):
    """appends a sentence to a file"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
