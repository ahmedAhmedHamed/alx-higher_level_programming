#!/usr/bin/python3
"""module for square class that inherits from rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """a square is a special case of a rectangle,
    this class implements this special case.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

