#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        flag = 0
        if i % 3 == 0:
            flag = 1
            print("fizz", end="")
        if i % 5 == 0:
            flag = 1
            print("buzz", end="")
        if flag:
            if i != 100:
                print(" ", end="")
            else:
                print("")
                break
            continue
        print(f"{i} ", end="")
