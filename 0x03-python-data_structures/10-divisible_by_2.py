#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = list(map(div2, my_list))
    return result


def div2(number):
    if number % 2 == 0:
        return True
    return False
