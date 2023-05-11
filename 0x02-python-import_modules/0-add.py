#!/usr/bin/python3
from add_0 import add as edd


def add(a, b):
    print("{} + {} = {}".format(a, b, edd(a, b)))


a = 1
b = 2
add(a, b)

if __name__ == '__main__':
    pass
