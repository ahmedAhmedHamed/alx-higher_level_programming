def max_integer(my_list=[]):
    mymax = None
    for i in my_list:
        if mymax is None or i > mymax:
            mymax = i
    return mymax
