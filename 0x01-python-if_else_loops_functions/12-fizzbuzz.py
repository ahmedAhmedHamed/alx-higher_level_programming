#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        flag = 0
        if i % 3 == 0:
            flag = 1
            print("Fizz", end="")
        if i % 5 == 0:
            flag = 1
            print("Buzz", end="")
        if flag:
            print(" ", end="")
            continue
        print(f"{i} ", end="")
