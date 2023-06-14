#!/usr/bin/python3
"""module that reads a file"""


def read_file(filename=""):
    """reads a file called filename"""
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end="")
