#!/usr/bin/python3
def islower(c):
    return (ord(c) > 96 and ord(c) < 123)


def uppercase(str):
    for character in str:
        if islower(character):
            print("{}".format(chr(ord(character) - 32)), end="")
        else:
            print("{}".format(character), end="")
    print("")
