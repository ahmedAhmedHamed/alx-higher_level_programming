#!/usr/bin/python3
j = 0
for i in range(25, -1, -1):
    k = 0
    if i % 2 == 0:
        k = i + 65
    else:
        k = i + 97
    print("{}".format(chr(k)), end="")
