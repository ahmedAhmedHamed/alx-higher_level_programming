#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = 0
    num2 = 0
    if len(tuple_a) > 0:
        num1 = tuple_a[0]
    if len(tuple_b) > 0:
        num2 = tuple_b[0]
    num3 = 0
    num4 = 0
    if len(tuple_a) > 1:
        num3 = tuple_a[1]
    if len(tuple_b) > 1:
        num4 = tuple_b[1]
    return (num1 + num2, num3 + num4)
