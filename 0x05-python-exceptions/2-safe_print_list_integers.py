#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print(my_list[i], end="")
                k = k + 1
    except:
        print()
        return k
    print()
    return k
