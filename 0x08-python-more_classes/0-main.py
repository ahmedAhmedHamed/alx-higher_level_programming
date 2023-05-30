#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(__import__('0-rectangle').__dict__)
print(my_rectangle.__dict__)
