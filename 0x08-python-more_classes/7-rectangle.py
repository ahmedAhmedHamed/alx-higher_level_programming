#!/usr/bin/python3
""" this is a rectangle """


class Rectangle:
    """ The aforementioned rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__exception_raiser(width, "width")
        self.__exception_raiser(height, "height")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perimeter_value = 2 * (self.__width + self.__height)
        if self.zero_checker():
            perimeter_value = 0
        return perimeter_value

    def __str__(self):
        return self.make_rectangle_array()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def make_rectangle_array(self):
        if self.zero_checker():
            return ""
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def zero_checker(self):
        if self.__width == 0 or self.__height == 0:
            return True
        return False

    def __exception_raiser(self, value, word_in_exception):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(word_in_exception))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(word_in_exception))
