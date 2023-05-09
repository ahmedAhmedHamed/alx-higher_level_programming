#!/usr/bin/python3
j = 0
for i in range(52):
    k = 0
    if i % 2 == 0:
        k = int(i / 2) + 65
    else:
        k = int(i / 2) + 97
    print("{}".format(chr(k)), end="")
