#!/usr/bin/python3
import dis


def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        a = a + b
        return a
    a = a * b
    a = a - c
    return a
