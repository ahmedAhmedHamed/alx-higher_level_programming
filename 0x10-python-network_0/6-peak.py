#!/usr/bin/python3
"""
finds peak in unsorted list of integers
"""


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

    N = 7
    [5, 4, 3, 2, 1, 6, 5, 4]
    0-1, 2-3, 4-5, 6-OUT OF INDEX
    [(4, 5,) (2, 3), (1, 6,) 4]
    1-3, 4-5
    [(4, 3, 2, 5,), 1, 6, 4]
    """
    num_max = float('-inf')
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > num_max:
            num_max = list_of_integers[i]
    return num_max
