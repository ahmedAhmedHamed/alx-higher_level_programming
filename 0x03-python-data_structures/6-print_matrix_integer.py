#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if not i:
            continue
        for j in i:
            print("{:d}".format(j), end=" ")
        print("")
