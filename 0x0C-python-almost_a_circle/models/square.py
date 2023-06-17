#!/usr/bin/python3
"""module for square class that inherits from rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """a square is a special case of a rectangle,
    this class implements this special case.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] (f{self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """updates the rectangle using *args and **kwargs"""
        if args.__len__():
            for counter, arg in enumerate(args):
                if counter == 0:
                    self.id = arg
                elif counter == 1:
                    self.size = arg
                elif counter == 2:
                    self.x = arg
                elif counter == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        variables = vars(self)
        new_dictionary = {
                            'id': variables['id'],
                            'size': variables['_Rectangle__width'],
                            'x': variables['_Rectangle__x'],
                            'y': variables['_Rectangle__y']
                          }
        return new_dictionary

    @property
    def size(self):
        return self.width * self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
