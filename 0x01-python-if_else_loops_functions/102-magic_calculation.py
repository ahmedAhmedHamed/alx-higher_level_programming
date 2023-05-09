#!/usr/bin/python3
import dis


def magic_calculation(a, b, c):
    if a < b:
        if c > b:
            a = a * b
            a = a - c
            return a
        else:
            a = a + b
            return a
    else:
        return c
