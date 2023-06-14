#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """writes a string to file with overwriting"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
