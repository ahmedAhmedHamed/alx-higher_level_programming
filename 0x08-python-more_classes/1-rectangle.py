#!/usr/bin/python3
""" this is a rectangle """


class Rectangle:
    """ The aforementioned rectangle """
    def __init__(self, width=0, height=0):
        self.__exception_raiser(width, "width")
        self.__exception_raiser(height, "height")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__exception_raiser(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__exception_raiser(value, "height")
        self.__width = value

    def __exception_raiser(self, value, word_in_exception):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(word_in_exception))
        elif value < 0:
            raise TypeError("{} must be >= 0".format(word_in_exception))
