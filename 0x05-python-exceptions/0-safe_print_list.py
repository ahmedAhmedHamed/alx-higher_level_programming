#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            k = k + 1
    except:
        print()
        return k
    print()
    return k
