#!/usr/bin/python3
"""
finds peak in unsorted list of integers
"""


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b


def find_peak(list_of_integers):
    """
    finds peak in unsorted list of integers
    N = 8
    [5, 4, 3, 2, 1, 6, 5, 4] start 0, cmp i&i+1, jump = 2
    0-1, 2-3, 4-5, 6-7
    [(4, 5,) (2, 3), (1, 6,) (4, 5)] start 1, cmp i&i+2, jump = i + 2 + 2
    1-3, 5-7
    [(4, 3, 2, 5,) (1, 5, 4, 6)] start 3, cmp i&i + 4
    3-7
    CMP * 2 every loop

    [1, 2, 4, 5, 10, 3, 2, 1, 5, 7] N = 10
    0-1, 2-3, 4-5, 6-7, 8-9
    1-3, 5-7

    """
    jump = 1
    cmp = 1
    start = 0
    while jump < len(list_of_integers):
        for i in range(start, len(list_of_integers) - 1, jump * 2):
            print(f"i = {i}, jump = {jump}")
            if list_of_integers[i] > list_of_integers[i + cmp]:
                print(list_of_integers)
                list_of_integers[i], list_of_integers[i + cmp] = list_of_integers[i + cmp], list_of_integers[i]
                print(list_of_integers)
                print()
        jump = jump * 2
        start = start + cmp
        cmp = cmp * 2
    print(list_of_integers)
    return list_of_integers[-1]
