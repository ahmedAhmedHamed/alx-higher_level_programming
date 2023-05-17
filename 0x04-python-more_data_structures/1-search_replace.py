#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = search_and_replace(search, replace)
    return list(map(x, my_list))


def search_and_replace(search, replace):
    return lambda x: x if (x != search) else replace
