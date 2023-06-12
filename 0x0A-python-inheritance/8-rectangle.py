#!/usr/bin/python3
"""8-rectangle - defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class
        is a rectangle inheriting from basegeometry
    """
    def __init__(self, width, height):
        """initializes the rectangle"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height
