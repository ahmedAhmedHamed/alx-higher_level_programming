#!/usr/bin/python3
def no_c(my_string):
    newString = list(my_string)
    i = len(newString)
    j = 0
    while j < i:
        if newString[j] == "c" or newString[j] == "C":
            newString.pop(j)
            i = i - 1
        j = j + 1
    return "".join(newString)
