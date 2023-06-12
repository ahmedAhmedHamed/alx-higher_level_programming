#!/usr/bin/python3
"""defines a square class inheriting form rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square class that inherits from rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        return self.size * self.size
