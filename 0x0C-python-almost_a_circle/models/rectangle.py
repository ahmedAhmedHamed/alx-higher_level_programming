#!/usr/bin/python3
""" this is the rectangle module for 0x0C - 2"""
from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def update(self, *args, **kwargs):
        """updates the rectangle using *args and **kwargs"""
        if args.__len__():
            for counter, arg in enumerate(args):
                if counter == 0:
                    self.id = arg
                elif counter == 1:
                    self.width = arg
                elif counter == 2:
                    self.height = arg
                elif counter == 3:
                    self.x = arg
                elif counter == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def display(self):
        """displays the rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns the class's representation as a string"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"

    def to_dictionary(self):
        """returns the rectangle as a dictionary"""
        variables = vars(self)
        new_dictionary = {
                            'id': variables['id'],
                            'width': variables['_Rectangle__width'],
                            'height': variables['_Rectangle__height'],
                            'x': variables['_Rectangle__x'],
                            'y': variables['_Rectangle__y']
                          }
        return new_dictionary

    def integer_validator(self, name, value):
        """validates that input is an integer not allowing 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def x_y_validator(self, name, value):
        """validates that input is an integer allowing 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """getter for __width instance attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for __width instance attribute"""
        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """getter for __height instance attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for __height instance attribute"""
        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """getter for __x instance attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for __x instance attribute"""
        self.x_y_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """getter for __y instance attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for __y instance attribute"""
        self.x_y_validator("y", y)
        self.__y = y

    def area(self):
        """gets the area of the rectangle"""
        return self.height * self.width
