#!/usr/bin/python3
def formatchr(c):
    if ord(c) > 96 and ord(c) < 123:
        return chr(ord(c) - 32)
    return (c)


def uppercase(str):
    for character in str:
        print("{}".format(formatchr(character)), end="")
    print("")
