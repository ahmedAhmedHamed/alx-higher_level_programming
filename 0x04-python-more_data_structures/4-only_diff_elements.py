#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    x = (set(set_1) - set(set_2))
    y = (set(set_2) - set(set_1))
    return x.union(y)
