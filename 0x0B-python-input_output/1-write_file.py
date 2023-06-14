#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
