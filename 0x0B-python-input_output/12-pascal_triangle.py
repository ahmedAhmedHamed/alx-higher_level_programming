#!/usr/bin/python3
"""module that houses the pascal triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers
     representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        new_row = create_new_row(triangle[i - 1])
        triangle.append(new_row)
    return triangle


def create_new_row(array):
    """responsible for creating a single row in the triangle"""
    new_row = [1]
    for i in range(len(array)):
        if i + 1 < len(array):
            number = array[i] + array[i + 1]
        else:
            number = 1
        new_row.append(number)
    return new_row
