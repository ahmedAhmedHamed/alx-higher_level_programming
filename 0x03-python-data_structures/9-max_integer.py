#!/usr/bin/python3
def max_integer(my_list=[]):
    mymax = None
    if not my_list:
        return None
    for i in my_list:
        if mymax is None or i > mymax:
            mymax = i
    return mymax
